# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

def fib(n):
    nums = [1, 1]
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(2, n):
            nums.append(nums[i-1] + nums[i-2])
        return nums[n-1]
    
print(fib(55))