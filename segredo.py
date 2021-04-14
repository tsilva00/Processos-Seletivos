import random

segredo = random.randrange(0,1000)

adivinhou = False  
tentativas = 0

def loc_certa(a, b):
    no_certos = 0
    
    i = 0
    while i < 3:
        if a % 10 == b % 10:
            no_certos += 1
        a = a // 10
        b = b // 10
        i = i + 1
        
    return no_certos
    
def no_casados(a, b):
    no_dig = 0

    au = a%10       
    ad = (a//10)%10 
    ac = (a//100)  

    bu = b%10 
    bd = (b//10)%10
    bc = b//100 

    if au == bu:
        no_dig += 1
        bu = -1
    elif au == bd:
        no_dig += 1
        bd = -1
    elif au == bc:
        no_dig += 1
        bc = -1
        
    if ad == bu:
        no_dig += 1
        c0 = -1
    elif ad == bd:
        no_dig += 1
        bd = -1
    elif ad == bc:
        no_dig += 1
        bc = -1
        
    if ac == bu or ac == bd or ac == bc:
        no_dig += 1

    return no_dig

while tentativas < 6 and not adivinhou:
    tentativas += 1
    print("%da tentativa" %tentativas)
    chute = int(input("Digite o seu chute: "))

    loca_certa = loc_certa(segredo, chute)
    no_certo = no_casados(segredo, chute)
    print("Posições certas = %d" %(loca_certa))
    print("Dígitos casados = %d" %(no_certo))
    print()
    if segredo == chute: 
        adivinhou = True
    
if adivinhou:
    print("Você adivinhou o segredo %d em %d tentativas!"
          %(segredo, tentativas))
else:
    print("Você não adivinhou o segredo %d" %(segredo))
