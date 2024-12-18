import { calculatePerformanceFinancialProjection } from "./finance";
import { describe, expect, it } from "vitest";

describe("calculatePerformanceFinancialProjection", () => {
  it("should calculate the correct financial projection", () => {
    const result = calculatePerformanceFinancialProjection({
      ticketPrice: 50,
      attendance: 100,
      totalExpenses: 20,
    });

    expect(result).toEqual({
      revenue: 5000,
      expenses: 20,
      profit: 4980,
    });
  });

  it("should handle zero attendance", () => {
    const result = calculatePerformanceFinancialProjection({
      ticketPrice: 50,
      attendance: 0,
      totalExpenses: 20,
    });

    expect(result).toEqual({
      revenue: 0,
      expenses: 20,
      profit: -20,
    });
  });

  it("should handle zero ticket price", () => {
    const result = calculatePerformanceFinancialProjection({
      ticketPrice: 0,
      attendance: 100,
      totalExpenses: 20,
    });

    expect(result).toEqual({
      revenue: 0,
      expenses: 20,
      profit: -20,
    });
  });

  it("should handle zero costs", () => {
    const result = calculatePerformanceFinancialProjection({
      ticketPrice: 50,
      attendance: 100,
      totalExpenses: 0,
    });

    expect(result).toEqual({
      revenue: 5000,
      expenses: 0,
      profit: 5000,
    });
  });

  describe("should handle negative values", () => {
    it("should handle negative ticket price", () => {
      const result = () =>
        calculatePerformanceFinancialProjection({
          ticketPrice: -50,
          attendance: 100,
          totalExpenses: 200,
        });

      expect(result).toThrowError("Ticket price must be positive");
    });
    it("should handle negative attendance", () => {
      const result = () =>
        calculatePerformanceFinancialProjection({
          ticketPrice: 50,
          attendance: -100,
          totalExpenses: 200,
        });

      expect(result).toThrowError("Attendance must be positive");
    });
    it("should handle negative costs", () => {
      const result = () =>
        calculatePerformanceFinancialProjection({
          ticketPrice: 50,
          attendance: 100,
          totalExpenses: -200,
        });

      expect(result).toThrowError("Total expenses must be positive");
    });
  });
});
