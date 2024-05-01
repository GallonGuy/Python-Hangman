import customtkinter as ctk

window = ctk.CTk()
window.geometry('920x1080')

backFrame = ctk.CTkFrame(window,
					 width = 950,
					 height = 1080,
					 fg_color = 'white',
					 corner_radius = 0)

backFrame.place(x = 0,
				y = 0)

veryTopBanner = ctk.CTkFrame(backFrame,
							width = 950,
							height = 53,
							fg_color = '#777777',
							corner_radius = 0)

veryTopBanner.place(x = 0,
					y = 0)

topBackBanner = ctk.CTkFrame(backFrame,
							 width = 950,
							 height = 76,
							 fg_color = '#111111',
							 corner_radius = 0)
topBackBanner.place(x = 0,
					y = 51)

aBanner = ctk.CTkFrame(backFrame,
					   width = 950,
					   height = 20,
					   fg_color = '#292929',
					   corner_radius = 0)
aBanner.place(x = 0,
			  y = 126)

bBanner = ctk.CTkFrame(backFrame,
					   width = 950,
					   height = 30,
					   fg_color = '#999999',
					   corner_radius = 0)
bBanner.place(x = 0,
			  y = 146)

bottomBackBanner = ctk.CTkFrame(backFrame,
								width = 950,
								height = 130,
								fg_color = '#111111',
								corner_radius = 0)
bottomBackBanner.place(x = 0,
					   y = 939)

window.mainloop()