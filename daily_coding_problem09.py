'''
Daily Coding Problem: Problem #9

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def sum_every_other(arr):
    b, a = 0, 0
    for c in arr:
        new_a = a if a>b else b
        b = a + c
        a = new_a
    return b

if __name__ == '__main__':
    # arr = [int(x) for x in input().split(' ')]
    try:
        arr = [5, 1, 1, 5, 2, 4, 6, 2, 5]
        print(arr)
        print(sum_every_other(arr=arr))
    except:
        print('error')
