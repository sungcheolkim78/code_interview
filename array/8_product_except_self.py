from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    Given a list of integers, return a list where each element is the product of all the elements except the one at the same index.
    For example, if nums = [1, 2, 3, 4], return [24, 12, 8, 6].
    :param nums: A list of integers.
    :return: A list of integers.
    """
    n = len(nums)
    L, R, ans = [1] * n, [1] * n, [1] * n

    for i in range(1, n):
        L[i] = L[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        R[i] = R[i + 1] * nums[i + 1]

    for i in range(n):
        ans[i] = L[i] * R[i]
    return ans


if __name__ == '__main__':
    print(product_except_self([1, 2, 3, 4]))
    print(product_except_self([-1, 1, 0, -3, 3]))
