

def formatar_texto(texto,n):
    
    x = 1  
    c = False

    repete = len(texto)//n
    #print(repete)
    for x in range(1,repete):
        print(x)
        texto = texto[:n*x] + "</p> <p>"+ texto[n*x:]

    print(len(texto))
    print(texto)
