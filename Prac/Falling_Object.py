import tkinter as tk


# ============================================================
# Falling Object Physics Lab
# ============================================================
#
# Big idea:
#
#   gravity changes velocity
#   velocity changes height
#   height gets converted into a screen position
#
# This is the same structure used in bigger simulations:
#
#   physics state -> update rules -> draw result -> repeat


# ----------------------------
# Window and world settings
# ----------------------------

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 620

CANVAS_WIDTH = 640
CANVAS_HEIGHT = 620

GROUND_Y = 540
CENTER_X = 320
BALL_RADIUS = 18

SCALE = 4.2
FRAME_MS = 16
BASE_DT = FRAME_MS / 1000
PHYSICS_SUBSTEPS = 3


# ----------------------------
# Simulation state
# ----------------------------

height = 100.0
velocity = 0.0
time = 0.0

bounces = 0
max_height = height
last_impact_speed = 0.0

paused = False
settled = False
environment_name = "Earth"

trail_points = []
frame_count = 0


# ----------------------------
# Window setup
# ----------------------------

window = tk.Tk()
window.title("Falling Object Physics Lab")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.configure(bg="#101418")

main_frame = tk.Frame(window, bg="#101418")
main_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(
    main_frame,
    width=CANVAS_WIDTH,
    height=CANVAS_HEIGHT,
    bg="#09111f",
    highlightthickness=0,
)
canvas.pack(side="left", fill="both")

panel = tk.Frame(main_frame, width=WINDOW_WIDTH - CANVAS_WIDTH, bg="#121820")
panel.pack(side="right", fill="y")
panel.pack_propagate(False)


# ----------------------------
# Control values
# ----------------------------

start_height_setting = tk.DoubleVar(value=100.0)
gravity_setting = tk.DoubleVar(value=9.81)
bounce_setting = tk.DoubleVar(value=0.72)
air_setting = tk.DoubleVar(value=0.015)
time_speed_setting = tk.DoubleVar(value=1.0)


# ----------------------------
# Readout values
# ----------------------------

status_readout = tk.StringVar(value="Running")
time_readout = tk.StringVar()
height_readout = tk.StringVar()
velocity_readout = tk.StringVar()
speed_readout = tk.StringVar()
gravity_readout = tk.StringVar()
energy_readout = tk.StringVar()
bounce_readout = tk.StringVar()
impact_readout = tk.StringVar()


# ----------------------------
# Coordinate conversion
# ----------------------------

def meters_to_screen_y(height_meters):
    return GROUND_Y - height_meters * SCALE


def clamp(value, smallest, largest):
    return max(smallest, min(value, largest))


# ----------------------------
# Background drawing
# ----------------------------

