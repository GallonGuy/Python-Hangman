
A1, A2, A3, A4, A5, A6, A7, A8, A9 = 7, 1, 0, 5, 3, 0, 4, 8, 2
B1, B2, B3, B4, B5, B6, B7, B8, B9 = 2, 5, 0, 0, 0, 4, 0, 0, 0
C1, C2, C3, C4, C5, C6, C7, C8, C9 = 8, 6, 0, 9, 7, 2, 1, 3, 0
D1, D2, D3, D4, D5, D6, D7, D8, D9 = 1, 0, 0, 3, 6, 0, 0, 0, 0
E1, E2, E3, E4, E5, E6, E7, E8, E9 = 0, 0, 2, 0, 0, 0, 6, 0, 0
F1, F2, F3, F4, F5, F6, F7, F8, F9 = 0, 0, 0, 0, 9, 1, 0, 4, 3
G1, G2, G3, G4, G5, G6, G7, G8, G9 = 3, 0, 0, 0, 0, 9, 0, 0, 0
H1, H2, H3, H4, H5, H6, H7, H8, H9 = 0, 0, 1, 7, 0 ,0, 0, 2, 6
I1, I2, I3, I4, I5, I6, I7, I8, I9 = 4, 0, 7, 0, 0, 0, 3, 5, 0

def buildRows(A1, A2, A3, A4, A5, A6, A7, A8, A9,
			  B1, B2, B3, B4, B5, B6, B7, B8, B9,
			  C1, C2, C3, C4, C5, C6, C7, C8, C9,
			  D1, D2, D3, D4, D5, D6, D7, D8, D9,
			  E1, E2, E3, E4, E5, E6, E7, E8, E9,
			  F1, F2, F3, F4, F5, F6, F7, F8, F9,
			  G1, G2, G3, G4, G5, G6, G7, G8, G9,
			  H1, H2, H3, H4, H5, H6, H7, H8, H9,
			  I1, I2, I3, I4, I5, I6, I7, I8, I9):
	row1 = A1, A2, A3, A4, A5, A6, A7, A8, A9
	row2 = B1, B2, B3, B4, B5, B6, B7, B8, B9
	row3 = C1, C2, C3, C4, C5, C6, C7, C8, C9
	row4 = D1, D2, D3, D4, D5, D6, D7, D8, D9
	row5 = E1, E2, E3, E4, E5, E6, E7, E8, E9
	row6 = F1, F2, F3, F4, F5, F6, F7, F8, F9
	row7 = G1, G2, G3, G4, G5, G6, G7, G8, G9
	row8 = H1, H2, H3, H4, H5, H6, H7, H8, H9
	row9 = I1, I2, I3, I4, I5, I6, I7, I8, I9
	rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
	return row1, row2, row3, row4, row5, row6, row7, row8, row9, rows

def buildColumns(A1, A2, A3, A4, A5, A6, A7, A8, A9,
			     B1, B2, B3, B4, B5, B6, B7, B8, B9,
			     C1, C2, C3, C4, C5, C6, C7, C8, C9,
			     D1, D2, D3, D4, D5, D6, D7, D8, D9,
			     E1, E2, E3, E4, E5, E6, E7, E8, E9,
			     F1, F2, F3, F4, F5, F6, F7, F8, F9,
			     G1, G2, G3, G4, G5, G6, G7, G8, G9,
			     H1, H2, H3, H4, H5, H6, H7, H8, H9,
			     I1, I2, I3, I4, I5, I6, I7, I8, I9):
	column1 = A1, B1, C1, D1, E1, F1, G1, H1, I1
	column2 = A2, B2, C2, D2, E2, F2, G2, H2, I2
	column3 = A3, B3, C3, D3, E3, F3, G3, H3, I3
	column4 = A4, B4, C4, D4, E4, F4, G4, H4, I4
	column5 = A5, B5, C5, D5, E5, F5, G5, H5, I5
	column6 = A6, B6, C6, D6, E6, F6, G6, H6, I6
	column7 = A7, B7, C7, D7, E7, F7, G7, H7, I7
	column8 = A8, B8, C8, D8, E8, F8, G8, H8, I8
	column9 = A9, B9, C9, D9, E9, F9, G9, H9, I9
	columns = [column1, column2, column3, column4, column5, column6, column7, column8, column9]
	return column1, column2, column3, column4, column5, column6, column7, column8, column9, columns

