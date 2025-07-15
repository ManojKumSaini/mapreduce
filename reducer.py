import sys

current_category = None
total_amount = 0.0
count = 0

for line in sys.stdin:
    category, amount_str = line.strip().split('\t')
    amount = float(amount_str)
    if current_category == category:
        total_amount += amount
        count += 1
    else:
        if current_category:
            avg = total_amount / count
            print(f"{current_category}\t{avg}")
        current_category = category
        total_amount = amount
        count = 1

if current_category:
    avg = total_amount / count
    print(f"{current_category}\t{avg}")
