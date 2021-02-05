f1 = open("file_name_here","r")
f2 = ""
while 1: 
    char = f1.read(1)
    if not char:  
        break
    else:
        x = 128 - ord(char)
        x = chr(x)
        f2 += x 
    
f1.close()

f2 = f2[::-1]
print(f2)