def buildBoxes(A1, A2, A3, A4, A5, A6, A7, A8, A9,
			   B1, B2, B3, B4, B5, B6, B7, B8, B9,
			   C1, C2, C3, C4, C5, C6, C7, C8, C9,
			   D1, D2, D3, D4, D5, D6, D7, D8, D9,
			   E1, E2, E3, E4, E5, E6, E7, E8, E9,
			   F1, F2, F3, F4, F5, F6, F7, F8, F9,
			   G1, G2, G3, G4, G5, G6, G7, G8, G9,
			   H1, H2, H3, H4, H5, H6, H7, H8, H9,
			   I1, I2, I3, I4, I5, I6, I7, I8, I9):
	box1 = A1, A2, A3, B1, B2, B3, C1, C2, C3
	box2 = A4, A5, A6, B4, B5, B6, C4, C5, C6
	box3 = A7, A8, A9, B7, B8, B9, C7, C8, C9
	box4 = D1, D2, D3, E1, E2, E3, F1, F2, F3
	box5 = D4, D5, D6, E4, E5, E6, F4, F5, F6
	box6 = D7, D8, D9, E7, E8, E9, F7, F8, F9 
	box7 = G1, G2, G3, H1, H2, H3, I1, I2, I3
	box8 = G4, G5, G6, H4, H5, H6, I4, I5, I6
	box9 = G7, G8, G9, H7, H8, H9, I7, I8, I9 
	boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]
	return box1, box2, box3, box4, box5, box6, box7, box8, box9, boxes

row1, row2, row3, row4, row5, row6, row7, row8, row9, rows = buildRows(A1, A2, A3, A4, A5, A6, A7, A8, A9,
		  B1, B2, B3, B4, B5, B6, B7, B8, B9,
		  C1, C2, C3, C4, C5, C6, C7, C8, C9,
		  D1, D2, D3, D4, D5, D6, D7, D8, D9,
		  E1, E2, E3, E4, E5, E6, E7, E8, E9,
		  F1, F2, F3, F4, F5, F6, F7, F8, F9,
		  G1, G2, G3, G4, G5, G6, G7, G8, G9,
		  H1, H2, H3, H4, H5, H6, H7, H8, H9,
		  I1, I2, I3, I4, I5, I6, I7, I8, I9)

column1, column2, column3, column4, column5, column6, column7, column8, column9, columns = buildColumns(A1, A2, A3, A4, A5, A6, A7, A8, A9,
			 B1, B2, B3, B4, B5, B6, B7, B8, B9,
			 C1, C2, C3, C4, C5, C6, C7, C8, C9,
		     D1, D2, D3, D4, D5, D6, D7, D8, D9,
		     E1, E2, E3, E4, E5, E6, E7, E8, E9,
		     F1, F2, F3, F4, F5, F6, F7, F8, F9,
		     G1, G2, G3, G4, G5, G6, G7, G8, G9,
		     H1, H2, H3, H4, H5, H6, H7, H8, H9,
		     I1, I2, I3, I4, I5, I6, I7, I8, I9)

box1, box2, box3, box4, box5, box6, box7, box8, box9, boxes = buildBoxes(A1, A2, A3, A4, A5, A6, A7, A8, A9,
		   B1, B2, B3, B4, B5, B6, B7, B8, B9,
		   C1, C2, C3, C4, C5, C6, C7, C8, C9,
		   D1, D2, D3, D4, D5, D6, D7, D8, D9,
		   E1, E2, E3, E4, E5, E6, E7, E8, E9,
		   F1, F2, F3, F4, F5, F6, F7, F8, F9,
		   G1, G2, G3, G4, G5, G6, G7, G8, G9,
		   H1, H2, H3, H4, H5, H6, H7, H8, H9,
		   I1, I2, I3, I4, I5, I6, I7, I8, I9)


print("The board initially looks like:")
for row in rows:
	print(row)

currentIndex = 0
for num in row1:
	if num == 0:
		print(currentIndex)
		for i in range(1,10):
			if i not in row1 and column1 and box1:
				print("True")
				if currentIndex == 0:
					A1 = i
					print(f"A1 is {A1}")
				elif currentIndex == 1:
					A2 = i
					print(f"A2 is {A2}")
				elif currentIndex == 2:
					A3 = i
					print(f"A3 is {A3}")
				elif currentIndex == 3:
					A4 = i
					print(f"A4 is {A4}")
				elif currentIndex == 4:
					A5 = i
					print(f"A5 is {A5}")
				elif currentIndex == 5:
					A6 = i
					print(f"A6 is {A6}")
				elif currentIndex == 6:
					A7 = i
					print(f"A7 is {A7}")
				elif currentIndex == 7:
					A8 = i
					print(f"A8 is {A8}")
				elif currentIndex == 8:
					A9 = i
					print(f"A9 is {A9}")
				row1 = A1, A2, A3, A4, A5, A6, A7, A8, A9
	currentIndex += 1
row1, row2, row3, row4, row5, row6, row7, row8, row9, rows = buildRows(A1, A2, A3, A4, A5, A6, A7, A8, A9,
		  B1, B2, B3, B4, B5, B6, B7, B8, B9,
		  C1, C2, C3, C4, C5, C6, C7, C8, C9,
		  D1, D2, D3, D4, D5, D6, D7, D8, D9,
		  E1, E2, E3, E4, E5, E6, E7, E8, E9,
		  F1, F2, F3, F4, F5, F6, F7, F8, F9,
		  G1, G2, G3, G4, G5, G6, G7, G8, G9,
		  H1, H2, H3, H4, H5, H6, H7, H8, H9,
		  I1, I2, I3, I4, I5, I6, I7, I8, I9)

