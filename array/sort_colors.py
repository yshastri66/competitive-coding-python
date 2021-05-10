'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Problem link - https://leetcode.com/problems/sort-colors/
'''


# Method 1 is simple with just sorting
# Time complexity : O(nlogn)  Space compelxity: O(1)
def method1(a):
    a.sort()
    return a


# Method 2 is using 3 pointers for 0,1,2 by pushing 0's to front and 2's to end and keeping 1's at mid using pointers.
# Time complexity : O(n) (just a while loop)  Space compelxity: O(1)

def method2(a):
    l, m, h = 0, 0, len(a) - 1

    while m <= h:
        if a[m] == 2:
            a[h], a[m] = a[m], a[h]
            h -= 1
        else:
            if a[m] == 0:
                a[l], a[m] = a[m], a[l]
                l += 1
            m += 1
    return a


def main():
    a = list(map(int, input().split()))
    sort_array = method1(a)
    print(*sort_array)

    sort_array = method2(a)
    print(*sort_array)


if __name__ == '__main__':
    main()
