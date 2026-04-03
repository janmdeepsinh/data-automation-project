# Data Automation Project
This project is a Python-based data automation tool that processes raw sales data from a CSV file, cleans invalid or missing values, generates summary insights, and exports the cleaned dataset.

## Problem
Raw business data often contains missing values, incorrect formats, or inconsistent entries. This project simulates a real-world scenario where such data needs to be cleaned and prepared for analysis.

## Solution
The script reads raw CSV data, applies validation and cleaning logic, and generates both a structured report and a cleaned output file.

## Features
- Reads raw CSV sales data
- Handles missing sales values by replacing them with 0
- Converts invalid sales values (e.g., text) into numeric format
- Fills missing region values with "Unknown"
- Calculates total sales
- Identifies the top-performing product
- Counts how many values were corrected
- Exports cleaned data into a new CSV file

## Project Structure
- `sales_data.csv` → raw input data
- `main.py` → Python automation script
- `cleaned_sales_data.csv` → cleaned output data

## Example Output
Total Sales: 158
Top Product: Toothbrush
Sales values fixed: 3
Region values fixed: 1
