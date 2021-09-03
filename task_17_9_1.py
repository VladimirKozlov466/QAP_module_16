original_list = list(map(int, input("Введите последовательность чисел через пробел:").split()))

element = int(input("Введите число для поиска в списке:"))


print(f'Вид оригинального списка: {original_list}')
print(f'Число для поиска введенное пользователем = {element}')


def merge_sort(original_list):  # функция для сортировки введенного списка "слиянием"
    if len(original_list) < 2:
        return original_list[:]
    else:
        middle = len(original_list) // 2
        left = merge_sort(original_list[:middle])
        right = merge_sort(original_list[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


list_sorted = merge_sort(original_list)  # сортируем введенный пользователем список


# и присваеваем ему новое значение переменной


def binary_search(list_sorted, element, left=0, right=len(list_sorted) -1):
    # функция с алгоритмом двоичного поиска

    if left > right:
        return f'Число {element} за пределами массива'

    if list_sorted[0] == element:
        return f'Число {element} равно наименьшему значению массива' \
               f' в массиве нет числа менее {element}'

    middle = (right + left) // 2

    if list_sorted[middle - 1] < element <= list_sorted[middle]:
        return f'Индекс элемента в списке значение ' \
               f'которого меньше введенного числа =  {middle - 1}'



    elif element < list_sorted[middle]:

        return binary_search(list_sorted, element, left, middle - 1)
    else:
        return binary_search(list_sorted, element, middle + 1, right)


print(f'Вид отсортированного списка {list_sorted}')
print(binary_search(list_sorted, element))