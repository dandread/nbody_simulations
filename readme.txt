Summary
In this module, the motion of celestial bodies is simulated by modeling the
gravitational forces between two bodies using kinematic equations. The goal
of the simulation is to calculate the final x and y positions/velocities
of the celestial bodies for a given total simulation time.

Kinematic Equations Overview
The formulas below are used through the steps of the simulation to eventually
calculate the new x and y positions of the celestial body in question.

Newton's law of universal gravitation states:

    F = (G * (m1 * m2)) / r ** 2

    where:
        F = pairwise force
        G = gravitational constant 6.67E-11 N m^2 kg^-2
        m1 = mass of body 1
        m2 = mass of body 2
        r = distance between two bodies

Since the simulation takes place in a 2D plane, the force calculation can
be broken out into its x and y components:

    Fx = F * (delta x / r)

    where:
        Fx = x component of force
        F = pairwise force
        delta x = x position of the sun - x position of celestial body
        r = distance between two bodies

    Note: The same equation is used to calculate the y position of force;
    swap Fx for Fy, and change delta x to delta y, or the y position of
    the sun minus the y position of the celestial body.

In addition, the acceleration of a body can broken down into its x and y
components:

    ax = Fx / m

    where:
        ax = x component of acceleration
        Fx = x component of force
        m = mass of celestial body

    Note: The same equation is used to calculate the y component of force;
    swap ax for ay, and Fx for Fy.

Parameters and Initial Inputs
For this simulation, several inputs were provided to get started.

First, two parameters were defined:

    1. total time of simulation (t) = 157788000
    2. time delta (dt) = 25000

The position of a celestial body is recalculated at each time step (dt)
under the total time of simulation. In this case, the position of a
celestial body is recalculated 6,311 times (t % dt).

Furthermore, five lists were provided containing the x position, y position,
x velocity, y velocity, and mass, respectively, for earth, mars, mercury,
the sun, and venus.

Simulation

Setup
Before getting into the calculations, the necessary pieces of the simulation
are setup. First, module 'math' is imported to provide supportive mathematical
functions needed for the calculations. Next, the lists containing the relevant
information for each planet were pasted into the program. To simplify the
code, another list, assigned to 'planets', was created to store each planet,
forming a simple nested list. This is the list that is called for the
calculations. Finally, the variables for the calculations are inserted.
A couple of notes:

    t_total: this variable calculates the running total simulation time. This
             is compared to the total time of simulation, 't', and the program
             continues to run as long as t_total < t.

    N: this variable stores the number of planets in the simulation, which is
       used in the 'for' loop.

    SUN: this variable is there to indicate the position of 'sun' in the list
         'planets'. The sun's x,y coordinates and x,y velocity are not
         calculated, as the sun is stationary relative to the celestial
         objects in question.

Calculations
The calculations are contained in a 'for' loop nested in a 'while' loop. The
'for' loop loops through all of the planets (excluding the sun) and performs
the calculations before ending. Once the 'for' loop is finished, 'dt' is added
to 't_total'. The 'while' loop continues as long as the total accumulated time
of simulation, or 't_total', is less then the total time of simulation, or 't'.
So, the calculations are performed on each planets in the list 'planets' until
the 'while' loop is no longer True.

Since N=5, i will be set to 0 first; this is planet earth in the list
'planets'. The calculations will be performed on planet earth before
moving on to mars, mercury, and venus, respectively. The 'for' loop is now
complete. 'dt' is added to 't_total', and while 't_total' is less than 't',
the 'for' loop runs again.

An 'if/else' statement is written first in the 'if' loop to make sure that
the sun is not included in the calculations. Since the sun does not move in
this simulation, it doesn't make sense to calculate its x,y positions/velocity.
Furthermore, trying to do so results in a divide by 0 error (the distance
between the sun and itself is 0; since the equation for force has distance in
the denominator, force is cannot be calculated).

Here are the following calculations performed in the simulation on planet i.
Note that each subsequent calculation builds off the prior calculation's
answer.

    1. r: In order to find the pairwise force between two celestial bodies,
          the distance between planet i and the sun must first be calculated.
          The variable 'r' calculates this distance by adding the square of
          the difference between the sun and the planet's x coordinate to the
          square of the difference between the sun and the planet's y
          coordinate and taking the square root of the sum. Here, the 'sqrt'
          function from module 'Math' is employed.

    2. F: Once the distance between planet i and the sun has been determined,
          the pairwise force between the two objects is calculated. This is
          found by dividing the product of the gravitational constant, mass of
          planet i, and the mass of the sun by the square of the distance
          between planet i and the sun.

    3. Fx/Fy: Since the simulation operates in 2D, the x,y components of force
              are calculated. The x component is found by dividing the
              difference between the sun and planet i's x coordinate by the
              distance between the two bodies, and multiplying the result by
              the pairwise force found in step 2. To calculate the y component,
              the y coordinates are swapped in where the x coordinates were.

    4. ax/ay: Once the x,y components of force are calculated, the x,y
              components of acceleration are found by dividing the
              individual components by the mass of planet i.

    5. v_x,v_y: Before determining the new x,y position of planet i, the new
                x,y velocity of planet i must first be found. To do this,
                the individual components of acceleration are multiplied
                by the time step, 'dt', and added to the velocity from the
                prior time step. For the initial round, each planet has an x,y
                velocity in its list. After the new velocity is calculated,
                the prior period's x,y velocity is replaced.

    6. p_x,p_y: With the x,y components of velocity, the x,y position of
                planet i at the end of the period is found by multiplying
                each component of velocity by the time step and adding the
                product to the prior period's x,y position. The x,y position
                for planet i is then updated.

As stated earlier, once all the calculations are complete, 'dt' is added to
't_total', and while 't_total' is less than 't', the simulation runs through
all the planets again for a total of 6,311 rounds.

Finally, after the last round is completed, the x,y positions, x,y velocities,
and mass of each planet is printed. The outputs are formatted in scientific
notation with four decimal places.
