'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Probelm link - https://leetcode.com/problems/maximum-subarray/
'''


# Brute force technique using 2 for loops and trying each sub array sum. sum is calculated automatically with j to avoid another loop.
# TC : O(n^2)  SC : O(1)

def method1(a):
    maxi = a[0]
    for i in range(len(a)):
        s = 0
        for j in range(i, len(a)):
            s += a[j]
            if s > maxi:
                maxi = s
    return maxi


# Usage of Kadens Algorithm. As sum will be greater than 0, finding for that by moving and neglecting sums when it go below 0.
# TC : O(n) Just 1 for loop. SC: O(1)
def method2(a):
    maxi = a[0]
    s = 0
    for i in a:
        s += i
        maxi = s if s > maxi else maxi
        s = 0 if s < 0 else s
    return maxi


def main():
    a = list(map(int, input().split()))

    m = method1(a)
    print("Maximum subarray sum: ", m)
    m = method2(a)
    print("Maximum subarray sum: ", m)


if __name__ == '__main__':
    main()
