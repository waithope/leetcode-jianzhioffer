
'''
参考：https://stackoverflow.com/questions/11587044/how-can-i-create-a-tree-for-huffman-encoding-and-decoding/42569875#42569875
'''

freq = [
    (8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
    (12.702, 'e'),(2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
    (6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
    (2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'),
    (0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'),
    (2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
    (1.974, 'y'), (0.074, 'z') ]


def assginCode(nodes, label, result, prefix=''):
    childs = nodes[label]
    tree = {}
    if len(childs) == 2:
        # tree['0'/'1'] will be assigned a subtree
        tree['0'] = assginCode(nodes, childs[0], result, prefix=prefix+'0')
        tree['1'] = assginCode(nodes, childs[1], result, prefix=prefix+'1')
        return tree
    else:
        result[label] = prefix
        return label

def huffmanCode(_vals):
    vals = _vals.copy()
    nodes = {}
    # leafs initialization
    for leaf in vals.keys():
        nodes[leaf] = []
    while len(vals) > 1:
        sortedVals = sorted(vals.items(), key=lambda x: x[1])
        n1 = sortedVals[0][0]
        n2 = sortedVals[1][0]
        # pop value from dict
        vals[n1 + n2] = vals.pop(n1) + vals.pop(n2)
        nodes[n1 + n2] = [n1, n2]

    code = {}
    root = n1 + n2
    tree = {}
    tree = assginCode(nodes, root, code, prefix='')
    return code, tree



if __name__ == '__main__':
    vals = {leaf:val for (val, leaf) in freq}
    code, tree = huffmanCode(vals)

    text = 'hello'
    encoded = ''.join([code[t] for t in text])
    print('Encoded text: ', encoded)

    decoded = []
    i = 0
    while i < len(encoded):
        ch = encoded[i]
        act = tree[ch]
        while not isinstance(act, str):
            i += 1
            ch = encoded[i]
            act = act[ch]
        decoded.append(act)
        i += 1
    print('Decoded text: ', ''.join(decoded))
