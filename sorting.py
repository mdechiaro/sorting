#!/usr/bin/python
# vim: et ts=4 sw=4
""" Various sorting algorithms."""
import random
import heapq
import itertools

class Sorting(object):
    """ Class contains various different sorting methods."""
    def __init__(self):
        pass

    @staticmethod
    def random_data(val=100, start=0, stop=1000):
        """ Method returns a list of random data. It is useful for testing. """
        return [random.randint(start, stop) for dummy in range(val)]

    @staticmethod
    def heap_sort(array):
        """ Heap sort an array """
        heapq.heapify(array)
        return [heapq.heappop(array) for dummy in range(len(array))]

    @staticmethod
    def quick_sort(array):
        """ Quick sort an array """
        if len(array) > 1:
            middle = len(array) / 2
            less = []
            more = []
            for num, item in enumerate(array):
                if num != middle:
                    if item < array[middle]:
                        less.append(item)
                    else:
                        more.append(item)
            Sorting.quick_sort(less)
            Sorting.quick_sort(more)
            array[:] = less + [array[middle]] + more
        return array

    @staticmethod
    def merge_sort(array):
        """ Merge sort an array """
        if len(array) <= 1:
            return array
        middle = len(array) / 2
        left = array[:middle]
        right = array[middle:]
        left = Sorting.merge_sort(left)
        right = Sorting.merge_sort(right)
        return list(heapq.merge(left, right))

    @staticmethod
    def radix_sort(array, subsets=10, modulo=10, divisor=1):
        """ Radix sort an array of positive integers """
        step = 10
        count = 0
        # number of digits in largest number
        largest = int(len(str(max(array))))
        while largest > count:
            segments = [list() for dummy in range(subsets)]
            for item in array:
                # match the digit to the correct segment
                segments[(item / divisor % modulo)].append(item)
            divisor = divisor * step
            # merge segments into list
            array = list(itertools.chain(*segments))
            count += 1
        return array
