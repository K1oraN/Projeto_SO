
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PyPDF2 import PdfReader

def simular_impressao_pdf():
    arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo PDF para 'imprimir'",
        filetypes=[("PDF files", "*.pdf")]
    )
    if not arquivo:
        return
    try:
        reader = PdfReader(arquivo)
        conteudo = ""
        for i, pagina in enumerate(reader.pages):
            conteudo += f"\n--- Página {i+1} ---\n"
            conteudo += pagina.extract_text() or "[Sem texto reconhecível]"
        messagebox.showinfo("Impressão", f"Simulando impressão do arquivo: {arquivo}")
        print("=== INÍCIO DA IMPRESSÃO ===")
        print(conteudo)
        print("=== FIM DA IMPRESSÃO ===")
        texto_area.delete(1.0, tk.END)
        texto_area.insert(tk.END, conteudo)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler o arquivo: {str(e)}")

janela = tk.Tk()
janela.title("🖨️ Simulador de Impressão PDF")
janela.geometry("700x500")
janela.configure(bg="#1e1e1e")
janela.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="white", background="#007acc", font=("Segoe UI", 11, "bold"))
style.map("TButton", background=[("active", "#005f9e")])

frame_top = tk.Frame(janela, bg="#1e1e1e")
frame_top.pack(pady=20)

titulo = tk.Label(frame_top, text="Simulador de Impressão PDF", fg="white", bg="#1e1e1e", font=("Segoe UI", 18, "bold"))
titulo.pack()

btn_imprimir = ttk.Button(janela, text="Selecionar Arquivo PDF", command=simular_impressao_pdf)
btn_imprimir.pack(pady=10)

frame_texto = tk.Frame(janela, bg="#1e1e1e")
frame_texto.pack(padx=20, pady=10, fill="both", expand=True)

scroll_y = tk.Scrollbar(frame_texto)
scroll_y.pack(side="right", fill="y")

texto_area = tk.Text(frame_texto, wrap="word", yscrollcommand=scroll_y.set, bg="#2d2d2d", fg="white", insertbackground="white", font=("Consolas", 11))
texto_area.pack(fill="both", expand=True)
scroll_y.config(command=texto_area.yview)

janela.mainloop()
