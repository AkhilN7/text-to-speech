from gtts import gTTS
fname=input("Enter the file name:")
fhand=open(fname)
language="en"
for line in fhand:
    line=line.strip()
#print(line)
voice=gTTS(text=line, lang=language, slow=False)
sname=input("Enter the name:")
voice.save(sname)


