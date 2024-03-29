import tkinter as tk


def set_default_email_username():
    entry_email_username.delete(0, tk.END)
    entry_email_username.insert(0, "example@email.com")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    print("password generated")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    # save inserted values as variables
    website = entry_website.get()
    email_username = entry_email_username.get()
    password = entry_password.get()
    connection_string = f'{website} | {email_username} | {password}\n'
    # open the file and check if the value already exists if not then add
    with open(file="credentials.txt", mode="r") as file:
        file_content = file.readlines()
        if connection_string in file_content:
            print("Such connection string already exists")
        else:
            with open(file="credentials.txt", mode="a") as file_to_write:
                file_to_write.write(connection_string)
                print("Connection string saved")
    entry_website.delete(0, tk.END)
    set_default_email_username()
    entry_password.delete(0, tk.END)
    entry_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(bg="white", padx=50, pady=50)
# canvas
canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=0)
# labels
label_website = tk.Label(text="Website:", bg="white", justify="right")
label_website.grid(column=0, row=1)
label_email_username = tk.Label(text="Email/Username:", bg="white")
label_email_username.grid(column=0, row=2)
label_password = tk.Label(text="Password:", bg="white")
label_password.grid(column=0, row=3)
# entries
entry_website = tk.Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)
# setting cursor on the entry for website
entry_website.focus()

entry_email_username = tk.Entry(width=35)
entry_email_username.grid(column=1, row=2, columnspan=2)
# insert already default value at the begging of the field - 0
entry_email_username.insert(0, "example@email.com")

entry_password = tk.Entry(width=21)
entry_password.grid(column=1, row=3)
# buttons
button_generate_password = tk.Button(text="Generate Password", command=password_generate)
button_generate_password.grid(column=2, row=3)

button_add = tk.Button(text="Add", command=add_password, width=36)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
