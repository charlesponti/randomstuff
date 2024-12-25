import { integer, real, sqliteTable, text } from "drizzle-orm/sqlite-core";

export const Users = sqliteTable("users", {
  id: text("id").primaryKey(),
  email: text("email").notNull(),
}, () => []);

export const Artists = sqliteTable("artists", {
  artistId: text("artist_id").primaryKey(),
  name: text("name").notNull(),
  genre: text("genre").notNull(),
  avgTicketPrice: real("avg_ticket_price").notNull(),
  avgAttendance: integer("avg_attendance").notNull(),
}, () => []);

export const Venues = sqliteTable("venues", {
  venueId: text("venue_id").primaryKey(),
  venueName: text("venue_name").notNull(),
  addressLine1: text("address_line1").notNull(),
  addressLine2: text("address_line2"),
  city: text("city").notNull(),
  state: text("state").notNull(),
  postalCode: text("postal_code").notNull(),
  country: text("country").notNull(),
  venueType: text("venue_type").notNull(),
  audienceStyle: integer("audience_style").notNull(),
  maxCapacity: integer("max_capacity").notNull(),
  hasAudioSystem: integer("has_audio_system", { mode: "boolean" }).notNull(),
  audioSystemType: text("audio_system_type"),
  hasLightingSystem: integer("has_lighting_system", { mode: "boolean" })
    .notNull(),
  lightingSystemType: text("lighting_system_type"),
  stageType: text("stage_type").notNull(),
  stageDimensions: text("stage_dimensions"),
  backstageArea: integer("backstage_area", { mode: "boolean" }).notNull(),
  greenRoom: integer("green_room", { mode: "boolean" }).notNull(),
  parkingInfo: text("parking_info"),
  loadInInfo: text("load_in_info"),
  contactPersonName: text("contact_person_name").notNull(),
  contactPhoneNumber: text("contact_phone_number").notNull(),
  contactEmail: text("contact_email").notNull(),
  notes: text("notes"),
}, () => []);
export type Venue = typeof Venues.$inferSelect;

export const Tours = sqliteTable("tours", {
  id: text("id").primaryKey(),
  name: text("name").notNull(),
  description: text("description"),
  url: text("url"),
  startDate: text("start_date").notNull(),
  endDate: text("end_date").notNull(),
}, () => []);

export const Performances = sqliteTable("performances", {
  id: text("id").primaryKey(),
  artistId: text("artist_id")
    .notNull()
    .references(() => Artists.artistId),
  venueId: text("venue_id")
    .notNull()
    .references(() => Venues.venueId),
  startTime: text("start_time").notNull(),
  endTime: text("end_time").notNull(),
  tourId: text("tour_id")
    .notNull()
    .references(() => Tours.id),
}, () => []);
