import unicodedata

def escolher_ave(catalogo, mensagem):
    listar_aves(catalogo)

    id_escolhido = input(f"\n{mensagem}:").strip()
    ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)

    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
        return None
    return ave_encontrada

def comparar_duas_aves(catalogo):
    
    print()
    print("Escolha a primeira ave")

    ave_1 = escolher_ave(catalogo, "Digite o ID da primeira ave")
    if ave_1 is None:
        return

    ave_2 = escolher_ave(catalogo, "Digite o ID da segunda ave")
    if ave_2 is None:
        return

    exibir_comparacao_aves(ave_1,ave_2)

def exibir_comparacao_aves(ave_1, ave_2):
    # Cabeçalho da comparação.
    print()
    print("=" * 78)
    print("COMPARAÇÃO ENTRE AVES")
    print("=" * 78)

    # Primeira linha: mostra os nomes das duas aves.
    imprimir_linha_comparacao(
        "Campo",
        ave_1["nome_popular"],
        ave_2["nome_popular"]
    )
    print("-" * 78)

    # Linhas de comparação textual.
    imprimir_linha_comparacao(
        "Nome científico",
        ave_1.get("nome_cientifico"),
        ave_2.get("nome_cientifico")
    )
    imprimir_linha_comparacao(
        "Ordem",
        ave_1.get("ordem"),
        ave_2.get("ordem")
    )
    imprimir_linha_comparacao(
        "Família",
        ave_1.get("familia"),
        ave_2.get("familia")
    )
    imprimir_linha_comparacao(
        "Dieta",
        ave_1.get("dieta_tipo"),
        ave_2.get("dieta_tipo")
    )
    imprimir_linha_comparacao(
        "Habitat",
        ave_1.get("habitat"),
        ave_2.get("habitat")
    )

    # Linhas de comparação numérica com unidade.
    imprimir_linha_comparacao(
        "Comprimento",
        valor_ou_indisponivel(ave_1.get("comprimento_cm"), "cm"),
        valor_ou_indisponivel(ave_2.get("comprimento_cm"), "cm")
    )
    imprimir_linha_comparacao(
        "Peso",
        valor_ou_indisponivel(ave_1.get("peso_g"), "g"),
        valor_ou_indisponivel(ave_2.get("peso_g"), "g")
    )
    imprimir_linha_comparacao(
        "Conservação",
        ave_1.get("status_conservacao", "Não informado"),
        ave_2.get("status_conservacao", "Não informado")
    )
    imprimir_linha_comparacao(
        "Índice",
        ave_1.get("indice_conservacao", "Não informado"),
        ave_2.get("indice_conservacao", "Não informado")
    )

def valor_ou_indisponivel(valor, unidade=""):
    if valor is None or valor == "":
        return "Não informado"
    if unidade != "":
        return f"{valor} {unidade}"

    return str(valor)


def imprimir_linha_comparacao(rotulo,valor_1,valor_2):
    print(f"{rotulo:<18} | {str(valor_1):<25} | {str(valor_2):<25}")


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
        # Código único da ave.
        "codigo": 1,
        # Nomes da ave.
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        # Classificação.
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",
        # Tipo principal de dieta.
        "dieta_tipo": "Omnívora",
        # Ambiente onde a ave costuma viver.
        "habitat": "Áreas abertas e cidades",
        # Medidas aproximadas usadas na comparação.
        "comprimento_cm": 23,
        "peso_g": 68,
        # Situação de conservação.
        # Nesta versão didática, usamos texto simples.
        "status_conservacao": "Pouco preocupante",
        # Índice numérico que será útil futuramente na batalha.
        # Quanto maior, maior será o nível de atenção na conservação.
        "indice_conservacao": 1,
        # Outros detalhes.
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
        "comprimento_cm": 13,
        "peso_g": 20,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
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
        "comprimento_cm": 20,
        "peso_g": 49,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
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
        "comprimento_cm": 100,
        "peso_g": 1500,
        "status_conservacao": "Vulnerável",
        "indice_conservacao": 2,
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
        "comprimento_cm": 55,
        "peso_g": 600,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
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