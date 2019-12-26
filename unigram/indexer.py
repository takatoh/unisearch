import os


def tokenize(text):
    return list(text)


def classify(token_list):
    tokens = {}
    pos = 0
    for t in token_list:
        if not t in tokens:
            tokens[t] = []
        tokens[t].append(pos)
        pos += 1
    return tokens


def save(index, doc_id, index_dir):
    for c, idx in index.items():
        l = str(doc_id) + ':' + ','.join(list(map(lambda x: str(x), idx))) + '\n'
        with open(os.path.join(index_dir, str(ord(c)) + '.index'), 'a') as f:
            f.write(l)


def parse_index(content):
    l = content.split('\n')
    l.pop()
    index = {}
    for l2 in l:
        a = l2.split(':')
        index[a[0]] = [int(x) for x in a[1].split(',')]
    return index
