import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Salaries.csv")
print(df.info())

df[["BasePay", "OvertimePay", "OtherPay", "Benefits"]] = df[["BasePay", "OvertimePay", "OtherPay", "Benefits"]].apply(pd.to_numeric, errors='coerce')
print(df.info())
print(df.describe())

df.isnull().sum()

df["BasePay"] = df["BasePay"].fillna(df["BasePay"].mean())
df[["OvertimePay","OtherPay","Benefits"]] = df[["OvertimePay","OtherPay","Benefits"]].fillna(0)

df.drop(columns=["Status"],inplace=True)
df.drop(columns=["Notes"],inplace=True)

df["TotalPay"] = df["BasePay"]+df["OvertimePay"]+df["OtherPay"]
df["TotalPayBenefits"] = df["TotalPay"]+df["Benefits"]

df[["BasePay","OvertimePay","OtherPay","Benefits","TotalPay","TotalPayBenefits"]].describe()

plt.style.use("dark_background")
plt.figure(figsize=(12, 6))
sns.histplot(df['BasePay'], color='#00BFFF', kde=True, linewidth=2, edgecolor='white', alpha=0.8)
plt.title('Distribution of BasePay', fontsize=16, fontweight='bold', color='white')
plt.xlabel('BasePay', fontsize=14, fontweight='bold', color='white')
plt.ylabel('Frequency', fontsize=14, fontweight='bold', color='white')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6, color='gray')
plt.tight_layout()
plt.savefig('basepay_distribution.png', dpi=300, bbox_inches='tight')
plt.show()


plt.style.use("dark_background")
plt.figure(figsize=(12, 6))
sns.histplot(df['OvertimePay'], bins=20, kde=True, color='#00FF7F', linewidth=2, edgecolor='white', alpha=0.8)
plt.title('Distribution of Overtime Pay', fontsize=16, fontweight='bold', color='white')
plt.xlabel('Overtime Pay', fontsize=14, fontweight='bold', color='white')
plt.ylabel('Frequency', fontsize=14, fontweight='bold', color='white')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6, color='gray')
plt.tight_layout()
plt.savefig('overtimepay_distribution.png', dpi=300, bbox_inches='tight')
plt.show()


plt.style.use("dark_background")
plt.figure(figsize=(12, 6))
sns.histplot(df['TotalPay'], bins=20, kde=True, color='#FF4500', linewidth=2, edgecolor='white', alpha=0.8)
plt.title('Distribution of Total Pay', fontsize=16, fontweight='bold', color='white')
plt.xlabel('Total Pay', fontsize=14, fontweight='bold', color='white')
plt.ylabel('Frequency', fontsize=14, fontweight='bold', color='white')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6, color='gray')
plt.tight_layout()
plt.savefig('totalpay_distribution.png', dpi=300, bbox_inches='tight')
plt.show()


average_BasePay_per_year = df.groupby("Year")["BasePay"].mean().reset_index()

plt.style.use("dark_background")
plt.figure(figsize=(12, 6))
sns.lineplot(data=average_BasePay_per_year, x="Year", y="BasePay", color='#00FFFF', linewidth=2.5, marker='o', markersize=8)
plt.title("Salary Trends Over Years (Average BasePay per Year)", fontsize=16, fontweight='bold', color='white')
plt.xlabel("Year", fontsize=14, fontweight='bold', color='white')
plt.ylabel("Average BasePay", fontsize=14, fontweight='bold', color='white')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6, color='gray')
plt.tight_layout()
plt.savefig('salary_trends.png', dpi=300, bbox_inches='tight')
plt.show()


TotalPay_expenditure_per_year = df.groupby("Year")["TotalPay"].sum().reset_index()

