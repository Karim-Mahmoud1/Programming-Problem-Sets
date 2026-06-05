import tkinter as tk
import random
import math

# --- CONFIGURATION CONSTANTS ---
WIDTH = 1000
HEIGHT = 700
NUM_PARTICLES = 300
GRAVITY_STRENGTH = 0.5
DAMPING = 0.999  # Subtle friction so things don't fly off to infinity forever
MAX_SPEED = 15

class Particle:
    def __init__(self, canvas):
        self.canvas = canvas
        # Random starting positions
        self.x = random.randint(100, WIDTH - 100)
        self.y = random.randint(100, HEIGHT - 100)
        
        # Random initial velocities (speeds)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        
        # Create the visual circle on the canvas
        self.radius = random.randint(2, 4)
        self.id = canvas.create_oval(
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius,
            fill="cyan", outline=""
        )

    def update_physics(self, mouse_x, mouse_y, is_mouse_pressed):
        if is_mouse_pressed and mouse_x and mouse_y:
            # Calculate distance between particle and mouse cursor
            dx = mouse_x - self.x
            dy = mouse_y - self.y
            distance = math.sqrt(dx**2 + dy**2)

            # Avoid division by zero if particle is exactly on the mouse
            if distance < 10:
                distance = 10

            # Newtonian Gravity calculation
            force = GRAVITY_STRENGTH * (1000 / (distance ** 1.5))
            
            # Accelerate the particle toward the mouse pointer
            self.vx += force * (dx / distance)
            self.vy += force * (dy / distance)

        # Apply friction/damping
        self.vx *= DAMPING
        self.vy *= DAMPING

        # Limit maximum speed to keep it controllable
        speed = math.sqrt(self.vx**2 + self.vy**2)
        if speed > MAX_SPEED:
            self.vx = (self.vx / speed) * MAX_SPEED
            self.vy = (self.vy / speed) * MAX_SPEED

        # Move the coordinates
        self.x += self.vx
        self.y += self.vy

        # Boundary collision (Bounce off walls)
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -0.8
            self.x = max(0, min(self.x, WIDTH))
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -0.8
            self.y = max(0, min(self.y, HEIGHT))

    def redraw(self):
        """Moves the particle on screen and dynamically updates its color based on speed."""
        speed = math.sqrt(self.vx**2 + self.vy**2)
        
        # Color shifting: slow = blue, medium = purple, hyper-fast = pink/white
        if speed < 3:
            color = "#00FFFF"  # Cyan
        elif speed < 7:
            color = "#9D00FF"  # Deep Purple
        elif speed < 12:
            color = "#FF007F"  # Hot Pink
        else:
            color = "#FFFFFF"  # Blazing White

        # Update position and color on the canvas
        self.canvas.coords(
            self.id, 
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius
        )
        self.canvas.itemconfig(self.id, fill=color)


class SandboxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Gravity Sandbox")
        
        # Setup dark-mode space canvas
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#050510", highlightthickness=0)
        self.canvas.pack()

        # State tracking for the mouse pointer
        self.mouse_x = None
        self.mouse_y = None
        self.is_pressed = False

        # Build particle swarm
        self.particles = [Particle(self.canvas) for _ in range(NUM_PARTICLES)]

        # Bind mouse events
        self.canvas.bind("<Motion>", self.track_mouse)
        self.canvas.bind("<ButtonPress-1>", self.mouse_down)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_up)

        # Add visual instruction overlay
        self.canvas.create_text(
            WIDTH // 2, 30, 
            text="CLICK AND HOLD MOUSE TO SPAWN GRAVITY WELL", 
            fill="#444466", font=("Helvetica", 14, "bold")
        )

        # Start the engine loop
        self.game_loop()

    def track_mouse(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def mouse_down(self, event):
        self.is_pressed = True
        self.mouse_x = event.x
        self.mouse_y = event.y

    def mouse_up(self, event):
        self.is_pressed = False

    def game_loop(self):
        # Update physics and drawings for all elements
        for particle in self.particles:
            particle.update_physics(self.mouse_x, self.mouse_y, self.is_pressed)
            particle.redraw()

        # Recursively loop back at ~60 frames per second
        self.root.after(16, self.game_loop)


if __name__ == "__main__":
    window = tk.Tk()
    app = SandboxApp(window)
    window.mainloop()