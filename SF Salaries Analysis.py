# import libraries we will use
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Salaries.csv")
df.info()

# Data Type Conversion The following columns were converted to numeric data types.
df[["BasePay", "OvertimePay", "OtherPay", "Benefits"]] = df[["BasePay", "OvertimePay", "OtherPay", "Benefits"]].apply(pd.to_numeric, errors='coerce')

df.describe()

# Check for empty values
df.isnull().sum()

# Data Cleaning
# BasePay: Missing values filled with the mean (66,325.45).
df["BasePay"] = df["BasePay"].fillna(df["BasePay"].mean())

# Dropped Columns: Status and Notes.
df.drop(columns=["Status"],inplace=True)
df.drop(columns=["Notes"],inplace=True)

# OvertimePay & OtherPay & Benefits: Missing values filled with 0.
df[["OvertimePay","OtherPay","Benefits"]] = df[["OvertimePay","OtherPay","Benefits"]].fillna(0)

df.isnull().sum()

# Ensuring Correct Calculation of TotalPay and TotalPayBenefits
df["TotalPay"] = df["BasePay"]+df["OvertimePay"]+df["OtherPay"]
df["TotalPayBenefits"] = df["TotalPay"]+df["Benefits"]

# Summary Statistics After Data Cleaning
df[["BasePay","OvertimePay","OtherPay","Benefits","TotalPay","TotalPayBenefits"]].describe()

# Distribution analysis
# Histogram of BasePay, OvertimePay, TotalPay

# BasePay Distribution
plt.figure(figsize=(10,5))
sns.histplot(df['BasePay'],color='blue' , kde=True)
plt.title('BasePay')
plt.xlabel('BasePay')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# OvertimePay Distribution
plt.figure(figsize=(10,5))
sns.histplot(df['OvertimePay'], bins=20, kde=True, color='green')
plt.title('OvertimePay')
plt.xlabel('OvertimePay')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# TotalPay Distribution
plt.figure(figsize=(10,5))
sns.histplot(df['TotalPay'], bins=20, kde=True, color='red', alpha=0.7)
plt.title('TotalPay')
plt.xlabel('TotalPay')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Salary trends over years(Average BasePay per year)
average_BasePay_per_year = df.groupby("Year")["BasePay"].mean().reset_index()
print(average_BasePay_per_year)

plt.figure(figsize=(10,5))
sns.lineplot(data=average_BasePay_per_year,x="Year",y="BasePay")
plt.title("Salary Trends Over Years (Average BasePay per Year)")
plt.xlabel("Year")
plt.ylabel("Average BasePay")
plt.grid(True)
plt.show()

# Total salary expenditure trends
TotalPay_expenditure_per_year = df.groupby("Year")["TotalPay"].sum().reset_index()
print(TotalPay_expenditure_per_year)

plt.figure(figsize=(10,5))
sns.lineplot(data=TotalPay_expenditure_per_year,x="Year",y="TotalPay")
plt.title("TotalPay Expenditure Trends Over Years")
plt.xlabel("Year")
plt.ylabel("TotalPay Expenditure")
plt.grid(True)
plt.show()

# The top 10 highest-paid job titles were identified based on TotalPay.
avg_TotalPay_per_job = df.groupby("JobTitle")["TotalPay"].mean().reset_index()
top_10_paid_job = (avg_TotalPay_per_job.sort_values(by="TotalPay",ascending=False)).head(10)
print(top_10_paid_job)

plt.figure(figsize=(10, 5))
sns.barplot(data=top_10_paid_job,x="JobTitle",y="TotalPay",color="#335BF9")
plt.title('Top Highest-Paid Job Titles')
plt.xlabel('Average TotalPay')
plt.ylabel('Job Title')
plt.xticks(rotation=85)
plt.show()

# The top 10 job roles with the highest average OvertimePay
avg_OvertimePay_job = df.groupby("JobTitle")["OvertimePay"].mean().reset_index()
top_10_overtime_paid_job = (avg_OvertimePay_job.sort_values(by="OvertimePay",ascending=False)).head(10)
print(top_10_overtime_paid_job)

plt.figure(figsize=(10, 5))
sns.barplot(data=top_10_overtime_paid_job,x="JobTitle",y="OvertimePay",color="#335BF9")
plt.title('Job Roles with Highest Overtime Pay')
plt.xlabel('Average OvertimePay')
plt.ylabel('Job Title')
plt.xticks(rotation=85)
plt.show()

# How many unique job titles exist?
print("There is ",df["JobTitle"].nunique()," unique job titles exist")

# Outliers in Total Compensation
plt.figure(figsize=(10, 4))
sns.boxplot(data=df,x="TotalPayBenefits",color="#33F98F")
plt.title('Boxplot for TotalPayBenefits (Identifying Unusually High Salaries)')
plt.xlabel("TotalPayBenefits")
plt.show()

# Who are the highest-paid employees?
top_10_highest_paid_employees = (df.sort_values(by="TotalPayBenefits",ascending=False)).head(10)
print(top_10_highest_paid_employees[["EmployeeName","JobTitle","TotalPayBenefits"]])


# Correlation Analysis: 
# Relationship between BasePay, OvertimePay, TotalPay, and Benefits.
correlation_matrix = df[['BasePay', 'OvertimePay', 'TotalPayBenefits']].corr()
print(correlation_matrix)

sns.heatmap(data=correlation_matrix,cmap='coolwarm',annot=True)
plt.title('Correlation Analysis: BasePay, OvertimePay, TotalPay, and Benefits')
plt.show()
