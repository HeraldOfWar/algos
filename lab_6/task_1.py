import random

print_dict = {}
max_i = 0


def merge(left_list, right_list, i=0, saved_list=[]):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    if not print_dict.get(str(i)):
        print_dict[str(i)] = []
    if saved_list:
        print_dict[str(i - 1)].append(saved_list)
    print_dict[str(i)].append(sorted_list)

    return sorted_list


def merge_sort(nums, i=2, saved_list=[]):
    global max_i
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    if not print_dict.get(str(i)):
        print_dict[str(i)] = []
    print_dict[str(i)].append(nums[:mid])
    print_dict[str(i)].append(nums[mid:])
    if len(nums[:mid]) == 1 and len(nums[mid:]) > 1:
        if not print_dict.get(str(i + 1)):
            print_dict[str(i + 1)] = []
        print_dict[str(i + 1)].append(nums[:mid])
        saved_list = nums[:mid]

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid], i + 1)
    right_list = merge_sort(nums[mid:], i + 1)

    max_i = max(max_i, i)
    new_i = max_i + (max_i - i) + 1

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list, new_i, saved_list)


test = [6, 5, 12, 10, 9, 1]
print_dict['1'] = [test]
merge_sort(test)
for key, item in print_dict.items():
    print(f'{key} {item}')

print()

max_i = 0
print_dict = {}
random_test = [random.randint(0, 100) for i in range(random.randint(4, 20))]
print_dict['1'] = [random_test]
merge_sort(random_test)
for key, item in print_dict.items():
    print(f'{key} {item}')