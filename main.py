import csv


def clean_sales_value(value):
    try:
        return int(value), False
    except:
        return 0, True


def clean_region_value(value):
    if value is None or value.strip() == "":
        return "Unknown", True
    return value.strip(), False


def read_and_clean_data(input_file):
    rows = []
    total_sales = 0
    product_totals = {}
    fixed_sales_count = 0
    fixed_region_count = 0

    with open(input_file, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            sales, sales_changed = clean_sales_value(row["Sales"])
            region, region_changed = clean_region_value(row["Region"])
            product = row["Product"].strip()
            date = row["Date"].strip()

            if sales_changed:
                fixed_sales_count += 1

            if region_changed:
                fixed_region_count += 1

            cleaned_row = {
                "Date": date,
                "Product": product,
                "Sales": sales,
                "Region": region
            }

            rows.append(cleaned_row)

            total_sales += sales

            if product in product_totals:
                product_totals[product] += sales
            else:
                product_totals[product] = sales

    return rows, total_sales, product_totals, fixed_sales_count, fixed_region_count


def save_cleaned_data(output_file, rows):
    with open(output_file, "w", newline="") as file:
        fieldnames = ["Date", "Product", "Sales", "Region"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)


def print_report(total_sales, product_totals, fixed_sales_count, fixed_region_count):
    if not product_totals:
        print("No product data found.")
        return

    top_product = max(product_totals, key=product_totals.get)

    print("\n=== Data Cleaning Report ===")
    print(f"Total Sales: {total_sales}")
    print(f"Top Product: {top_product}")
    print(f"Product Totals: {product_totals}")
    print(f"Sales values fixed: {fixed_sales_count}")
    print(f"Region values fixed: {fixed_region_count}")


def main():
    input_file = "sales_data.csv"
    output_file = "cleaned_sales_data.csv"

    try:
        rows, total_sales, product_totals, fixed_sales_count, fixed_region_count = read_and_clean_data(input_file)
        save_cleaned_data(output_file, rows)

        print("Data cleaned successfully.")
        print(f"Cleaned file saved as {output_file}")
        print_report(total_sales, product_totals, fixed_sales_count, fixed_region_count)

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()