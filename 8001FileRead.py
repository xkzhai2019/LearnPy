with open("fileRead.txt","r") as f:
    text = f.read()
    print(text)

with open("fileRead.txt","r") as f:
    text1 = f.readline()
    print(text1)
    text2 = f.readline()
    print(text2)
    text3 = f.readline()
    print(text3)

print("---------------------------")
with open("fileRead.txt","r") as f:
    while True:
        text = f.readline()
        if not text:
            break
        else:
        #   print(text,end="")
            print(text)

print("---------------------------")
with open("fileRead.txt","r") as f:
    text = f.readlines()
    print(text)

print("---------------------------")
with open("fileRead.txt","r") as f:
    for lines in f:
        print(lines,end="")
