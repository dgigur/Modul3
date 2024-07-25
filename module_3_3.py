def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# 1
print_params()
print_params(4)
print_params('Log', True)
print_params([1, 2, 3], {'a': 1, 'b': True}, 'Kisa')
print_params(b = 25)
print_params(c = [1,2,3])

# 2
values_list = [True, (1, 2, 3), 'Kraska']
values_dict = {'a': {1, 1, 2, 5, 2}, 'b': 980, 'c': 'Ogyrec'}
print_params(*values_list)
print_params(**values_dict)

# 3
values_list_2 = ['Kolenka', [43, 1, 'Pypok']]
print_params(*values_list_2, 42)