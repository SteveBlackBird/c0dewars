def friend(x):
    """My friends have only 4 word in name"""
    my_friends = []
    for friend in x:
        if len(friend) == 4:
            my_friends.append(friend)
    return my_friends

def friend2(x):
    """The same one, but with list generator"""
    return [f for f in x if len(f) == 4]