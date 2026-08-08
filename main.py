# DataClass -

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __repr__(self):
#         return f"Product(name='{self.name}', price={self.price})"
#
#     def __eq__(self, other):
#         if not isInstance(other, Product):
#           return NotImplemented
#         return (self.name, self.price) == (other.name, other.price)

from dataclasses import dataclass, field

# @dataclass
# class Product:
#     name: str
#     price: float = 0.0
#
# p1 = Product(name="Ноутбук", price=5.00)
# p2 = Product("Телефон", 100.00)
# print(p1)
# print(p1.name, p1.price)
# print(p1 == p2)




# @dataclass
# class User:
#     username: str
#     email: str
#     roles: list[str] = field(default_factory=list)
#     _internal_id: int = field(default=0, init=False, repr=False)
#
# p1 = User(username="p1", email="")



# @dataclass
# class Order:
#     name: str
#     price: float
#     quantity: int
#     total_price: float = field(init=False)
#  @classmethod # Привязан к классу вместо объекта
#     def change_class_id(cls, new_id: int):
#         cls.id = new_id
#     def __post_init__(self):
#         if self.quantity <= 0:
#             raise ValueError("Количество должно быть положительным")
#         else:
#             self.total_price = self.price * self.quantity
#
# order = Order("Ноутбук", 1000.0, 2)
#
# print(order)



# @dataclass(frozen=True)
# class Point:
#     x: int
#     y: int
#
# p = Point(1, 2)



# @dataclass(order=True)
# class User:
#     user_id: int
#     age: int
#
# u1 = User(1,2)
# u2 = User(3,4)
#
# print(u1 < u2)


# from dataclasses import dataclass, asdict, astuple
#
# @dataclass
# class User:
#     username: str
#     active: bool
#
# user = User("Саша", True)
#
# print(user)
#
# print(asdict(user))
#(*args, **kwargs
# print(astuple(user))

# def logger(func):
#     def wrapper():
#         print("Вызываю функцию")
#         func()
#         print("Функция была вызвана и отработана")
#     return wrapper


# decorator_hello = logger(say_hello)
#
# decorator_hello()

# @logger
# def say_hello():
#     print("Hello, world")
#
# say_hello()


# class User:
#     id: int
#
#     def __init__(self, username: str, password: str):
#         self.username = username
#         self.__password = password
#
#     def verify_password(self, password: str) -> bool:
#         return password == self.__password
#
#     @staticmethod # не привязан к объекту
#     def count(num, num2):
#         return num + num2
#
#     @classmethod # Привязан к классу вместо объекта
#     def change_class_id(cls, new_id: int):
#         cls.id = new_id
#
# u1 = User("user1", "")
#
# print(User.count(2,2))


