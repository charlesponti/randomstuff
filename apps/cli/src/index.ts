import process from "node:process";
import { Command } from "commander";

import aiCommand from "./ai/index.ts";
import scrapeCommand from "./commands/scrape.ts";
import financeCommand from "./finance/index.ts";
import googleCommand from "./google/cli.js";

const program = new Command();

program.version("1.0.0").description("Collection of useful tools");

program.addCommand(scrapeCommand);
program.addCommand(aiCommand);
program.addCommand(financeCommand);
program.addCommand(googleCommand);

program.parse(process.argv);
