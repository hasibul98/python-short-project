# importing the complex math module
import cmath
num = 1 + 2j
numSqrt = cmath.sqrt(num)
print("the square root of {0} is {1:0.3f}+{2:0.3f}j".format(num,numSqrt.real,numSqrt.imag))
