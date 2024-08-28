from jogos import *

def main():
    print("Jogos:\n1 - Advinhar numero\n2 - Cara ou coroa\n3 - Advinhar soma de dois dados\n4 - Pedra papel e tesoura\n5 - Jogo da Forca")
    escolha = input("Escolha um jogo para jogar: ")

    while(escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4" and escolha != "5"):
        escolha = input("Escolha um jogo para jogar: ")

    match escolha:
        case "1":
            advinhaValor()
        case "2":
            caraOuCoroa()
        case "3":
            advinhaSomaDados()
        case "4":
            pedraPapelTesoura()
        case "5":
            forca()

if __name__=="__main__":
    main()