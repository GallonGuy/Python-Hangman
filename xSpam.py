# Use the file name mbox-short.txt as the file name
fname = input("Enter file name:") # mbox-short.rtf
fh = open(fname)
valBadWord = 0
count = 0 
for line in fh: # would do line = line.rstrip() but this python uses invisible \\ instead of \n 
                # and the \\ doesn't get stripped so index is just -2 when going to end of line
    if line.startswith("X-DSPAM-Confidence:"):
        valBadWord += float(line[20:-2])
        count += 1
        continue
    else:
        continue
poggers = valBadWord / count
print(f"Average spam confidence: {poggers}")