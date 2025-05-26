import tkinter as tk
from tkinter import ttk, messagebox
import database

# Cores e fontes
COR_BG = "#1e1e2f"
COR_ENTRADA = "#2e2e3f"
COR_TEXTO = "#ffffff"
COR_BOTAO = "#4e8cff"
COR_BOTAO_HOVER = "#6faeff"
FONTE = ("Segoe UI", 11)

def estilizar(root):
    estilo = ttk.Style()
    root.tk.call("source", "azure.tcl")  # Se quiser usar temas externos como 'Azure'
    estilo.theme_use("default")

    estilo.configure("TLabel", foreground=COR_TEXTO, background=COR_BG, font=FONTE)
    estilo.configure("TEntry", padding=6, font=FONTE)
    estilo.configure("TButton",
                     font=FONTE,
                     padding=6,
                     background=COR_BOTAO,
                     foreground=COR_TEXTO)
    estilo.map("TButton",
               background=[("active", COR_BOTAO_HOVER)])

def limpar_tela(root):
    for widget in root.winfo_children():
        widget.destroy()
    root.configure(bg=COR_BG)

def mostrar_tela_login(root):
    limpar_tela(root)
    estilizar(root)

    ttk.Label(root, text="LOGIN", font=("Segoe UI", 18, "bold")).pack(pady=20)

    ttk.Label(root, text="Usuário:").pack(pady=5)
    entry_user = ttk.Entry(root, width=30)
    entry_user.pack()

    ttk.Label(root, text="Senha:").pack(pady=5)
    entry_pass = ttk.Entry(root, show="*", width=30)
    entry_pass.pack()

    def verificar_login():
        user = entry_user.get()
        senha = entry_pass.get()
        if user in database.usuarios and database.usuarios[user] == senha:
            mostrar_tela_cadastro(root)
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    ttk.Button(root, text="Entrar", command=verificar_login).pack(pady=10)
    ttk.Button(root, text="Cadastrar novo usuário", command=lambda: mostrar_tela_cadastro_login(root)).pack()

def mostrar_tela_cadastro(root):
    limpar_tela(root)

    ttk.Label(root, text="CADASTRO", font=("Segoe UI", 18, "bold")).pack(pady=15)

    ttk.Label(root, text="Nome:").pack(pady=5)
    entry_nome = ttk.Entry(root, width=30)
    entry_nome.pack()

    ttk.Label(root, text="Idade:").pack(pady=5)
    entry_idade = ttk.Entry(root, width=30)
    entry_idade.pack()

    resultado_text = tk.Text(root, height=8, width=45, bg=COR_ENTRADA, fg=COR_TEXTO,
                             font=("Consolas", 10), bd=0, relief=tk.FLAT)
    resultado_text.pack(pady=15)

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
            resultado_text.insert(tk.END, f"Nome: {nome}  |  Idade: {idade} anos\n")

    ttk.Button(root, text="Cadastrar", command=cadastrar).pack(pady=10)

# NOVA FUNÇÃO: Cadastro de novo usuário (login e senha)
def mostrar_tela_cadastro_login(root):
    limpar_tela(root)

    ttk.Label(root, text="CRIAR CONTA", font=("Segoe UI", 18, "bold")).pack(pady=15)

    ttk.Label(root, text="Novo usuário:").pack(pady=5)
    entry_user = ttk.Entry(root, width=30)
    entry_user.pack()

    ttk.Label(root, text="Senha:").pack(pady=5)
    entry_pass = ttk.Entry(root, width=30, show="*")
    entry_pass.pack()

    ttk.Label(root, text="Confirmar senha:").pack(pady=5)
    entry_confirm = ttk.Entry(root, width=30, show="*")
    entry_confirm.pack()

    def cadastrar_usuario():
        user = entry_user.get()
        senha = entry_pass.get()
        confirmar = entry_confirm.get()

        if not user or not senha or not confirmar:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        if user in database.usuarios:
            messagebox.showerror("Erro", "Usuário já existe.")
            return

        if senha != confirmar:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return

        database.usuarios[user] = senha
        database.salvar_usuarios()
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        mostrar_tela_login(root)

    ttk.Button(root, text="Cadastrar", command=cadastrar_usuario).pack(pady=10)
    ttk.Button(root, text="Voltar", command=lambda: mostrar_tela_login(root)).pack(pady=5)
