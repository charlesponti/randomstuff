import { drizzle } from "drizzle-orm/libsql";
export { applications } from "./schema";

export const db = drizzle("file:db.sqlite");
