class WeatherData:
    def __init__(self):
        self.observers = []
        self.humidity = 50
        self.temperature = 25
        self.pressure = 1000

        self.humidity_unit = '%'
        self.temperature_unit = 'K'
        self.pressure_unit = 'Pa'

    def stringlize(self):
        return str(self.humidity) + self.humidity_unit, str(self.temperature) + self.temperature_unit, str(
            self.pressure) + self.pressure_unit

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(*self.stringlize())


class HumidityBoard:
    def __init__(self):
        self.humidity = None

    def update(self, humidity, _, __):
        self.humidity = humidity

    def show(self):
        print('Current Humidity is ' + self.humidity)


class TemperatureBoard:
    def __init__(self):
        self.temperature = None

    def update(self, _, temperature, __):
        self.temperature = temperature

    def show(self):
        print('Current Temperature is ' + self.temperature)


class PressureBoard:
    def __init__(self):
        self.pressure = None

    def update(self, _, __, pressure):
        self.pressure = pressure

    def show(self):
        print('Current Pressure is ' + self.pressure)


if __name__ == '__main__':
    weather_data = WeatherData()
    board1 = HumidityBoard()
    board2 = TemperatureBoard()
    board3 = PressureBoard()
    weather_data.register_observer(board1)
    weather_data.register_observer(board2)
    weather_data.register_observer(board3)

    weather_data.notify()
    board1.show()
    board2.show()
    board3.show()

    weather_data.remove_observer(board1)

    weather_data.humidity *= 2
    weather_data.temperature *= 2
    weather_data.pressure *= 2

    weather_data.notify()
    board1.show()
    board2.show()
    board3.show()