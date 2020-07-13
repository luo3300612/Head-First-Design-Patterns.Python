import abc


class Beverage(metaclass=abc.ABCMeta):
    def __repr__(self):
        return '名称:{}, 价格:{}'.format(self.name, self.cost)


class Supplement:
    def __call__(self, beverage):
        beverage.name = self.name + beverage.name
        beverage.cost = self.cost + beverage.cost
        return beverage


class Milk(Beverage):
    def __init__(self):
        self.name = '牛奶'
        self.cost = 9


class MilkyTea(Beverage):
    def __init__(self):
        self.name = '奶茶'
        self.cost = 10


class Cappuccino(Beverage):
    def __init__(self):
        self.name = '卡布奇诺'
        self.cost = 15


class Pearl(Supplement):
    def __init__(self):
        self.name = '波霸'
        self.cost = 2


class Coconut(Supplement):
    def __init__(self):
        self.name = '椰果'
        self.cost = 1


## 配料
pearl = Pearl()
coconut = Coconut()

order1 = MilkyTea()
order1 = pearl(order1)
print(order1)

order2 = Cappuccino()
order2 = pearl(coconut(pearl(order2)))
print(order2)
