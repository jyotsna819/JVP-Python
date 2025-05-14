from collections import defaultdict

docs = [
    "doc1:hello world hello mapreduce",
    "doc2:goodbye world",
    "doc3:hello again"
]

index = defaultdict(set)

for line in docs:
    doc_id, content = line.split(':')
    for word in set(content.split()):
        index[word].add(doc_id)

for word in sorted(index):
    print(f'"{word}" {sorted(index[word])}')
