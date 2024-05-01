import customtkinter as ctk

# Creating the window
window = ctk.CTk(fg_color = '#000030')
window.geometry("1920x1080") # Produces the pixel geometry of window
window.title('CTk Example') # Produces the title of the window

# Creating the widgets
frame1 = ctk.CTkFrame(window,
			width = 400,
			height = 1055,
			fg_color = '#000000')
frame1.place(x = 5,
			 y = 5)

child1frame1 = ctk.CTkFrame(frame1,
							width = 100,
							height = 1055,
							fg_color = '#666666') # Gray
child1frame1.place(x = 0,
				   y = 0)

child2frame1 = ctk.CTkFrame(frame1,
							width = 300,
							height = 1055,
							fg_color = '#222222') # Dark Gray
child2frame1.place(x = 100,
				   y = 0)

frame2 = ctk.CTkFrame(window,
					  width = (1380),
					  height = 1055,
					  fg_color = '#111111') # Very Dark Gray
frame2.place(x = 405,
			 y = 5)

child1frame2 = ctk.CTkFrame(frame2,
							width = 200,
							height = 200,
							fg_color = '#666666') # Gray

child1frame2.place(x = 1180,
				   y = 0)
child2frame2 = ctk.CTkFrame(frame2,
							width = 1380,
							height = 250,
							fg_color = '#333333') # Somewhat Dark Gray
child2frame2.place(x = 0,
				   y = 805)
window.mainloop()