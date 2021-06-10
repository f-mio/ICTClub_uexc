import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("data.csv", parse_dates=["date"])

plt.plot(df["date"], df["t"])

plt.ylim([15, 30])

plt.xlabel("date")
plt.ylabel("temperature (Celsius)")
plt.grid()

plt.savefig("graph.png")