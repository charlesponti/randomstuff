import { eq, type SQL } from "drizzle-orm";
import type { connectToDatabase } from "../db/connection.ts";
import {
	companies,
	type Company,
	type NewCompany,
} from "../db/schema/company.schema.ts";

export class CompanyService {
	constructor(private db: ReturnType<typeof connectToDatabase>) {}

	async create(
		data: Omit<NewCompany, "id" | "version" | "createdAt" | "updatedAt">,
	) {
		const [result] = await this.db.insert(companies).values(data).returning();
		return result;
	}

	async update(id: string, data: Partial<NewCompany>) {
		const [result] = await this.db
			.update(companies)
			.set({
				...data,
				updatedAt: new Date(),
				version: (Number(data.version || 1) + 1).toString(),
			})
			.where(eq(companies.id, id))
			.returning();
		return result;
	}

	async findById(id: string) {
		return await this.db.select().from(companies).where(eq(companies.id, id));
	}

	async findMany(query: SQL<Company>) {
		return await this.db.select().from(companies).where(query);
	}

	async delete(id: string) {
		const [result] = await this.db
			.delete(companies)
			.where(eq(companies.id, id))
			.returning();
		return result;
	}
}
