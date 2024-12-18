export type Artist = {
  artistId: string;
  name: string;
  genre: string;
  avgTicketPrice: number;
  avgAttendance: number;
};

export type Venue = {
  venueId: string;
  venueName: string;
  addressLine1: string;
  addressLine2: string;
  city: string;
  state: string;
  postalCode: string;
  country: string;
  venueType: string;
  audienceStyle: number;
  maxCapacity: number;
  hasAudioSystem: boolean;
  audioSystemType: string;
  hasLightingSystem: boolean;
  lightingSystemType: string;
  stageType: string;
  stageDimensions: string;
  backstageArea: boolean;
  greenRoom: boolean;
  parkingInfo: string;
  loadInInfo: string;
  contactPersonName: string;
  contactPhoneNumber: string;
  contactEmail: string;
  notes: string;
};

export type Tour = {
  id: string;
  name: string;
  description: string;
  url: string;
  startDate: string;
  endDate: string;
};

export type Performance = {
  id: string;
  artistId: string;
  venueId: Venue["venueId"];
  startTime: string;
  endTime: string;
  tourId: Tour["id"];
};
