from leetcode.algorithms.running_sum_of_1d_array import Solution


def test_asc_order():
    assert Solution().runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]


def test_same():
    assert Solution().runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]


def test_no_order():
    assert Solution().runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
