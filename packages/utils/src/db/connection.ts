import { drizzle, type PostgresJsDatabase } from "drizzle-orm/postgres-js";
import postgres from "postgres";
import * as schema from "./schema";

const databaseUrl =
	process.env.NODE_ENV === "test"
		? "postgres://postgres:postgres@localhost:4433/hominem-test"
		: process.env.DATABASE_URL;

if (!databaseUrl) {
	throw new Error("DATABASE_URL environment variable is not set");
}

const client = postgres(databaseUrl);

export const db: PostgresJsDatabase<typeof schema> = drizzle(client, {
	schema,
});
