import { Hono } from "hono";
import { HTTPException } from "hono/http-exception";

import { calculatePerformanceFinancialProjection } from "./utils/finance";
import { authMiddleware } from "./utils/auth";
import { getVenue } from "./utils";

const musicMaker = new Hono();

function getProjectedAttendance(
  { maxCapacity, avgAttendance, query }: {
    maxCapacity?: number;
    avgAttendance?: number;
    query: Record<string, string>;
    artist: { avgAttendance: number; avgTicketPrice: number };
  },
): number {
  let attendance: number;
  if (query.attendance) {
    try {
      attendance = Number(query.attendance);
    } catch (e) {
      throw Error("Invalid attendance value");
    }

    if (maxCapacity && attendance > maxCapacity) {
      throw Error("Attendance exceeds venue capacity");
    }
  } else if (avgAttendance) {
    attendance = avgAttendance;
  } else if (maxCapacity) {
    attendance = maxCapacity * 0.8;
  } else {
    attendance = 0;
  }

  return attendance;
}

musicMaker.get("/venue/:venueId", authMiddleware, async (c) => {
  const query = c.req.query();
  const venueId = c.req.param("venueId");

  const { artist } = c.var;
  const venue = await getVenue(venueId);

  const ticketPrice = Number(query.ticketPrice) ||
    artist.avgTicketPrice;

  const attendance = getProjectedAttendance({
    maxCapacity: venue.maxCapacity,
    avgAttendance: artist.avgAttendance,
    query,
    artist,
  });

  if (ticketPrice < 0 || attendance < 0) {
    throw new HTTPException(400, {
      message: "Ticket price and attendance must be positive",
    });
  }

  let totalExpenses = 0;
  if (query.cost) {
    try {
      totalExpenses = Number(query.cost);
    } catch (e) {
      throw new HTTPException(400, {
        message: "Invalid cost value",
      });
    }
  }

  const projection = calculatePerformanceFinancialProjection({
    ticketPrice,
    attendance,
    totalExpenses,
  });

  return c.json({
    venue,
    projection,
  });
});

export default musicMaker;
