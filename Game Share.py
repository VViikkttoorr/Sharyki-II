import tkinter as tk
import random

# Создаем окно
window = tk.Tk()
window.title("Игра с шарами")

# Устанавливаем размер окна
window.geometry("500x500")

# Создаем метку для отображения счета
score_label = tk.Label(window, text="Счет: 0")
score_label.pack()

# Создаем метку для отображения таймера
timer_label = tk.Label(window, text="Время: 10")
timer_label.pack()

# Создаем кнопку для сброса счета
def reset_score():
    global red_count, green_count, blue_count
    red_count, green_count, blue_count = 0, 0, 0
    score_label.config(text="Счет: 0 (красных: 0, зеленых: 0, синих: 0)")

reset_button = tk.Button(window, text="Сбросить счет", command=reset_score)
reset_button.pack()

# Создаем холст для отображения шаров
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Определяем цвета шаров
colors = ["red", "green", "blue"]

# Создаем функцию для создания шаров
def create_ball():
    # Генерируем случайные координаты для шара
    x = random.randint(50, 350)
    y = random.randint(50, 350)
    
    # Выбираем случайный цвет для шара
    color = random.choice(colors)
    
    # Создаем шар на холсте
    ball = canvas.create_oval(x, y, x+50, y+50, fill=color)
    
    # Увеличиваем счет при попадании на шар
    def on_click(event):
        global red_count, green_count, blue_count
        if color == "red":
            red_count += 1
        elif color == "green":
            green_count += 1
        elif color == "blue":
            blue_count += 1
        score_label.config(text=f"Счет: {red_count+green_count+blue_count} (красных: {red_count}, зеленых: {green_count}, синих: {blue_count})")
        canvas.delete(ball)
        create_ball()
        
    canvas.tag_bind(ball, "<Button-1>", on_click)

# Создаем функцию для старта игры
def start_game():
    global red_count, green_count, blue_count
    red_count, green_count, blue_count = 0, 0, 0
    score_label.config(text="Счет: 0 (красных: 0, зеленых: 0, синих: 0)")
    create_ball()
    window.after(10000, end_game)

# Создаем функцию для окончания игры
def end_game():
    canvas.delete("all")
    timer_label.config(text="Время: 0")

# Создаем кнопку для начала игры
start_button = tk.Button(window, text="Начать игру", command=start_game)
start_button.pack()

# Запускаем главный цикл
window.mainloop()
