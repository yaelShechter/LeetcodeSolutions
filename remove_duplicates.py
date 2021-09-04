#return number of unique numbers, change sorted array in place. 

def remove_duplicates(nums: List[int]) -> int:
    current_index = 1
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[current_index] = nums[i + 1]
            current_index += 1
    return current_index
