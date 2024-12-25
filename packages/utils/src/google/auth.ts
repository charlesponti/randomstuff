import { readFile, writeFile } from "node:fs/promises";
import * as path from "node:path";
import { authenticate as googleAuthenticate } from "@google-cloud/local-auth";
import { google } from "googleapis";
import { Credentials, GoogleAuth, OAuth2Client } from "google-auth-library";

import logger from "../logger";

type JSONClient = ReturnType<typeof google.auth.fromJSON>;
type AuthClient =
  | OAuth2Client
  | GoogleAuth<JSONClient>
  | null;

export const TOKEN_PATH = path.join(__dirname, "token.json");
export const CREDENTIALS_PATH = path.join(__dirname, "credentials.json");
export const DEFAULT_SCOPES = [
  "https://www.googleapis.com/auth/contacts",
  "https://www.googleapis.com/auth/drive",
  "https://www.googleapis.com/auth/calendar",
  "https://mail.google.com/",
];
type GoogleOAuthServiceOptions = {
  scopes: string[];
};
export class GoogleOAuthService {
  private client: AuthClient;
  private options: GoogleOAuthServiceOptions;

  static async getCredentials(): Promise<{ installed: any; web: any }> {
    try {
      const content = await readFile(CREDENTIALS_PATH);
      return JSON.parse(content.toString());
    } catch (err) {
      logger.error("Error loading client secret file:", err);
      throw err;
    }
  }

  static async getSavedAuth(): Promise<
    JSONClient | null
  > {
    try {
      const content = await readFile(TOKEN_PATH);
      const credentials = JSON.parse(content.toString());
      return google.auth.fromJSON(credentials);
    } catch (err) {
      logger.warn("No token file found. Requesting authorization...");
      return null;
    }
  }

  constructor(options: GoogleOAuthServiceOptions) {
    this.client = null;
    this.options = options;
  }

  // Load or request or authorization to call APIs
  async authorize(): Promise<GoogleAuth<JSONClient> | OAuth2Client> {
    let client = await GoogleOAuthService.getSavedAuth();

    if (client) {
      if (!client.credentials) {
        await this.saveCredentials(client.credentials);
      }

      return client as any as GoogleAuth<JSONClient>;
    }

    // Since we don't have credentials, we need to request them
    const newClient = await googleAuthenticate({
      scopes: this.options.scopes,
      keyfilePath: CREDENTIALS_PATH,
    });

    // Save new credentials
    await this.saveCredentials(newClient.credentials);

    return newClient as any as OAuth2Client;
  }

  // Create token file if it doesn't exist
  async saveCredentials(
    credentials: Credentials,
  ): Promise<void> {
    try {
      const keys = await GoogleOAuthService.getCredentials();
      const key = keys.installed || keys.web;
      const payload = JSON.stringify({
        type: "authorized_user",
        client_id: key.client_id,
        client_secret: key.client_secret,
        refresh_token: credentials.refresh_token,
      });
      await writeFile(TOKEN_PATH, payload);
    } catch (err) {
      logger.error("Error loading client secret file:", err);
      throw err;
    }
  }
}
