"""this module contain the definition of the find_peak function"""


def find_peak(list_of_integers):
    """Find the peak(highest number) in a list of an unsorted integers"""
    if len(list_of_integers) == 0:
        return
    number_comparison = len(list_of_integers) - 1
    comparison = 0
    i = 0
    j = 1
    while comparison < number_comparison:
        if list_of_integers[i] > list_of_integers[j]:
            temp = list_of_integers[j]
            list_of_integers[j] = list_of_integers[i]
            list_of_integers[i] = temp
        i += 1
        j += 1
        comparison += 1
    return list_of_integers[number_comparison]
