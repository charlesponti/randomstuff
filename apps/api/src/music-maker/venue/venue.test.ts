import { describe, expect, test } from "vitest";

import venueApi from ".";

describe("venue", () => {
  test("GET venue projection", async () => {
    const res = await venueApi.request(
      "/venue/456?ticketPrice=50&attendance=100",
    );
    expect(res.status).toBe(200);
    expect(await res.json()).toEqual({
      venue: {
        venueId: "456",
        venueName: "The Hono Jazz Club",
        maxCapacity: 1000,
      },
      projection: {
        revenue: 5000,
        expenses: 0,
        profit: 5000,
      },
    });
  });

  test("GET venue projection with cost", async () => {
    const res = await venueApi.request(
      "/venue/456?ticketPrice=50&attendance=100&cost=20",
    );
    expect(res.status).toBe(200);
    expect(await res.json()).toEqual({
      venue: {
        venueId: "456",
        venueName: "The Hono Jazz Club",
        maxCapacity: 1000,
      },
      projection: {
        revenue: 5000,
        expenses: 20,
        profit: 4980,
      },
    });
  });
});
