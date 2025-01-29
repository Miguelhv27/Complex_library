import math

def sumcplx(x,y):
    return (x[0]+y[0], x[1]+y[1])

def mulcplx(x,y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+y[0]*x[1])

def rescplx(x,y):
    return (x[0]-y[0], x[1]-y[1])

def divcplx(x,y):
    real = ((x[0]*y[0]) + (x[1]*y[1])) / ((y[0]**2)+(y[1]**2))
    imag = ((y[0]*x[1]) - (x[0]*y[1]))/ ((y[0]**2)+(y[1]**2))
    return (real, imag)

def modulo (x):
    mod = round(math.sqrt((x[0]**2) + (x[1]**2)), 2)
    return mod

def conjugado(x):
    return (x[0], x[1]*-1)

def pol_car(x):
    r = x[0]
    theta = x[1]
    result1 = round(r*math.cos(theta), 2)
    result2 = round(r*math.sin(theta) , 2)
    return (result1, result2)

def car_pol(x):
    r = round(math.sqrt((x[0]**2)+(x[1]**2)), 2)
    theta = round(math.atan((x[1]/x[0])), 2)
    return (r, theta)

def fase(x):
    fase = round(math.atan(x[1]/x[0]), 2)
    return fase

if __name__ == '__main__':
    print(car_pol((1, 1)))

