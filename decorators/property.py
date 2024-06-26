class MyClass:
    def __init__(self, x):
        self.x = x

    @property
    def x_doubled(self):
        return self.x * 2

    @x_doubled.setter
    def x_doubled(self, x_doubled):
        self.x = x_doubled // 2


my_object = MyClass(5)
print(my_object.x_doubled)  # 10
print(my_object.x)  # 5
my_object.x_doubled = 1000  #
print(my_object.x_doubled)  # 100
print(my_object.x)  # 50