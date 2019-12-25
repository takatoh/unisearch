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
