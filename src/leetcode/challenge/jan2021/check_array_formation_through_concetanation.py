#
# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3589/
#
# january-leetcoding-challenge-2021
# [3589] Check Array Formation Through Concatenation
#
#
# You are given an array of distinct integers arr and an array of integer arrays pieces,
# where the integers in pieces are distinct.
# Your goal is to form arr by concatenating the arrays in pieces in any order.
# However, you are not allowed to reorder the integers in each array pieces[i].
#
# Return true if it is possible to form the array arr from pieces.
# Otherwise, return false.
#
# Constraints:
# - 1 <= pieces.length <= arr.length <= 100
# - sum(pieces[i].length) == arr.length
# - 1 <= pieces[i].length <= arr.length
# - 1 <= arr[i], pieces[i][j] <= 100
# - The integers in arr are distinct.
# - The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).


from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for piece in pieces:
            i = None
            try:
                i = arr.index(piece[0])
            except ValueError:
                return False

            for val in piece:
                if len(arr) <= i or arr[i] != val:
                    return False
                i += 1

        return True
