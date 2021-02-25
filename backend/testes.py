"""

#sala1

pessoas11 = ["a","b","c"]
pessoas12 = ["a","d","f"]
lotacao1 = 3
lotacao2 = 0

print(lotacao1//2)
for pessoa in pessoas11[:(lotacao1//2)]:
    print(pessoa)

#sala 2
pessoas21 = ["d","e","carlos"]
pessoas22 = ["e","b","c"]
lotacao1 = 2
lotacao2 = 0

print(lotacao1//2)
for pessoa in pessoas21[:(lotacao1//2)]:
    print(pessoa)

#sala 3
pessoas31 = ["f","g","h"]
pessoas31 = ["g","j"]
lotacao1 = 3
lotacao2 = 0

print(lotacao1//2)
for pessoa in pessoas31[:(lotacao1//2)]:
    print(pessoa)

#sala 4

pessoas41 = ["i","j","k"]
pessoas41 = ["i","k"]
lotacao1 = 4
lotacao2 = 0
print(lotacao1//2)
for pessoa in pessoas41[:(lotacao1//2)]:
    print(pessoa)
    

pessoas66 = ["i","j","k","l"]
pessoas69 = ["i","y","k","t"]

conincide =  len([p for p in pessoas66 if p in pessoas69 ])
print(conincide)



print(1//2)

def teste(a):
    b = a+2
    c = a+4
    return (b,c)


d,e = teste(1)
print(d,e)

f = teste(1)[0]
print(f)

"""
def fib(n):
    
    i = 0
    b = 0
    a = 0
    
    while (i <= n):

        b = b + a
        a = b - a

        if (b == 0) :
            b = b + 1

        i = i + 1
        
        print(i,b)
        
    return b
        
print(fib(8))


