import pandas as pd
import matplotlib.pyplot as plt
url = "https://en.wikipedia.org/wiki/Minnesota"
dfs = pd.read_html(url, match = "Historical population")

df = dfs[0]
df = df.iloc[0:-2]
df = df[["Census", "Pop."]].astype("int")
print(df.info())
df.plot(x = "Census", y = "Pop.")

url = "https://en.wikipedia.org/wiki/Minnesota"
ds = pd.read_html(url, match = "Religious affiliation in Minnesota by movement (2014)")

d = ds[0]
d = d[["Affiliation", "% of population"]].astype("int")
print(d.info())
d.plot(x = "Affiliation", y = "% of population")
plt.show()