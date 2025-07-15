import sys

allowed = {"Computers", "Cameras", "Video Games"}

for line in sys.stdin:
    fields = line.strip().split(',')
    category = fields[1]
    if category not in allowed:
        continue
    amount = float(fields[3])
    print(f"{category}\t{amount}")
