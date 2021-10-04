# v=u+at
print('v = u + at')
u = float(input('Initial velocity (m/s): '))
a = float(input('Acceleration (m/s²): '))
t = float(input('Time (secs): '))

v = u + (a * t)
print('Final velocity is', v, 'm/s')
print('\n')

# s=ut+at²/2
print('s = ut + at²/2')
u = float(input('Initial velocity (m/s): '))
a = float(input('Acceleration (m/s²): '))
t = float(input('Time (secs): '))

s = (u*t) + (a*(t**2))/2
print('Displacement is', s, 'meters')
print('\n')

# v²=u²-2as
print('v² = u² - 2as')
u = float(input('Initial velocity (m/s): '))
a = float(input('Acceleration (m/s²): '))
s = float(input('Displacement (meters): '))

v = ((u**2) - (2*a*s))**0.5
print('Final velocity is', v, 'm/s')
