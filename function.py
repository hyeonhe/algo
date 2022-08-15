from collections import defaultdict
def solution(arr):
    arr_dict = defaultdict(int)
    for i in arr:
        arr_dict[i] += 1

    result = []

    for i, v in arr_dict.items():
        if arr_dict[i] > 1:
            result.append(v)

    return result or [-1]


print(solution([1, 2, 3, 3, 3, 3, 4, 4]))
print(solution([3, 2, 4, 4, 2, 5, 2, 5, 5]))
print(solution([3, 5, 7, 9, 1]))