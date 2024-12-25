import { openai } from "@ai-sdk/openai";
import { google } from "@ai-sdk/google";
import * as mathjs from "mathjs";
import { generateText, tool } from "ai";
import "dotenv/config";
import { z } from "zod";

export async function toolCall({ prompt }: { prompt: string }) {
  const response = await generateText({
    model: openai("gpt-4o-2024-08-06", { structuredOutputs: true }),
    tools: {
      calculate: tool({
        description:
          "A tool for evaluating mathematical expressions. Example expressions: " +
          "'1.2 * (2 + 4.5)', '12.7 cm to inch', 'sin(45 deg) ^ 2'.",
        parameters: z.object({ expression: z.string() }),
        execute: async ({ expression }: { expression: string }) =>
          mathjs.evaluate(expression),
      }),
      // answer tool: the LLM will provide a structured answer
      answer: tool({
        description: "A tool for providing the final answer.",
        parameters: z.object({
          steps: z.array(
            z.object({
              calculation: z.string(),
              reasoning: z.string(),
            }),
          ),
          answer: z.string(),
        }),
        // no execute function - invoking it will terminate the agent
      }),
    },
    toolChoice: "required",
    maxSteps: 10,
    system: "You are solving math problems. " +
      "Reason step by step. " +
      "Use the calculator when necessary. " +
      "The calculator can only do simple additions, subtractions, multiplications, and divisions. " +
      "When you give the final answer, provide an explanation for how you got it.",
    prompt,
  });

  return response;
}

export async function cityInfoToolCall({ prompt }: { prompt: string }) {
  const response = await generateText({
    model: google("gemini-1.5-pro-latest", { structuredOutputs: true }),
    // model: openai("gpt-4o-2024-08-06", { structuredOutputs: true }),
    tools: {
      get_location_info: tool({
        description: "A tool for getting information about a city.",
        parameters: z.object({ city: z.string() }),
        execute: async ({ city }: { city: string }) => {
          return `Information about ${city}`;
        },
      }),
      get_driving_directions: tool({
        description: "A tool for getting driving directions to a city.",
        parameters: z.object({ city: z.string() }),
        execute: async ({ city }: { city: string }) => {
          return `Driving directions to ${city}`;
        },
      }),
      get_weather: tool({
        description: "A tool for getting the current weather in a city.",
        parameters: z.object({ city: z.string() }),
        execute: async ({ city }: { city: string }) => {
          return `Current weather in ${city}`;
        },
      }),
      answer: tool({
        description: "A tool for providing the final answer.",
        parameters: z.object({
          steps: z.array(
            z.object({ stepName: z.string() }),
          ),
          answer: z.string(),
        }),
      }),
    },
    toolChoice: "required",
    maxSteps: 10,
    system: "You are providing information about cities. " +
      "Use the appropriate tools to provide the user with the information they require about the location provided." +
      "Provide detailed and accurate information.",
    prompt,
  });

  return response;
}

export async function eventInfoToolCall({ prompt }: { prompt: string }) {
  const response = await generateText({
    model: google("gemini-1.5-pro-latest", { structuredOutputs: true }),
    tools: {
      get_event_finances_by_id: tool({
        description: "A tool for getting financial data for an event.",
        parameters: z.object({ eventId: z.string() }),
        execute: async ({ eventId }: { eventId: string }) => {
          return [
            { date: "2023-10-01", revenue: 1000, expenses: 500, eventId: 1 },
            { date: "2023-10-02", revenue: 1500, expenses: 700, eventId: 2 },
            { date: "2023-10-03", revenue: 2000, expenses: 800, eventId: 3 },
            { date: "2023-10-04", revenue: 2500, expenses: 900, eventId: 4 },
            { date: "2023-10-05", revenue: 3000, expenses: 1000, eventId: 5 },
          ];
        },
      }),
      get_events: tool({
        description: "A tool to get one or more events by id, name, or date.",
        parameters: z.object({
          query: z.object({
            eventName: z.string().optional(),
            eventId: z.string().optional(),
            eventDate: z.string().optional(),
          }),
        }),
        execute: async ({ query }: { query: any }) => {
          return [
            { id: 1, date: "2023-10-01", event: "Coachella" },
            { id: 2, date: "2023-10-02", event: "Eras Tour" },
            { id: 3, date: "2023-10-03", event: "Big Concert" },
            { id: 4, date: "2023-10-04", event: "Medium-sized Concert" },
            { id: 5, date: "2023-10-05", event: "Small Concert" },
          ];
        },
      }),
      get_ticket_sales_by_event_id: tool({
        description: "A tool for getting ticket sales data for an event.",
        parameters: z.object({
          query: z.object({
            eventId: z.string().optional(),
          }),
        }),
        execute: async ({ query }: { query: any }) => {
          return [
            { date: "2023-10-01", ticketsSold: 100, eventId: 1 },
            { date: "2023-10-02", ticketsSold: 150, eventId: 2 },
            { date: "2023-10-03", ticketsSold: 200, eventId: 3 },
            { date: "2023-10-04", ticketsSold: 250, eventId: 4 },
            { date: "2023-10-05", ticketsSold: 300, eventId: 5 },
          ];
        },
      }),
      answer: tool({
        description: "A tool for providing the final answer.",
        parameters: z.object({
          steps: z.array(
            z.object({
              stepName: z.string(),
              stepArguments: z.any(),
            }),
          ),
          answer: z.string(),
        }),
      }),
    },
    toolChoice: "required",
    maxSteps: 10,
    system: "You are providing information about events. " +
      "Use the appropriate tools to provide the user with the information they require about the event provided." +
      "Provide detailed and accurate information.",
    prompt,
  });

  return response;
}
