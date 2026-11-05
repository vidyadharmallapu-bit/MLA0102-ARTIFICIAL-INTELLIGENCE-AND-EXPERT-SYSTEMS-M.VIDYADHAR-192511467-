"""Train a single perceptron for the Boolean AND gate."""

TRAINING_DATA = [((0, 0), 0), ((0, 1), 0), ((1, 0), 0), ((1, 1), 1)]


def predict(inputs, weights, bias):
    activation = sum(value * weight for value, weight in zip(inputs, weights)) + bias
    return 1 if activation >= 0 else 0


def train(learning_rate=0.2, maximum_epochs=100):
    weights = [0.0, 0.0]
    bias = 0.0
    for epoch in range(1, maximum_epochs + 1):
        errors = 0
        for inputs, target in TRAINING_DATA:
            output = predict(inputs, weights, bias)
            error = target - output
            if error:
                weights = [weight + learning_rate * error * value
                           for weight, value in zip(weights, inputs)]
                bias += learning_rate * error
                errors += 1
        print(f"Epoch {epoch:2}: weights={weights}, bias={bias:.2f}, errors={errors}")
        if errors == 0:
            return weights, bias
    raise RuntimeError("Perceptron did not converge within the epoch limit")


def main():
    weights, bias = train()
    print("\nAND gate predictions:")
    for inputs, expected in TRAINING_DATA:
        print(f"{inputs} -> {predict(inputs, weights, bias)} (expected {expected})")


if __name__ == "__main__":
    main()