import { eq, type SQL } from "drizzle-orm";
import type { connectToDatabase } from "../db/index.ts";
import {
  job_applications,
  type JobApplication,
  type NewJobApplication,
} from "./job-applications.schema.ts";

export class ApplicationService {
  constructor(private db: ReturnType<typeof connectToDatabase>) {}

  async create(data: NewJobApplication) {
    const [result] = await this.db
      .insert(job_applications)
      .values(data)
      .returning();
    return result;
  }

  async update(id: string, data: Partial<NewJobApplication>) {
    const [result] = await this.db
      .update(job_applications)
      .set({
        ...data,
        updatedAt: new Date(),
      })
      .where(eq(job_applications.id, id))
      .returning();
    return result;
  }

  async findById(id: string) {
    return await this.db
      .select()
      .from(job_applications)
      .where(eq(job_applications.id, id));
  }

  async findMany(query?: SQL<JobApplication>) {
    return await this.db.select().from(job_applications).where(query);
  }

  async delete(id: string) {
    const [result] = await this.db
      .delete(job_applications)
      .where(eq(job_applications.id, id))
      .returning();
    return result;
  }
}
