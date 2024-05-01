import customtkinter as ctk

# window
window = ctk.CTk()
window.title("My Title")
window.geometry('800x600')

# widgets
label = ctk.CTkLabel(window, text = "Label only")
label.pack()

# run
window.mainloop()
