import unicodedata

def normalizar_texto(texto):
    texto = str(texto)
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    
    # Filtra os acentos do texto
    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )
    return texto


def exibir_linha():
    print("=" * 25)


def exibir_menu():
    print()
    exibir_linha()
    print("AVEDEX - MENU PRINCIPAL")
    exibir_linha()
    print("1 - Ver mensagem de boas-vindas")
    print("2 - Listar aves")
    print("3 - Ver detalhes de uma ave")
    print("4 - Sobre a AveDex")
    print("5 - Buscar aves (por nome, família, ordem ou dieta)")
    print("0 - Sair")


def mostrar_boas_vindas(nome_usuario):
    print(f"Olá, {nome_usuario}!")
    print("Seja bem-vindo(a) à AveDex.")
    print("Aqui vamos conhecer aves e praticar boas práticas.")


def listar_aves(catalogo):
    print()
    print("=" * 50)
    print("AVES CADASTRADAS")
    print("=" * 50)
    for ave in catalogo:
        print(f"{ave['codigo']} - {ave['nome_popular']}")



def buscar_aves(catalogo, termo_busca):
  
    resultados = []
  
    termo = normalizar_texto(termo_busca)
   
    for ave in catalogo:
      
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]
     
        texto_busca = " ".join(campos_busca)
        
        texto_busca = normalizar_texto(texto_busca)
        
        if termo in texto_busca:
            resultados.append(ave)
    return resultados


def buscar_ave_por_id(catalogo, id_procurado):
    for ave in catalogo:
        if str(ave["codigo"]) == id_procurado:
            return ave
    return None


def exibir_resultados_busca(resultados):
    print()
    exibir_linha()
    print("RESULTADOS DA BUSCA")
    exibir_linha()

    if len(resultados) == 0:
        print("Nenhuma ave encontrada.")
    else:
        for ave in resultados:
            print(f"{ave['codigo']} - {ave['nome_popular']} [{ave['nome_cientifico']}] ({ave['familia']}, {ave['dieta_tipo']})")


def tela_busca(catalogo):
    termo = input("Digite parte do nome, família, ordem ou dieta: ").strip()

    if termo == "":
        print("Digite algum texto para realizar a busca.")
        return

    resultados = buscar_aves(catalogo, termo)
    exibir_resultados_busca(resultados)

    if len(resultados) > 0:
        escolha = input("\nDigite o código para ver detalhes ou ENTER para voltar: ").strip()
        if escolha != "":
            ave_encontrada = buscar_ave_por_id(resultados, escolha)
            if ave_encontrada is None:
                print("Código não encontrado nos resultados.")
            else:
                exibir_detalhes(ave_encontrada)


def exibir_detalhes(ave):
    print()
    exibir_linha()
    print("DETALHES DA AVE")
    exibir_linha()

    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Ordem: {ave['ordem']}")
    print(f"Família: {ave['familia']}")
    print(f"Tipo de Dieta: {ave['dieta_tipo']}")
    print(f"Habitat: {ave['habitat']}")
    print(f"Alimentação: {ave['alimentacao']}")
    print(f"Curiosidade: {ave['curiosidade']}")


def mostrar_sobre():
    print("Sobre a AveDex:")
    print("A AveDex é um catálogo interativo de aves.")
    print("O projeto evolui durante a disciplina de Boas Práticas.")


def pausar():
    input("\nPressione ENTER para voltar ao menu...")


catalogo_aves = [
    {
        "codigo": 1,
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",
        "dieta_tipo": "Omnívora",
        "habitat": "Áreas abertas e cidades",
        "alimentacao": "Insetos, frutos e pequenos animais",
        "curiosidade": "Seu canto lembra a expressão bem-te-vi."
    },
    {
        "codigo": 2,
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "ordem": "Passeriformes",
        "familia": "Thraupidae",
        "dieta_tipo": "Granívora",
        "habitat": "Campos e áreas rurais",
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "O macho possui plumagem amarela intensa."
    },
    {
        "codigo": 3,
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "ordem": "Passeriformes",
        "familia": "Furnariidae",
        "dieta_tipo": "Insetívora",
        "habitat": "Campos, cidades e áreas rurais",
        "alimentacao": "Insetos e pequenos invertebrados",
        "curiosidade": "Constrói ninhos de barro."
    },
    {
        "codigo": 4,
        "nome_popular": "Arara-azul",
        "nome_cientifico": "Anodorhynchus hyacinthinus",
        "ordem": "Psittaciformes",
        "familia": "Psittacidae",
        "dieta_tipo": "Frugívora",
        "habitat": "Pantanal e Cerrado",
        "alimentacao": "Frutos e sementes",
        "curiosidade": "É uma das maiores araras do mundo."
    },
    {
        "codigo": 5,
        "nome_popular": "Tucano-toco",
        "nome_cientifico": "Ramphastos toco",
        "ordem": "Piciformes",
        "familia": "Ramphastidae",
        "dieta_tipo": "Omnívora",
        "habitat": "Florestas e Cerrado",
        "alimentacao": "Frutas, ovos e pequenos animais",
        "curiosidade": "Possui um bico que pode chegar a 20 cm."
    }
]


# --- Fluxo Principal do Programa ---

print("=" * 50)
print("AVEDEX")
print("=" * 50)

nome_usuario = input("Digite seu nome: ").strip()

opcao_menu = ""

while opcao_menu != "0":

    exibir_menu()

    opcao_menu = input("Escolha uma opção: ").strip()

    print()

    if opcao_menu == "1":
        mostrar_boas_vindas(nome_usuario)

    elif opcao_menu == "2":
        listar_aves(catalogo_aves)

    elif opcao_menu == "3":
        listar_aves(catalogo_aves)

        codigo_escolhido = input(
            "\nDigite o código da ave: "
        ).strip()

        ave_encontrada = buscar_ave_por_id(
            catalogo_aves,
            codigo_escolhido
        )

        if ave_encontrada is not None:
            exibir_detalhes(ave_encontrada)
        else:
            print("Ave não encontrada.")

    elif opcao_menu == "4":
        mostrar_sobre()

    elif opcao_menu == "5":
        tela_busca(catalogo_aves)

    elif opcao_menu == "0":
        print("Encerrando a AveDex.")
        print(f"Até logo, {nome_usuario}!")

    else:
        print("Opção inválida. Digite apenas uma das opções listadas (0 a 5).")

    if opcao_menu != "0":
        pausar()