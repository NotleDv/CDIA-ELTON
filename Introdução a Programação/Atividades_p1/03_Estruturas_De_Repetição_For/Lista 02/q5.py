n_eleitores = 10

c1 = 0
c2 = 0
c3 = 0
for i in range(10):
    print("Candidato 1: 1 | Candidato 2: 2 | Candidato 3: 3")
    voto = int(input("Digite o número do candidato: "))
    
    if voto == 1:
        c1+=1
    elif voto == 2:
        c2+=1
    else:
        c3+=1
    print()
        
print(f"\nApuração de votos: \nCandidato 1 -> total: {c1}\nCandidato 2 -> total: {c2}\nCandidato 3 -> total: {c3}")