import numpy as np

identity = np.eye(5)
print(identity)

random = np.random.rand(5)
print(random)
random_matrix = np.random.rand(5, 5)
print(random_matrix)

random_int = np.random.randint(1, 100, 10)
print(random_int)

print(random_int.reshape(2, 5))

print(random_int.min())
print(random_int.max())

print(random_int.argmax())
print(random_int.argmin())
print(random_int.dtype)

