
"""
PANDAS DON 🕴️ — DAY 02
Mission: Multi-condition filtering and ranking.

REASONING:
1. NumPy arrays hold the raw stats; Pandas organizes them into a DataFrame.
2. Power, Speed, and Stamina are numerical attributes, so sum(axis=1)
   and mean(axis=1) calculate each knight's stats across columns.
3. Elite is derived from Average >= 80, so it should be a Boolean column.
4. Filtering needs a Boolean Series for each row. Use & when BOTH
   conditions must be true, and | when EITHER condition may be true.
5. Each comparison needs parentheses because Pandas Series comparisons
   must be combined with &, | rather than Python's and/or.
6. sort_values() creates a ranking by Total. ascending=False puts the
   highest score first.

DESIGN PRINCIPLE:
Keep raw data, derived columns, filtering, and ranking distinct.
This makes the analysis easier to inspect, modify, and extend.
"""

import numpy as np
import pandas as pd

names = np.array(["KIRTI", "ROY"])
power = np.array([87, 64])
speed = np.array([91, 78])
stamina = np.array([84, 73])

df = pd.DataFrame({
    "Knight": names,
    "Power": power,
    "Speed": speed,
    "Stamina": stamina
})

stats = ["Power", "Speed", "Stamina"]

df["Total"] = df[stats].sum(axis=1)
df["Average"] = df[stats].mean(axis=1)
df["Elite"] = df["Average"] >= 80

# Both conditions must be true.
qualified = df[
    (df["Speed"] > 80) &
    (df["Stamina"] >= 80)
]

# At least one condition must be true.
high_performance = df[
    (df["Power"] >= 85) |
   (df["Speed"] >= 85)
]

# Highest Total comes first.
ranking = df.sort_values("Total", ascending=False)

print("FULL DATA:")
print(df)

print("\nQUALIFIED KNIGHTS:")
print(qualified)

print("\nHIGH-PERFORMANCE KNIGHTS:")
print(high_performance)

print("\nRANKING:")
print(ranking[["Knight", "Total", "Average"]])