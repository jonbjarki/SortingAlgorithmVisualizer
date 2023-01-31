import random
def bogosort(l):
    """Applies the bogosort algorithm to a list once and returns the list"""
    l_copy = l.copy()
    l_new = []
    for x in range(len(l_copy)):
        ind = random.randint(0,len(l_copy)-1)
        el = l_copy.pop(ind)
        l_new.append(el)
    return l_new
