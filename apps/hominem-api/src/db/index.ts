import fastifyPlugin from "fastify-plugin";
import * as schema from "./drizzle/schema";
import postgres from "postgres";
import { drizzle, type PostgresJsDatabase } from "drizzle-orm/postgres-js";
import assert from "node:assert";

const DATABASE_URL =
	process.env.NODE_ENV === "test"
		? "postgres://postgres:postgres@localhost:4433/hominem-test"
		: process.env.DATABASE_URL;

assert(DATABASE_URL, "Missing DATABASE_URL");

const client = postgres(DATABASE_URL);

export const db: PostgresJsDatabase<typeof schema> = drizzle(client, {
	schema,
});

export const PgPlugin = fastifyPlugin(async (server) => {
	server.addHook("onClose", async () => {
		await client.end();
	});
});

export const takeOne = <T>(values: T[]): T => {
	return values[0];
};

// Define this helper somewhere in your codebase:
export const takeUniqueOrThrow = <T>(values: T[]): T => {
	if (!Array.isArray(values)) return values;
	if (values.length !== 1)
		throw new Error("Found non unique or inexistent value");
	return values[0];
};
