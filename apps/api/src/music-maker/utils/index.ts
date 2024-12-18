import { Artist, Venue } from "../types";

export async function getArtistData(artistId: string): Promise<Artist> {
  setTimeout(() => {}, 1000);

  return {
    artistId,
    name: "The Jazz Cats",
    genre: "jazz",
    avgTicketPrice: 50,
    avgAttendance: 500,
  };
}

export async function getVenue(venueId: string): Promise<Partial<Venue>> {
  setTimeout(() => {}, 1000);
  return {
    venueId,
    venueName: "The Hono Jazz Club",
    maxCapacity: 1000,
  };
}
