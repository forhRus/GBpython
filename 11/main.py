import numpy as np
# import matplotlib
# import tkinter
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

color = 'b'
direct_up = True
line = '-'
limit = 10
step = 0.01
x = np.arange(-limit, limit, step)
a, b, c, d, e = -12, -18, 5, 10, -30  

def switch_color():
    global color
    color = 'r' if color == 'b' else 'b'
    return color
def switch_line():
    global line
    line = '--' if line == '-' else '-'
    return line

def func(x):
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e

x_change = [(-limit, 'limit')]
for i in range(len(x)-1):
    if (func(x[i]) > 0 and func(x[i+1]) < 0) or (func(x[i]) < 0 and func(x[i+1]) > 0):
        x_a = np.arange(x[i], x[i+1], 0.0001)
        for j in range(len(x_a) - 1):
            if (func(x_a[j]) > 0 and func(x_a[j+1]) < 0) or (func(x_a[j]) < 0 and func(x_a[j+1]) > 0):
                x_change.append((x_a[j] if abs(0 - x_a[j]) < abs(0 - x_a[j+1]) else x_a[j+1], 'zero'))
    if direct_up:   
        if func(x[i]) > func(x[i+1]):
            x_a = np.arange(x[i], x[i+1], 0.0001)   
            for j in range(len(x_a) - 1):
                if func(x_a[j]) > func(x_a[j+1]):
                    x_change.append((x_a[j], 'direct'))   
                    direct_up = False
    else:     
        if func(x[i]) < func(x[i+1]):
            x_a = np.arange(x[i], x[i+1], 0.0001) 
            for j in range(len(x_a) - 1):
                if func(x_a[j]) < func(x_a[j+1]):
                    x_change.append((x_a[j], 'direct'))  
                    direct_up = True
x_change.append((limit, 'limit'))    

min_y = min(func(x))
min_x = -limit
for x in x_change:
    if x[1] == 'direct':
        if abs(func(x[0]) - min_y) < abs(func(min_x) - min_y):
            min_x = x[0]

for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i+1][0]+step, step)
    if x_change[i][1] == 'zero':
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
    else:
        plt.plot(cur_x, func(cur_x), switch_color())  
roots = []
for x in x_change:
    if x[1] == 'zero':
        roots.append(str(round(x[0], 2)))
        plt.plot(x[0], func(x[0]), 'gx')
           
plt.plot(min_x, min_y, 'yo', label = f'Экстремум функции на промежутке [{-limit}, {limit}]: ({round(min_x, 2)}, {round(min_y, 2)})')            
plt.rcParams['lines.linestyle']= '-'
plt.plot(0, 0, 'b', label='Убывание > 0')
plt.plot(0, 0, 'r', label='Возрастание > 0')
plt.rcParams['lines.linestyle']= '--'
plt.plot(0, 0, 'b', label='Убывание < 0')
plt.plot(0, 0, 'r', label='Возрастание < 0')
plt.title(f'Корни на промежутке [{-limit};{limit}]: {", ".join(roots)}')
plt.legend()
plt.grid()
plt.show()


