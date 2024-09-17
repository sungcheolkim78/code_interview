from typing import List

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry

        return bin(x)[2:]

    def addBinary2(self, a: str, b: str) -> str:
        answer = int(a, 2) + int(b, 2)
        return bin(answer)[2:]

    def addBinary3(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')

            carry //= 2

        if carry == 1:
            answer.append('1')
        answer.reverse()

        return ''.join(answer)


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary("1010", "1011"))
    print(solution.addBinary("10101", "1011"))
    print(solution.addBinary("11111", "11"))

    print('-' * 80)
    print(solution.addBinary3("1010", "1011"))
    print(solution.addBinary3("10101", "1011"))
    print(solution.addBinary3("11111", "11"))
