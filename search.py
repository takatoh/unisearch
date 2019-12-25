from unigram import document
import json
import os
import sys


INDEX_DIR = 'indexes'
DOC_DATA = 'docs.json'


string = sys.argv[1]

with open(DOC_DATA, 'r') as f:
    docs = json.load(f)
fcount = len(docs)

index_files = list(map(lambda x: os.path.join(INDEX_DIR, x), os.listdir(INDEX_DIR)))
index = {}
for file in index_files:
    c = chr(int(os.path.basename(file).replace('.index', '')))
    with open(file, 'r') as f:
        index[c] = document.parse_index(f.read())

m = list(map(lambda x: index[x], list(string)))

for i in range(fcount):
    doc_id = str(i)
    if not all(map(lambda x: doc_id in x.keys(), m)):
        continue
    n = list(map(lambda x: x[doc_id], m))
    s = set(n[0])
    for s1 in n[1:]:
        s = set(list(map(lambda x: x + 1, s)))
        s = s & set(s1)
    if len(s) > 0:
        pos = list(map(lambda x: x - fcount + 1, s))
        pos.sort()
        print(docs[doc_id]['name'], pos)
