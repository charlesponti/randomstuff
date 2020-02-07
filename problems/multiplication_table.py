from typing import List

import numpy as np
import pandas as pd


def multiplication_table(max: int) -> List:
    """
    Create a grid containing the multiplication table up
    a max.
    """
    rows = []

    for i in range(1, max + 1):
        inner_row = []

        for j in range(1, max + 1):
            inner_row.append(j * i)

        rows.append(inner_row)

    return rows


def grid_to_strings(rows: list):
    ""
    for row in rows:
        row_as_string = ""
        for num in row:
            row_as_string += str(num) + " "

        print(row_as_string)


rows = pd.DataFrame(multiplication_table(12))

if __name__ == "main":
    print(rows.describe())
