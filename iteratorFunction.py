lst = ["Test", 1, 3, 4, 5, 6, 7, 8]
my_iterator = iter(lst)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

for _ in range(len(lst)):
    print(next(my_iterator))
