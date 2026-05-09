import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# تخيل هذا الملف جاك من الـ HR
data = {
    'employee': ['Ahmed', 'Sara', 'Omar', 'Layla', 'Khalid', 'zakaria', ' souad'],
    'age': [28, 35, '  ', 42, 30, 29,38],
    'salary': ['50k', '60,000', '$45,000', 'N/A', ' 75,000 ', ' $90000', '80k'],
    'department': ['IT', 'HR', 'IT', 'Finance', None, 'HR', None]
}
df = pd.DataFrame(data)
print("قبل التنظيف:")
#print(df.info())
df['age']=df['age'].astype(str).str.strip().replace(' ','')
df['age']=pd.to_numeric(df['age'], errors='raise').astype('Int64')
df['salary']=df['salary'].astype(str).str.strip().str.lower()
df['salary']=df['salary'].str.replace('[$,]', '',regex=True)
df['salary']=df['salary'].str.replace('k', '000',regex=True)
df['salary']=pd.to_numeric(df['salary'], errors='coerce').astype('Int64')
df['department']=df['department'].astype('string')
df['department']=df['department'].fillna('Unknown')
df.dropna(subset=['salary', 'age'], inplace=True)
print(df)
department=df.groupby('department')['salary'].mean().sort_values(ascending=False)
df.to_csv('cleaned_employee_data.csv', index=False)
department.plot(kind='bar', title='Average Salary by Department', xlabel='Department', ylabel='Average Salary')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
plt.savefig('average_salary_by_department.png')