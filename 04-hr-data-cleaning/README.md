# 04 - HR Data Cleaning Project

### Business Problem
Raw HR data contained critical inconsistencies: salaries as '50k', '$45,000', 'N/A', null departments, and string-type ages, blocking any meaningful analysis.

### My Solution - End-to-End Pipeline
1. **Data Standardization**: Used `.str.replace()` and `pd.to_numeric()` to convert all salary formats to integers
2. **Missing Data Strategy**: `fillna('Unknown')` for departments, `dropna()` for rows with null age/salary  
3. **Type Enforcement**: `astype('Int64')` for numerical columns
4. **Insight Generation**: `groupby()` + `mean()` to visualize Average Salary by Department

### Key Business Insight
The 'Unknown' department had the highest average salary at 77,500 MAD, indicating a data entry issue that HR must address.

### Tech Stack
Python, Pandas, Matplotlib