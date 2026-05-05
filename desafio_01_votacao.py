votos = []

print("Candidatos:")
print("1. Ana")
print("2. Bruno")
print("3. Carlos")

while True:
    voto = input("\nDigite o nome do candidato (fim para encerrar): ").strip().capitalize()
    
    if voto == "Fim":
        break
    
    if voto in ["Ana", "Bruno", "Carlos"]:
        votos.append(voto)
    else:
        print("Voto inválido. Tente novamente.")
        input("\nPressione Enter para continuar...")
        print("\nCandidatos:")
        print("1. Ana")
        print("2. Bruno")
        print("3. Carlos")

if len(votos) == 0:
    print("\nNenhum voto foi registrado.")
else:
    votos_ana = votos.count("Ana")
    votos_bruno = votos.count("Bruno")
    votos_carlos = votos.count("Carlos")

    print("\nResultado da votação:")
    print(f"Ana: {votos_ana} votos")
    print(f"Bruno: {votos_bruno} votos")
    print(f"Carlos: {votos_carlos} votos")

    maior = max(votos_ana, votos_bruno, votos_carlos)

    vencedores = []
    if votos_ana == maior:
        vencedores.append("Ana")
    if votos_bruno == maior:
        vencedores.append("Bruno")
    if votos_carlos == maior:
        vencedores.append("Carlos")

    if len(vencedores) > 1:
        print("Houve um empate entre os candidatos.")
    else:
        print(f"O vencedor é: {vencedores[0]}")