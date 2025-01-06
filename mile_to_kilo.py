from tkinter import *
def mile_to_kilo():
    miles = float(miles_input.get())
    km = miles * 1.609
    answer.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=150, pady=150)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

miles_input =Entry(width=10)
miles_input.grid(column=1, row=0)

answer = Label()
answer.grid(column=1,row=1)

button= Button(text="Calculate", command=mile_to_kilo)
button.grid(column=1,row=2)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

window.mainloop()