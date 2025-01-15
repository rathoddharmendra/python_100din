import tkinter

window = tkinter.Tk()
window.title("Miles to Km Convertor")
window.minsize(width=300, height=100)
window.config(padx=50, pady=10)

# Entry and Label
miles_entry = tkinter.Entry(window, width=10)
miles_entry.grid(row=0, column=1)

miles_label = tkinter.Label(window, text="Miles")
miles_label.grid(row=0, column=2)

km_label = tkinter.Label(window, text="is equal to")
km_label.grid(row=1, column=0)

km_data = tkinter.Label(window, text='0', font=('Arial', 12, 'italic'))
km_data.grid(row=1, column=1)

km_label2 = tkinter.Label(window, text="Kms")
km_label2.grid(row=1, column=2)


# Function to convert miles to kms
def convert_miles_to_km():
    try:
        miles = float(miles_entry.get())
        km = round(miles * 1.60934, 2)
        km_data.config(text=km)
    except Exception as e:
        km_data.config(text="Invalid input")


# Button
calculate = tkinter.Button(window,text="Calculate", command=convert_miles_to_km)
calculate.grid(row=2, column=1)

window.mainloop()