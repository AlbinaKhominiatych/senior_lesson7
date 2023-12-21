# ітератори
lst = ["one", 2, 3]  # список
index = lst[0]
print(index)
# for elem in lst:
#     print(elem)
iterator = iter(lst)
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))


# ітератор через класи

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
#Використання ітератора
my_list = [1, 5, 7, 90, 5.5]
my_iterator = MyIterator(my_list)
print(my_iterator)
print(*my_iterator)

#генератори
def my_generator(data):
    for item in data:
        yield item
#використання
my_list = [1, 5, 7, 90, 5.5]
my_gen = my_generator(my_list)
print(*my_gen)