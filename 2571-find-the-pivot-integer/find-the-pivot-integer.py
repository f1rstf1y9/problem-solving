class Solution:
    def pivotInteger(self, n: int) -> int:
        numbers = [i for i in range(n+1)]
        for i in range(1, n+1):
            if sum(list(numbers[:i+1])) == sum(numbers[i:]):
                return i
        return -1
