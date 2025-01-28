import { openai } from "@ai-sdk/openai";
import { generateObject, generateText } from "ai";
import assert from "node:assert";
import { z } from "zod";
import {
	get_performance_location_suggestions,
	performanceCostCalculatorTool,
	transportationCostCalculatorTool,
	accommodationCostCalculatorTool,
} from "@/lib/tour.tools";

const { OPENAI_API_KEY } = process.env;
assert(OPENAI_API_KEY, "Missing OPENAI_API_KEY");

async function tourAgent(message: string) {
	const messages = [{ message }];
	const model = openai("gpt-4o-2024-08-06", { structuredOutputs: true });
	const result = await generateObject({
		model,
		prompt: `Get the locations from this message: ${message}`,
		schema: z.object({
			locations: z.array(z.string()),
		}),
	});
	const { locations } = result.object;

	if (!locations.length) {
		messages.push({ message: "Please provide a location" });
	} else {
		const { response } = await generateText({
			model,
			prompt: `
        Create a tour plan using the available tools for the following locations: 
        ${locations.join(", ")}

        Provide the user with the locations and costs for the tour.
      `,
			tools: {
				get_performance_location_suggestions,
				performanceCostCalculatorTool,
				transportationCostCalculatorTool,
				accommodationCostCalculatorTool,
				// answer: tool({
				//   description: "A tool for providing the final answer.",
				//   parameters: z.object({
				//     plan: z.array(z.object({ locationPlan: z.string() })),
				//   }),
				// }),
			},
			maxSteps: 5,
			// toolChoice: "required",
		});

		return response;
	}

	return { messages };
}

export async function POST(req: Request) {
	const { message } = await req.json();
	try {
		const response = await tourAgent(message);
		return Response.json(response, { status: 200 });
	} catch (error) {
		console.log(error);
		return Response.json({ error: error.message }, { status: 500 });
	}
}
