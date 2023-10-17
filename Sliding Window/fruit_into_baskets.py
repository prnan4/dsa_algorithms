class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        fruits_count = {}
        max_fruits = 0
        while r < len(fruits):
            if fruits[r] not in fruits_count.keys():
                if len(fruits_count) == 2:

                    min_value = float(inf)
                    min_key = float(inf)
                    for key in fruits_count:
                        if fruits_count[key] < min_value:
                            min_value = fruits_count[key]
                            min_key = key

                    del fruits_count[min_key]
                    l = min_value + 1
            fruits_count[fruits[r]] = r
            max_fruits = max(max_fruits, r - l + 1)
            r += 1
        return max_fruits