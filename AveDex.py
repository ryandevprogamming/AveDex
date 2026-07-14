# --- Banco de dados inicial (Catálogo de Aves atualizado) ---
catalogo_aves = [
    {
        "id": 1,
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",
        "dieta_tipo": "Onívora",
        "habitat": "Áreas abertas, cidades e bordas de florestas",
        "alimentacao": "Insetos, frutos e pequenos animais",
        "curiosidade": "Seu canto parece dizer o próprio nome."
    },
    {
        "id": 2,
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "ordem": "Passeriformes",
        "familia": "Furnariidae",
        "dieta_tipo": "Insetívora",
        "habitat": "Campos, cidades e áreas rurais",
        "alimentacao": "Insetos e outros invertebrados",
        "curiosidade": "É conhecido por construir ninhos de barro com formato de forno."
    },
    {
        "id": 3,
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "ordem": "Passeriformes",
        "familia": "Thraupidae",
        "dieta_tipo": "Granívora",
        "habitat": "Campos e áreas abertas",
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "Possui canto forte e melodioso."
    },
    {
        "id": 4,
        "nome_popular": "Carcará",
        "nome_cientifico": "Caracara plancus",
        "ordem": "Falconiformes",
        "familia": "Falconidae",
        "dieta_tipo": "Carnívora (Necrófaga/Onívora)",
        "habitat": "Campos, pastagens e centros urbanos",
        "alimentacao": "Presas vivas, carcaças, frutos e ovos",
        "curiosidade": "É um predador oportunista muito inteligente que caminha bastante pelo chão."
    },
    {
        "id": 5,
        "nome_popular": "Beija-flor-tesoura",
        "nome_cientifico": "Eupetomena macroura",
        "ordem": "Apodiformes",
        "familia": "Trochilidae",
        "dieta_tipo": "Nectarívora",
        "habitat": "Jardins, parques e bordas de matas",
        "alimentacao": "Néctar de flores e pequenos insetos em pleno voo",
        "curiosidade": "Possui uma cauda longa e bifurcada que lembra uma tesoura."
    }
]

# --- Funções do Sistema ---

def exibir_linha():
    print("=" * 40)


def exibir_menu():
    print()
    exibir_linha()
    print("MENU PRINCIPAL")
    exibir_linha()
    print("1 - Listar aves")
    print("2 - Conhecer uma ave (Detalhes por ID)")
    print("3 - Ver uma curiosidade sobre aves")
    print("4 - Sobre a AveDex")
    print("5 - Buscar aves por parte do nome")
    print("0 - Sair")


def listar_aves(catalogo):
    print()
    print("-" * 50)
    print("AVES CADASTRADAS")
    print("-" * 50)

    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


def buscar_ave_por_id(catalogo, id_procurado):
    for ave in catalogo:
        if str(ave["id"]) == id_procurado:
            return ave
    return None


def exibir_detalhes_ave(ave):
    print()
    print("=" * 50)
    print("DETALHES DA AVE")
    print("=" * 50)
    print(f"ID: {ave['id']}")
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Ordem: {ave.get('ordem', 'Não informada')}")
    print(f"Família: {ave.get('familia', 'Não informada')}")
    print(f"Tipo de dieta: {ave.get('dieta_tipo', 'Não informado')}")
    print(f"Habitat: {ave['habitat']}")
    print(f"Alimentação: {ave['alimentacao']}")
    print(f"Curiosidade: {ave.get('curiosidade', 'Não informada')}")


def selecionar_ave_por_id(catalogo):
    listar_aves(catalogo)

    id_escolhido = input("\nDigite o ID da ave: ").strip()
    ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)

    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
    else:
        exibir_detalhes_ave(ave_encontrada)


def buscar_aves_por_nome(catalogo, termo_busca):
    resultados = []
    for ave in catalogo:
        nome = ave["nome_popular"].lower()
        termo = termo_busca.lower()
        if termo in nome:
            resultados.append(ave)
    return resultados


def interagir_busca_por_nome(catalogo):
    print()
    print("-" * 50)
    print("BUSCAR AVE POR NOME")
    print("-" * 50)
    
    termo = input("Digite o nome ou parte do nome da ave: ").strip()
    
    if not termo:
        print("Busca cancelada. O termo não pode ser vazio.")
        return

    resultados = buscar_aves_por_nome(catalogo, termo)
    
    if len(resultados) == 0:
        print("\nNenhuma ave encontrada com esse termo.")
    else:
        print(f"\nForam encontradas {len(resultados)} ave(s):")
        for ave in resultados:
            print(f"- {ave['nome_popular']} (ID: {ave['id']})")


def mostrar_curiosidade():
    print("Curiosidade Geral:")
    print("Muitas aves ajudam no equilíbrio ambiental ao dispersar sementes.")


def mostrar_sobre():
    print("Sobre a AveDex:")
    print("A AveDex é um catálogo interativo de aves brasileiras.")
    print("Desenvolvida para ajudar estudantes e entusiastas a conhecerem nossa fauna!")


def pausar():
    input("\nPressione ENTER para voltar ao menu...")


# --- Programa principal ---
exibir_linha()
print("AVEDEX")
exibir_linha()

nome_usuario = input("Digite seu nome: ").strip()

print(f"\nOlá, {nome_usuario}!")
print("Seja bem-vindo(a) à AveDex.")

opcao_menu = ""

while opcao_menu != "0":
    exibir_menu()

    opcao_menu = input("Escolha uma opção: ").strip()
    print()

    if opcao_menu == "1":
        listar_aves(catalogo_aves)

    elif opcao_menu == "2":
        selecionar_ave_por_id(catalogo_aves)

    elif opcao_menu == "3":
        mostrar_curiosidade()

    elif opcao_menu == "4":
        mostrar_sobre()

    elif opcao_menu == "5":
        interagir_busca_por_nome(catalogo_aves)

    elif opcao_menu == "0":
        print(f"Até logo, {nome_usuario}! Obrigado por usar a AveDex.")

    else:
        print("Opção inválida. Tente novamente.")

    if opcao_menu != "0":
        pausar()