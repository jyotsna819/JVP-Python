from collections import defaultdict

data = ["p1,4.5", "p2,3.0", "p1,5.0", "p2,2.5", "p3,4.0"]

ratings = defaultdict(list)
for entry in data:
    product, rating = entry.split(',')
    ratings[product].append(float(rating))

averages = {product: sum(values)/len(values) for product, values in ratings.items()}
for product, avg in averages.items():
    print(f'"{product}" {round(avg, 2)}')
