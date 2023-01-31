def selectionsort(l: list):
    # First find where the unsorted area is
    for cur_ind in range(len(l)-1):
        if l[cur_ind] > l[cur_ind+1]:
            unsorted_index = cur_ind
            break

    # Now find the smallest index after the unsorted part and swap their places
    min_value = l[unsorted_index]
    min_value_index = unsorted_index
    for current_index in range(unsorted_index,len(l)):
        if l[current_index] < min_value:
            min_value = l[current_index]
            min_value_index = current_index
    
    swap_indexes(l,unsorted_index,min_value_index)
    return unsorted_index,l

        
def swap_indexes(l,index1,index2):
    l[index1], l[index2] = l[index2], l[index1]