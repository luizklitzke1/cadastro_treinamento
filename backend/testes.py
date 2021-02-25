testes = [1,2 ,2 ,2, 1, 2, 1 ,1]
mec =[]


for teste in testes:
    elegivel = True
    for t2 in testes:
        
        if teste > t2:
            print(teste,t2)
            elegivel = False

    if elegivel:
        mec.append(teste)
        
print(mec)