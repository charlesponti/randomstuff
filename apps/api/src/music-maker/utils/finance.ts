export function calculatePerformanceFinancialProjection({
  ticketPrice,
  attendance,
  totalExpenses,
}: {
  totalExpenses: number;
  ticketPrice: number;
  attendance: number;
}) {
  if (attendance < 0) {
    throw Error("Attendance must be positive");
  }

  if (ticketPrice < 0) {
    throw Error("Ticket price must be positive");
  }

  if (totalExpenses < 0) {
    throw Error("Total expenses must be positive");
  }

  const projectedRevenue = ticketPrice * attendance;
  const projectedProfit = projectedRevenue - totalExpenses;

  return {
    revenue: projectedRevenue,
    expenses: totalExpenses,
    profit: projectedProfit,
  };
}
