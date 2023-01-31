def bubblesort(l,index):
    """Applies the bubblesort algorithm to a list once and returns the list"""
    if l[index] > l[index+1]:
        temp = l[index]
        l[index] = l[index+1]
        l[index+1] = temp
    return l
