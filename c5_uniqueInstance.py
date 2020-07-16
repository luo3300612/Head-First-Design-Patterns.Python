class Singleton:
    _instance = None

    def __init__(self, name, age):
        if self._instance is not None:
            raise Exception('This is a singleton')
        self.name = name
        self.age = age
        Singleton._instance = self

    @staticmethod
    def get_instance(name,age):
        if Singleton._instance is None:
            Singleton(name,age)
        return Singleton._instance


a = Singleton.get_instance(1, 2)
b = Singleton.get_instance(2, 3)
print(id(a))
print(id(b))
