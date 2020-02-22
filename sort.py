def Exchange2Items(listStrings, I0, I1):
    listStrings[I0], listStrings[I1] = listStrings[I1], listStrings[I0]
    return listStrings


def FindSmallestIndex(listStrings):
    smallestI = 0
    for string in range(0, len(listStrings)):
        if listStrings[string] < listStrings[smallestI]:
            smallestI = string

    return smallestI


def SelectionSort(listStrings):
    for x in range(len(listStrings)):
        smallest_index = FindSmallestIndex(listStrings[x:])

        Exchange2Items(listStrings, x, smallest_index + x)

    return listStrings


L1 = Exchange2Items(["banana", "kiwi", "orange"], 0, 2)
print(L1)

L2 = FindSmallestIndex(["orange", "kiwi", "banana"])
print(L2)

L = ["marked", "float", "straight", "overconfident", "party", "thin", "room", "stroke"]
L3 = SelectionSort(L)
print(L3)


def bubble_sort(L):
    stop_counting = True
    pass_number = len(L) - 1
    while stop_counting and pass_number > 0:
        stop_counting = False
        for index in range(pass_number):
            if L[index] > L[index + 1]:
                stop_counting = True
                container = L[index]
                L[index] = L[index + 1]
                L[index + 1] = container
        pass_number = pass_number - 1

    return L


bubble_sort(L)
print(L)
