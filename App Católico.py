import customtkinter as ctk
import webbrowser

# Função para abrir um site da Bíblia online
def abrir_biblia():
    webbrowser.open("https://www.fatima.org.br/biblia-online/")

# Função para exibir uma oração
def exibir_oracao():
    oracao_texto = (
        "Ave Maria, cheia de graça, o Senhor é convosco; "
        "bendita sois vós entre as mulheres, e bendito é o fruto do vosso ventre, Jesus. "
        "Santa Maria, Mãe de Deus, rogai por nós, pecadores, agora e na hora de nossa morte. Amém."
    )
    texto_oracao.configure(text=oracao_texto)

# Configuração da janela principal
app = ctk.CTk()
app.geometry("800x600")
app.title("APP Católico")

# Configuração de widgets
label_titulo = ctk.CTkLabel(app, text="Aplicativo Católico", font=("Arial", 20))
label_titulo.pack(pady=10)

botao_oracao = ctk.CTkButton(app, text="Exibir Oração", command=exibir_oracao)
botao_oracao.pack(pady=10)

botao_biblia = ctk.CTkButton(app, text="Abrir Bíblia", command=abrir_biblia)
botao_biblia.pack(pady=10)

texto_oracao = ctk.CTkLabel(app, text="", wraplength=350)
texto_oracao.pack(pady=10)

# Iniciar o loop principal da aplicação
app.mainloop()
