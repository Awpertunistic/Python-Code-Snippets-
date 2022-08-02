import random
import numpy as np

from numpy.random import seed
from numpy.random import randint


def binary_search(nums, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if target == nums[mid]:
        return mid


    elif target < nums[mid]:
        return binary_search(nums, left, mid - 1, target)


    else:
        return binary_search(nums, mid + 1, right, target)


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        already_sorted = True

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                already_sorted = False

        if already_sorted:
            break

    return arr



if __name__ == '__main__':

    # Creates an array of size 50 of unique numbers between 1-100.
    nums = random.sample(range(1, 100), 50)
    print("\nThis program creates an array of size (50-100) that holds randomly generated integers.")
    print("The larger the array, the higher your chances of winning!")
    target = int(input("Enter an integer between (1-100) to search the array for a hit:\n"))

    # Input validation.
    while not(100 > target > 0):
        target = int(input("Please. Enter an integer between (1-100) to search the array for a hit:\n"))

    # Sorts array using the bubble sort function.
    bubble_sort(nums)
    seed(1)
    print(nums)
    (left, right) = (0, len(nums) - 1)

    # Uses a binary search to locate the index if it exists.
    index = binary_search(nums, left, right, target)

    if index != -1:
        print('\nElement found at index', index)
    else:
        print('\nElement found not in the list')
