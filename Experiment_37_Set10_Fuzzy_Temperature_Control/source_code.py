"""Use simple fuzzy memberships to choose a temperature-control fan speed."""


def triangular(value, left, peak, right):
    if value <= left or value >= right:
        return 0.0
    if value == peak:
        return 1.0
    if value < peak:
        return (value - left) / (peak - left)
    return (right - value) / (right - peak)


def memberships(temperature):
    cold = 1.0 if temperature <= 15 else max(0.0, (25 - temperature) / 10)
    warm = triangular(temperature, 18, 25, 32)
    hot = 0.0 if temperature <= 28 else min(1.0, (temperature - 28) / 12)
    return {"Cold": cold, "Warm": warm, "Hot": hot}


def fan_speed(temperature):
    degrees = memberships(temperature)
    output_levels = {"Cold": 20, "Warm": 55, "Hot": 90}
    total_weight = sum(degrees.values())
    if total_weight == 0:
        return 0.0, degrees
    speed = sum(degrees[label] * output_levels[label] for label in degrees) / total_weight
    return speed, degrees


def main():
    temperature = 30.0
    speed, degrees = fan_speed(temperature)
    print(f"Temperature: {temperature:.1f} C")
    print("Membership degrees:", ", ".join(f"{name}={value:.2f}" for name, value in degrees.items()))
    print(f"Fan speed: {speed:.1f}%")


if __name__ == "__main__":
    main()