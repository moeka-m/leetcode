#
# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3591/
#
# january-leetcoding-challenge-2021
# [3591] Beautiful Arrangement
#
# Suppose you have n integers labeled 1 through n.
# A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement
# if for every i (1 <= i <= n), either of the following is true:
#
# perm[i] is divisible by i.
# i is divisible by perm[i].
#
# Given an integer n, return the number of the beautiful arrangements that you can construct.
#
# Constraints:
# - 1 <= n <= 15
#


from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        self.__count = 0
        self.__calc(n, 1, [False] * (n + 1))
        return self.__count

    def __calc(self, n: int, pos: int, visited: List[bool]) -> None:
        """タイトル
        計算

        Args:
            n int: n
            pos int: 現在、何番目に数字を配置しようとしているか
            visited List[bool]: 配置済みの数字の管理をする配列。visited[1] == True の場合、1はすでに配置済みであり使えない。
        """
        if pos > n:
            self.__count += 1

        for i in range(1, n + 1):
            if not visited[i] and self.__isBeautiful(i, pos):
                visited[i] = True
                self.__calc(n, pos + 1, visited)
                visited[i] = False

    def __isBeautiful(self, i: int, pos: int) -> bool:
        """
        配置しようとしているものが条件に合うかを返す

        Args:
            i int: 配置しようとしている数字
            pos int: 配置しようとしている場所
        """
        return pos % i == 0 or i % pos == 0
