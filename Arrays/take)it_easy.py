# cook your dish here

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    num_sub = 0
    num_add = 0
    
    result = "No"
    
    flag = True
    sum_n = sum(nums)
    
    if sum_n % len(nums) == 0:
        avg = sum_n // len(nums)
        for num in nums:
            if abs(num - avg) % 2 == 1:
                flag = False
                break
            else:
                if num > avg:
                    num_add += (num - avg) / 2
                elif num < avg:
                    num_sub += (avg - num) / 2
        if not flag:
            print("No")
        else:
            if num_add == num_sub:
                print("Yes")
            else:
                print("No")
    else:
        print("No")