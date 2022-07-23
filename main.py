import math
from time import time
import random
import sys


# This is required as python has a very conservative recursion depth limit of 1000 and it is
# required for us to have at least 1050 recursion depth to solve quicksort with 10000 elements
sys.setrecursionlimit(1050)

"""
    Programming Assignment 1 by Aadim Chaulagain
"""


class Programming1:

    @staticmethod
    def arrayMaker(n: int) -> list:
        temp = []
        for _ in range(n):
            temp.append(random.randint(0, n))
        return temp

    @staticmethod
    def sortedArray(n: int, asc=True) -> list:
        temp = []
        if asc:
            for _ in range(n):
                temp.append(n)
        else:
            for _ in range(n, -1, -1):
                temp.append(n)
        return temp

    @staticmethod
    def merge(A: list, left: int, mid: int, right: int):
        leftArray = []
        rightArray = []

        # divides the array in two halves to compare them
        for i in range(left, mid + 1):
            leftArray.append(A[i])

        for j in range(mid + 1, right + 1):
            rightArray.append(A[j])

        l = r = 0
        index = left

        while l < len(leftArray) and r < len(rightArray):
            if leftArray[l] <= rightArray[r]:
                A[index] = leftArray[l]
                l = l + 1
            else:
                A[index] = rightArray[r]
                r = r + 1
            index = index + 1

        # checks if there are any remaining value in either left or right array
        while l < len(leftArray):
            A[index] = leftArray[l]
            index = index + 1
            l = l + 1

        while r < len(rightArray):
            A[index] = rightArray[r]
            index = index + 1
            r = r + 1

    def merge_sort(self, array: list, left: int, right: int):
        start_time = time()
        if left < right:
            mid = math.floor((left + right) / 2)

            self.merge_sort(array, left, mid)
            self.merge_sort(array, mid + 1, right)
            self.merge(array, left, mid, right)
        return array, (time() - start_time)

    @staticmethod
    def partition(A: list, p: int, r: int) -> int:
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
        temp = A[i + 1]
        A[i + 1] = A[r]
        A[r] = temp
        return i + 1

    def quicksort(self, A: list, p: int, r: int):
        startTime = time()
        if p < r:
            q = self.partition(A, p, r)
            self.quicksort(A, p, q - 1)
            self.quicksort(A, q + 1, r)
        return A, (time() - startTime)

    @staticmethod
    def insertionSort(array: list):
        startTime = time()
        for i in range(1, len(array)):
            temp = array[i]
            j = i - 1
            while j >= 0 and (array[j] >= temp):
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = temp
        return array, (time() - startTime)

    def showMergeSort(self):
        print("--------Showcasing Merge Sort--------\n")
        print("Making sure that merge sort works correctly")
        tempArray = self.arrayMaker(10)
        print(f"Original Array: {tempArray}")
        answer = (self.merge_sort(tempArray, 0, len(tempArray) - 1))[0]
        print(f"Sorted Array: {answer}")

        print("----Running time analysis----")
        descSortArr = self.sortedArray(1000, asc=False)
        answer = (self.merge_sort(descSortArr, 0, len(descSortArr) - 1))[1]
        print(f"  1. A descending sorted array with 1000 elements took: {answer} second(s).")

        ascSortArr = self.sortedArray(1000)
        answer = (self.merge_sort(ascSortArr, 0, len(ascSortArr) - 1))[1]
        print(f"  2. A descending sorted array with 1000 elements took: {answer} second(s).")

        randomGenThous = self.arrayMaker(1000)
        answer = (self.merge_sort(randomGenThous, 0, len(randomGenThous) - 1))[1]
        print(f"  3. A randomly generated array with 1000 elements took: {answer} second(s).")

        randomGenTenThous = self.arrayMaker(10000)
        answer = (self.merge_sort(randomGenTenThous, 0, len(randomGenTenThous) - 1))[1]
        print(f"  4. A randomly generated array with 10000 elements took: {answer} second(s).")

    def showQuickSort(self):
        print("\n--------Showcasing Quick Sort--------\n")
        print("Making sure that Quick sort works correctly")
        tempArray = self.arrayMaker(10)
        print(f"Original Array: {tempArray}")
        answer = (self.quicksort(tempArray, 0, len(tempArray) - 1))[0]
        print(f"Sorted Array: {answer}")

        print("----Running time analysis----")
        descSortArr = self.sortedArray(1000, asc=False)
        answer = (self.quicksort(descSortArr, 0, len(descSortArr) - 1))[1]
        print(f"  1. A descending sorted array with 1000 elements took: {answer} second(s).")

        ascSortArr = self.sortedArray(1000)
        answer = (self.quicksort(ascSortArr, 0, len(ascSortArr) - 1))[1]
        print(f"  2. A descending sorted array with 1000 elements took: {answer} second(s).")

        randomGenThous = self.arrayMaker(1000)
        answer = (self.quicksort(randomGenThous, 0, len(randomGenThous) - 1))[1]
        print(f"  3. A randomly generated array with 1000 elements took: {answer} second(s).")

        randomGenTenThous = self.arrayMaker(10000)
        answer = (self.quicksort(randomGenTenThous, 0, len(randomGenTenThous) - 1))[1]
        print(f"  4. A randomly generated array with 10000 elements took: {answer} second(s).")

    def showInsertionSort(self):
        print("\n--------Showcasing Insertion Sort--------\n")
        print("Making sure that Insertion sort works correctly")
        tempArray = self.arrayMaker(10)
        print(f"Original Array: {tempArray}")
        answer = (self.insertionSort(tempArray))[0]
        print(f"Sorted Array: {answer}")

        print("----Running time analysis----")
        descSortArr = self.sortedArray(1000, asc=False)
        answer = (self.insertionSort(descSortArr))[1]
        print(f"  1. A descending sorted array with 1000 elements took: {answer} second(s).")

        ascSortArr = self.sortedArray(1000)
        answer = (self.insertionSort(ascSortArr))[1]
        print(f"  2. A descending sorted array with 1000 elements took: {answer} second(s).")

        randomGenThous = self.arrayMaker(1000)
        answer = (self.insertionSort(randomGenThous))[1]
        print(f"  3. A randomly generated array with 1000 elements took: {answer} second(s).")

        randomGenTenThous = self.arrayMaker(10000)
        answer = (self.insertionSort(randomGenTenThous))[1]
        print(f"  4. A randomly generated array with 10000 elements took: {answer} second(s).")


def main():
    assignment = Programming1()
    assignment.showMergeSort()
    assignment.showQuickSort()
    assignment.showInsertionSort()


if __name__ == '__main__':
    main()
