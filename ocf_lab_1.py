#deetermination of state of flow and cricitical depth in open channel flow
#necessary functions

def Re(V, R, u):                #function to calculate Reynolds number
    Re = (V * R) / u
    return Re

def Fr(V, D, g):                #function to calculate Froude number
    Fr = V / ((g * D) ** 0.5)
    return Fr

def yc(Q, g, B):                #function to calculate critical depth
    yc = (Q**2 / (g * B**2))**(1/3)
    return yc

def Q(L, t):                     #function to calculate discharge
    Q = ( L * 1e-3) / t 
    return Q

def y():                         #function to calculate average depth
    a =float(input("enter the 1st value of y: "))
    b =float(input("enter the 2nd value of y: "))
    c =float(input("enter the 3rd value of y: "))
    y = (a + b + c) / 3
    return y

def A(B,y):                 #function to calculate area
    A = B * y
    return A

def P(B,y):                 #function to calculate wetted perimeter
    P = B + 2 * y
    return P

def D(A,T):                 #function to calculate hydraulic depth
    D = A / T
    return D

def V(Q, B, y):             #function to calculate velocity
    V = Q / (B * y)
    return V

def Re_Cmnt(Re):           #function to comment on Reynolds number
    if  Re < 500: 
        return "Laminar"
    elif  Re >= 500 and Re <= 12500: 
        return "Transitional"
    else: 
        return "Turbulent"

def Fr_Cmnt(Fr):            #function to comment on Froude number
    if Fr < 1: 
        return "Subcritical"
    elif Fr == 1: 
        return "Critical"
    else: 
        return "Supercritical"

#TAKING NECESSARY INPUTS

B = float(input("Enter flume width (B) in meter: "))
u = float(input("Enter kinematic viscosity (u) in m2/s: "))
g = 9.81  # Acceleration due to gravity in m/s^2
T = B 
L = float(input("Enter volume of water (L) in liters: "))
t = float(input("Enter time (t) in seconds: "))
Q = Q(L, t)

#section 1

y1 = y()
# print(y)
Area1 = B * y1
Perimeter1 = P(B, y1)
R1 = Area1 / Perimeter1
D1 = D(Area1, T)
Velocity1 = V(Q, B, y1)
Fr1 = Fr(Velocity1, D1, g)
Re1 = Re(Velocity1, R1, u)

# print(f"Fr num is {Fr1} & Re num is {Re1} for section 1")

#section 2

y2 = y()
# print(y)
Area2 = B * y2
Perimeter2 = P(B, y2)
R2 = Area1 / Perimeter2
D2 = D(Area2, T)
Velocity2 = V(Q, B, y2)
Fr2 = Fr(Velocity2, D2, g)
Re2 = Re(Velocity2, R2, u)

print("======="*10)
print("======="*10)

print(f"y1 {y1} y2 {y2}")
print(f"Area1 {Area1} Area2 {Area2}")
print(f"Perimeter1 {Perimeter1} Perimeter2 {Perimeter2}")
print(f"R1 {R1} R2 {R2}")
print(f"D1 {D1} D2 {D2}")
print(f"Velocity1 {Velocity1} Velocity2 {Velocity2}")
print(f"Fr1 {Fr1} Fr2 {Fr2}")
print(f"Re1 {Re1} Re2 {Re2}")

print(f"Section 1 is {Fr_Cmnt(Fr1)} {Re_Cmnt(Re1)}")
print(f"Section 2 is {Fr_Cmnt(Fr2)} {Re_Cmnt(Re2)}")

print("======="*10)
print("======="*10)
