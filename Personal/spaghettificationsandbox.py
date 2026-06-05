import tkinter as tk
import math
import random

# --- CINEMATIC WINDOW CONFIGURATION ---
WIDTH = 1200
HEIGHT = 800
G = 4.0                       # Gravity constant
BH_MASS = 180000              # Supermassive calculation factor
SCHWARZSCHILD_RADIUS = 50     # The dark core dimensions
TIME_STEP = 0.15

# Real World Stellar Data Map: [Mass, Envelope Scale, Color, Plasma Count]
STAR_DATA = {
    "1. Proxima Centauri (Dense Red Dwarf)": [0.12, 12, "#FF3300", 350],
    "2. The Sun (Main Sequence Yellow)":     [1.00, 24, "#FFCC00", 500],
    "3. Sirius A (Luminous White Star)":    [2.06, 35, "#DFFFFA", 700],
    "4. Pollux (Massive Orange Giant)":      [2.10, 65, "#FF6600", 900]
}

class PlasmaNode:
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.base_color = color
        self.is_devoured = False
        self.tk_id = None  # Holds the canvas rectangle reference object

class CinematicSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermassive Black Hole Accretion & Lensing Simulator")
        
        # UI Control Board Frame
        self.control_panel = tk.Frame(root, bg="#07070d", pady=12)
        self.control_panel.pack(side=tk.TOP, fill=tk.X)
        
        lbl = tk.Label(self.control_panel, text="🌌 SELECT TARGET STELLAR SYSTEM:", fg="#8a99ad", bg="#07070d", font=("Arial", 10, "bold"))
        lbl.pack(side=tk.LEFT, padx=20)
        
        self.star_choice = tk.StringVar(value="2. The Sun (Main Sequence Yellow)")
        dropdown = tk.OptionMenu(self.control_panel, self.star_choice, *sorted(STAR_DATA.keys()))
        dropdown.config(bg="#121224", fg="#ffffff", font=("Arial", 10), highlightthickness=0)
        dropdown.pack(side=tk.LEFT, padx=5)

        # Custom Styled Buttons
        spawn_btn = tk.Button(self.control_panel, text="LAUNCH STAR", command=self.spawn_stellar_body, bg="#ff4500", fg="white", font=("Arial", 10, "bold"), relief=tk.FLAT, padx=15)
        spawn_btn.pack(side=tk.LEFT, padx=15)
        
        clear_btn = tk.Button(self.control_panel, text="RESET SIMULATION", command=self.clear_all, bg="#22223b", fg="#a3a3c2", font=("Arial", 10, "bold"), relief=tk.FLAT, padx=10)
        clear_btn.pack(side=tk.LEFT, padx=5)

        # High-Performance Dark Space Canvas
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#020205", highlightthickness=0)
        self.canvas.pack(side=tk.BOTTOM)

        self.bh_x = WIDTH // 2
        self.bh_y = HEIGHT // 2
        self.plasma_field = []

        self.render_cinematic_background()
        self.update_physics_engine()

    def render_cinematic_background(self):
        """Draws the artistic background layers mimicking the Einstein Ring and deep space depth."""
        # Far Out Dust Glow
        self.canvas.create_oval(self.bh_x-240, self.bh_y-240, self.bh_x+240, self.bh_y+240, fill="", outline="#0c0414", width=120)
        self.canvas.create_oval(self.bh_x-160, self.bh_y-160, self.bh_x+160, self.bh_y+160, fill="", outline="#1f0721", width=60)
        
        # Einstein Ring Lensing Layer (The fiery outer boundary)
        self.canvas.create_oval(self.bh_x-95, self.bh_y-95, self.bh_x+95, self.bh_y+95, fill="", outline="#ff3c00", width=3)
        self.canvas.create_oval(self.bh_x-90, self.bh_y-90, self.bh_x+90, self.bh_y+90, fill="", outline="#ff7700", width=2)
        
        # Absolute Event Horizon Blackness
        self.canvas.create_oval(self.bh_x-SCHWARZSCHILD_RADIUS, self.bh_y-SCHWARZSCHILD_RADIUS,
                                self.bh_x+SCHWARZSCHILD_RADIUS, self.bh_y+SCHWARZSCHILD_RADIUS, fill="#000000", outline="#0a0a14")

        # Static Ambient Background Stars
        for _ in range(80):
            sx = random.randint(0, WIDTH)
            sy = random.randint(0, HEIGHT)
            sz = random.randint(1, 2)
            alpha = random.choice(["#333355", "#445577", "#555555"])
            self.canvas.create_oval(sx, sy, sx+sz, sy+sz, fill=alpha, outline="")

    def spawn_stellar_body(self):
        """Assembles and launches a dense, high-particle count stellar cluster into orbit."""
        name = self.star_choice.get()
        mass, radius, color, count = STAR_DATA[name]

        # Insertion Point (Top-right quadrant vector)
        spawn_x = self.bh_x + 350
        spawn_y = self.bh_y - 200

        # Calculate orbital mechanics entry speeds
        dx = spawn_x - self.bh_x
        dy = spawn_y - self.bh_y
        dist = math.sqrt(dx**2 + dy**2)
        
        # Velocity targeted to clip the Roche limit intentionally
        v_orbital = math.sqrt((G * BH_MASS) / dist) * 0.85
        vx_init = -(dy / dist) * v_orbital
        vy_init = (dx / dist) * v_orbital

        for i in range(count):
            # Create a dense distribution toward center
            r = random.gauss(0, 1) * (radius * 0.5)
            if abs(r) > radius: r = random.uniform(0, radius)
            
            theta = random.uniform(0, 2 * math.pi)
            px = spawn_x + r * math.cos(theta)
            py = spawn_y + r * math.sin(theta)

            # Give outer gas envelopes slight rotation speeds (stellar spin)
            spin_factor = 0.3
            pvx = vx_init + spin_factor * (-r * math.sin(theta) / radius)
            pvy = vy_init + spin_factor * (r * math.cos(theta) / radius)

            node = PlasmaNode(px, py, pvx, pvy, color)
            
            # FIXED: Changed from .create_line() to a 2x2 solid pixel rectangle for absolute display stability
            ix = int(px)
            iy = int(py)
            node.tk_id = self.canvas.create_rectangle(ix, iy, ix+2, iy+2, fill=color, outline="")
            
            self.plasma_field.append(node)

    def clear_all(self):
        for p in self.plasma_field:
            self.canvas.delete(p.tk_id)
        self.plasma_field.clear()

    def update_physics_engine(self):
        """Advanced relativistic trajectory loop detailing the over-under lensing illusion."""
        for p in self.plasma_field:
            if p.is_devoured: continue

            dx = self.bh_x - p.x
            dy = self.bh_y - p.y
            r_sq = dx**2 + dy**2
            r = math.sqrt(r_sq)

            # Inside the Singularity check
            if r <= SCHWARZSCHILD_RADIUS:
                self.canvas.delete(p.tk_id)
                p.is_devoured = True
                continue

            # Core Gravitational Physics: Modulates pull acceleration via inverse cube adjustment
            f_scalar = (G * BH_MASS) / (r_sq * (1.0 - (SCHWARZSCHILD_RADIUS / r)))
            p.vx += (dx / r) * f_scalar * TIME_STEP
            p.vy += (dy / r) * f_scalar * TIME_STEP

            # Move current actual position mapping metrics
            p.x += p.vx * TIME_STEP
            p.y += p.vy * TIME_STEP

            # --- THE INTERSTELLAR LENSING ENGINE TWEAK ---
            render_x, render_y = p.x, p.y
            if 45 < r < 140:
                lens_distortion = (1.4 - (r / 140)) * 25
                if dy < 0:
                    render_y -= lens_distortion * (abs(dx) / r)
                else:
                    render_y += lens_distortion * (abs(dx) / r)

            # Velocity calculations define core brightness color maps
            vel_magnitude = math.sqrt(p.vx**2 + p.vy**2)
            if vel_magnitude > 24:
                glow_color = "#FFFFFF" # White Hot
            elif vel_magnitude > 15:
                glow_color = "#FFAA44" # Accretion Orange
            elif vel_magnitude > 9:
                glow_color = "#FF4400" # Crimson Red
            else:
                glow_color = p.base_color

            # FIXED: Direct pixel repositioning using integers ensures they never fade or fail
            rx = int(render_x)
            ry = int(render_y)
            self.canvas.coords(p.tk_id, rx, ry, rx+2, ry+2)
            self.canvas.itemconfig(p.tk_id, fill=glow_color)

        # Cache clear step removes devoured particles
        self.plasma_field = [p for p in self.plasma_field if not p.is_devoured]
        
        # Frame refresh loop set to ~60fps
        self.root.after(16, self.update_physics_engine)


if __name__ == "__main__":
    window = tk.Tk()
    window.configure(bg="#07070d")
    app = CinematicSimulation(window)
    window.mainloop()