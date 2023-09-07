import secrets
import string

def gera_senha_forte (tamanho = 6) :
    if tamanho < 6 :
        print("Erro", "O tamanho da senha deve ser maior ou igual a 6 caracteres")
        return None
        
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = [
        secrets.choice (string.ascii_uppercase),
        secrets.choice (string.ascii_lowercase),
        secrets.choice (string.digits),
        secrets.choice (string.punctuation)
        ]

    for i in range (tamanho - 4) :
        senha.append (secrets.choice(caracteres))

    secrets.SystemRandom() .shuffle (senha)
    return "".join (senha)

if __name__ == "__main__" :
    while True:
        tamanho = int(input("Digite o tamanho da senha a ser gerada (mínimo 6): "))
        senha = gera_senha_forte (tamanho)

        if senha:
            print ("Senha gerada: " + senha)

        sair = input("Gostaria de gerar outra senha? [S/N]")
        if sair[0] in ["N", "n"]:
            break