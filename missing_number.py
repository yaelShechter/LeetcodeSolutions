def find_missing_number(nums: List[int]) -> int:
    n = len(nums) + 1
    total_sum = int((n * (n + 1)) / 2)
    sum_of_nums = 0
    for num in nums:
        sum_of_nums += num

    return total_sum - sum_of_nums
