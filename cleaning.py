import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("data.csv")

print("Descriptive Statistics:")
print(df.describe())

group1 = df[df['group'] == 'A']['salary']
group2 = df[df['group'] == 'B']['salary']

t_stat , p_value = ttest_ind(group1,group2)

print("\nT-Test Result:")
print("T-Statistic:",t_stat)
print("P-Value:",p_value)
