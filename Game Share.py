import tkinter as tk
import random

class BallGame:
    def __init__(self, master):
        self.master = master
        master.title("Ball Game")
        master.geometry("400x450")

        self.canvas = tk.Canvas(master, width=300, height=300, bg="white")
        self.canvas.pack(pady=20)

        self.score_label = tk.Label(master, text="Score: 0")
        self.score_label.pack()

        self.missed_label = tk.Label(master, text="Missed: 0")
        self.missed_label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_game)
        self.start_button.pack()

        self.timer_label = tk.Label(master, text="")
        self.timer_label.pack()

        self.canvas.bind("<Button-1>", self.handle_click)

        self.balls = []
        self.colors = ["blue", "red", "yellow"]
        self.sizes = [6, 9, 12]
        self.score = {"blue": 0, "red": 0, "yellow": 0}
        self.missed = 0
        self.timer = None
        self.time_left = 10

    def start_game(self):
        self.start_button.config(state=tk.DISABLED)
        self.spawn_ball()
        self.timer_label.config(text=f"Time left: {self.time_left}")
        self.timer = self.master.after(1000, self.update_timer)

    def spawn_ball(self):
        color = random.choice(self.colors)
        size = random.choice(self.sizes)
        x = random.randint(size, 300 - size)
        y = random.randint(size, 300 - size)
        ball = self.canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)
        self.balls.append(ball)
        self.master.after(1000, self.spawn_ball)

    def update_timer(self):
        self.time_left -= 1
        self.timer_label.config(text=f"Time left: {self.time_left}")
        if self.time_left == 0:
            self.end_game()
        else:
            self.timer = self.master.after(1000, self.update_timer)

    def handle_click(self, event):
        x, y = event.x, event.y
        for ball in self.balls:
            coords = self.canvas.coords(ball)
            if coords[0] <= x <= coords[2] and coords[1] <= y <= coords[3]:
                color = self.canvas.itemcget(ball, "fill")
                self.score[color] += 1
                self.score_label.config(text=f"Score: {sum(self.score.values())}")
                self.canvas.delete(ball)
                self.balls.remove(ball)
                return
        self.missed += 1
        self.missed_label.config(text=f"Missed: {self.missed}")

    def end_game(self):
        self.master.after_cancel(self.timer)
        self.canvas.delete("all")
        self.balls.clear()
        self.score = {"blue": 0, "red": 0, "yellow": 0}
        self.missed = 0
        self.time_left = 10
        self.score_label.config(text="Score: 0")
        self.missed_label.config(text="Missed: 0")
        self.timer_label.config(text="")
        self.start_button.config(state=tk.NORMAL)

root = tk.Tk()
game = BallGame(root)
root.mainloop()
