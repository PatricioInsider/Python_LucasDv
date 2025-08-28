def read():
    numbers =[]
    with open("ejer-intermedio/archivo/numbers.txt","r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
            
    print(numbers)
            

def wr():
    names = ["Juan","Pedro","Cantuña","Amanecida","San Lucas"]
    with open("ejer-intermedio/archivo/names.txt","w", encoding = "utf-8") as f:
        for name in names:
            f.write(name) #archivo.write(lo que queremos escribir en el archivo)
            f.write("\n")

def add():
    addText = str(input("Que deceas agregar al archivo: "))
    with open("ejer-intermedio/archivo/names.txt","a", encoding = "utf-8") as f:
        f.write(addText)
    


def run():
    read()

if __name__=='__main__':
    run()    
    wr()
    add()
    
