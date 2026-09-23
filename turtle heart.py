import turtle
import math
import random
import colorsys


class Turtle:
    def __init__(self):
        self.screen = None
        self.turtle_obj = None
        self.positions = []
        self.targets = []
        self.sizes = []
        self.hues = []
        self.swarm_size = 0
        self.scale = 0
        self.x = 0.0
        self.y = 0.0
        self.tx = 0.0
        self.ty = 0.0
        self.fx = 0.0
        self.fy = 0.0
        self.frame = 0

    def heart_point(self, t, scale):
        x = scale * 16 * (math.sin(t) ** 3)
        y = scale * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
        return x, y

    def main(self):
        self.screen = turtle.Screen()
        self.screen.setup(800, 600)
        self.screen.bgcolor("black")
        self.screen.title("Turtle Heart Drawing")
        self.screen.tracer(0, 0)

        self.turtle_obj = turtle.Turtle(visible=False)
        self.turtle_obj.penup()
        self.turtle_obj.speed(0)

        self.swarm_size = 1400
        self.scale = 15
        self.positions = []
        self.targets = []
        self.sizes = []
        self.hues = []

        for i in range(self.swarm_size):
            angle = random.uniform(0, 2 * math.pi)
            disk = random.uniform(50, 320)
            self.positions.append([
                disk * math.cos(angle),
                disk * math.sin(angle)
            ])

            t = (i / self.swarm_size) * 2 * math.pi
            self.tx, self.ty = self.heart_point(t, self.scale)

            self.targets.append([
                self.tx + random.uniform(-8, 8),
                self.ty + random.uniform(-8, 8)
            ])
            self.sizes.append(random.uniform(2, 4))
            self.hues.append(random.random())

        self.frame = 0
        self.animation()
        self.screen.mainloop()

    def animation(self):
        self.turtle_obj.clear()
        for i in range(self.swarm_size):
            self.x = self.positions[i][0]
            self.y = self.positions[i][1]

            target_x = self.targets[i][0]
            target_y = self.targets[i][1]

            self.x += (target_x - self.x) * 0.025
            self.y += (target_y - self.y) * 0.025

            self.positions[i][0] = self.x
            self.positions[i][1] = self.y

            self.fx = math.sin(self.frame * 0.035 + i * 0.5) * 0.025
            self.fy = math.cos(self.frame * 0.035 + i * 0.7) * 0.025

            self.hues[i] = (self.hues[i] + self.frame * 0.001) % 1
            r, g, b = colorsys.hsv_to_rgb(self.hues[i], 0.75, 1)

            self.turtle_obj.goto(self.x + self.fx, self.y + self.fy)
            self.turtle_obj.dot(self.sizes[i], (r, g, b))

        self.screen.update()
        self.frame += 1
        self.screen.ontimer(self.animation, 16)


if __name__ == "__main__":
    obj = Turtle()
    obj.main()