column1, column2, column3, column4, column5, column6, column7, column8, column9, columns = buildColumns(A1, A2, A3, A4, A5, A6, A7, A8, A9,
			 B1, B2, B3, B4, B5, B6, B7, B8, B9,
			 C1, C2, C3, C4, C5, C6, C7, C8, C9,
		     D1, D2, D3, D4, D5, D6, D7, D8, D9,
		     E1, E2, E3, E4, E5, E6, E7, E8, E9,
		     F1, F2, F3, F4, F5, F6, F7, F8, F9,
		     G1, G2, G3, G4, G5, G6, G7, G8, G9,
		     H1, H2, H3, H4, H5, H6, H7, H8, H9,
		     I1, I2, I3, I4, I5, I6, I7, I8, I9)

box1, box2, box3, box4, box5, box6, box7, box8, box9, boxes = buildBoxes(A1, A2, A3, A4, A5, A6, A7, A8, A9,
		   B1, B2, B3, B4, B5, B6, B7, B8, B9,
		   C1, C2, C3, C4, C5, C6, C7, C8, C9,
		   D1, D2, D3, D4, D5, D6, D7, D8, D9,
		   E1, E2, E3, E4, E5, E6, E7, E8, E9,
		   F1, F2, F3, F4, F5, F6, F7, F8, F9,
		   G1, G2, G3, G4, G5, G6, G7, G8, G9,
		   H1, H2, H3, H4, H5, H6, H7, H8, H9,
		   I1, I2, I3, I4, I5, I6, I7, I8, I9)

print("The board now looks like:")
for row in rows:
	print(row)

currentIndex = 0
for num in row2:
	if num == 0:
		print(currentIndex)
		for i in range(1,10):
			if i not in row2 and column2 and box2:
				print("True")
				if currentIndex == 0:
					B1 = i
					print(f"A1 is {B1}")
				elif currentIndex == 1:
					B2 = i
					print(f"A2 is {B2}")
				elif currentIndex == 2:
					B3 = i
					print(f"A3 is {B3}")
				elif currentIndex == 3:
					B4 = i
					print(f"A4 is {B4}")
				elif currentIndex == 4:
					B5 = i
					print(f"A5 is {B5}")
				elif currentIndex == 5:
					B6 = i
					print(f"A6 is {B6}")
				elif currentIndex == 6:
					B7 = i
					print(f"A7 is {B7}")
				elif currentIndex == 7:
					B8 = i
					print(f"A8 is {B8}")
				elif currentIndex == 8:
					B9 = i
					print(f"A9 is {B9}")
				row1 = B1, B2, B3, B4, B5, B6, B7, B8, B9
	currentIndex += 1
row1, row2, row3, row4, row5, row6, row7, row8, row9, rows = buildRows(A1, A2, A3, A4, A5, A6, A7, A8, A9,
		  B1, B2, B3, B4, B5, B6, B7, B8, B9,
		  C1, C2, C3, C4, C5, C6, C7, C8, C9,
		  D1, D2, D3, D4, D5, D6, D7, D8, D9,
		  E1, E2, E3, E4, E5, E6, E7, E8, E9,
		  F1, F2, F3, F4, F5, F6, F7, F8, F9,
		  G1, G2, G3, G4, G5, G6, G7, G8, G9,
		  H1, H2, H3, H4, H5, H6, H7, H8, H9,
		  I1, I2, I3, I4, I5, I6, I7, I8, I9)

column1, column2, column3, column4, column5, column6, column7, column8, column9, columns = buildColumns(A1, A2, A3, A4, A5, A6, A7, A8, A9,
			 B1, B2, B3, B4, B5, B6, B7, B8, B9,
			 C1, C2, C3, C4, C5, C6, C7, C8, C9,
		     D1, D2, D3, D4, D5, D6, D7, D8, D9,
		     E1, E2, E3, E4, E5, E6, E7, E8, E9,
		     F1, F2, F3, F4, F5, F6, F7, F8, F9,
		     G1, G2, G3, G4, G5, G6, G7, G8, G9,
		     H1, H2, H3, H4, H5, H6, H7, H8, H9,
		     I1, I2, I3, I4, I5, I6, I7, I8, I9)

box1, box2, box3, box4, box5, box6, box7, box8, box9, boxes = buildBoxes(A1, A2, A3, A4, A5, A6, A7, A8, A9,
		   B1, B2, B3, B4, B5, B6, B7, B8, B9,
		   C1, C2, C3, C4, C5, C6, C7, C8, C9,
		   D1, D2, D3, D4, D5, D6, D7, D8, D9,
		   E1, E2, E3, E4, E5, E6, E7, E8, E9,
		   F1, F2, F3, F4, F5, F6, F7, F8, F9,
		   G1, G2, G3, G4, G5, G6, G7, G8, G9,
		   H1, H2, H3, H4, H5, H6, H7, H8, H9,
		   I1, I2, I3, I4, I5, I6, I7, I8, I9)

print("The board now looks like:")
for row in rows:
	print(row)
