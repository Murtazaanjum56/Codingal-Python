import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
import seaborn as sns
# df = dataframe
df = pd.read_csv("USA_Housing (1).csv")

print(df.head(10))


print(df.info())

print(df.describe())

print(df.columns)

sns.pairplot(df)

sns.heatmap(df.corr(), annot = True)

plt.show()