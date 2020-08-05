import abc


class DuckInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def quack(self):
        pass

    @abc.abstractmethod
    def fly(self):
        pass


class SomeDuck(DuckInterface):
    def quack(self):
        print('ga ga ga')

    def fly(self):
        print('wu hu~')


class TurkeyInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def gobble(self):
        pass

    @abc.abstractmethod
    def fly(self):
        pass


class SomeTurkey(TurkeyInterface):
    def gobble(self):
        print('em em em')

    def fly(self):
        print('fly short')


# 对象适配器
class DuckAdapter(DuckInterface):
    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()


# 类适配器
class DuckAdapter2(SomeDuck, SomeTurkey):
    def quack(self):
        SomeTurkey.gobble(self)

    def fly(self):
        for i in range(5):
            SomeTurkey.fly(self)


turkey = SomeTurkey()
print('d1...')
d1 = DuckAdapter(turkey)
d1.fly()
d1.quack()

print('d2...')
d2 = DuckAdapter2()
d2.fly()
d2.quack()