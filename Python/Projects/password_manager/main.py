import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(bg="white", padx=20, pady=20)
# canvas
canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=1)

window.mainloop()
