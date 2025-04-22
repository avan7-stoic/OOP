class Hero:
    def __init__(self, name, power_level):
        self.name = name
        self._power_level = power_level  # protected (encapsulation)

    def introduce(self):
        return f"I am {self.name}, with power level {self._power_level}."

    def get_power_level(self):
        return self._power_level

    def boost_power(self, amount):
        self._power_level += amount
