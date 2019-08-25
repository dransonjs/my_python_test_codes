# 优化冒泡排序，对已经有序的数字不再做无用功的排序


def bubble_sort(nums):
    for i in range(len(nums) - 1):
        ex_flag = False  # 改进后的冒泡，设置一个交换标志位
        for j in range(len(nums) - i - 1):

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                ex_flag = True
        if not ex_flag:
            return nums  # 这里代表计算机偷懒成功 (〃'▽'〃)

    return nums  # 这里代表计算机没有偷懒成功 o(╥﹏╥)o


list1 = [2, 3, 1, 4, 78, 51, 23]

print(bubble_sort(list1))
