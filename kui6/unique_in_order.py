message = ''

def unique_in_order(iterable):
    i = 1
    j = 0
    r = []
    iterables = [letter for letter in iterable]
    if iterable != '':
        r.append(iterables[0])
    else:
        pass
    while i < len(iterables):
        if r[j] != iterables[i]:
            r.append(iterables[i])
            j += 1
        i += 1
    return r

x = unique_in_order(message)
print(x)