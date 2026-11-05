"""Fuzzy Logic Demo

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""



def temperature_to_fan(temp):
    if temp < 20:
        return 'Off'
    if temp < 30:
        return 'Low'
    if temp < 40:
        return 'Medium'
    return 'High'


def main():
    for t in [15, 22, 28, 35, 45]:
        print(f'Temperature: {t} -> Fan speed: {temperature_to_fan(t)}')


if __name__ == "__main__":
    main()
