# Day 1 Advent of Code 2021 Sonar Sweep

#Part 1
f=open("input.txt","r")

list=[]

for line in f:
        list.append(int(line.strip()))

i=1
aux=list[0]
cont=0

for i in range(len(list)):
        if(aux<list[i]):
                cont+=1
        aux=list[i]

print(f"Counter part 1: {cont}")

#Part 2
list2=[]
i=0
suma=0

for i in range(len(list)-2):
        suma=list[i]+list[i+1]+list[i+2]
        list2.append(suma)
i=1
aux=list2[0]
cont=0
for i in range(len(list2)):
        if(aux<list2[i]):
                cont+=1
        aux=list2[i]

print(f"Counter part 2: {cont}")
