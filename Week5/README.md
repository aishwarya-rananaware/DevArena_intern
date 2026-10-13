# Customer Sales & Retention Analytics

## 1. Project Overview

Customer Sales & Retention Analytics is a data analysis project developed as part of Week 5 of a data analytics internship.

The project uses Python, Pandas, Matplotlib, and Seaborn to analyze sales transactions, customer purchasing patterns, regional performance, monthly sales trends, and customer churn.

The objective is to transform raw CSV data into meaningful business insights that can support better sales and customer retention decisions.

## 2. Project Objectives

- Analyze total sales and transaction values.
- Identify the top 10 customers by recorded revenue.
- Evaluate product and regional sales performance.
- Analyze monthly sales trends.
- Apply advanced Pandas operations, including grouping, aggregation, filtering, string manipulation, and datetime extraction.
- Create pivot tables for sales summarization.
- Analyze customer churn and contract-wise churn rates.
- Develop visualizations and a business analysis report.
- Validate data quality and calculation consistency.

## 3. Technologies Used

- **Python** — Programming language.
- **Pandas** — Data cleaning, manipulation, grouping, aggregation, and pivot tables.
- **Matplotlib** — Data visualization.
- **Seaborn** — Heatmap visualization.
- **Jupyter Notebook** — Interactive analysis and documentation.
- **ReportLab** — PDF report generation.
- **Git and GitHub** — Version control and project submission.

## 4. Project Structure

```text
customer-sales-retention-analytics/
│
├── Data/
│   ├── sales_data.csv
│   ├── customer_churn.csv
│   └── processed/
│       └── cleaned_sales_data.csv
│
├── outputs/
│   ├── charts/
│   │   ├── monthly_sales.png
│   │   ├── top_customers.png
│   │   ├── product_revenue.png
│   │   ├── regional_revenue.png
│   │   └── customer_churn.png
│   │
│   └── analysis_report.pdf
│
├── customer_analysis.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

The structure above describes the intended layout. Include only files and folders that actually exist in your repository.

## 5. Dataset Description

### Sales Dataset

**File:** `Data/sales_data.csv`

The sales dataset contains 100 transaction records and 7 columns.

| Column | Description |
|---|---|
| Date | Transaction date |
| Product | Product sold |
| Quantity | Quantity sold |
| Price | Price per unit |
| Customer_ID | Customer identifier |
| Region | Sales region |
| Total_Sales | Recorded transaction value |

### Customer Churn Dataset

**File:** `Data/customer_churn.csv`

The supplied customer churn dataset contains 500 records and 9 columns.

It includes customer-related information such as tenure, monthly charges, total charges, contract type, payment method, and churn status.

The `Churn` column uses numeric labels:

- `0` — Customer did not churn.
- `1` — Customer churned.

The observed churn rate in this sample is 10.6%.

## 6. Key Analysis Performed

### Sales Analysis

- Calculated total revenue and average transaction value.
- Grouped sales by month and identified the best-performing month.
- Identified the top 10 customers by recorded revenue.
- Compared product revenue and quantities sold.
- Analyzed regional sales performance.
- Used conditional filtering with AND and OR operators.
- Extracted year, month, and day from transaction dates.
- Created a pivot table comparing products and regions.

### Customer Churn Analysis

- Calculated the overall churn rate.
- Compared churn percentages across contract types.
- Visualized customer churn distribution.
- Developed recommendations based on observed churn patterns.

### Data Visualization

The project includes the following planned charts:

1. Monthly Sales Trend
2. Top 10 Customers by Revenue
3. Revenue by Product
4. Revenue by Region
5. Customer Churn Rate by Contract Type

A region-versus-product heatmap is also created from the sales pivot table.

## 7. Key Findings

The following results were calculated from the supplied datasets.

| Metric | Result |
|---|---:|
| Total recorded sales | 12,365,048 |
| Total quantity sold | 478 |
| Sales transactions | 100 |
| Unique sales customer IDs | 100 |
| Average transaction value | 123,650.48 |
| Customer churn rate | 10.6% |

The currency unit is not specified in the supplied sales dataset.

### Product Performance

- Laptop generated the highest recorded product revenue: 3,889,210.
- Tablet generated revenue of 2,884,340.
- Phone generated revenue of 2,859,394.

### Regional Performance

- North recorded the highest regional revenue: 3,983,635.
- South recorded revenue of 3,737,852.
- West recorded the lowest regional revenue: 2,123,922.

### Customer Churn

The observed churn rates by contract type were:

- Month-to-month: 20.6%
- Two year: 6.9%
- One year: 4.3%

These results describe the supplied samples and should not be assumed to represent an entire business population.

## 8. Business Recommendations

- Investigate the reasons for monthly sales fluctuations.
- Evaluate pricing, demand, and promotional opportunities across products.
- Examine regional differences to identify opportunities for improvement.
- Investigate the factors associated with higher churn among month-to-month customers.
- Consider appropriate retention initiatives and evaluate their effectiveness.
- Collect transaction histories with reliable customer identifiers to support repeat-purchase and lifetime-value analysis.

## 9. Data Limitations

The sales dataset contains 100 transaction records and 100 unique customer IDs. Therefore, repeat purchasing and customer lifetime value cannot be established reliably from this sample alone.

The customer IDs in the sales and churn datasets do not have an established matching relationship. The datasets were analyzed separately rather than merged using unverified identifiers.

Product cross-selling analysis also requires suitable order-level data that identifies products purchased together.

The supplied sales data does not specify a currency unit.

## 10. Data Validation and Testing

The notebook includes validation checks for:

- Required columns
- Missing values
- Duplicate rows
- Numeric data validity
- Date validity
- Sales calculation consistency
- Positive quantities and prices
- Churn label validity

The implemented checks passed during execution. These checks improve confidence in the analysis but do not guarantee the absence of every possible data-quality issue.

## 11. Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version
- Visual Studio Code or Jupyter Notebook
- Git, if using GitHub

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd customer-sales-retention-analytics
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Open the notebook

Open `customer_analysis.ipynb` in VS Code or Jupyter Notebook.

Select the Python environment in which the required libraries are installed.

### Step 5: Run the analysis

Execute the notebook cells in order, starting with imports and data loading.

Ensure that the CSV file paths match the repository structure.

## 12. How to View the Results

- Open `customer_analysis.ipynb` to inspect the code, outputs, and analysis.
- Open `outputs/charts/` to view the saved chart images.
- Open `outputs/analysis_report.pdf` to read the report.

## 13. Future Improvements

- Obtain a verified customer dataset that can be joined with sales transactions.
- Analyze repeat purchases using multi-transaction customer histories.
- Calculate customer lifetime value using an appropriate observation period.
- Analyze product combinations using order-level data.
- Expand the dataset to evaluate seasonal patterns more reliably.
- Develop an interactive dashboard using Streamlit or Power BI.

## 14. Conclusion

This project demonstrates the application of advanced Pandas operations, exploratory data analysis, data validation, visualization, and business interpretation.

The analysis identifies high-revenue customers, leading products, regional sales differences, monthly trends, and customer churn patterns. The findings provide a foundation for further business analysis using more comprehensive and reliably linked datasets.

## Author

**Name:** Your Name

**Project:** Customer Sales & Retention Analytics

**Program:** Data Analytics Internship — Week 5