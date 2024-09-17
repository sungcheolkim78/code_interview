from typing import List
from itertools import zip_longest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        # reverse both numbers
        first = num1[::-1]
        second = num2[::-1]

        # for each digit in second, multiply the digit by first and then
        # store the multiplication result (reversed) in the result array
        results = []
        for index, digit in enumerate(second):
            results.append(self.multiply_on_digit(digit, index, first))

        # add all of the results together to get the final result
        answer = self.sum_results(results)

        return "".join(str(digit) for digit in reversed(answer))

    def multiply_on_digit(self, digit2: str, num_zeros: int, first: List[str]) -> List[int]:
        """Multiplies first by a digit from second (digit2)"""

        # Insert zeros at the beginning of the current result based on the current digit's place
        current_result = [0] * num_zeros
        carry = 0

        # multiply each digit in first with the current digit of the second
        for digit1 in first:
            multiplication = int(digit1) * int(digit2) + carry
            carry = multiplication // 10
            current_result.append(multiplication % 10)

        if carry != 0:
            current_result.append(carry)

        return current_result

    def sum_results(self, results: List[List[int]]) -> List[int]:
        # initialize answer as a number from results.
        answer = results.pop()

        # add each result to answer one at a time
        for result in results:
            new_answer = []
            carry = 0

            for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
                curr_sum = digit1 + digit2 + carry
                carry = curr_sum // 10
                new_answer.append(curr_sum % 10)

            if carry != 0:
                new_answer.append(carry)

            answer = new_answer

        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.multiply("123", "456"))

    print(solution.multiply("100", "456"))

    print(solution.multiply("105", "45"))
