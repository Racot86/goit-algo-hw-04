from random import randint
import timeit

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def generate_random_list(n):
    unsorted_list = []
    for i in range(0, n):
        unsorted_list.append(randint(0,400))
    return unsorted_list

unsorted_list = generate_random_list(1000)
sorted_by_insertion_list = unsorted_list.copy()
sorted_by_merge_list = unsorted_list.copy()


print(f'Test with {len(unsorted_list)} numbers list:')
print('  Inesrtion sort test - ', timeit.timeit('insertion_sort(sorted_by_insertion_list)', globals=globals(),number=1000))
print('  Merge sort test - ', timeit.timeit('merge_sort(sorted_by_merge_list)', globals=globals(),number=1000))
print('  python sorted test - ', timeit.timeit('unsorted_list.sort()', globals=globals(),number=1000))

unsorted_list = generate_random_list(10)
sorted_by_insertion_list = unsorted_list.copy()
sorted_by_merge_list = unsorted_list.copy()


print(f'Test with {len(unsorted_list)} numbers list:')
print('  Inesrtion sort test - ', timeit.timeit('insertion_sort(sorted_by_insertion_list)', globals=globals(),number=1000))
print('  Merge sort test - ', timeit.timeit('merge_sort(sorted_by_merge_list)', globals=globals(),number=1000))
print('  python sorted test - ', timeit.timeit('unsorted_list.sort()', globals=globals(),number=1000))