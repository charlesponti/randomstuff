import { pgTable, text, integer, uuid, geometry } from "drizzle-orm/pg-core";

export const transportationRoutes = pgTable("transportation_routes", {
	id: uuid("id").primaryKey().defaultRandom(),
	name: text("name").notNull(),
	description: text("description"),
	mode: text("mode").notNull(),
	startLocationId: uuid("start_location_id").notNull(),
	endLocationId: uuid("end_location_id").notNull(),
	location: geometry("location").notNull(),
	duration: integer("duration").notNull(),
});
