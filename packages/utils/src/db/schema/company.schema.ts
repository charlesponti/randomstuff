import { pgTable, text, timestamp, uuid, jsonb } from "drizzle-orm/pg-core";

export const companies = pgTable("companies", {
  id: uuid("id").primaryKey().defaultRandom(),
  name: text("name").notNull(),
  description: text("description").notNull(),
  website: text("website").notNull(),
  industry: text("industry").notNull(),
  size: text("size").notNull(),
  location: jsonb("location").notNull(),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
  version: text("version").notNull().default("1"),
});

export type Company = typeof companies.$inferSelect;
export type NewCompany = typeof companies.$inferInsert;
