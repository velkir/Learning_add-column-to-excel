import pandas as pd

df = pd.read_excel("input.xlsx")

print(df)

df["Total"] = df["Price"]*df["Quantity"]
print(df)

df.to_excel("output.xlsx", columns=df.columns)