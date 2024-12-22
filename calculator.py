import tkinter as tk
from tkinter import messagebox


def click(button_text):
    if button_text == 'C':
        entry.delete(0, tk.END)

    elif button_text == '<--':
        current_text = entry.get()
        entry.delete(len(current_text) - 1, tk.END)

    elif button_text == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror('Error', 'Invalid input')

    elif button_text == '()':
        current_text = entry.get()
        if not current_text or current_text[-1] in '+-*/(':
            entry.insert(tk.END, '(')
        else:
            entry.insert(tk.END, ')')

    elif button_text == '%':
        current_text = entry.get()
        if current_text:
            try:
                for i in range(len(current_text) - 1, -1, -1):
                    if current_text[i] in "+-*/":
                        base = current_text[i + 1:]
                        result = f"({base}/100)"
                        entry.delete(len(current_text) - len(base), tk.END)
                        entry.insert(tk.END, result)
                        break
                else:
                    result = float(current_text) / 100
                    entry.delete(0, tk.END)
                    entry.insert(tk.END, result)
            except Exception:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, button_text)


# Main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="#202124")
root.resizable(False, False)
# root.iconbitmap('icon1.ico')

# Entry widget for user input
entry = tk.Entry(
    root,
    font=("Roboto", 32, "bold"),
    bd=0,
    insertwidth=2,
    justify="right",
    bg="#202124",
    fg="#FFFFFF",
    highlightthickness=0,
)
entry.place(x=20, y=20, width=360, height=70)


# Function to create circular buttons
def create_circle_button(parent, x, y, text, command, bg_color="#3C4043", fg_color="#FFFFFF"):
    canvas = tk.Canvas(parent, width=100, height=100, bg="#202124", highlightthickness=0)
    canvas.place(x=x, y=y)

    circle = canvas.create_oval(10, 10, 90, 90, fill=bg_color, outline="")

    label = canvas.create_text(50, 50, text=text, fill=fg_color, font=("Roboto", 22, "bold"))

    def on_press(event):
        canvas.itemconfig(circle, fill="#545454")
        canvas.move(label, 1, 1)
        canvas.move(circle, 1, 1)

    def on_release(event):
        canvas.itemconfig(circle, fill=bg_color)
        canvas.move(label, -1, -1)
        canvas.move(circle, -1, -1)
        command()


    canvas.tag_bind(circle, "<ButtonPress-1>", on_press)
    canvas.tag_bind(label, "<ButtonPress-1>", on_press)
    canvas.tag_bind(circle, "<ButtonRelease-1>", on_release)
    canvas.tag_bind(label, "<ButtonRelease-1>", on_release)

    return canvas


# Button layout
buttons = [
    ('C', "#FF5252"), ('()', "#3C4043"), ('%', "#3C4043"), ('/', "#FFAB40"),
    ('7', "#303134"), ('8', "#303134"), ('9', "#303134"), ('*', "#FFAB40"),
    ('4', "#303134"), ('5', "#303134"), ('6', "#303134"), ('-', "#FFAB40"),
    ('1', "#303134"), ('2', "#303134"), ('3', "#303134"), ('+', "#FFAB40"),
    ('0', "#303134"), ('.', "#303134"), ('<--', "#FF5252"), ('=', "#FF5252"),
]

# Add buttons to the window
x_start = 15
y_start = 110
x_offset = 90
y_offset = 90


for i, (text, color) in enumerate(buttons):
    x = x_start + (i % 4) * x_offset
    y = y_start + (i // 4) * y_offset
    create_circle_button(
        root,
        x,
        y,
        text,
        lambda t=text: click(t),
        bg_color=color,
        fg_color="#FFFFFF"
    )


# Run the application
root.mainloop()
