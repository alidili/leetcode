N = int(input())
nums = list(map(int, input().split()))


def quick_sort(nums, left, high):
    if left >= high:
        return
    i, j = left - 1, high + 1
    x = nums[(left + high) >> 1]
    while i < j:
        while 1:
            i += 1
            if nums[i] >= x:
                break
        while 1:
            j -= 1
            if nums[j] <= x:
                break
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    quick_sort(nums, left, j)
    quick_sort(nums, j + 1, high)


quick_sort(nums, 0, N - 1)
print(' '.join(list(map(str, nums))))
