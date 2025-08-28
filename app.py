import json
import os

# Nome do arquivo para armazenar os dados
ARQUIVO_ESTOQUE = 'estoque.json'

# Função para carregar os dados do estoque
def carregar_estoque():
    if os.path.exists(ARQUIVO_ESTOQUE):
        try:
            with open(ARQUIVO_ESTOQUE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    return {}

# Função para salvar os dados do estoque
def salvar_estoque(estoque):
    with open(ARQUIVO_ESTOQUE, 'w') as f:
        json.dump(estoque, f, indent=4)

# Função para adicionar um novo produto
def adicionar_produto(estoque):
    print("\n--- Adicionar Novo Produto ---")
    
    try:
        codigo = input("Código do produto: ").strip()
        if not codigo:
            print("Erro: Código do produto não pode estar vazio.")
            return
        
        if codigo in estoque:
            print("Erro: Já existe um produto com este código.")
            return
        
        nome = input("Nome do produto: ").strip()
        if not nome:
            print("Erro: Nome do produto não pode estar vazio.")
            return
        
        preco = float(input("Preço do produto: R$ "))
        if preco <= 0:
            print("Erro: Preço deve ser maior que zero.")
            return
        
        quantidade = int(input("Quantidade em estoque: "))
        if quantidade < 0:
            print("Erro: Quantidade não pode ser negativa.")
            return
        
        estoque[codigo] = {
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        }
        
        salvar_estoque(estoque)
        print(f"Produto '{nome}' adicionado com sucesso!")
        
    except ValueError:
        print("Erro: Valor inválido. Certifique-se de digitar números para preço e quantidade.")

# Função para visualizar todos os produtos
def visualizar_estoque(estoque):
    print("\n--- Estoque Atual ---")
    
    if not estoque:
        print("Nenhum produto em estoque.")
        return
    
    print(f"{'Código':<10} {'Nome':<20} {'Preço (R$)':<12} {'Quantidade':<10}")
    print("-" * 55)
    
    for codigo, produto in estoque.items():
        print(f"{codigo:<10} {produto['nome']:<20} {produto['preco']:<12.2f} {produto['quantidade']:<10}")

# Função para atualizar um produto
def atualizar_produto(estoque):
    print("\n--- Atualizar Produto ---")
    
    codigo = input("Digite o código do produto que deseja atualizar: ").strip()
    
    if codigo not in estoque:
        print("Erro: Produto não encontrado.")
        return
    
    produto = estoque[codigo]
    print(f"Produto encontrado: {produto['nome']}")
    
    try:
        print("\nDeixe em branco para manter o valor atual.")
        
        novo_nome = input(f"Novo nome [{produto['nome']}]: ").strip()
        if novo_nome:
            produto['nome'] = novo_nome
        
        novo_preco = input(f"Novo preço [R$ {produto['preco']}]: ").strip()
        if novo_preco:
            produto['preco'] = float(novo_preco)
            if produto['preco'] <= 0:
                print("Erro: Preço deve ser maior que zero.")
                return
        
        nova_quantidade = input(f"Nova quantidade [{produto['quantidade']}]: ").strip()
        if nova_quantidade:
            produto['quantidade'] = int(nova_quantidade)
            if produto['quantidade'] < 0:
                print("Erro: Quantidade não pode ser negativa.")
                return
        
        salvar_estoque(estoque)
        print("Produto atualizado com sucesso!")
        
    except ValueError:
        print("Erro: Valor inválido. Certifique-se de digitar números para preço e quantidade.")

# Função para excluir um produto
def excluir_produto(estoque):
    print("\n--- Excluir Produto ---")
    
    codigo = input("Digite o código do produto que deseja excluir: ").strip()
    
    if codigo not in estoque:
        print("Erro: Produto não encontrado.")
        return
    
    produto = estoque[codigo]
    confirmacao = input(f"Tem certeza que deseja excluir o produto '{produto['nome']}'? (s/n): ").strip().lower()
    
    if confirmacao == 's':
        del estoque[codigo]
        salvar_estoque(estoque)
        print("Produto excluído com sucesso!")
    else:
        print("Operação cancelada.")

# Função para exibir o menu
def exibir_menu():
    print("\n" + "="*40)
    print("      SISTEMA DE CONTROLE DE ESTOQUE")
    print("="*40)
    print("1. Adicionar produto")
    print("2. Visualizar estoque")
    print("3. Atualizar produto")
    print("4. Excluir produto")
    print("5. Sair")
    print("="*40)

# Função principal
def main():
    estoque = carregar_estoque()
    
    while True:
        exibir_menu()
        
        opcao = input("Digite a opção desejada: ").strip()
        
        if opcao == '1':
            adicionar_produto(estoque)
        elif opcao == '2':
            visualizar_estoque(estoque)
        elif opcao == '3':
            atualizar_produto(estoque)
        elif opcao == '4':
            excluir_produto(estoque)
        elif opcao == '5':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()