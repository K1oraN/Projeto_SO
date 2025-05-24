import tkinter as tk
import telas

def iniciar():
    janela = tk.Tk()
    janela.title("Sistema de Entrada e Saída")
    janela.geometry("400x400")
    telas.mostrar_tela_login(janela)
    janela.mainloop()

if __name__ == "__main__":
    iniciar()
