# Question prompt: https://leetcode.com/discuss/interview-question/1930478/football-scores-hackerrank-question
# Tested in Goldman sachs coding assesment

# a = [1, 2, 4]
# b = [3, 5]

def football_scores(a, b):
    a.sort()
    result = []

    # Get the number of elements in list a which are lesser than or equal to value of element i in list b
    for i in b:
        low = 0
        high = len(a) -1
        while (high >= low):
            mid = (low + high)//2
            if i >= a[mid]:
                low = mid + 1
            else:
                high = mid - 1
        result.append(low)
    return result

#print(football_scores([1, 2, 4], [3, 5]))
