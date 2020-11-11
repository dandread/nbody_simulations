# Simulation of the motion of celestial bodies

import math

# planetary information, containing x-position, y-position, x velocity,
# y velocity, and mass, respectively
earth = [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
mars = [2.2790e+11, 0.0000e+00, 0.0000e+00, 2.4100e+04, 6.4190e+23]
mercury = [5.7900e+10, 0.0000e+00, 0.0000e+00, 4.7900e+04, 3.3020e+23]
sun = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
venus = [1.0820e+11, 0.0000e+00, 0.0000e+00, 3.5000e+04, 4.8690e+24]

# nested list of planets
planets = [earth, mars, mercury, sun, venus]

# variables for calculations
t_total = 0.0  # running total of time elapsed
dt = 25000.0  # time delta
t = 157788000  # total time of simulation
N = 5  # number of 'planets' in simulation
G = 6.67e-11  # gravitational constant, in N*m^2*kg^-2
SUN = 3  # skip the sun when i = location of sun in list

# simulation
while t_total < t:
    for i in range(N):
        # skip the sun
        if i == 3:
            continue

        # calculate the radius between the i'th planet and the sun
        r = math.sqrt((planets[i][0] - planets[3][0]) ** 2 + (planets[i][1] - planets[3][1]) ** 2)

        # calculate the pair-wise force between i'th planet and the sun
        F = (G * planets[i][4] * planets[3][4]) / r ** 2

        # calculate the x and y components of the force
        # x component of the force
        Fx = F * ((planets[3][0] - planets[i][0]) / r)
        # y component of the force
        Fy = F * ((planets[3][1] - planets[i][1]) / r)

        # calculate the x and y component of the acceleration for the current time step
        # x component of acceleration
        ax = Fx / planets[i][4]
        # y component of acceleration
        ay = Fy / planets[i][4]

        # calculate the x an y components of the velocity for the next time step
        # x component of velocity
        v_x = planets[i][2] + (ax * dt)
        planets[i][2] = v_x
        # y component of  velocity
        v_y = planets[i][3] + (ay * dt)
        planets[i][3] = v_y

        # calculate the x and y components of the resulting position
        # x component of new position
        p_x = planets[i][0] + (v_x * dt)
        planets[i][0] = p_x
        # y component of new position
        p_y = planets[i][1] + (v_y * dt)
        planets[i][1] = p_y

    # update the time by delta_t
    t_total = t_total + dt

for i in range(N):
    print(f'{planets[i][0]:.4e} {planets[i][1]: .4e} '
          f'{planets[i][2]: .4e} {planets[i][3]: .4e} '
          f'{planets[i][4]: .4e}')
