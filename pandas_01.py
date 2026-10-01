import numpy as np
import pandas as pd

names = np.array([ "KIRTI","ROY" ])
power = np.array([87, 64])
speed = np.array([91, 78])
stamina = np.array([84, 73])

df = pd.DataFrame({
    "Knight": names,
    "Power": power,
    "Speed": speed,
    "Stamina": stamina
})

df["Total"] = df[["Power", "Speed", "Stamina"]].sum(axis=1)
df["Average"] = df[["Power", "Speed", "Stamina"]].mean(axis=1)
df["Elite"] = df["Average"] >= 80

print(df)
print("\nELITE KNIGHTS:")
print(df[df["Elite"]])
