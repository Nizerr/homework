class CelsiusTemperatureSensor:
    def __init__(self):
        self._temperature = 0

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_celsius(self):
        return self._temperature

class FahrenheitTemperatureSensor:
    def __init__(self):
        self._temperature = 77

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_fahrenheit(self):
        return self._temperature

class TemperatureSensorAdapter:
    def __init__(self, fahrenheit_sensor):
        self.fahrenheit_sensor = fahrenheit_sensor

    def get_temperature_celsius(self):
        fahrenheit_temperature = self.fahrenheit_sensor.get_temperature_fahrenheit()
        celsius_temperature = (fahrenheit_temperature - 32) * 5/9
        return celsius_temperature

def display_temperature(sensor):
    print(f"Temperature: {sensor.get_temperature_celsius():.2f} °C")

# Створюємо об'єкти датчиків
celsius_sensor = CelsiusTemperatureSensor()
fahrenheit_sensor = FahrenheitTemperatureSensor()
adapter = TemperatureSensorAdapter(fahrenheit_sensor)

celsius_sensor.set_temperature(25)
fahrenheit_sensor.set_temperature(77)

print("Celsius Temperature:")
display_temperature(celsius_sensor)

print("\nAdapted Fahrenheit Temperature:")
display_temperature(adapter)
