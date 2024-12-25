import { Artist } from "../types";

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
