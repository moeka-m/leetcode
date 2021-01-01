from leetcode.algorithms.two_sum import Solution


def test_asc_order():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_desc_order():
    assert Solution().twoSum([15, 11, 7, 2], 9) == [2, 3]


def test_no_order():
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]


def test_same():
    assert Solution().twoSum([3, 3], 6) == [0, 1]
