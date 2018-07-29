'''
Daily Coding Problem- Problem #1

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def sum2k(arr, k):
    if len(arr) > 1 and k > 0:
        adict = {}
        for a in arr:
            if a not in adict:
                adict[k-a] = a
            else:
                return [k-a, a]

if __name__ == '__main__':
    # arr = [int(x) for x in input().split(' ')]
    # k = int(input())
    try:
        arr = [10, 15, 3, 7]
        k = 17
        print(arr,'sum:', k)
        print(sum2k(arr=arr, k=k))
    except:
        print('error')
