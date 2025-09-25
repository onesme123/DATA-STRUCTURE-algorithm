# project 58: book fair sale


# --- Integers ---
sales = [120, 150, 90, 200, 170]   # Example sales quantities
total_sales = sum(sales)
average_sales = total_sales / len(sales)
min_sales = min(sales)
max_sales = max(sales)

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Minimum Sales:", min_sales)
print("Maximum Sales:", max_sales)


# --- Strings ---
report = f"Book Fair Sales Report:\nTotal = {total_sales}, Average = {average_sales:.2f}"
summary = f"Highest = {max_sales}, Lowest = {min_sales}"
print(report)
print(summary)


# --- Booleans ---
threshold = 140
if average_sales > threshold and max_sales > 180:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")


# --- Lists ---
book_titles = ["Book A", "Book B", "Book C", "Book D"]
print("Original list:", book_titles)

# Add new element
book_titles.append("Book E")

# Remove one based on condition
if "Book B" in book_titles:
    book_titles.remove("Book B")

# Sort list
book_titles.sort()
print("Modified and Sorted list:", book_titles)


# --- Arrays ---
import array
sales_array = array.array  ('i',[120, 150, 90, 200, 170])
print("Array sum:", sum(sales_array))
print("List sum:", sum(sales))


# --- Dictionaries ---
book_records = [
    {"id": 1, "name": "Book A", "value": 120},
    {"id": 2, "name": "Book B", "value": 150},
    {"id": 3, "name": "Book C", "value": 90}
]

# Update one record
book_records[0]["value"] = 130

# Delete one record
del book_records[1]

# Compute total value
total_value = sum(record["value"] for record in book_records)
print("Updated Records:", book_records)
print("Total Value:", total_value)
