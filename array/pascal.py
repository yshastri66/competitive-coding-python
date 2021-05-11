'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Probelm Link - https://leetcode.com/problems/pascals-triangle/
'''


# TC: O(n^2) and Auxiliary space : O(n) as we need to store previous row to get current row.
def solution(n):
    tri = []
    for i in range(n):
        temp = [0] * (i + 1)
        temp[0], temp[-1] = 1, 1
        for j in range(1, len(temp) - 1):
            temp[j] = tri[i - 1][j - 1] + tri[i - 1][j]
        tri.append(temp)
    return tri


def main():
    n = int(input())

    a = solution(n)
    print("Pascal Triangle :\n ", a)


if __name__ == '__main__':
    main()
