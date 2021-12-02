#Day 2 Dive!

f=open("prueba.txt","r")

horizontal=0
depth=0

list=[]

for line in f:
    #Split
    list=line.split()
    #Checking
    if (list[0]=='forward'):
        horizontal+=int(list[1])
    if (list[0]=='down'):
        depth+=int(list[1])
    if (list[0]=='up'):
        depth-=int(list[1])

f.close()
result=horizontal*depth
print(f"Horizontal={horizontal}, Depth={depth}, Result={result}")

#Part 2
f=open("prueba.txt","r")
horizontal=0
depth=0
aim=0

for line in f:
    #Separo la linea por espacios para obtener 2 argumentos
    list=line.split()
    #Checking
    if (list[0]=='forward'):
        horizontal+=int(list[1])
        depth=depth+(aim*int(list[1]))
    if (list[0]=='down'):
        aim+=int(list[1])
    if (list[0]=='up'):
        aim-=int(list[1])

f.close()
result=horizontal*depth
print(f"Horizontal={horizontal}, Depth={depth}, Result={result}")