from tkinter import *
import os
from PIL import Image, ImageTk
from password_generator import PasswordGenerator
from save_file import SaveFile

# Define constants
BACKGROUND_COLOR = '#FFFAEC'
ENTRY_COLOR = '#EFF3EA'
BUTTON_COLOR = '#479e85'
TEXT_COLOR = '#3D3D3D'
ERROR_COLOR = '#FF8383'            
window = Tk()
window.title("PASSWORD MANAGER")
window.minsize(width=400, height=400)
window.config(bg=BACKGROUND_COLOR, padx=50)

# initialize classes
password_generator = PasswordGenerator()
save_file = SaveFile(filename='passwords.csv')

def show_validation_errors(text: str):
    label_validation.config(text=text)
    window.after(3000, show_validation_errors, "")

def generate_password():
    new_password = password_generator.generate_password(pass_length=14)
    entry_password.delete(0, END)
    entry_password.insert(0, new_password)
    return new_password

def add():
    website = entry_website.get().strip()
    current_email = email.get()
    password = entry_password.get().strip()

    print(f'{website=} {current_email=} {password=}')
    
    if len(website) < 1 or len(current_email) < 1 or len(password) < 1:
        show_validation_errors('Please enter all required fields')
        return
    if not current_email.count('@'):
        show_validation_errors('Invalid email')
        return
    save_file.save_to_disk(website, current_email, password)
    print("Saved")
    
# Load lock photo
try:
    image_path=os.path.join(os.path.dirname(__file__), 'new_lock.png')
    lock_img = Image.open(image_path)  # Open the image
    lock_img = lock_img.resize((180, 180))  # Resize if needed
    lock_photo = ImageTk.PhotoImage(lock_img)  # Convert to PhotoImage
except Exception as e:
    print(f"Error loading image: {e}")
    lock_photo = None


# todo - create design ✅

canvas = Canvas(window, width=200, height=200, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(100, 100, image=lock_photo)
canvas.grid(row=0, column=1)

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
    "font": ("Arial", 16),
    # "align": "center",
    "bg": ENTRY_COLOR,
    "fg": TEXT_COLOR,
    "highlightbackground": BACKGROUND_COLOR,
    "highlightthickness": 0,
    "insertbackground": BUTTON_COLOR,
    "relief": "flat"
}
# WEBSITE - create labels and entries
label_website = Label(window, common_design_dict, text="Website: " )
label_website.grid(row=1, column=0)

entry_website = Entry(window, common_entry_dict, width=40)
entry_website.grid(row=1, column=1, columnspan=2)

# EMAIL - create labels and entries
label_email = Label(window, common_design_dict, text="Email: ")
label_email.grid(row=2, column=0)

email = StringVar(window, name='email', value='rathoddharmendra.business@gmail.com')
entry_email = Entry(window, common_entry_dict, textvariable=email, width=40)
entry_email.grid(row=2, column=1, columnspan=2)

# PASSWORD - create labels and entries
label_password = Label(window, common_design_dict, text="Password: ")
label_password.grid(row=3, column=0)

entry_password = Entry(window, common_entry_dict, width=21)
entry_password.grid(row=3, column=1)

# show validation errors
label_validation = Label(window, common_design_dict, text="", fg=ERROR_COLOR, width=40)
label_validation.grid(row=5, column=1, columnspan=2)

# GENERATE PASSWORD - create button

generate_password_button = Button(window, common_design_dict, text="Generate Password", width=15, fg=BUTTON_COLOR, bg=BUTTON_COLOR, command=generate_password)
generate_password_button.grid(row=3, column=2)

# SUBMIT - create button
submit_button = Button(window, common_design_dict, text="ADD", width=40,fg=BUTTON_COLOR, highlightcolor=BUTTON_COLOR,command=add )
submit_button.grid(row=4, column=1,columnspan=2)

window.mainloop()