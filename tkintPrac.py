import customtkinter as ctk

# Creating the window
window = ctk.CTk()
window.geometry("800x600") # Produces the pixel geometry of window
window.title('CTk Example') # Produces the title of the window

# Functional tools 
timesPressed1 = 0
slider1Str = 'Not set'

def button1Event():
	global timesPressed1
	if timesPressed1 == 0:
		print("Thanks for pressing me!")
		timesPressed1 += 1
	elif timesPressed1 == 1:
		print("That's plenty, thank you.")
		timesPressed1 += 1
	else:
		print("STAHP!")
	return timesPressed

def button2Event():
	global slider1Str
	print("The selected difficulty is:",slider1Str)
	
def slider1Event(diffSlider):
	slider1Val = diffSlider
	if slider1Val == 1:
		slider1Str = 'Very easy'
	elif slider1Val == 2:
		slider1Str = 'Easy'
	elif slider1Val == 3:
		slider1Str = 'Normal'
	elif slider1Val == 4:
		slider1Str = 'Hard'
	elif slider1Val == 5:
		slider1Str = 'Very hard'
	return slider1Str

# Creating the widgets in the window

button1 = ctk.CTkButton(window,
						text = "Press me, please",
						command = button1Event)
button1.pack()

button2 = ctk.CTkButton(window,
						text = "Press me to see difficulty selected",
						command = button2Event)
button2.pack()

diffSlider = ctk.CTkSlider(window,
							from_ = 1,
							to = 5,
							number_of_steps = 4,
							command = slider1Event
							)
diffSlider.pack()

# Running the window
window.mainloop()