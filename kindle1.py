import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# window
window = ctk.CTk()
window.title("My Title")
window.geometry('800x600')


# widgets
string_var = ctk.StringVar(value = 'a custom string')
label = ctk.CTkLabel(window,
	text = "Label only",
	fg_color = ('blue','red'),
	text_color = ('white','black'),
	corner_radius = 10,
	textvariable = string_var)
label.pack()

button1 = ctk.CTkButton(window,
	text = "Button",
	fg_color = 'purple',
	text_color = 'white',
	hover_color = 'blue',
	corner_radius = 10,
	command = lambda: ctk.set_appearance_mode('light'))
button1.pack()

frame = ctk.CTkFrame(window) # Window is the 'home' for the frame
frame.pack()

slider = ctk.CTkSlider(frame) # frame is the 'home' for the slider
slider.pack(padx = 20, pady = 20) # padx and pady act as the border, making it more visible

# Exercise:
# CTk switch with label "Exercise Switch"
# red switch that has a blue border and rounded corners
# when switched, the border remains blue but the interior is a very light pink
# the LHS is green initially but after switch the RHS is yellow

switch1 = ctk.CTkSwitch(window,
	text = 'Exercise Switch',
	fg_color = 'red',
	progress_color = 'pink',
	button_color = 'green',
	button_hover_color = 'yellow',
	border_color = 'blue',
	corner_radius = 2,
	switch_height = 28,
	switch_width = 56
	)
switch1.pack()




# run
window.mainloop()