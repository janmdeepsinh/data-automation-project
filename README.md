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

## Example Output
Total Sales: 158
Top Product: Toothbrush
Sales values fixed: 3
Region values fixed: 1

## Input vs Output Example

### Raw Input (sales_data.csv)
```csv
Date,Product,Sales,Region
2026-01-02,Toothbrush,,EU
2026-01-03,Floss,15,
2026-01-04,Floss,abc,US


### Cleaned Output
Date,Product,Sales,Region
2026-01-02,Toothbrush,0,EU
2026-01-03,Floss,15,Unknown
2026-01-04,Floss,0,US

## How to Run

1. Make sure Python is installed
2. Place your input file as `sales_data.csv`
3. Run the script:

```bash
python main.py

## Real-World Application

This project simulates a common data processing task where raw business data needs to be cleaned before analysis. Such workflows are widely used in data engineering, reporting pipelines, and business intelligence systems.

