import { Command } from 'commander'
import { cityInfoToolCall, eventInfoToolCall, toolCall } from './tools'

const program = new Command()

program.name('ai')

program
  .command('tool-call')
  .description('AI tools')
  .requiredOption('-t, --text <text>', 'Text to analyze')
  .action(async (options) => {
    const response = await toolCall({
      prompt: `
        A taxi driver earns $9461 per 1-hour work.
        If he works 12 hours a day and in 1 hour he uses 14-liters petrol with price $134 for 1-liter.
        How much money does he earn in one day?
      `,
    })

    console.log(`FINAL TOOL CALLS: ${JSON.stringify(response.toolCalls, null, 2)}`)
  })

program
  .command('city-info')
  .description('City info tool')
  .requiredOption('-c, --city <city>', 'City name')
  .action(async (options) => {
    const response = await cityInfoToolCall({
      prompt: options.city,
    })

    console.log(`City info: ${JSON.stringify(response, null, 2)}`)
  })

program
  .command('event-info')
  .description('Event info tool')
  .requiredOption('-q, --query <query>', 'Query')
  .action(async (options) => {
    const response = await eventInfoToolCall({ prompt: options.query })
    console.log(`Event info: ${JSON.stringify(response.toolCalls, null, 2)}`)
  })
export default program
