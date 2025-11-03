# MANIPULATING TEXT DATA FOR REPORTING PURPOSES

# 1. Clean and Formatting Text
text = "  Total Sales: $ 1 ,200.50  \n"

# Remove extra spaces and newlines
cleaned = text.strip()

# Replace characters
cleaned = cleaned.replace("$", "").replace(",", "")

# Split into label and value
label, value = cleaned.split(":")
label = label.strip()
value = float(value.strip())

print(label, "=", value)

"""
Output: 
  Total Sales = 1200.5
"""





# 2. Working with Multi-line Text

#Suppose you have a log-like text:
# Data = 
"""
Name: Alice, Sales: 1200
Name: Bob, Sales: 1500
Name: Charlie, Sales: 900
"""

# You can extract and process it easily:
report = []
for line in data.splitlines():
  parts = line.split(",")
  name = parts[0].split(":")[1].strip()
  sales = int(parts[1].split(":")[1].strip())
  report.append((name, sales))

print(report)

"""
Output:
[('Alice', 1200), ('Bob', 1500), ('Charlie', 900)]
"""




# 3. Summarizing for Reporting
total_sales = sum(sales for name, sales in report)
average_sales = total_sales / len(report)

print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales:.2f}")

"""
Output:
Total Sales: 3600
Average Sales: 1200.00
"""



# 4. Using Regular Expressions (Regex) for Pattern Extraction
#NB: When the text is unstructured, you can used the Regex module.

import re

text = """
2025-11-03 INFO User: Alice, Sales: 1200
2025-11-03 INFO User: Bob, Sales: 1500
"""

pattern = r"User:\s(w+),\sSales:\s(\d+)"
matches = re.findall(pattern, text)

print(matches)

# Output: [('Alice', '1200), ('Bob', '1500')]
# Now you can convert to numbers and summarize them as was done in #3.



# 5. Generating Simple Text
# You can generate formatted reports easily:

report_text = "Sales Report\n"
report_text += "-" * 30 + "\n"

for name, sales in report:
  report_text += f"{name:<10} | $(sales:>6}\n"

report_text += "-" * 30 + "\n"
report_text += f"Total: ${total_sales}\nAverage: ${average_sales:.2f}"

print(report_text)

"""
Output:
Sales Report
------------------------------
Alice          | $ 1200
Bob            | $ 1500
Charlie        | $  900
------------------------------
Total: $3600
Average: $1200.00
"""

# 7. Saving the Report to a File
with open("sales_report.txt", "w") as f:
  f.write(report_text)



"""
Use Cases:
- Cleaning logs: Remove timestamps, extract errors
- Summarizing text: Total requests, average response time
- Converting text to CSV: Convert "key:value" pairs into spreadsheet-ready data
- Automating reports: Generate daily summarirs from logs or APIs.
"""

