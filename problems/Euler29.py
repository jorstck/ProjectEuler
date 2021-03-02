list= []

for i in range(2,101):
    for j in range(2,101):
        list.append(i**j)
        list.append(j**i)

print(len(list))
