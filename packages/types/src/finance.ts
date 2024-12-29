export type TransactionType = "credit" | "debit" | "transfer" | "investment";

export interface FinancialTransaction {
  id: string;
  type: TransactionType;
  amount: number;
  date: Date;
  description?: string;
  fromAccount?: string;
  toAccount?: string;
  investmentDetails?: {
    assetType: string;
    quantity: number;
    pricePerUnit: number;
  };
}
