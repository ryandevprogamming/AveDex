# --- Banco de dados inicial (Catálogo de Aves atualizado com detalhes) ---
catalogo_aves = [
    {
        "id": 1, 
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "habitat": "Cidades, matas e proximidades de rios",
        "alimentacao": "Insetos, frutas, pequenos peixes e anfíbios",
        "curiosidade": "Seu canto característico soa exatamente como seu nome popular."
    },
    {
        "id": 2, 
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "habitat": "Campos, pastagens e áreas urbanas",
        "alimentacao": "Insetos, larvas e aranhas no solo",
        "curiosidade": "Constrói seu ninho em formato de forno usando barro e palha."
    },
    {
        "id": 3, 
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "habitat": "Campos abertos e áreas de cerrado",
        "alimentacao": "Sementes e pequenos insetos"
        # Deixado sem o campo 'curiosidade' para testar a robustez do método .get()
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
    print("2 - Conhecer uma ave (Detalhes)")  # Atualizado para refletir a nova funcionalidade
    print("3 - Ver uma curiosidade sobre aves")
    print("4 - Sobre a AveDex")
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


# Nova função da Etapa 3: Exibir os detalhes completos de uma ave
def exibir_detalhes_ave(ave):
    print()
    print("=" * 50)
    print("DETALHES DA AVE")
    print("=" * 50)
    print(f"ID: {ave['id']}")
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Habitat: {ave['habitat']}")
    print(f"Alimentação: {ave['alimentacao']}")
    # Uso do método .get() para chaves opcionais (como no Canário-da-terra)
    print(f"Curiosidade: {ave.get('curiosidade', 'Não informada')}")


# Nova função da Etapa 4: Coordenar a tela de seleção por ID
def selecionar_ave_por_id(catalogo):
    listar_aves(catalogo)
    id_escolhido = input("\nDigite o ID da ave: ").strip()
    ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)
    
    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
    else:
        exibir_detalhes_ave(ave_encontrada)


def mostrar_curiosidade():
    print("Curiosidade Geral:")
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

# Mensagem de boas-vindas inicial
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
        # Opção atualizada na Etapa 4