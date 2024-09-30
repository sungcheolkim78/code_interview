from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        answers = []

        def recurse(index: int, prev_op: int, current_op: int, value: int, string: list[str]):
            print(index, current_op, string, value)
            if index == n:
                if value == target and current_op == 0:
                    answers.append("".join(string[1:]))
                return

            current_op = current_op * 10 + int(num[index])
            str_op = str(current_op)

            if current_op > 0:
                recurse(index + 1, prev_op, current_op, value, string)

            string.append('+')
            string.append(str_op)
            recurse(index + 1, current_op, 0, value + current_op, string)
            string.pop()
            string.pop()

            if string:
                string.append('-')
                string.append(str_op)
                recurse(index + 1, -current_op, 0, value - current_op, string)
                string.pop()
                string.pop()

                string.append('*')
                string.append(str_op)
                recurse(index + 1, current_op * prev_op, 0, value - prev_op + current_op * prev_op, string)
                string.pop()
                string.pop()

        recurse(0, 0, 0, 0, [])
        return answers


if __name__ == "__main__":
    solution = Solution()
    print(solution.addOperators("123", 6))
    print(solution.addOperators("10", 1))
    print(solution.addOperators("3", 9))
