import random

def advinhaValor():
    numeroAleatorio = random.randint(0, 100)
    isContinuarAdvinhando = True
    tentativas = 0

    while(isContinuarAdvinhando):
        numeroUsuario = int(input("Advinhe um valor entre 100 e 0: "))
        tentativas += 1

        if(numeroUsuario == numeroAleatorio):
            print(f"Você acertou!, O numero era {numeroAleatorio}\nVoce tentou acertar o numero {tentativas} vezes")
            isContinuarAdvinhando = False
        elif(numeroUsuario > numeroAleatorio):
            print(f"{numeroUsuario} é maior que o numero aleatorio...")
            
        elif(numeroUsuario < numeroAleatorio):
            print(f"{numeroUsuario} é menor que o numero aleatorio...")

def caraOuCoroa():
    moedaValor = random.randint(1,2)

    if(moedaValor == 1):
        moedaValor = "cara"
    else:
        moedaValor = "coroa"

    valorAdvinha = input("Você acha que a moeda caiu em cara ou coroa?(cara/coroa): ")

    while(valorAdvinha != "cara" and valorAdvinha != "coroa"):
        valorAdvinha = input("escolha cara ou coroa seu animal: ")

    if(valorAdvinha == moedaValor):
        print("A moeda caiu do seu lado escolhido")
    else:
        print("A moeda nao caiu no seu lado escolhido")

def advinhaSomaDados():
    numeroAleatorioDado = random.randint(0, 12)
    print("Dois dados foram rolados...")
    numeroUsuario = int(input("Advinhe a soma dos dados: "))

    if(numeroUsuario == numeroAleatorioDado):
        print("Você acertou!")
    else:
        print("Você errou...")

def pedraPapelTesoura():
    escolhaMaquina = random.randint(1,3)

    match escolhaMaquina:
        case 1:
            escolhaMaquina = "pedra"
        case 2:
            escolhaMaquina = "papel"
        case 3:
            escolhaMaquina = "tesoura"
    

    escolhaUsuario = input("Escolha uma opção(pedra/papel/tesoura): ")

    while(escolhaUsuario != "pedra" and escolhaUsuario != "papel" and escolhaUsuario != "tesoura"):
        escolhaUsuario = input("Escolha uma opção(pedra/papel/tesoura): ")

    if(escolhaUsuario == escolhaMaquina):
        print(f"A maquina jogou {escolhaMaquina}, voce jogou {escolhaUsuario}")
        print("O jogo empatou!")
    elif((escolhaUsuario == "pedra" and escolhaMaquina == "tesoura") or (escolhaUsuario == "papel" and escolhaMaquina == "pedra") or (escolhaUsuario == "tesoura" and escolhaMaquina == "papel")):
        print(f"A maquina jogou {escolhaMaquina}, voce jogou {escolhaUsuario}")
        print("Você ganhou!")
    else:
        print(f"A maquina jogou {escolhaMaquina}, voce jogou {escolhaUsuario}")
        print("Você perdeu!")

def forca():
    lerArquivo = open("./palavras.txt", "r")
    arrayPalavrasArquivo = lerArquivo.readlines()
    lerArquivo.close()

    palavraEscolhida = random.choice(arrayPalavrasArquivo).strip("\n")
    chances = 6
    palavraMostrarLista = []
    acertos = 0
    jogando = True
    letrasJaChutadas = []

    def printarPalavraEscolhida():
        for i in range(0, len(palavraEscolhida)):

            print(palavraMostrarLista[i], end=" ")

    def palavraChuteJaExisteNoArray(a):
        retornaBool = False

        for i in range(0, len(letrasJaChutadas)):
            if(a == letrasJaChutadas[i]):
                retornaBool = True

        return retornaBool
            
    for i in range(0, len(palavraEscolhida)):
        palavraMostrarLista.append("_")

        print(palavraMostrarLista[i], end=" ")
    print("Bem vindo ao jogo da forca.💀🧛🦇")
    print("Você tem 6 tentativas")

    while(jogando):
    
        palavraChute = input(f"\nChute uma letra({chances} chances):").lower()
        while(palavraChuteJaExisteNoArray(palavraChute)):
            palavraChute = input("\nEssa palavra você ja chutou:").lower()
            tamanhoPalavraChute = len(palavraChute)
            if(tamanhoPalavraChute > 1):
                while(tamanhoPalavraChute > 1):
                    palavraChute = input("Chute UMA letra:")
                    tamanhoPalavraChute = len(palavraChute)
            elif(not palavraChuteJaExisteNoArray(palavraChute)):
                break
                
        tamanhoPalavraChute = len(palavraChute)
        while(tamanhoPalavraChute > 1):
            palavraChute = input("Chute UMA letra:")
            tamanhoPalavraChute = len(palavraChute)

        
        if palavraChute in palavraEscolhida:
            letrasJaChutadas.append(palavraChute)
            for i in range(0, len(palavraEscolhida)):
                if(palavraChute == palavraEscolhida[i]):
                    palavraMostrarLista[i] = palavraChute
                    acertos+=1
            print(f"Você acertou!")
            printarPalavraEscolhida()
            
        else:
            if(palavraChuteJaExisteNoArray(palavraChute)):
                print('teste')
            else:
                chances-=1
                letrasJaChutadas.append(palavraChute)
                print(f"Não tem '{palavraChute}' nessa palavra")
                
                if(chances == 0):
                    print("Acabaram as suas chances")

                elif(chances != 0):
                    printarPalavraEscolhida()
                    print(f"Você tem ainda {chances} chances")
            
        if(acertos == len(palavraEscolhida)):
            print("\nPARABENS! voce descobriu a palavra!")
            break

        if(chances == 0):
            jogando = False
            print("Você perdeu ;(")