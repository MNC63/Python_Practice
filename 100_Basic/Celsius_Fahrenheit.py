"""
Convert from Celsius to Fahrenheit and vice versa
"""

from enum import Enum


class Scale(Enum):
    CELSIUS = "C"
    FAHRENHEIT = "F"


class Temperature:

    def __init__(self, value: float, scale: Scale):
        self.value = value
        self.scale = scale

    def convert_to(self, target_scale: Scale) -> float:
        if self.scale == target_scale:
            return self.value

        if self.scale == Scale.CELSIUS and target_scale == Scale.FAHRENHEIT:
            return (self.value * 9 / 5) + 32

        elif self.scale == Scale.FAHRENHEIT and target_scale == Scale.CELSIUS:
            return (self.value - 32) * 5 / 9
        else:
            raise ValueError(
                f"Conversion from {self.scale} to {target_scale} not supported ")

    def __repr__(self):
        return f"{self.value:.2f}°{self.scale.value}"


def main():
    c = float(input("Enter the Celsius temperature: "))
    t1 = Temperature(c, Scale.CELSIUS)
    print(f"{t1} is {t1.convert_to(Scale.FAHRENHEIT):.2f}°F")

    f = float(input("Enter the Fahrenheit temperature: "))
    t2 = Temperature(f, Scale.FAHRENHEIT)
    print(f"{t2} is {t2.convert_to(Scale.CELSIUS):.2f}°C")


if __name__ == "__main__":
    main()
