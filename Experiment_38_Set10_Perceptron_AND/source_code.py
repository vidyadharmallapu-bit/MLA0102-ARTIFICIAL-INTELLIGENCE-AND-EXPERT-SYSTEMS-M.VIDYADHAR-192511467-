"""Perceptron AND Gate Demo

Beginner-friendly version.
This file uses simple Python loops, lists, and dictionaries.
No heavy libraries or advanced tricks are used.
"""




def perceptron_and():
    weights = [0.0, 0.0]
    bias = -0.5
    learning_rate = 0.5
    data = [
        ([0, 0], 0),
        ([0, 1], 0),
        ([1, 0], 0),
        ([1, 1], 1),
    ]

    for _ in range(20):
        for inputs, expected in data:
            total = sum(w * x for w, x in zip(weights, inputs)) + bias
            prediction = 1 if total >= 0 else 0
            error = expected - prediction
            if error != 0:
                for i in range(len(weights)):
                    weights[i] += learning_rate * error * inputs[i]
                bias += learning_rate * error

    for inputs, expected in data:
        total = sum(w * x for w, x in zip(weights, inputs)) + bias
        prediction = 1 if total >= 0 else 0
        print(inputs, '->', prediction, '(expected', expected, ')')


if __name__ == "__main__":
    perceptron_and()
