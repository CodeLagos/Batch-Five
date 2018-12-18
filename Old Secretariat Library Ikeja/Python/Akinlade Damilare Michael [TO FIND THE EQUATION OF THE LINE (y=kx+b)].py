# To find the equation of a straight line
# (y = kx + b) that passes through
# two known points, it is necessary
# to solve the system of equations
# (y1 = kx1 + b and y2 = kx2 + b),
# where x1, y1, x2, y2 are known variables,
# k and b are coefficients to be found.
# from this system of equations derive
# the coefficients b and k:
# the second equation is converted to the form
# b = y2 - kx2
# after it the value of b is substituted into
# the first equation and get
# k = (y1 - y2) / (x1 - x2).
# at the end k and b are substituted into the
# equation y = kx + b and get
# the equation of a particular line.

print("A(x1; y1):")
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))

print("B(x2; y2):")
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))

print("Equation:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k * + x2
print("\ty = %.2f*x + %.2f" % (k, b))

