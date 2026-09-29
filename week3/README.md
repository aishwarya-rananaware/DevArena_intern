# Sales Data Analysis Using Python and Pandas

## 1. Project Overview

This project is a Python-based Sales Data Analysis application developed using the Pandas library.

The purpose of this project is to load, validate, clean, and analyze sales transaction data stored in a CSV file.

The application performs data-quality checks before calculating sales metrics. It is designed to handle common real-world data problems such as missing values, invalid numbers, duplicate records, invalid dates, blank fields, negative values, missing columns, and inconsistent sales calculations.

The project uses a sample sales dataset containing 100 transaction records and the following fields:

* Date
* Product
* Quantity
* Price
* Customer_ID
* Region
* Total_Sales

---

## 2. Project Objectives

The main objectives of this project are:

1. Load sales data from a CSV file using Pandas.
2. Explore the structure and contents of the dataset.
3. Validate the required columns.
4. Detect missing and invalid values.
5. Detect duplicate records.
6. Validate dates and numerical fields.
7. Detect invalid or negative quantities and prices.
8. Verify that `Total_Sales` matches `Quantity × Price`.
9. Clean the dataset before analysis.
10. Calculate important sales metrics.
11. Identify the best-performing products.
12. Analyze sales by region.
13. Generate a clear and readable sales analysis report.
14. Test the application using valid and invalid datasets.

---

## 3. Technologies Used

| Technology | Purpose                                          |
| ---------- | ------------------------------------------------ |
| Python     | Programming language                             |
| Pandas     | Data loading, cleaning, validation, and analysis |
| CSV        | Dataset format                                   |
| VS Code    | Development environment                          |
| Git        | Version control                                  |
| GitHub     | Project repository                               |

---

## 4. Dataset Description

The project uses `sales_data.csv`.

### Dataset Columns

| Column      | Description                    | Data Type |
| ----------- | ------------------------------ | --------- |
| Date        | Date of the sales transaction  | Date      |
| Product     | Name of the product sold       | Text      |
| Quantity    | Number of units sold           | Integer   |
| Price       | Price per unit                 | Numeric   |
| Customer_ID | Unique customer identifier     | Text      |
| Region      | Sales region                   | Text      |
| Total_Sales | Total value of the transaction | Numeric   |

### Sales Calculation

The expected sales amount is calculated using:

`Total_Sales = Quantity × Price`

The program independently calculates this value and compares it with the `Total_Sales` value provided in the dataset.

---

## 5. Project Structure

```text
week-3-sales-data-analysis/
│
├── sales_analysis.py
├── sales_data.csv
├── requirements.txt
├── README.md
├── analysis_report.md
│
└── screenshots/
    └── testing/
        ├── test_missing_column.png
        ├── test_invalid_number.png
        ├── test_negative_value.png
        ├── test_duplicate.png
        ├── test_empty_csv.png
        ├── test_missing_values.png
        ├── test_invalid_date.png
        ├── test_blank_product.png
        ├── test_blank_region.png
        ├── test_sales_mismatch.png
        ├── test_zero_quantity.png
       
```
