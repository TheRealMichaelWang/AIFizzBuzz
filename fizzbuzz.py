import keras
import numpy as np

model = keras.models.load_model('fizzbuzz.keras')
model.summary()

while True:
    print("Type in a number to fizzbuzz to.")
    num = int(input())

    result = model.predict([np.array([num])])[0]
    for i in range(num):
        current = result[i]

        print(i, end="")
        if current[0] > 0.25:
            print("Fizz", end="")
        if current[1] > 0.25:
            print("Buzz", end="")
        print()
