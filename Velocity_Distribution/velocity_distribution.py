import sympy as smp
y = smp.symbols('y', real=True, positive=True)

b = 1
yo = float(input("Enter the maximum velocity (yo): "))
A =  yo * b
v = (y/yo) ** smp.Rational(1/7)

V_avg = (1/A) * smp.integrate(v , (y,0,yo))
alpha = (1/(A * V_avg**3) ) * smp.integrate(v**3 , (y,0,yo))
beta = (1/(A * V_avg**2) ) * smp.integrate(v**2 , (y,0,yo))

print("V_avg", V_avg)
print("alpha", alpha)
print("beta", beta)