import { google } from "googleapis";
import { DEFAULT_SCOPES, GoogleOAuthService } from "./auth";

export async function listCalendars() {
  const service = new GoogleOAuthService({
    scopes: DEFAULT_SCOPES,
  });
  const client = await service.authorize();

  if (!client) {
    throw new Error("No client found");
  }

  const calendar = google.calendar({ version: "v3", auth: client });
  const response = await calendar.calendarList.list();

  return response.data.items;
}

export async function getCalendarEvents(
  { calendarId, q, timeMin, timeMax }: {
    calendarId: string;
    timeMin?: string;
    timeMax?: string;
    q?: string;
  },
) {
  const service = new GoogleOAuthService({
    scopes: DEFAULT_SCOPES,
  });
  const client = await service.authorize();

  if (!client) {
    throw new Error("No client found");
  }

  const calendar = google.calendar({ version: "v3", auth: client });
  const response = await calendar.events.list({
    q,
    calendarId,
    timeMin,
    timeMax,
    singleEvents: true,
    orderBy: "startTime",
  });

  return response.data.items;
}
