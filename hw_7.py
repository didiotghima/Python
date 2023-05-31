
def binary_search(element, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == element:
            return mid
        elif guess < element:
            low = mid + 1
        else:
            high = mid - 1

    return -1


my_list = [1, 3, 5, 7, 9]
search_element = 5

result = binary_search(search_element, my_list)
if result != -1:
    print(f"Элемент {search_element} найден на позиции {result}.")
else:
    print("Элемент не найден.")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

unsorted_list = [9, 5, 1, 3, 7]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)
