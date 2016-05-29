def group(seq, sep):
    g = []
    for el in seq:
        if el == sep:
            g.append(el)
            yield g
            g = []
        else: g.append(el)
    yield g