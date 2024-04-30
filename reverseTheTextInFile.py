f1=open("input.txt","r")
line=f1.readline()
words=line.split(" ")
words.reverse()

reversedLine=" ".join(words)
f2=open("output.txt","w")
f2.write(reversedLine)

