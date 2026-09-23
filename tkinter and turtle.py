import tkinter
import turtle


class TurtleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("turtle in tkinter")
        self.root.geometry("1000x600")

        self.canvas = tkinter.Canvas(self.root, width=800, height=550, bg="white")
        self.canvas.place(x=400, y=100)

        self.screen = turtle.TurtleScreen(self.canvas)
        self.t = turtle.RawTurtle(self.screen)
        self.t.speed(1)
        self.t.pensize(3)
        self.t.hideturtle()

        self.header = tkinter.Label(
            self.root, width=200, height=5, bg="gray", relief="groove"
        ).place(x=0, y=0)

        self.header_text = tkinter.Label(
            self.root,
            text="Rashid Teck Authority",
            font=("arial", 40, "bold"),
            bg="#706464",
            fg="white",
        ).place(x=250, y=10)

        self.menu_panel = tkinter.Label(
            self.root, width=40, height=4, relief="groove"
        ).place(x=5, y=90)

        tkinter.Label(
            self.root,
            text="Try Shapes",
            font=("arial", 20, "bold"),
            bg="gray",
            fg="white",
        ).place(x=20, y=97)

        tkinter.Button(
            self.root,
            text="Draw Square",
            command=self.draw_square,
            font=("arial", 15, "bold"),
            bg="gray",
            fg="white",
            width=20,
        ).place(x=10, y=200)
        tkinter.Button(
            self.root,
            text="Draw Circle",
            command=self.draw_circle,
            font=("arial", 15, "bold"),
            bg="gray",
            fg="white",
            width=20,
        ).place(x=10, y=250)
        tkinter.Button(
            self.root,
            text="Draw Triangle",
            command=self.draw_triangle,
            font=("arial", 15, "bold"),
            bg="gray",
            fg="white",
            width=20,
        ).place(x=10, y=300)

    def draw_square(self):
        self.t.reset()
        self.t.speed(1)
        self.t.pensize(3)
        self.t.penup()
        self.t.goto(-80, -80)
        self.t.pendown()
        self.t.begin_fill()
        self.t.fillcolor("blue")
        for _ in range(4):
            self.t.forward(160)
            self.t.left(90)
        self.t.end_fill()

    def draw_triangle(self):
        self.t.reset()
        self.t.speed(1)
        self.t.pensize(3)
        self.t.penup()
        self.t.goto(-100, -80)
        self.t.pendown()
        self.t.begin_fill()
        self.t.fillcolor("red")
        for _ in range(3):
            self.t.forward(200)
            self.t.left(120)
        self.t.end_fill()

    def draw_circle(self):
        self.t.reset()
        self.t.speed(1)
        self.t.pensize(3)
        self.t.penup()
        self.t.goto(0, -80)
        self.t.pendown()
        self.t.begin_fill()
        self.t.fillcolor("green")
        self.t.circle(80)
        self.t.end_fill()


if __name__ == "__main__":
    root = tkinter.Tk()
    app = TurtleApp(root)
    root.mainloop()