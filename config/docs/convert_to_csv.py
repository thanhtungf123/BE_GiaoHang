import csv
import re

# Read the markdown file
with open('Issues_Report_GiaoHang.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Prepare CSV data
rows = []
header = ['Title', 'Description', 'Issue ID', 'URL', 'State', 'Assignee', 'Created At', 'Due Date', 'Milestone', 'Labels', 'Functions/Screens']
rows.append(header)

# Parse markdown table rows (lines 13-142, skipping header and separator)
for line in lines[12:142]:
    line = line.strip()
    if line.startswith('|') and not line.startswith('|---'):
        # Split by | and remove first and last empty elements
        cells = [cell.strip() for cell in line.split('|')[1:-1]]
        # Remove backticks from URL
        if len(cells) > 3:
            cells[3] = cells[3].replace('`', '')
        rows.append(cells)

# Write to CSV with UTF-8 BOM for Excel compatibility
with open('Issues_Report_GiaoHang.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f'CSV file created successfully with {len(rows)-1} issues')








