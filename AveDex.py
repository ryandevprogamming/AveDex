# --- Banco de dados inicial (Catálogo de Aves) ---
catalogo_aves = [
    {"id": 1, "nome_popular": "Bem-te-vi"},
    {"id": 2, "nome_popular": "João-de-barro"},
    {"id": 3, "nome_popular": "Canário-da-terra"}
]

# --- Funções do Sistema ---

def exibir_linha():
    print("=" * 40)


def exibir_menu():
    print()
    exibir_linha()
    print("MENU PRINCIPAL")
    exibir_linha()
    print("1 - Listar aves")  # Atualizado para a Etapa 1
    print("2 - Conhecer uma ave")
    print("3 - Ver uma curiosidade sobre aves")
    print("4 - Sobre a AveDex")
    print("0 - Sair")


# Nova função da Etapa 1
def listar_aves(catalogo):
    print()
    print("-" * 50)
    print("AVES CADASTRADAS")
    print("-" * 50)
    
    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


def mostrar_ave_inicial():
    print("Ave escolhida: Bem-te-vi")
    print("Nome científico: Pitangus sulphuratus")
    print("O bem-te-vi é uma das aves mais conhecidas do Brasil.")


def mostrar_curiosidade():
    print("Curiosidade:")
    print("Muitas aves ajudam no equilíbrio ambiental ao dispersar sementes.")


def mostrar_sobre():
    print("Sobre a AveDex:")
    print("A AveDex será um catálogo interativo de aves.")
    print("Ao longo da disciplina, adicionaremos novas funcionalidades.")


def pausar():
    input("\nPressione ENTER para voltar ao menu...")


# --- Programa principal ---
exibir_linha()
print("AVEDEX")
exibir_linha()

nome_usuario = input("Digite seu nome: ").strip()

# Mensagem de boas-vindas inicial (fora do loop, já que a opção 1 mudou)
print(f"\nOlá, {nome_usuario}!")
print("Seja bem-vindo(a) à AveDex.")

opcao_menu = ""

while opcao_menu != "0":
    exibir_menu()

    opcao_menu = input("Escolha uma opção: ").strip()
    print()

    if opcao_menu == "1":
        listar_aves(catalogo_aves)  # Chamada atualizada da Etapa 1

    elif opcao_menu == "2":
        mostrar_ave_inicial()

    elif opcao_menu == "3":
        mostrar_curiosidade()

    elif opcao_menu == "4":
        mostrar_sobre()

    elif opcao_menu == "0":
        print("Encerrando a AveDex.")
        print(f"Até logo, {nome_usuario}!")

    else:
        print("Opção inválida. Digite apenas 0, 1, 2, 3 ou 4.")

    if opcao_menu != "0":
        pausar()