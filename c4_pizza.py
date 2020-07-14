class Pizza:
    def __init__(self):
        self.name = 'pizza'

    def make(self):
        print('normal make {}'.format(self.name))


class PizzaStore:
    def __init__(self):
        self.name = 'Normal Store'

    def order_pizza(self, string):
        pizza = self.create_pizza(string)
        pizza.make()


class PizzaA(Pizza):
    def __init__(self):
        self.name = 'pizzaA'


class PizzaB(Pizza):
    def __init__(self):
        self.name = 'pizzaB'

    def make(self):
        print('special make {}'.format(self.name))


class PizzaC(Pizza):
    def __init__(self):
        self.name = 'pizzaC'

    def make(self):
        print('special make {}'.format(self.name))


class NewYorkPizzaStore(PizzaStore):
    def __init__(self):
        self.name = 'New York Pizza Store'

    def create_pizza(self, string):
        if string == 'PizzaA':
            return PizzaA()
        elif string == 'PizzaB':
            return PizzaB()


class ChicagoPizzaStore(PizzaStore):
    def __init__(self):
        self.name = 'Chicago Pizza Store'

    def create_pizza(self, string):
        if string == 'PizzaA':
            return PizzaA()
        elif string == 'PizzaC':
            return PizzaC()


pizza_store = NewYorkPizzaStore()
pizza_store.order_pizza('PizzaA')
pizza_store.order_pizza('PizzaB')

pizza_store = ChicagoPizzaStore()
pizza_store.order_pizza('PizzaA')
pizza_store.order_pizza('PizzaC')