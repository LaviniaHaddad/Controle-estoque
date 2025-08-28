# Sistema de Controle de Estoque

Um sistema simples de controle de estoque desenvolvido em Python com duas versões: terminal e interface gráfica.

## 📋 Funcionalidades

- **Adicionar produtos** com código, nome, preço e quantidade
- **Visualizar estoque** completo de forma organizada
- **Atualizar informações** de produtos existentes
- **Excluir produtos** do sistema
- **Persistência de dados** em arquivo JSON
- **Duas versões** disponíveis: terminal e interface gráfica

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior

### Desenvolvimento
Primeira Versão (Terminal)
A primeira versão foi desenvolvida como um sistema de terminal com:

Menu interativo no console

Validação de entradas

Persistência em JSON

Interface textual simples

Segunda Versão (Interface Gráfica)
Posteriormente, foi adicionada uma versão com interface gráfica usando Tkinter:

Popups interativos para todas as operações

Janela de visualização com scroll

Mesma lógica de negócio com experiência visual melhorada

### 💾 Armazenamento de Dados
Os dados são armazenados automaticamente no arquivo estoque.json que é criado na primeira execução. O arquivo mantém:

Código do produto (chave única)

Nome do produto

Preço (float)

Quantidade em estoque (integer)

### 🎯 Exemplo de Uso
Execute o programa

Escolha a opção desejada no menu

Siga as instruções nos popups

Os dados são salvos automaticamente

### 📝 Próximas Melhorias
Sistema de categorias

Relatórios de estoque baixo

Histórico de movimentações

Backup automático dos dados
