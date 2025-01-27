import { ChatOpenAI } from '@langchain/openai'
import { AgentExecutor, createToolCallingAgent } from 'langchain/agents'
import { ChatPromptTemplate } from '@langchain/core/prompts'
import { tool } from '@langchain/core/tools'

const factCheckerTool = tool(
  async function call(input: string): Promise<string> {
    return `Fact-check result for "${input}": All facts seem correct.`
  },
  {
    name: 'fact-checker',
    description: 'Checks the input for factual correctness',
  }
)

const grammarCheckerTool = tool(
  async function call(input: string): Promise<string> {
    return `Grammar-check result for "${input}": No errors found.`
  },
  {
    name: 'grammar-checker',
    description: 'Checks the input for spelling and grammatical errors',
  }
)

const sentimentAnalysisTool = tool(
  async function call(input: string): Promise<string> {
    return `Sentiment analysis for "${input}": Positive.`
  },
  {
    name: 'sentiment-analysis',
    description: 'Analyzes the sentiment of the input text',
  }
)

const tools = [factCheckerTool, grammarCheckerTool, sentimentAnalysisTool]

const model = new ChatOpenAI({
  temperature: 0,
  streaming: true,
})

const prompt = ChatPromptTemplate.fromMessages([
  ['system', 'You are a helpful assistant'],
  ['placeholder', '{chat_history}'],
  ['human', '{input}'],
  ['placeholder', '{agent_scratchpad}'],
])

const agent = createToolCallingAgent({
  llm: model,
  tools,
  prompt,
})

const agentExecutor = new AgentExecutor({
  agent,
  tools,
  maxIterations: 3,
  returnIntermediateSteps: true,
})

export async function POST(req: Request) {
  try {
    const body = await req.json()

    if (!body.input || typeof body.input !== 'string') {
      return Response.json({ error: 'Input must be a non-empty string' }, { status: 400 })
    }

    const result = await agentExecutor.invoke({
      input: body.input,
      chat_history: body.chat_history || [],
    })

    return Response.json({
      output: result.output,
      steps: result.intermediateSteps,
    })
  } catch (error) {
    console.error('Agent execution failed:', error)
    return Response.json({ error: 'Failed to process input' }, { status: 500 })
  }
}
