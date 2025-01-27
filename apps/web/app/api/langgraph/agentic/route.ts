import { type BaseMessage, type AIMessage, HumanMessage } from '@langchain/core/messages'
import { tool } from '@langchain/core/tools'
import { z } from 'zod'
import { ChatOpenAI } from '@langchain/openai'
import { StateGraph } from '@langchain/langgraph'
import { MemorySaver, Annotation, messagesStateReducer } from '@langchain/langgraph'
import { ToolNode, createReactAgent } from '@langchain/langgraph/prebuilt'

// Define the graph state
// See here for more info: https://langchain-ai.github.io/langgraphjs/how-tos/define-state/
const StateAnnotation = Annotation.Root({
  messages: Annotation<BaseMessage[]>({
    // `messagesStateReducer` function defines how `messages` state key should be updated
    // (in this case it appends new messages to the list and overwrites messages with the same ID)
    reducer: messagesStateReducer,
  }),
})

// Define the tools for the agent to use
const weatherTool = tool(
  async ({ location }) => {
    return `The weather in ${location} is 90 degrees and sunny.`
  },
  {
    name: 'current_weather',
    description: 'Call to get the current weather for a location.',
    schema: z.object({
      location: z.string().describe('The location to get the weather for.'),
    }),
  }
)

const transportationCostTool = tool(
  async ({ startingLocation, endingLocation }) => {
    return `Traveling from ${startingLocation} to ${endingLocation} costs $100.`
  },
  {
    name: 'transportation_cost',
    description: 'Call to get the cost of transportation between locations.',
    schema: z.object({
      startingLocation: z.string().optional().describe('The starting location.'),
      endingLocation: z.string().optional().describe('The ending location.'),
    }),
  }
)

const tools = [weatherTool, transportationCostTool]
const toolNode = new ToolNode(tools)

// Define the model
const model = new ChatOpenAI({
  model: 'gpt-4', // Changed from gpt-4o-mini to supported model
  temperature: 0,
})

// Bind the tools to the model
model.bindTools(tools)

const agent = createReactAgent({ llm: model, tools })

// Define the function that determines whether to continue or not
// We can extract the state typing via `StateAnnotation.State`
function shouldContinue(state: typeof StateAnnotation.State) {
  const messages = state.messages
  const lastMessage = messages[messages.length - 1] as AIMessage

  // If the LLM makes a tool call, then we route to the "tools" node
  if (lastMessage.tool_calls?.length) {
    return 'tools'
  }

  // Otherwise, we stop (reply to the user)
  return '__end__'
}

// Define the function that calls the model
async function callModel(state: typeof StateAnnotation.State) {
  const messages = [
    new HumanMessage(
      'You are a helpful assistant with access to tools. Always use tools when appropriate. ' +
        'After using a tool, explain what you found.'
    ),
    ...state.messages,
  ]

  try {
    const response = await model.invoke(messages)
    console.log('Model response:', response) // Debug logging
    return { messages: [response] }
  } catch (error) {
    console.error('Error calling model:', error)
    throw error
  }
}

// Define a new graph
const workflow = new StateGraph(StateAnnotation)
  .addNode('agent', callModel)
  .addNode('tools', toolNode)
  .addEdge('__start__', 'agent')
  .addConditionalEdges('agent', shouldContinue)
  .addEdge('tools', 'agent')

// Initialize memory to persist state between graph runs
const checkpointer = new MemorySaver()

// Finally, we compile it!
// This compiles it into a LangChain Runnable.
// Note that we're (optionally) passing the memory when compiling the graph
const app = workflow.compile({ checkpointer })

export async function POST(req: Request) {
  const { message } = (await req.json()) as { message: string }
  const messages = [new HumanMessage(message)]

  try {
    // const finalState = await app.invoke(
    //   { messages },
    //   { configurable: { thread_id: "42" } }
    // );
    // console.log("Final state:", JSON.stringify(finalState.messages, null, 2));
    // return Response.json(finalState.messages, { status: 200 });

    const foo = await agent.invoke({ messages })
    return Response.json(foo.messages, { status: 200 })
  } catch (error) {
    console.error('Error in POST handler:', error)
    return Response.json({ error: 'Internal Server Error' }, { status: 500 })
  }
}
