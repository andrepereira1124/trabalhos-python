import tkinter as tk  # Alterei para o import padrão de 'tkinter'

def machado_de_assis(entrada_widget, destino_label):
    inspiracao = entrada_widget.get()
    destino_label.config(text=inspiracao)

def abrir_nova_janela():
    nova_janela = tk.Toplevel(window)
    nova_janela.title("Só raul estelionatario 🎭💸")
    nova_janela.geometry("400x400")
    nova_janela.configure(background='lightgreen')

    # Adicionando elementos à nova janela
    nome_nova = tk.Label(nova_janela, text='Só raul estelionatario 🎭💸')
    nome_nova.pack()

    txtentrada_nova = tk.Entry(nova_janela)
    txtentrada_nova.pack()

    t_nova = tk.Label(nova_janela, text="")
    t_nova.pack()

    btn_novo = tk.Button(nova_janela, text="Mostrar", command=lambda: machado_de_assis(txtentrada_nova, t_nova))
    btn_novo.pack()

window = tk.Tk()
window.title("Dreep")
window.geometry("400x400")
window.configure(background='blue')

# Adicionando elementos à janela principal
nome = tk.Label(window, text='Maitê mvhd')
nome.pack()

txtentrada = tk.Entry(window)
txtentrada.pack()

t = tk.Label(window, text="")
t.pack()

btn = tk.Button(window, text="Mostrar", command=lambda: machado_de_assis(txtentrada, t))
btn.pack()

# Botão para abrir a nova janela
btn_abrir_nova_janela = tk.Button(window, text="Abrir Nova Janela", command=abrir_nova_janela)
btn_abrir_nova_janela.pack()

window.mainloop()
