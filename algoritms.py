#----------------SORT----------------------------
array = [3, 5, 2, 1, 8, 9, 4, 0]

def bubble_sort(array):
    flag = True
    while flag:
        flag = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag = True
    print(array)

#bubble_sort(array)

def selection_sort(array):
    for i in range(len(array)):
        low_value_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[low_value_index]:
                low_value_index = j
        array[i], array[low_value_index] = array[low_value_index], array[i]
    print(array)

#selection_sort(array)

def insertion_sort(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i - 1

        while j >= 0 and array[j] > item_to_insert:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item_to_insert
    print(array)

#insertion_sort(array)
