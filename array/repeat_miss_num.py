'''
Given an unsorted array Arr of size N of positive integers.
One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.
Example 2:

Input:
N = 3
Arr[] = {1, 3, 3}
Output: 3 2
Explanation: Repeating number is 3 and
smallest positive missing number is 2.

Problem link - https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1

'''


# Casual method. First sorting, then finding any element eqaul to next element and seeing any element missing.
# TC: O(nlogn+n) or just O(nlogn)  Space complexity: O(1)
def method1(a):
    a.sort()
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            r_num = a[i]
            break
    for i in range(1, len(a) + 1):
        if a[i - 1] != i:
            m_num = i
            break
    return m_num, r_num


# Using Dictionary mapping.
# TC : O(2n) Only two loops.  SC: O(n) to store array in dict.
def method2(a):
    d = {}
    for i in a:
        if i in d:
            r_num = i
        else:
            d[i] = 1

    for i in range(1, len(a) + 1):
        if i not in d:
            m_num = i
    return m_num, r_num


# Making numbers index number as negative and then detecting. works here only because range 1 - n.
# TC : O(2n) only 2 loops.   SC: O(1) as no space is consumed.
def method3(a):
    for i in range(len(a)):
        x = abs(a[i])
        if a[x - 1] > 0:
            a[x - 1] *= -1
        else:
            r_num = x

    for i in range(len(a)):
        if a[i] > 0:
            m_num = i + 1
    return m_num, r_num


# Mathematical method. By finding sum of n and n^2. By solving simultanious equations.
# TC : O(n) only one loop.  SC: O(1)
def method4(a):
    n = len(a)

    s = (n * (n + 1)) // 2
    sq_sum = (n * (n + 1) * (2 * n + 1)) // 6

    for i in range(len(a)):
        s -= a[i]
        sq_sum -= (a[i] * a[i])

    m_num = (s + (sq_sum // s)) // 2
    r_num = m_num - s
    return m_num, r_num


def main():
    a = list(map(int, input().split()))
    a1, a2, a3, a4 = a[:], a[:], a[:], a[:]
    m_num, r_num = method1(a1)
    print("missing num: ", m_num, " Repeating num: ", r_num)
    m_num, r_num = method2(a2)
    print("missing num: ", m_num, " Repeating num: ", r_num)
    m_num, r_num = method3(a3)
    print("missing num: ", m_num, " Repeating num: ", r_num)
    m_num, r_num = method4(a4)
    print("missing num: ", m_num, " Repeating num: ", r_num)


if __name__ == '__main__':
    main()
