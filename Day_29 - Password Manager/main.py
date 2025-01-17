from tkinter import *
import os
from PIL import Image, ImageTk
from password_generator import PasswordGenerator
from save_file import SaveFile

# Define constants
BACKGROUND_COLOR = '#FFFAEC'
ENTRY_COLOR = '#EFF3EA'
BUTTON_COLOR = '#578E7E'
TEXT_COLOR = '#3D3D3D'
                 
window = Tk()
window.title("PASSWORD MANAGER")
window.minsize(width=500, height=500)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=25)

# initialize classes
password_generator = PasswordGenerator()
save_file = SaveFile()

def submit():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not email or not password:
        messagebox.showerror("Error", "All fields must be filled")
        return

    if not website_validation(website):
        messagebox.showerror("Error", "Invalid website")
        return

    if not email_validation(email):
        messagebox.showerror("Error", "Invalid email")
        return

    if not password_validation(password):
        messagebox.showerror("Error", "Invalid password")
        return
    save_file.save_to_disk('hdfc.com', 'john@example.com', 'save_to_disk')
    print("Saved")

    # Generate and display password
    generated_password = password_generator.generate_password(12)
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)

    messagebox.showinfo("Success", "Password generated successfully")
# Load lock photo
try:
    image_path=os.path.join(os.path.dirname(__file__), 'lock.png')
    lock_img = Image.open(image_path)  # Open the image
    lock_img = lock_img.resize((100, 100))  # Resize if needed
    lock_photo = ImageTk.PhotoImage(lock_img)  # Convert to PhotoImage
except Exception as e:
    print(f"Error loading image: {e}")
    lock_photo = None


# todo - create design ✅

canvas = Canvas(window, width=200, height=200, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(100, 100, image=lock_photo)
canvas.grid(row=0, column=1)
# canvas.config(padx=10, pady=20)

common_design_dict = {
    "font": ("Arial", 14, 'italic'),
    "padx": 10,
    "pady": 10,
    "bg": BACKGROUND_COLOR,
    "fg": TEXT_COLOR,
    "highlightbackground": BACKGROUND_COLOR,
    "highlightthickness": 0,
    "relief": "flat"
}

common_entry_dict = {
    "font": ("Arial", 14),
    # "align": "center",
    "bg": ENTRY_COLOR,
    "fg": TEXT_COLOR,
    "highlightbackground": BACKGROUND_COLOR,
    "highlightthickness": 0,
    "relief": "flat"
}
# WEBSITE - create labels and entries
label_website = Label(window, common_design_dict, text="Website: " )
label_website.grid(row=1, column=0)

entry_website = Entry(window, common_entry_dict)
entry_website.grid(row=1, column=1)

# EMAIL - create labels and entries
label_email = Label(window, common_design_dict, text="Email: ")
label_email.grid(row=2, column=0)

entry_email = Entry(window, common_entry_dict)
entry_email.grid(row=2, column=1)

# PASSWORD - create labels and entries
label_password = Label(window, common_design_dict, text="Password: ")
label_password.grid(row=3, column=0)

entry_password = Entry(window, common_entry_dict)
entry_password.grid(row=3, column=1)

# GENERATE PASSWORD - create button
def generate_password():
    new_password = password_generator.generate_password(pass_length=14)
    entry_password.delete(0, END)
    entry_password.insert(0, new_password)
    messagebox.showinfo("Success", "Password generated successfully")

generate_password_button = Button(window, common_design_dict, text="Generate Password", width=12, fg=TEXT_COLOR, bg=BUTTON_COLOR, command=generate_password)
generate_password_button.grid(row=3, column=2)

# SUBMIT - create button
submit_button = Button(window, common_design_dict, text="Add", width=12,fg=TEXT_COLOR, bg=BUTTON_COLOR)
submit_button.grid(row=4, column=1)

window.mainloop()