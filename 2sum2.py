def two_sum_two(nums, target):
    left_pointer, right_pointer = 0, len(nums) - 1
    while left_pointer < right_pointer:
        current_sum = nums[left_pointer] + nums[right_pointer]
        if current_sum > target:
            right_pointer -= 1
        elif current_sum < target:
            left_pointer += 1
        else:
            return [left_pointer + 1, right_pointer + 1]
    return []
print(two_sum_two([2,3,4], 6))