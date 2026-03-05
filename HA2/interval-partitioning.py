"""
Problem 2 (10):
This is the interval partitioning problem that we discussed in the class.
You are given a list of intervals where each interval represents the start and end times of a lecture. Your task is to determine the minimum number of classrooms needed so that every lecture can be scheduled without any overlap in the same classroom.
The input to your program will be a variable named intervals which will be a list of lists. Each interval is in the form [start, end]. The intervals are NOT sorted. You are allowed to use library functions for sorting.
Example:
intervals = [[30, 75], [0, 50], [60, 150], [80, 120], [55, 65]]
The output will be 3, which is the minimum number of classrooms required to schedule all lectures.
Explanation:
One possible scheduling could be:
Classroom 1: [0, 50], [55, 65], [80, 120]
Classroom 2: [30, 75] (and possibly another lecture if it fits)
Classroom 3: [60, 150]
HINT: Look at the interval partitioning part of the lecture slides to implement it using priority queue (min-heap).

EARLIEST-START-TIME-FIRST (n, s1, s2, …, sn , f1, f2, …, fn)
_________________________________ ______ ______ ______ ______
SORT lectures by start times and renumber so that s1 ≤ s2 ≤ … ≤ sn.
d ← 0
FOR j = 1 TO n
IF (lecture j is compatible with some classroom)
Schedule lecture j in any such classroom k.
ELSE
Allocate a new classroom d + 1.
Schedule lecture j in classroom d + 1.
d ← d + 1
RETURN schedule.
_________________________________ ______ ______ ______ ______

"""
import heapq

def interval_partitioning(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    pq = []
    num_classrooms = 0
    for interval in sorted_intervals:
        start = interval[0]
        end = interval[1]
        if (len(pq) == 0 or pq[0] > start):
            heapq.heappush(pq, end)
            num_classrooms+=1
        else:
            heapq.heappop(pq)
            heapq.heappush(pq, end)
    return num_classrooms

intervals = [[3, 5]]
print(interval_partitioning(intervals))
print("----------------------------")

intervals = [[1, 2], [2, 4], [4, 6], [6, 7]]
print(interval_partitioning(intervals))
print("----------------------------")

intervals = [[1, 10], [2, 9], [3, 8], [4, 7]]
print(interval_partitioning(intervals))
print("----------------------------")

intervals = [[0, 3], [1, 2], [3, 5], [4, 6], [6, 8]]
print(interval_partitioning(intervals))
print("----------------------------")

intervals = [[0, 4], [0, 2], [1, 5], [2, 3], [3, 7], [3, 6], [5, 8], [6, 9], [8, 10]]
print(interval_partitioning(intervals))
print("----------------------------")
            
        