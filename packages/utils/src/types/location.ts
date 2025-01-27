import type { CalendarEvent } from "./calendar-event.ts";
import type { Person } from "./people.ts";

export type PlaceVisit = {
  eventId: CalendarEvent["id"];

  placeId: Place["id"];

  /**
   * The meal that the user had at this place.
   */
  notes: string;

  /**
   * The rating that the user gave to this place.
   */
  rating: number;

  /**
   * The review that the user wrote for this place.
   */
  review: string;

  /**
   * List of user IDs of people who were with the user at this place.
   */
  people: string[];
};

export type Place = {
  id: string;

  /**
   * The Google Maps ID for this place.
   */
  googleMapsId: string;

  /**
   * The latitude and longitude of this place.
   */
  lat: number;
  lng: number;

  name: string;

  /**
   * The meal that this place is best for.
   *
   * For instance, if the user wants to visit this place for breakfast,
   * this field will be set to `["breakfast"]`.
   */
  best_for: string[];

  /**
   * The address of the place.
   */
  address: string;

  /**
   * The date when the user visited this place.
   */
  visits: PlaceVisit[];

  /**
   * Indicates if the place is public or private.
   */
  isPublic: boolean;

  /**
   * List of user IDs who have access to this place.
   */
  sharedWith: string[];

  /**
   * Tags for the place.
   */
  tags: string[];

  /**
   * List of event IDs associated with this place.
   */
  eventIds: string[];

  /**
   * List of financial transaction IDs associated with this place.
   */
  transactionIds: string[];

  /**
   * List of user IDs tagged in this place.
   */
  people: Person["id"][];

  /**
   * Information about the location's wifi.
   * An array is used because places can have multiple available wifi options.
   */
  wifi_info: WifiInfo[];
};

interface WifiInfo {
  /**
   * The WiFi network name.
   */
  network: string;

  /**
   * The WiFi password.
   */
  password: string;
}

export type Waypoint = {
  latitude: number; // Latitude in decimal degrees
  longitude: number; // Longitude in decimal degrees
  elevation?: number; // Optional elevation in meters
  timestamp?: Date; // Optional timestamp for the waypoint
};

export type Route = {
  id: string; // Unique identifier for the route
  name?: string; // Optional name of the route
  waypoints: Waypoint[]; // List of waypoints
  distance: number; // Distance in meters
};
