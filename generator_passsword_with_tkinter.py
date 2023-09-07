import secrets
import string
import tkinter as tk
from tkinter import messagebox

def gera_senha_forte(tamanho=6):
    if tamanho < 6:
        messagebox.showerror("Erro", "O tamanho da senha deve ser maior ou igual a 6 caracteres")
        return None
        
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = [
        secrets.choice (string.ascii_uppercase),
        secrets.choice (string.ascii_lowercase),
        secrets.choice (string.digits),
        secrets.choice (string.punctuation)
    ]

    for i in range(tamanho - 4):
        senha.append(secrets.choice(caracteres))

    secrets.SystemRandom().shuffle(senha)
    return "".join(senha)

def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
    except ValueError:
        print("Digite apenas números de tamanho maior que 6")
    else:    
        senha = gera_senha_forte(tamanho)

        if senha:
            resultado.config(text="Senha gerada: " + senha)
            
            with open("senha_gerada.txt", "w") as arquivo:
                for valor in senha:
                    arquivo.write(str(valor) + "\n")
                    
                   
#! Interface gráfica
janela = tk.Tk()
janela.title("Gerador de senhas:")

#! Elementos na interface
label_tamanho = tk.Label(janela, text="𝘿𝙞𝙜𝙞𝙩𝙚 𝙤 𝙩𝙖𝙢𝙖𝙣𝙝𝙤 𝙙𝙖 𝙨𝙚𝙣𝙝𝙖 𝙖 𝙨𝙚𝙧 𝙜𝙚𝙧𝙖𝙙𝙖 (mínimo 𝟲):")
entry_tamanho = tk.Entry(janela)
button_gerar = tk.Button(janela, text="𝐆𝐞𝐫𝐚𝐫 𝐬𝐞𝐧𝐡𝐚", command=gerar_senha)
resultado = tk.Label(janela, text="")
janela.configure(bg="darkblue")


#! Posicionamento dos elementos na interface
janela.geometry("600x400")
label_tamanho.pack()
entry_tamanho.pack()
button_gerar.pack()
resultado.pack()

janela.mainloop()
