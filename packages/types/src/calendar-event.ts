import { FinancialTransaction } from "./finance";
import { Place } from "./location";
import { Person } from "./people";
import { Route } from "./travel-route";

export type CalendarEvent = {
  id: string;

  /**
   * The date when the event occurred.
   */
  date: string;

  /**
   * The time when the event occurred.
   */
  time: string;

  /**
   * The name of the event.
   */
  name: string;

  /**
   * The description of the event.
   */
  description: string;

  /**
   * Logical tags based on the type of event, location, etc.
   * Helpful for semantic search.
   */
  tags: string[];

  /**
   * The location ID where the event occurred.
   */
  locationId: Place["id"];

  /**
   * List of user IDs who attended the event.
   */
  attendees: Person["id"][];

  /**
   * List of financial transaction IDs associated with this event.
   */
  transactionIds: FinancialTransaction["id"][];

  /**
   * The route ID associated with this event.
   */
  routeId: Route["id"];
};

export type TransportationRoute = {
  id: string;

  /**
   * The name of the route.
   */
  name: string;

  /**
   * The description of the route.
   */
  description: string;

  /**
   * The mode of transportation for this route.
   */
  mode: string;

  /**
   * The start location ID for this route.
   */
  startLocationId: string;

  /**
   * The end location ID for this route.
   */
  endLocationId: string;

  /**
   * The duration of the route in seconds.
   */
  duration: number;

  /**
   * The route ID associated with this route.
   */
  routeId: Route["id"];
};

export function getEventsByLocationId(
  locationId: string,
  events: CalendarEvent[],
): CalendarEvent[] {
  return events.filter((event) => event.locationId === locationId);
}
