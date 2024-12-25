import { Hono } from "hono";
import { cors } from "hono/cors";

import venueApi from "./music-maker/venue";

type Bindings = {
  ENV: string;
  API_ORIGIN: string;
};

const app = new Hono<{ Bindings: Bindings }>();

app.use(
  "api/*",
  async (c, next) => {
    cors({
      origin: c.env.API_ORIGIN,
      allowMethods: ["GET", "POST"],
      allowHeaders: ["Content-Type"],
      maxAge: 600,
    });
  },
);

app.get("/", (c) => {
  return c.text("Hello Hono!");
});

app.route("/music-maker", venueApi);

export default app;
