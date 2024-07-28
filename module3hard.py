data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
#list_1 = [[1, 2, 3], [4, 5, 'Odis']]
#list_2 = [{"5": 'Hello3123'}]            #Опыты
#list_3 = {9: 'Bye', 10: 'talk'}


def dict_unpacking(**kwargs):
    dict_to_list = list(kwargs.items())
    return dict_to_list


def calculate_structure_sum(*args):
    sum_of_elements = 0
    for i in args:
        if isinstance(i, int or float):
            sum_of_elements += i
        elif isinstance(i, str):
            sum_of_elements += len(i)
        elif isinstance(i, dict):
            #new_list = dict_unpacking(**i)
            sum_of_elements = sum_of_elements + calculate_structure_sum(list(i.items()))
            #sum_of_elements = sum_of_elements + calculate_structure_sum(*new_list) # Так тоже можно но это +1 функция
        else:
            for j in i:
                sum_of_elements = sum_of_elements + calculate_structure_sum(j)
    return sum_of_elements


#print(calculate_structure_sum(list_2))

result = calculate_structure_sum(data_structure)
print(result)
