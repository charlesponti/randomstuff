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
