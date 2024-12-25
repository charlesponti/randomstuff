import { Venue } from "../types";

export async function getVenue(venueId: string): Promise<Partial<Venue>> {
  setTimeout(() => {}, 1000);
  return {
    venueId,
    venueName: "The Hono Jazz Club",
    maxCapacity: 1000,
  };
}
