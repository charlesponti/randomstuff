import { createMiddleware } from "hono/factory";
import { Artist } from "../types";

export const authMiddleware = createMiddleware<{
  Variables: {
    artist: Artist;
  };
}>(async (c, next) => {
  c.set("artist", {
    artistId: "123",
    name: "The Jazz Cats",
    genre: "jazz",
    avgTicketPrice: 50,
    avgAttendance: 500,
  });
  next();
});
