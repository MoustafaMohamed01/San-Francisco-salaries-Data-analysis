# Salary Data Analysis

## Overview
This project analyzes salary data to identify trends, distributions, and anomalies in employee compensation. The dataset has been cleaned, missing values handled, and various insights derived, including salary trends over the years, job roles with the highest pay, and correlations between different salary components.

## Features
- **Data Cleaning**: Handling missing values, converting data types, and removing irrelevant columns.
- **Descriptive Statistics**: Summary statistics before and after cleaning.
- **Distribution Analysis**: Visualizing the distributions of BasePay, OvertimePay, and TotalPay.
- **Salary Trends**: Analyzing salary trends over the years and total salary expenditure.
- **Job Analysis**: Identifying the highest-paid job titles and roles with the most overtime pay.
- **Outlier Detection**: Identifying extreme values in total compensation.
- **Correlation Analysis**: Understanding relationships between BasePay, OvertimePay, and TotalPayBenefits.

## Technologies Used
- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **Jupyter Notebook**
- **Git & GitHub**

## Data Cleaning Process
1. Converted relevant columns to numeric types.
2. Filled missing values appropriately (mean for BasePay, 0 for others).
3. Dropped columns with excessive missing data.
4. Ensured TotalPay and TotalPayBenefits were correctly calculated.

## Visualizations & Insights
- **Histograms** to analyze salary distributions.
- **Line charts** for salary trends and expenditure trends over the years.
- **Bar charts** for top-paid job roles.
- **Boxplots** for detecting outliers in total compensation.
- **Heatmaps** to visualize correlations between salary components.

## How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/MoustafaMohamed01/San-Francisco-salaries-Data-analysis.git
   ```
2. Install dependencies:
   ```sh
   pip install pandas numpy matplotlib seaborn
   ```
3. Run the Jupyter Notebook:
   ```sh
   jupyter notebook
   ```
4. Open the notebook and execute the cells to explore the analysis.

## Dataset
- The dataset contains salary-related information, including `BasePay`, `OvertimePay`, `OtherPay`, `Benefits`, `TotalPayBenefits`, and `TotalPay`.
- Contains variables such as `Id`, `EmployeeName`, `JobTitle`, `Year`, `Notes`, `Agency`, and `Status`

## Contributing
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

## Acknowledgments
- The dataset was sourced from [Kaggle].
- The dataset link: [https://www.kaggle.com/datasets/kaggle/sf-salaries].

