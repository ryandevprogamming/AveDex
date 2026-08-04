# AveDex
Catálogo interativo de aves desenvolvido na disciplina de
Boas Práticas de Programação.
## Funcionalidades atuais
- menu em repetição;
- mensagem personalizada;
- apresentação inicial de uma ave;
- tratamento de opção inválida.
## Como executar


## Testes manuais realizados
- [x] Listagem de aves
- [x] Seleção de ave por ID existente
- [x] Seleção de ave por ID inexistente
- [x] Opção inválida no menu
- [x] Encerramento do programa

## Fontes dos dados
- Nome da instituição ou site: endereço consultado
- Nome da instituição ou site: endereço consultado
## Evolução do projeto
Nesta versão, as aves foram organizadas em uma lista de
dicionários e as funcionalidades foram separadas em funções.


```bash
python avedex.py
```
## Autor
Ryan dos Santos Leal

# AveDex

Catálogo interativo de aves desenvolvido na disciplina de Boas Práticas de Programação.

## Testes manuais realizados

- [x] Listagem de aves
- [x] Seleção de ave por ID existente
- [x] Seleção de ave por ID inexistente
- [x] Opção inválida no menu
- [x] Encerramento do programa


# AveDex

Catálogo interativo de aves desenvolvido na disciplina **Boas Práticas de Programação** (IFMG - Campus Ouro Preto).

## Funcionalidades atuais

- Menu principal com opções de interação
- Mensagem de boas-vindas personalizada
- Listagem de aves cadastradas
- Consulta de detalhes de uma ave pelo código
- Busca textual por nome, nome científico, família, ordem ou dieta (ignorando maiúsculas/minúsculas e acentos)
- Abertura de detalhes diretamente a partir dos resultados da busca
- Informações sobre o projeto
- Tratamento de opções inválidas
- Encerramento seguro do programa

## Estrutura do código

- **Lista de dicionários**: cada ave é representada por um dicionário com as mesmas chaves (`codigo`, `nome_popular`, `nome_cientifico`, `habitat`, `alimentacao`, `curiosidade`).
- **Funções**: cada responsabilidade está separada em funções (`listar_aves`, `buscar_ave_por_id`, `exibir_detalhes`, `buscar_aves`, `exibir_resultados_busca`, `tela_busca`, etc.).
- **Normalização de texto**: `normalizar_texto()` remove acentos e padroniza maiúsculas/minúsculas para tornar a busca mais amigável.
- **Parâmetros**: funções recebem os dados necessários por parâmetro, evitando dependência de variáveis globais.
- **Commits**: evolução registrada passo a passo no GitHub.

## Como executar

```bash
python avedex.py


## Testes manuais realizados
- [x] Listagem de aves
- [x] Seleção de ave por ID existente
- [x] Seleção de ave por ID inexistente
- [x] Opção inválida no menu
- [x] Encerramento do programa
- [x] Busca por parte do nome popular
- [x] Busca ignorando acentos e maiúsculas/minúsculas
- [x] Busca por família
- [x] Busca por ordem
- [x] Busca por dieta
- [x] Busca sem resultados
- [x] Busca com entrada vazia
- [x] Abertura de detalhes a partir dos resultados da busca
- [x] Tentativa de abrir código fora dos resultados
- [x] Comparação entre duas aves existentes
- [x] Comparação exibindo família, dieta e habitat
- [x] Comparação exibindo peso e comprimento
- [x] Comparação exibindo status e índice de conservação
- [x] Tratamento de ID inexistente na comparação
- [x] Comparação da mesma ave com ela mesma
- [x] Opção inválida no menu



## Testes de regressão
- [ ] Listar aves
- [ ] Buscar por parte do nome
- [ ] Buscar por família
- [ ] Buscar por ordem
- [ ] Buscar por dieta
- [ ] Ver detalhes por ID
- [ ] Comparar duas aves
- [ ] Tratar ID inexistente
- [ ] Tratar opção inválida no menu
- [ ] Encerrar o programa