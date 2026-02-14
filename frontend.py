import tkinter as tk
from square_test import generate_square, columns_rev, check_color

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.fails = 0
        self.max_fails = 3
        self.square = None

        self.center_frame = tk.Frame(self)
        self.center_frame.pack(expand=True, fill="both")

        self.prompt = tk.Label(self.center_frame, text="", anchor="center", justify="center", font=("Arial", 32))
        self.output = tk.Label(self.center_frame, text="", font=("Arial", 16))
        self.button_frame = tk.Frame(self.center_frame)
        self.white_btn = tk.Button(self.button_frame, text="White", width=10, command=lambda: self.check_answer("white"))
        self.black_btn = tk.Button(self.button_frame, text="Black", width=10, command=lambda: self.check_answer("black"))

        self.prompt.pack(side="top", fill="x", pady=20)
        self.output.pack(side="top", fill="x", pady=10)
        self.button_frame.pack(side="top", pady=20)
        self.white_btn.pack(side="left", padx=40)
        self.black_btn.pack(side="right", padx=40)

        self.new_question()

    def new_question(self):
        self.square = generate_square()
        self.prompt.config(text=f"{columns_rev[self.square.column]}{self.square.row}")
        self.output.config(text="")

    def check_answer(self, color):
        correct_color = check_color(self.square)
        if color == correct_color:
            self.output.config(text="Correct!", fg="green")
            self.after(500, self.new_question) 
        else:
            self.fails += 1
            self.output.config(text=f"Wrong! It was {correct_color}.", fg="red")
            if self.fails >= self.max_fails:
                self.white_btn.config(state="disabled")
                self.black_btn.config(state="disabled")
                self.output.config(text="Game over! You have failed 3 times.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chess Square Color Quiz")
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
