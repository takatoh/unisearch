from unigram import document
import json
import os
import sys
import click


DOC_DIR = 'documents'
INDEX_DIR = 'indexes'
DOC_DATA = 'docs.json'


@click.group()
@click.pass_context
def cmd(ctx):
    pass


@cmd.command(help='Create indexes.')
@click.pass_context
def index(ctx):
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


@cmd.command(help='Search string.')
@click.pass_context
@click.argument('string')
def search(ctx, string):
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
            pos = list(map(lambda x: x - len(string) + 1, s))
            pos.sort()
            print(docs[doc_id]['name'], pos)


def main():
    cmd(obj={})


if __name__ == '__main__':
    main()