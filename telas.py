import tkinter as tk
from tkinter import messagebox
import database

def mostrar_tela_login(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Usuário:").pack()
    entry_user = tk.Entry(root)
    entry_user.pack()

    tk.Label(root, text="Senha:").pack()
    entry_pass = tk.Entry(root, show="*")
    entry_pass.pack()

    def verificar_login():
        user = entry_user.get()
        senha = entry_pass.get()
        if user in database.usuarios and database.usuarios[user] == senha:
            mostrar_tela_cadastro(root)
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    tk.Button(root, text="Entrar", command=verificar_login).pack(pady=10)

def mostrar_tela_cadastro(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Cadastro de Pessoas", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Nome:").pack()
    entry_nome = tk.Entry(root)
    entry_nome.pack()

    tk.Label(root, text="Idade:").pack()
    entry_idade = tk.Entry(root)
    entry_idade.pack()

    resultado_text = tk.Text(root, height=8, width=50)
    resultado_text.pack(pady=10)

    def cadastrar():
        nome = entry_nome.get()
        idade = entry_idade.get()

        if not nome or not idade:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        try:
            idade = int(idade)
        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser um número.")
            return

        database.cadastros.append((nome.upper(), idade))
        atualizar_resultado()

        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)

    def atualizar_resultado():
        resultado_text.delete("1.0", tk.END)
        for nome, idade in database.cadastros:
            resultado_text.insert(tk.END, f"Nome: {nome}, Idade: {idade} anos\n")

    tk.Button(root, text="Cadastrar", command=cadastrar).pack(pady=5)
