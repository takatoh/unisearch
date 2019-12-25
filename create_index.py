from unigram import document
import json
import os


DOC_DIR = 'documents'
INDEX_DIR = 'indexes'
DOC_DATA = 'docs.json'


files = [os.path.join(DOC_DIR, f) for f in os.listdir(DOC_DIR)]
docs = {}
doc_id = 0
for file in files:
    with open(file, 'r') as f:
        text = f.read()
        tokens = document.tokenize(text)
        index = document.classify(tokens)
        document.save_index(index, doc_id, INDEX_DIR)
    docs[str(doc_id)] = {'name': os.path.basename(file), 'path': file}
    doc_id += 1

with open(DOC_DATA, 'w') as f:
    json.dump(docs, f, indent=2)
