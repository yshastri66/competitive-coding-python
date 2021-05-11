'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Problem Link - https://leetcode.com/problems/merge-intervals/

'''


# Sorting the array. If probelm statement gives array as sorted, then we need'nt sort it.
# Merging overlapping using temp variable and putting into final array after merging.
# TC: 1.If array sorted : just O(m+n) since a.sort() is not needed.
# 2. If array not sorted : O(m+n)log(m+n) as we need a.sort()
# Auxiliary space : O(1) just one temp variable.
def method1(a):
    a.sort()
    temp = a[0]
    final = []
    for i, j in a:
        if temp[1] >= i:
            temp[1] = max(temp[1], j)
        else:
            final.append(temp)
            temp = [i, j]
    final.append(temp)
    return final


def main():
    n = int(input())
    a = []
    for _ in range(n):
        i, j = map(int, input().split())
        a.append([i, j])

    op_arr = method1(a)
    print(" Array after merging :", op_arr)


if __name__ == '__main__':
    main()
