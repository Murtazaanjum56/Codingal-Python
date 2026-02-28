import pandas as py
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = py.read_csv("IMDB Dataset.csv")

print(df.head(3))

print(df.tail(3))

print(df.info())

df.isnull().sum()

subset = df.iloc[40:75]
print(subset)

best = df.loc[df['No_of_Votes'].idxmax()]
print(best)

plt.figure(figsize=(10,6))
sns.boxplot(x = df['Rating'])
plt.title('Boxplot of Ratings')
plt.xlabel('Rating')
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(x = df['Runtime'])
plt.title('Boxplot of Runtime')
plt.xlabel('runtime(minutes)')
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(df['Runtime'], df['Rating'])
plt.title('Scatter Plot of Runtime vs Rating')
plt.xlabel('Runtime (minutes)')
plt.ylabel('Rating')
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(df['Rating'], bins = 20, kde=True)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(x=df['Rating'])
plt.title("Count of Movies by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45)
plt.show()
