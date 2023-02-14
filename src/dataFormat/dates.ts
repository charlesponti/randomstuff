/**
 * This file is used to fix the dates in the movie data.
 *
 * In some cases, the dates are not in the correct format. The dates were
 * originally in the format of "DD/MM/YYYY" and were making it impossible to
 * properly sort the rows in the Google Sheet.
 *
 * This file:
 * 1. converts the dates to the correct format: "YYYY-MM-DD".
 * 2. Dumps the dates into text file: dates.txt.
 */

import fs from 'fs';

export function dateFormat(dates: string[], dateFormat: string) {
  fs.writeFileSync(
    'dates.txt',
    dates
      .map((date: string) => {
        if (dateFormat === 'dd/mm/yyyy') {
          const [day, month, year] = date.split('/');
          return `${year}-${month}-${day}\n`;
        }
        const [day, month, year] = date.split('/');
        return `${year}-${month}-${day}\n`;
      })
      .join('')
  );
}
