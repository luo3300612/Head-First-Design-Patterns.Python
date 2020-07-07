import abc


class Duck(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fly(self):
        pass

    @abc.abstractmethod
    def quack(self):
        pass


class FlyBehaviour(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fly(self):
        pass


class QuackBehaviour(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def quack(self):
        pass


class FlyInTheSky(FlyBehaviour):
    def fly(self):
        print('fly in the sky')


class CanNotFly(FlyBehaviour):
    def fly(self):
        print('can not fly')


class QuackOut(QuackBehaviour):
    def quack(self):
        print('Ga Ga Ga')


class CanNotQuack(QuackBehaviour):
    def quack(self):
        print('can not quack')


class MallardDuck(Duck):
    def __init__(self):
        self.fly_behaviour = FlyInTheSky()
        self.quack_behaviour = QuackOut()

    def fly(self):
        self.fly_behaviour.fly()

    def quack(self):
        self.quack_behaviour.quack()


class RedheadDuck(Duck):
    def __init__(self):
        self.fly_behaviour = FlyInTheSky()
        self.quack_behaviour = QuackOut()

    def fly(self):
        self.fly_behaviour.fly()

    def quack(self):
        self.quack_behaviour.quack()


class RubberDuck(Duck):
    def __init__(self):
        self.fly_behaviour = CanNotFly()
        self.quack_behaviour = QuackOut()

    def fly(self):
        self.fly_behaviour.fly()

    def quack(self):
        self.quack_behaviour.quack()


class DecoyDuck(Duck):
    def __init__(self):
        self.fly_behaviour = CanNotFly()
        self.quack_behaviour = CanNotQuack()

    def fly(self):
        self.fly_behaviour.fly()

    def quack(self):
        self.quack_behaviour.quack()


if __name__ == '__main__':
    print('MallardDuck')
    duck = MallardDuck()
    duck.fly()
    duck.quack()

    print('RedheadDuck')
    duck = MallardDuck()
    duck.fly()
    duck.quack()

    print('RubberDuck')
    duck = RubberDuck()
    duck.fly()
    duck.quack()

    print('DecoyDuck')
    duck = DecoyDuck()
    duck.fly()
    duck.quack()
