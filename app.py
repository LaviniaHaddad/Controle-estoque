import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

ARQUIVO_ESTOQUE = 'estoque.json'

class SistemaEstoque:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Controle de Estoque")
        self.root.geometry("500x400")
        
        self.carregar_estoque()
        self.criar_interface()
    
    def carregar_estoque(self):
        if os.path.exists(ARQUIVO_ESTOQUE):
            try:
                with open(ARQUIVO_ESTOQUE, 'r') as f:
                    self.estoque = json.load(f)
            except:
                self.estoque = {}
        else:
            self.estoque = {}
    
    def salvar_estoque(self):
        with open(ARQUIVO_ESTOQUE, 'w') as f:
            json.dump(self.estoque, f, indent=4)
    
    def criar_interface(self):
        # Frame principal
        frame = tk.Frame(self.root)
        frame.pack(pady=20)
        
        # Botões
        botoes = [
            ("Adicionar Produto", self.adicionar_produto),
            ("Visualizar Estoque", self.visualizar_estoque),
            ("Atualizar Produto", self.atualizar_produto),
            ("Excluir Produto", self.excluir_produto),
            ("Sair", self.sair)
        ]
        
        for texto, comando in botoes:
            btn = tk.Button(frame, text=texto, command=comando, width=20, height=2)
            btn.pack(pady=5)
    
    def adicionar_produto(self):
        codigo = simpledialog.askstring("Adicionar Produto", "Código do produto:")
        if not codigo:
            return
            
        if codigo in self.estoque:
            messagebox.showerror("Erro", "Já existe um produto com este código.")
            return
            
        nome = simpledialog.askstring("Adicionar Produto", "Nome do produto:")
        if not nome:
            return
            
        try:
            preco = float(simpledialog.askstring("Adicionar Produto", "Preço do produto (R$):"))
            quantidade = int(simpledialog.askstring("Adicionar Produto", "Quantidade em estoque:"))
            
            if preco <= 0 or quantidade < 0:
                messagebox.showerror("Erro", "Valores inválidos.")
                return
                
            self.estoque[codigo] = {
                'nome': nome,
                'preco': preco,
                'quantidade': quantidade
            }
            
            self.salvar_estoque()
            messagebox.showinfo("Sucesso", f"Produto '{nome}' adicionado com sucesso!")
            
        except ValueError:
            messagebox.showerror("Erro", "Valores inválidos para preço ou quantidade.")
    
    def visualizar_estoque(self):
        if not self.estoque:
            messagebox.showinfo("Estoque", "Nenhum produto em estoque.")
            return
            
        # Criar janela para visualização
        janela = tk.Toplevel(self.root)
        janela.title("Estoque Atual")
        janela.geometry("600x400")
        
        texto = scrolledtext.ScrolledText(janela, width=70, height=20)
        texto.pack(pady=10, padx=10)
        
        # Cabeçalho
        cabecalho = f"{'Código':<10} {'Nome':<20} {'Preço (R$)':<12} {'Quantidade':<10}\n"
        texto.insert(tk.END, cabecalho)
        texto.insert(tk.END, "-" * 55 + "\n")
        
        # Produtos
        for codigo, produto in self.estoque.items():
            linha = f"{codigo:<10} {produto['nome']:<20} {produto['preco']:<12.2f} {produto['quantidade']:<10}\n"
            texto.insert(tk.END, linha)
        
        texto.config(state=tk.DISABLED)
    
    def atualizar_produto(self):
        codigo = simpledialog.askstring("Atualizar Produto", "Código do produto para atualizar:")
        if not codigo or codigo not in self.estoque:
            messagebox.showerror("Erro", "Produto não encontrado.")
            return
            
        produto = self.estoque[codigo]
        
        nome = simpledialog.askstring("Atualizar Produto", f"Novo nome [{produto['nome']}]:")
        if nome is None:  # Usuário cancelou
            return
        if nome:  # Se não estiver vazio
            produto['nome'] = nome
            
        try:
            preco = simpledialog.askstring("Atualizar Produto", f"Novo preço [R$ {produto['preco']}]:")
            if preco is not None and preco:  # Se não for None e não estiver vazio
                produto['preco'] = float(preco)
                
            quantidade = simpledialog.askstring("Atualizar Produto", f"Nova quantidade [{produto['quantidade']}]:")
            if quantidade is not None and quantidade:  # Se não for None e não estiver vazio
                produto['quantidade'] = int(quantidade)
                
            if produto['preco'] <= 0 or produto['quantidade'] < 0:
                messagebox.showerror("Erro", "Valores inválidos.")
                return
                
            self.salvar_estoque()
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
            
        except ValueError:
            messagebox.showerror("Erro", "Valores inválidos para preço ou quantidade.")
    
    def excluir_produto(self):
        codigo = simpledialog.askstring("Excluir Produto", "Código do produto para excluir:")
        if not codigo or codigo not in self.estoque:
            messagebox.showerror("Erro", "Produto não encontrado.")
            return
            
        produto = self.estoque[codigo]
        resposta = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir o produto '{produto['nome']}'?")
        
        if resposta:
            del self.estoque[codigo]
            self.salvar_estoque()
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
    
    def sair(self):
        self.root.quit()
    
    def executar(self):
        self.root.mainloop()

# Executar o sistema
if __name__ == "__main__":
    app = SistemaEstoque()
    app.executar()