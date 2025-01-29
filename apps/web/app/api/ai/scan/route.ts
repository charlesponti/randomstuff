import { ChatOpenAI } from "@langchain/openai";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import { tool } from "@langchain/core/tools";
import { ToolNode } from "@langchain/langgraph/prebuilt";
import z from "zod";

const factCheckerTool = tool(
	async function call({ input }: { input: string }): Promise<string> {
		return `Fact-check result for "${input}": All facts seem correct.`;
	},
	{
		name: "fact-checker",
		description: "Checks the input for factual correctness",
		schema: z.object({
			input: z.string(),
		}),
	},
);

const grammarCheckerTool = tool(
	async function call({ input }: { input: string }): Promise<string> {
		return `Grammar-check result for "${input}": No errors found.`;
	},
	{
		name: "grammar-checker",
		description: "Checks the input for spelling and grammatical errors",
		schema: z.object({
			input: z.string(),
		}),
	},
);

const sentimentAnalysisTool = tool(
	async function call({ input }: { input: string }): Promise<string> {
		return `Sentiment analysis for "${input}": Positive.`;
	},
	{
		name: "sentiment-analysis",
		description: "Analyzes the sentiment of the input text",
		schema: z.object({
			input: z.string(),
		}),
	},
);

const tools = [factCheckerTool, grammarCheckerTool, sentimentAnalysisTool];
const toolNode = new ToolNode(tools);

const model = new ChatOpenAI({
	model: "gpt-4o-mini",
	temperature: 0,
	streaming: true,
}).bindTools(tools);

const prompt = ChatPromptTemplate.fromMessages([
	["system", "You are a helpful assistant"],
	["placeholder", "{chat_history}"],
	["human", "{input}"],
	["placeholder", "{agent_scratchpad}"],
]);

export async function POST(req: Request) {
	try {
		const body = await req.json();

		if (!body.input || typeof body.input !== "string") {
			return Response.json(
				{ error: "Input must be a non-empty string" },
				{ status: 400 },
			);
		}

		const result = await model.invoke(body.input);

		const calls = await toolNode.invoke({ messages: [result] });

		return Response.json(calls);
	} catch (error) {
		console.error("Agent execution failed:", error);
		return Response.json({ error: "Failed to process input" }, { status: 500 });
	}
}
