import tkinter as tk

window = tk.Tk()
window.title("Falling Object Simulation")

canvas = tk.Canvas(window, width=400, height=400, bg="black")
canvas.pack()

ground_y = 350
canvas.create_line(0, ground_y, 400, ground_y, fill="white")

height = 100
velocity = 0
gravity = -9.8
time = 0
dt = 0.05
scale = 3

center_x = 200
ball_radius = 15

ball = canvas.create_oval(0, 0, 0, 0, fill="red")


def draw_ball():
    screen_y = ground_y - height * scale

    canvas.coords(
        ball,
        center_x - ball_radius,
        screen_y - ball_radius * 2,
        center_x + ball_radius,
        screen_y,
    )


def update():
    global height, velocity, time

    velocity = velocity + gravity * dt
    height = height + velocity * dt
    time = time + dt

    if height <= 0:
        height = 0

    draw_ball()

    if height > 0:
        window.after(30, update)
    else:
        print("The ball hit the ground.")
        print("Final time:", round(time, 2))
        print("Impact speed:", round(-velocity, 2))


draw_ball()
update()

window.mainloop()