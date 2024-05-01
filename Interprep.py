import customtkinter as ctk


# Interview Application

import customtkinter as ctk

# Creating the window
window = ctk.CTk(fg_color = '#000060')
window.geometry("1920x1080") # Produces the pixel geometry of window
window.title('CTk Example') # Produces the title of the window

# Creating the widgets
chatFrame = ctk.CTkFrame(window,
			width = 403,
			height = 1058,
			fg_color = '#666666')
chatFrame.place(x = 1385,
			    y = 5)

videoFrame = ctk.CTkFrame(window,
					  width = (1380),
					  height = 1058,
					  fg_color = '#111111') # Very Dark Gray
videoFrame.place(x = 5,
			     y = 5)

userVideoFrame = ctk.CTkFrame(videoFrame,
							width = 200,
							height = 200,
							fg_color = '#222222') # Gray

userVideoFrame.place(x = 1177,
				     y = 3)

muteButton = ctk.CTkButton(videoFrame,
						  width = 80,
						  height = 80,
						  corner_radius = 80,
						  fg_color = '#444444',
						  text = 'A')
muteButton.place(x = 450,
				 y = 973)

settingsButton = ctk.CTkButton(videoFrame,
						  width = 80,
						  height = 80,
						  corner_radius = 80,
						  fg_color = '#444444',
						  text = 'B')
settingsButton.place(x = 550,
				 y = 973)

transcriptButton = ctk.CTkButton(videoFrame,
						  width = 80,
						  height = 80,
						  corner_radius = 80,
						  fg_color = '#444444',
						  text = 'C')
transcriptButton.place(x = 650,
				 y = 973)

endCallButton = ctk.CTkButton(videoFrame,
						  width = 80,
						  height = 80,
						  corner_radius = 80,
						  fg_color = 'red',
						  text = 'X')
endCallButton.place(x = 750,
				 y = 973)

window.mainloop()