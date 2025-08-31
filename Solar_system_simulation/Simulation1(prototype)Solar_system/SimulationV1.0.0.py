from vpython import *
import math

# -----------------------------
# Canvas setup
# -----------------------------
scene = canvas(title='Earth-Moon-Mars Simulation',
               width=1200, height=800,
               background=color.black,
               center=vector(0,0,0))

# -----------------------------
# Sun with glow
# -----------------------------
sun = sphere(pos=vector(0,0,0), radius=2, color=color.yellow, emissive=True)
light = local_light(pos=sun.pos, color=color.yellow)
sun_glow = sphere(pos=sun.pos, radius=4, color=color.yellow, opacity=0.1)

# -----------------------------
# Planets and Moon
# -----------------------------
earth = sphere(pos=vector(10,0,0), radius=1, color=color.blue, make_trail=True, trail_color=color.cyan)
moon = sphere(pos=vector(12,0,0), radius=0.27, color=color.white, make_trail=True, trail_color=color.white, retain=100)
mars = sphere(pos=vector(16,0,0), radius=0.87, color=color.red, make_trail=True, trail_color=color.yellow)

# -----------------------------
# Orbit parameters
# -----------------------------
moon_orbit_radius = 2
moon_tilt = radians(5)   # Moon orbit tilt
mars_tilt = radians(1.85) # Mars orbit tilt

# -----------------------------
# Time parameters
# -----------------------------
t = 0
dt = 0.5  # base time step (days)

# -----------------------------
# Real orbital periods (days)
# -----------------------------
earth_period = 365.0
moon_period = 27.3
mars_period = 687.0

# Angular speeds (radians/day)
omega_earth = 2*pi / earth_period
omega_moon = 2*pi / moon_period
omega_mars = 2*pi / mars_period

# Angle counters
earth_angle = 0
moon_angle = 0
mars_angle = 0

# -----------------------------
# Speed multiplier slider
# -----------------------------
speed_multiplier = 0.1

def update_speed(s):
    global speed_multiplier
    speed_multiplier = s.value

wtext(text='Simulation speed multiplier: ')
speed_slider = slider(min=0.1, max=5, value=1, length=300, bind=update_speed, right=15)
speed_text = wtext(text=f' {speed_multiplier:.1f}x')

def update_slider_text():
    speed_text.text = f' {speed_multiplier:.1f}x'

# -----------------------------
# Date display
# -----------------------------
date_text = wtext(text='\nDay: 0\n')

def update_date_text():
    year = int(t // 365) + 1
    day_of_year = int(t % 365) + 1
    date_text.text = f'\nYear: {year}, Day: {day_of_year}'

# -----------------------------
# Simulation loop
# -----------------------------
while True:
    rate(200)

    # Increment angles using speed multiplier
    earth_angle += omega_earth * dt * speed_multiplier
    moon_angle += omega_moon * dt * speed_multiplier
    mars_angle += omega_mars * dt * speed_multiplier
    t += dt * speed_multiplier

    # Update Earth position
    earth.pos = vector(10*cos(earth_angle), 10*sin(earth_angle), 0)

    # Update Moon position (tilted orbit around Earth)
    moon.pos = earth.pos + vector(
        moon_orbit_radius * cos(moon_angle),
        moon_orbit_radius * sin(moon_angle) * cos(moon_tilt),
        moon_orbit_radius * sin(moon_angle) * sin(moon_tilt)
    )

    # Update Mars position (tilted orbit around Sun)
    mars.pos = vector(
        16*cos(mars_angle),
        16*sin(mars_angle)*cos(mars_tilt),
        16*sin(mars_angle)*sin(mars_tilt)
    )

    # Update slider text and date display
    update_slider_text()
    update_date_text()
