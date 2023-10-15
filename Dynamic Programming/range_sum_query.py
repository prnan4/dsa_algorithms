class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        sum_nums = 0
        for i in range(left, right+1):
            sum_nums += self.nums[i]
        return sum_nums
