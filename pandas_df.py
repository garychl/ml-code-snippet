import pandas as pd

df = pd.DataFrame(data={'Values':range(1,100000)})

# slow
summed = 0

for _, row in df.iterrows():
    summed += row['Values']

# fast
summed = 0

for row in df.itertuples(index=False):
    summed += row.Values