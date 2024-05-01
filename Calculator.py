import customtkinter as ctk

window = ctk.CTk()
window.geometry('400x500')

number = 3.1415927 ** 3

if len(str(number)) > 10:
	numberStr = str(number)
	number = numberStr[:10]

topFrame = ctk.CTkFrame(window,
						width = 400,
						height = 100,
						fg_color = '#555999')

topFrame.place(x = 0,
			   y = 0)

textFrame = ctk.CTkFrame(topFrame,
						 width = 390,
						 height = 90)

textFrame.place(x = 5,
				y = 5)

textLabel = ctk.CTkLabel(textFrame,
						 text = str(number),
						 font = ('Arial', 70),
						 text_color = 'white',
						 width = 390,
						 height = 90)
textLabel.place(x = 0,
				y = 0)

bottomFrame = ctk.CTkFrame(window,
						   width = 400,
						   height = 400,
						   fg_color = '#666699')
bottomFrame.place(x = 0,
				  y = 100)

zeroFrame = ctk.CTkFrame(bottomFrame,
						 width = 90,
						 height = 90,
						 fg_color = '#999999')
zeroFrame.place(x = 5,
				y = 305)

zeroButton = ctk.CTkButton(zeroFrame,
						 text = '0',
						 font = ('Arial', 75),
						 fg_color = '#999999',
						 width = 70,
						 height = 70)

zeroButton.place(x = 10,
				y = 0)

decimalFrame = ctk.CTkFrame(bottomFrame,
							width = 90,
							height = 90,
							fg_color = '#999999')

decimalFrame.place(x = 105,
				   y = 305)

decimalButton = ctk.CTkButton(decimalFrame,
							text = '.',
							font = ('Arial', 75),
							fg_color = '#999999',
							width = 70,
							height = 70)

decimalButton.place(x = 10,
				   y = 0)

equalsFrame = ctk.CTkFrame(bottomFrame,
							width = 90,
							height = 90,
							fg_color = '#999999')

equalsFrame.place(x = 205,
				  y = 305)

equalsButton = ctk.CTkButton(equalsFrame,
							text = '=',
							font = ('Arial', 75),
							fg_color = '#999999',
							width = 70,
							height = 70)

equalsButton.place(x = 10,
				  y = 0)

minusFrame = ctk.CTkFrame(bottomFrame,
						  width = 90,
						  height = 90,
						  fg_color = '#999999')

minusFrame.place(x = 305,
				 y = 305)

minusButton = ctk.CTkButton(minusFrame,
							text = '-',
							font = ('Arial', 75),
							fg_color = '#999999',
							width = 80,
							height = 70)

minusButton.place(x = 5,
				 y = -2)


oneFrame = ctk.CTkFrame(bottomFrame,
						 width = 90,
						 height = 90,
						 fg_color = '#999999')
oneFrame.place(x = 5,
			   y = 205)

oneButton = ctk.CTkButton(oneFrame,
						 text = '1',
						 font = ('Arial', 75),
					     fg_color = '#999999',
						 width = 70,
						 height = 70)

oneButton.place(x = 10,
			   y = 0)

twoFrame = ctk.CTkFrame(bottomFrame,
							width = 90,
							height = 90,
							fg_color = '#999999')

twoFrame.place(x = 105,
			   y = 205)

twoButton = ctk.CTkButton(twoFrame,
							text = '2',
							font = ('Arial', 75),
							fg_color = '#999999',
							width = 70,
							height = 70)

twoButton.place(x = 10,
			   y = 0)

threeFrame = ctk.CTkFrame(bottomFrame,
							width = 90,
							height = 90,
							fg_color = '#999999')
threeFrame.place(x = 205,
				 y = 205)

threeButton = ctk.CTkButton(threeFrame,
							text = '3',
							font = ('Arial', 75),
							fg_color = '#999999',
							width = 70,
							height = 70)

threeButton.place(x = 10,
				 y = 0)

plusFrame = ctk.CTkFrame(bottomFrame,
						  width = 90,
						  height = 90,
						  fg_color = '#999999')

plusFrame.place(x = 305,
				y = 205)

plusButton = ctk.CTkButton(plusFrame,
							text = '+',
							font = ('Arial', 75),
							fg_color = '#999999',
							width = 80,
							height = 70)

plusButton.place(x = 5,
				y = -2)

fourFrame = ctk.CTkFrame(bottomFrame,
						 width = 90,
						 height = 90,
						 fg_color = '#999999')
fourFrame.place(x = 5,
				y = 105)

fourButton = ctk.CTkButton(fourFrame,
						 text = '4',
						 font = ('Arial', 75),
						 fg_color = '#999999',
						 width = 70,
						 height = 70)

fourButton.place(x = 10,
				y = 0)

fiveFrame = ctk.CTkFrame(bottomFrame,
							width = 90,
							height = 90,
							fg_color = '#999999')

fiveFrame.place(x = 105,
				y = 105)

fiveButton = ctk.CTkButton(fiveFrame,
							text = '5',
							font = ('Arial', 75),
							fg_color = '#999999',
							width = 70,
							height = 70)

fiveButton.place(x = 10,
			    y = 0)

sixFrame = ctk.CTkFrame(bottomFrame,
							width = 90,
							height = 90,
							fg_color = '#999999')

sixFrame.place(x = 205,
			   y = 105)

sixButton = ctk.CTkButton(sixFrame,
							text = '6',
							font = ('Arial', 75),
							fg_color = '#999999',
							width = 70,
							height = 70)

sixButton.place(x = 10,
			   y = 0)

multiplyFrame = ctk.CTkFrame(bottomFrame,
						  width = 90,
						  height = 90,
						  fg_color = '#999999')

multiplyFrame.place(x = 305,
				    y = 105)

multiplyButton = ctk.CTkButton(multiplyFrame,
							text = 'X',
							font = ('Arial', 75),
							fg_color = '#999999',
							width = 80,
							height = 70)

multiplyButton.place(x = 5,
				     y = 0)

sevenFrame = ctk.CTkFrame(bottomFrame,
						 width = 90,
						 height = 90,
						 fg_color = '#999999')
sevenFrame.place(x = 5,
				 y = 5)

sevenButton = ctk.CTkButton(sevenFrame,
						 text = '7',
						 font = ('Arial', 75),
						 fg_color = '#999999',
						 width = 70,
						 height = 70)

sevenButton.place(x = 10,
				 y = 0)

eightFrame = ctk.CTkFrame(bottomFrame,
							width = 90,
							height = 90,
							fg_color = '#999999')

eightFrame.place(x = 105,
				 y = 5)

eightButton = ctk.CTkButton(eightFrame,
							text = '8',
							font = ('Arial', 75),
							fg_color = '#999999',
							width = 70,
							height = 70)

eightButton.place(x = 10,
			     y = 0)

nineFrame = ctk.CTkFrame(bottomFrame,
							width = 90,
							height = 90,
							fg_color = '#999999')

nineFrame.place(x = 205,
			    y = 5)

nineButton = ctk.CTkButton(nineFrame,
							text = '9',
							font = ('Arial', 75),
							fg_color = '#999999',
							width = 70,
							height = 70)

nineButton.place(x = 10,
			    y = 0)

divideFrame = ctk.CTkFrame(bottomFrame,
						  width = 90,
						  height = 90,
						  fg_color = '#999999')

divideFrame.place(x = 305,
				  y = 5)

divideButton = ctk.CTkButton(divideFrame,
							text = '÷',
							font = ('Arial', 75),
							fg_color = '#999999',
							width = 80,
							height = 70)

divideButton.place(x = 5,
				  y = 0)
window.mainloop()