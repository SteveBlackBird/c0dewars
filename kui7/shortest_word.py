message = "Here we go again"

def find_short(s):
    """Return the shortest word's lenght in a string"""
    words = s.split(" ")
    l = []
    for word in words:
        l.append(len(word))
    l.sort()
    return l[0]

x = find_short(message)
print(x)

def find_short2(s):
    """List generator with min function"""
    return min([len(i) for i in s.split()])