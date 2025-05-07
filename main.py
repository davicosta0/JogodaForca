import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "jogo", "forca"]
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    return " ".join([letra if letra in letras_corretas else "_" for letra in palavra])

def jogo_da_forca():
    print("Bem-vindo ao Jogo da Forca!")
    palavra = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 6

    while tentativas > 0:
        print("\nPalavra:", exibir_palavra(palavra, letras_corretas))
        print(f"Tentativas restantes: {tentativas}")
        print("Letras erradas:", ", ".join(letras_erradas))

        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra:
            letras_corretas.add(letra)
            print("Boa! Você acertou uma letra.")
        else:
            letras_erradas.add(letra)
            tentativas -= 1
            print("Ops! Essa letra não está na palavra.")

        if all(letra in letras_corretas for letra in palavra):
            print("\nParabéns! Você adivinhou a palavra:", palavra)
            break
    else:
        print("\nVocê perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    jogo_da_forca()