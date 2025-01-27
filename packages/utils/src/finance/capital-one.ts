// import { type FinancialTransaction, FinancialTransactionType } from ".";
import { randomUUID } from "node:crypto";

export interface CapitalOneTransaction {
	"Account Number": string;
	"Transaction Date": string;
	"Transaction Amount": string;
	"Transaction Type": string;
	"Transaction Description": string;
	Balance: string;
}

export function getCapitalOneTransactionType(
	type: string,
): FinancialTransactionType {
	return type === "Credit"
		? FinancialTransactionType.credit
		: FinancialTransactionType.debit;
}

export function convertCapitalOneTransaction(
	t: CapitalOneTransaction,
): FinancialTransaction {
	return {
		id: randomUUID(),
		description: t["Transaction Description"],
		amount: Number.parseFloat(t["Transaction Amount"]),
		date: new Date(t["Transaction Date"]),
		type: getCapitalOneTransactionType(t["Transaction Type"]),
	};
}
