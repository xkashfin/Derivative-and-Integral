import numpy as np
from scipy.integrate import quad

# Define a function to differentiate and integrate
def my_function(x):
    return np.sin(x)

# Define the interval over which to differentiate and integrate
a = 0
b = np.pi/2

# Calculate the first derivative of the function using central difference method
h = 1e-6
f_prime = (my_function(a+h) - my_function(a-h)) / (2*h)
print('First derivative:', f_prime)

# Calculate the second derivative of the function using central difference method
f_double_prime = (my_function(a+h) - 2*my_function(a) + my_function(a-h)) / (h**2)
print('Second derivative:', f_double_prime)

# Calculate the definite integral of the function using quad function from scipy.integrate
integral, error = quad(my_function, a, b)
print(f'Definite integral from {a} to {b}:', integral)

# Calculate the indefinite integral of the function using quad function from scipy.integrate
def indefinite_integral(u):
    return quad(my_function, a, u)[0]

u = np.linspace(a, b, 100)
v_indefinite_integral = np.vectorize(indefinite_integral)
plt.plot(u, v_indefinite_integral(u))
plt.xlabel('x')
plt.ylabel('Integral')
plt.show()
