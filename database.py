import json
import os

ARQUIVO_USUARIOS = "usuarios.json"

# Carrega usuários do arquivo, se existir
def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {
            "admin": "1234",
            "aluno": "abcd"
        }

# Salva os usuários no arquivo
def salvar_usuarios():
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4)

# Inicializa
usuarios = carregar_usuarios()
cadastros = []
