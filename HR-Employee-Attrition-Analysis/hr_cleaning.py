import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
print(df.head(5))
print(df.columns)
print(df.isnull().sum())
print(df.T)
attrition_rate=df['Attrition'].value_counts(normalize=True)*100
print("\nAttrition Rate %")
print(attrition_rate)

plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Department', hue='Attrition')
plt.title('Attrition by Department')
plt.tight_layout()
plt.savefig('attrition_by_department.png')

sns.countplot(data=df, x='OverTime', hue='Attrition')
plt.title('Attrition by Overtime')
plt.savefig('attrition_by_overtime.png')
plt.show()