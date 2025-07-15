import sys

for line in sys.stdin:
    fields = line.strip().split(',')
    if len(fields) != 6:
        raise ValueError(f"Expected 6 elements, got {len(fields)}: {line.strip()}")
    category = fields[1]
    amount = float(fields[3])
    print(f"{category}\t{amount}")