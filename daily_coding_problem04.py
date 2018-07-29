'''
Daily Coding Problem: Problem #4

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

'''

def missing_pos(arr):
    if len(arr) > 0:
        count = [0 for _ in range(256)]
        for a in arr:
            if a >= 0:
                count[a] += 1
        for i,c in enumerate(count[1:]):
            if c == 0:
                return i+1

if __name__ == '__main__':
    # arr = [int(x) for x in input().split(' ')]
    try:
        arr = [3, 4, -1, 1]
        print(arr)
        print(missing_pos(arr=arr))
    except:
        print('error')