plt.style.use("dark_background")
plt.figure(figsize=(12, 6))
sns.lineplot(data=TotalPay_expenditure_per_year, x="Year", y="TotalPay", color='#FFA500', linewidth=2.5, marker='o', markersize=8)
plt.title("TotalPay Expenditure Trends Over Years", fontsize=16, fontweight='bold', color='white')
plt.xlabel("Year", fontsize=14, fontweight='bold', color='white')
plt.ylabel("TotalPay Expenditure", fontsize=14, fontweight='bold', color='white')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6, color='gray')
plt.tight_layout()
plt.savefig('totalpay_expenditure_trends.png', dpi=300, bbox_inches='tight')
plt.show()


avg_TotalPay_per_job = df.groupby("JobTitle")["TotalPay"].mean().reset_index()

top_10_paid_job = (avg_TotalPay_per_job.sort_values(by="TotalPay",ascending=False)).head(10)

plt.style.use("dark_background")
plt.figure(figsize=(12, 6))
sns.barplot(data=top_10_paid_job, x="JobTitle", y="TotalPay", color="#335BF9")
plt.title('Top Highest-Paid Job Titles', fontsize=16, fontweight='bold', color='white')
plt.xlabel('Job Title', fontsize=14, fontweight='bold', color='white')
plt.ylabel('Average TotalPay', fontsize=14, fontweight='bold', color='white')
plt.xticks(rotation=85, fontsize=12, color='white')
plt.yticks(fontsize=12, color='white')
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.6, color='gray')
plt.savefig('top_highest_paid_jobs.png', dpi=300, bbox_inches='tight')
plt.show()


avg_OvertimePay_job = df.groupby("JobTitle")["OvertimePay"].mean().reset_index()

top_10_overtime_paid_job = (avg_OvertimePay_job.sort_values(by="OvertimePay",ascending=False)).head(10)

plt.style.use("dark_background")
plt.figure(figsize=(12, 6), dpi=200)
sns.barplot(data=top_10_overtime_paid_job, x="JobTitle", y="OvertimePay", color="#335BF9")
plt.title('Job Roles with Highest Overtime Pay', fontsize=16, fontweight='bold', color='white')
plt.xlabel('Job Title', fontsize=14, fontweight='bold', color='white')
plt.ylabel('Average OvertimePay', fontsize=14, fontweight='bold', color='white')
plt.xticks(rotation=85, fontsize=12, color='white')
plt.yticks(fontsize=12, color='white')
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.6, color='gray')
plt.savefig('highest_overtime_paid_jobs.png', dpi=300, bbox_inches='tight')
plt.show()

df["JobTitle"].nunique()

plt.style.use("dark_background")
plt.figure(figsize=(12, 5), dpi=200)
sns.boxplot(data=df, x="TotalPayBenefits", color="#33F98F")
plt.title('Boxplot for TotalPayBenefits (Identifying Unusually High Salaries)', fontsize=16, fontweight='bold', color='white')
plt.xlabel("TotalPayBenefits", fontsize=14, fontweight='bold', color='white')
plt.xticks(fontsize=12, color='white')
plt.yticks(fontsize=12, color='white')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6, color='gray')
plt.tight_layout()
plt.savefig('boxplot_totalpaybenefits.png', dpi=300, bbox_inches='tight')
plt.show()

top_10_highest_paid_employees = (df.sort_values(by="TotalPayBenefits",ascending=False)).head(10)
top_10_highest_paid_employees[["EmployeeName","JobTitle","TotalPayBenefits"]]

correlation_matrix = df[['BasePay', 'OvertimePay', 'TotalPayBenefits']].corr()

plt.style.use("dark_background")
plt.figure(figsize=(10, 8))
sns.heatmap(data=correlation_matrix, cmap='coolwarm', annot=True, linewidths=0.5, fmt=".2f", cbar_kws={'shrink': 0.8})
plt.title('Correlation Analysis: BasePay, OvertimePay, TotalPay, and Benefits', fontsize=16, fontweight='bold', color='white')
plt.tight_layout()
plt.savefig('correlation_analysis.png', dpi=300, bbox_inches='tight')
plt.show()