def make_color(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


def draw_background():
    canvas.delete("background")

    top_color = (8, 18, 34)
    horizon_color = (24, 38, 58)

    for y in range(0, GROUND_Y, 4):
        blend = y / GROUND_Y
        r = int(top_color[0] + (horizon_color[0] - top_color[0]) * blend)
        g = int(top_color[1] + (horizon_color[1] - top_color[1]) * blend)
        b = int(top_color[2] + (horizon_color[2] - top_color[2]) * blend)
        canvas.create_rectangle(
            0,
            y,
            CANVAS_WIDTH,
            y + 4,
            fill=make_color(r, g, b),
            outline="",
            tags="background",
        )

    canvas.create_rectangle(
        0,
        GROUND_Y,
        CANVAS_WIDTH,
        CANVAS_HEIGHT,
        fill="#162118",
        outline="",
        tags="background",
    )
    canvas.create_line(
        0,
        GROUND_Y,
        CANVAS_WIDTH,
        GROUND_Y,
        fill="#d7e3ea",
        width=2,
        tags="background",
    )

    for meters in range(0, 121, 20):
        y = meters_to_screen_y(meters)
        if 30 <= y <= GROUND_Y:
            canvas.create_line(
                70,
                y,
                CANVAS_WIDTH - 35,
                y,
                fill="#243247",
                dash=(2, 7),
                tags="background",
            )
            canvas.create_text(
                45,
                y,
                text=f"{meters} m",
                fill="#8da0b5",
                font=("Segoe UI", 9),
                tags="background",
            )

    canvas.create_text(
        CANVAS_WIDTH // 2,
        26,
        text="Falling Object Physics Lab",
        fill="#e8f0f7",
        font=("Segoe UI", 18, "bold"),
        tags="background",
    )


draw_background()


# ----------------------------
# Canvas objects
# ----------------------------

trail_line = canvas.create_line(
    0,
    0,
    0,
    0,
    fill="#ffcc66",
    width=2,
    smooth=True,
)

shadow = canvas.create_oval(
    CENTER_X - 40,
    GROUND_Y + 6,
    CENTER_X + 40,
    GROUND_Y + 15,
    fill="#05070b",
    outline="",
)

height_line = canvas.create_line(
    CENTER_X + 45,
    GROUND_Y,
    CENTER_X + 45,
    GROUND_Y,
    fill="#62d6ff",
    width=2,
)

height_text = canvas.create_text(
    CENTER_X + 92,
    GROUND_Y - 20,
    text="",
    fill="#b9edff",
    font=("Segoe UI", 10, "bold"),
)

velocity_arrow = canvas.create_line(
    CENTER_X - 42,
    GROUND_Y,
    CENTER_X - 42,
    GROUND_Y,
    fill="#ff6b6b",
    width=3,
    arrow=tk.LAST,
)

velocity_text = canvas.create_text(
    CENTER_X - 88,
    GROUND_Y - 40,
    text="",
    fill="#ffc9c9",
    font=("Segoe UI", 10, "bold"),
)

ball = canvas.create_oval(
    CENTER_X - BALL_RADIUS,
    GROUND_Y - BALL_RADIUS * 2,
    CENTER_X + BALL_RADIUS,
    GROUND_Y,
    fill="#f94144",
    outline="#ffb4b6",
    width=2,
)

canvas.tag_raise(ball)


# ----------------------------
# Panel helpers
# ----------------------------

def add_title(text):
    label = tk.Label(
        panel,
        text=text,
        bg="#121820",
        fg="#eef5fb",
        font=("Segoe UI", 17, "bold"),
        anchor="w",
    )
    label.pack(fill="x", padx=18, pady=(18, 4))


def add_small_text(text):
    label = tk.Label(
        panel,
        text=text,
        bg="#121820",
        fg="#9eacba",
        font=("Segoe UI", 9),
        justify="left",
        anchor="w",
    )
    label.pack(fill="x", padx=18, pady=(0, 12))


def add_readout(label_text, variable):
    row = tk.Frame(panel, bg="#121820")
    row.pack(fill="x", padx=18, pady=3)

    label = tk.Label(
        row,
        text=label_text,
        bg="#121820",
        fg="#95a7b9",
        font=("Segoe UI", 10),
        anchor="w",
    )
    label.pack(side="left")

    value = tk.Label(
        row,
        textvariable=variable,
        bg="#121820",
        fg="#f4f8fb",
        font=("Consolas", 10, "bold"),
        anchor="e",
    )
    value.pack(side="right")


def add_slider(label_text, variable, from_value, to_value, resolution):
    label = tk.Label(
        panel,
        text=label_text,
        bg="#121820",
        fg="#d7e1ea",
        font=("Segoe UI", 10, "bold"),
        anchor="w",
    )
    label.pack(fill="x", padx=18, pady=(10, 0))

    slider = tk.Scale(
        panel,
        from_=from_value,
        to=to_value,
        resolution=resolution,
        variable=variable,
        orient="horizontal",
        bg="#121820",
        fg="#d7e1ea",
        troughcolor="#253142",
        highlightthickness=0,
        activebackground="#4cc9f0",
        length=210,
    )
    slider.pack(fill="x", padx=18)
    return slider


def add_button(text, command):
    button = tk.Button(
        panel,
        text=text,
        command=command,
        bg="#243044",
        fg="#f5f7fb",
        activebackground="#33445f",
        activeforeground="#ffffff",
        relief="flat",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        padx=10,
        pady=7,
        cursor="hand2",
    )
    button.pack(fill="x", padx=18, pady=4)
    return button


# ----------------------------
# Simulation controls
# ----------------------------

def reset_simulation():
    global height, velocity, time
    global bounces, max_height, last_impact_speed
    global paused, settled, trail_points, frame_count

    height = float(start_height_setting.get())
    velocity = 0.0
    time = 0.0

    bounces = 0
    max_height = height
    last_impact_speed = 0.0

    paused = False
    settled = False
    trail_points = []
    frame_count = 0

    pause_button.config(text="Pause")
    canvas.coords(trail_line, 0, 0, 0, 0)
    draw_scene()
    update_readouts()


def toggle_pause():
    global paused
    paused = not paused

    if paused:
        pause_button.config(text="Resume")
    else:
        pause_button.config(text="Pause")


def clear_trail():
    global trail_points
    trail_points = []
    canvas.coords(trail_line, 0, 0, 0, 0)


def set_environment(name, gravity_value, bounce_value, air_value):
    global environment_name

    environment_name = name
    gravity_setting.set(gravity_value)
    bounce_setting.set(bounce_value)
    air_setting.set(air_value)


# ----------------------------
# Physics
# ----------------------------

def physics_step(dt):
    global height, velocity, time
    global bounces, max_height, last_impact_speed, settled

    if settled:
        return

    gravity = -float(gravity_setting.get())
    air_resistance = float(air_setting.get())
    bounce_strength = float(bounce_setting.get())

    acceleration = gravity - air_resistance * velocity

    velocity = velocity + acceleration * dt
    height = height + velocity * dt
    time = time + dt

    max_height = max(max_height, height)

    if height <= 0:
        height = 0
        last_impact_speed = abs(velocity)

        if last_impact_speed < 0.35:
            velocity = 0
            settled = True
        else:
            velocity = -velocity * bounce_strength
            bounces = bounces + 1


# ----------------------------
# Drawing
# ----------------------------

def draw_scene():
    global trail_points, frame_count

    screen_bottom = meters_to_screen_y(height)
    screen_bottom = clamp(screen_bottom, 70, GROUND_Y)
    center_y = screen_bottom - BALL_RADIUS

    canvas.coords(
        ball,
        CENTER_X - BALL_RADIUS,
        screen_bottom - BALL_RADIUS * 2,
        CENTER_X + BALL_RADIUS,
        screen_bottom,
    )

    shadow_width = clamp(95 - height * 0.55, 24, 95)
    canvas.coords(
        shadow,
        CENTER_X - shadow_width / 2,
        GROUND_Y + 7,
        CENTER_X + shadow_width / 2,
        GROUND_Y + 16,
    )

    canvas.coords(height_line, CENTER_X + 45, screen_bottom, CENTER_X + 45, GROUND_Y)
    canvas.coords(height_text, CENTER_X + 92, (screen_bottom + GROUND_Y) / 2)
    canvas.itemconfigure(height_text, text=f"{height:.1f} m")

    arrow_length = clamp(-velocity * 3.0, -90, 90)
    canvas.coords(
        velocity_arrow,
        CENTER_X - 42,
        center_y,
        CENTER_X - 42,
        center_y + arrow_length,
    )
    canvas.coords(velocity_text, CENTER_X - 95, center_y + arrow_length / 2)
    canvas.itemconfigure(velocity_text, text=f"{velocity:.1f} m/s")

    frame_count = frame_count + 1
    if frame_count % 4 == 0 and not settled:
        trail_points.append((CENTER_X, center_y))
        trail_points = trail_points[-150:]

    if len(trail_points) >= 2:
        flat_points = []
        for point_x, point_y in trail_points:
            flat_points.extend([point_x, point_y])
        canvas.coords(trail_line, *flat_points)

    canvas.tag_lower(trail_line, ball)
    canvas.tag_raise(ball)


def update_readouts():
    global environment_name

    gravity = float(gravity_setting.get())
    speed = abs(velocity)
    energy = gravity * height + 0.5 * velocity * velocity

    if settled:
        status = "Settled"
    elif paused:
        status = "Paused"
    elif velocity < 0:
        status = "Falling"
    elif velocity > 0:
        status = "Rising"
    else:
        status = "Ready"

    status = f"{status} | {environment_name}"
    status_readout.set(status)
    time_readout.set(f"{time:6.2f} s")
    height_readout.set(f"{height:6.2f} m")
    velocity_readout.set(f"{velocity:6.2f} m/s")
    speed_readout.set(f"{speed:6.2f} m/s")
    gravity_readout.set(f"{gravity:6.2f} m/s^2")
    energy_readout.set(f"{energy:6.2f}")
    bounce_readout.set(str(bounces))
    impact_readout.set(f"{last_impact_speed:6.2f} m/s")


def update_loop():
    if not paused:
        time_speed = float(time_speed_setting.get())
        dt = BASE_DT * time_speed / PHYSICS_SUBSTEPS

        for _ in range(PHYSICS_SUBSTEPS):
            physics_step(dt)

    draw_scene()
    update_readouts()
    window.after(FRAME_MS, update_loop)


# ----------------------------
# Panel layout
# ----------------------------

add_title("Physics Controls")
add_small_text(
    "Space pauses. R resets. The ball is simulated in meters, then drawn in pixels."
)

add_readout("Status", status_readout)
add_readout("Time", time_readout)
add_readout("Height", height_readout)
add_readout("Velocity", velocity_readout)
add_readout("Speed", speed_readout)
add_readout("Gravity", gravity_readout)
add_readout("Energy", energy_readout)
add_readout("Bounces", bounce_readout)
add_readout("Impact", impact_readout)

add_slider("Start height", start_height_setting, 10, 120, 1)
add_slider("Gravity strength", gravity_setting, 0.5, 25, 0.1)
add_slider("Bounce strength", bounce_setting, 0.0, 0.95, 0.01)
add_slider("Air resistance", air_setting, 0.0, 0.08, 0.001)
add_slider("Simulation speed", time_speed_setting, 0.2, 3.0, 0.1)

pause_button = add_button("Pause", toggle_pause)
add_button("Reset", reset_simulation)
add_button("Clear Trail", clear_trail)

add_small_text("Environment presets")
add_button("Earth", lambda: set_environment("Earth", 9.81, 0.72, 0.015))
add_button("Moon", lambda: set_environment("Moon", 1.62, 0.82, 0.002))
add_button("Jupiter", lambda: set_environment("Jupiter", 24.79, 0.62, 0.025))
add_button("Soft Foam", lambda: set_environment("Soft Foam", 9.81, 0.25, 0.04))


# ----------------------------
# Keyboard shortcuts
# ----------------------------

window.bind("<space>", lambda event: toggle_pause())
window.bind("r", lambda event: reset_simulation())
window.bind("R", lambda event: reset_simulation())


# ----------------------------
# Start
# ----------------------------

reset_simulation()
update_loop()

window.mainloop()
