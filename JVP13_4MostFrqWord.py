from collections import Counter

text = """hello world hello mapreduce
hello again world
world of mapreduce
goodbye world"""

words = text.split()
counter = Counter(words)

for word, count in counter.most_common():
    print(f'"{word}" {count}')
