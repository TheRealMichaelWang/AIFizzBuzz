import keras
import numpy as np

test_case_max = 1000
test_inputs = np.array([np.array([i]) for i in range(test_case_max)])

arr = []
for i in range(test_case_max):
    expected_output = []
    for j in range(i):
        expected_output.append([
            1 if j % 3 == 0 else 0,
            1 if j % 5 == 0 else 0
        ])
    for j in range(i, test_case_max):
        expected_output.append([0, 0])
    arr.append(expected_output)
expected_outputs = np.array(arr)

model = keras.models.Sequential([
    #keras.layers.Input(shape=(1,1)),
    keras.layers.Dense(64, activation=keras.activations.sigmoid),
    keras.layers.Dense(test_case_max * 2),
    keras.layers.Reshape((test_case_max, 2))
])

model.compile(
    #optimizer=keras.optimizers.SGD(learning_rate=0.002),
    optimizer = keras.optimizers.Adam(learning_rate = 0.001),
    loss=keras.losses.MeanSquaredError(),
    metrics=[keras.metrics.BinaryAccuracy()],
)

model.fit(test_inputs, expected_outputs, epochs=150, verbose=1)
model.save("fizzbuzz.keras", overwrite=False)