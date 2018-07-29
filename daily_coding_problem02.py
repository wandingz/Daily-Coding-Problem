'''
Daily Coding Problem: Problem #2

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def get_prod(arr):
    if len(arr) > 1:
        product = 1
        alst = []
        for a in arr:
            alst.append(product)
            product *= a

        product = 1
        for i in range(len(arr)-1,-1,-1):
            alst[i] *= product
            product *= arr[i]
        return alst

if __name__ == '__main__':
    try:
        arr = [1, 2, 3, 4, 5]
        print(arr)
        if get_prod(arr) == [120, 60, 40, 30, 24]:
            print('test array passed')
    except:
        print('error')
    # arr = [int(x) for x in input().split(' ')]
    print(get_prod(arr))
