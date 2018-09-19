'''
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
'''

class Solution:
    def powNaive(self, a, b):
        # naive method of repeated multiplication
        result = 1
        for _ in range(b):
            result *= a
        return result

    def powNaive2(self, a, b):
        # naive method of repeated multiplication
        if not b:
            return 1
        return a * self.powNaive2(a, b-1)

    def powSquaring(self, a, b):
        # exponentiation by squaring
        if b == 1:
            return a
        elif b % 2 == 1:
            return a * self.powSquaring(a, b-1)
        else:
            p = self.powSquaring(a, b/2)
            return p*p

    def powSquaring2(self, a, b):
        # exponentiation by squaring
        result = 1
        while True:
            if b % 2 == 1:
                result *= a
                b -= 1
                if b == 0:
                    break
            b /= 2
            a *= a
        return result

    def powBinary(self, a, b):
        # left-to-right binary exponentiation
        def _traversal(n):
            bits = []
            while n:
                bits.append(n % 2)
                if n % 2 == 1:
                    n -= 1
                n /= 2
            return bits

        result = 1
        for x in reversed(_traversal(b)):
            result *= result
            if x == 1:
                result *= a
        return result

a, b = 2, 5
a, b = 3, 4
Solution().powBinary(a, b)
