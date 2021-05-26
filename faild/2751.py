count = int(input())
nums = []


# for i in range(count):
#     a = int(input())
#     nums.append(a)


def merge(list1, list2):
    merged_list = []

    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    if i == len(list1):
        merged_list += list2[j:]
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list


def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list
    else:
        left_half = my_list[:len(my_list) // 2]
        right_half = my_list[len(my_list) // 2:]

        return merge(merge_sort(left_half), merge_sort(right_half))


merge_sort(nums)
for i in range(count):
    print(nums[i])
