from leetcode.challenge.jan2021.check_array_formation_through_concetanation import (
    Solution,
)


def test_1():
    assert Solution().canFormArray([85], [[85]]) is True


def test_2():
    """
    Concatenate [15] then [88]
    """
    assert Solution().canFormArray([15, 88], [[88], [15]]) is True


def test_3():
    """
    Even though the numbers match, we cannot reorder pieces[0].
    """
    assert Solution().canFormArray([49, 18, 16], [[16, 18, 49]]) is False


def test_4():
    """
    Concatenate [91] then [4,64] then [78]
    """
    assert Solution().canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]) is True


def test_5():
    assert Solution().canFormArray([1, 3, 5, 7], [[2, 4, 6, 7]]) is False


def test_6():
    assert Solution().canFormArray([1, 2, 3], [[2], [1, 3]]) is False
