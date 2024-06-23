import random
from datetime import datetime

# Definindo as opções da roleta
opcoes = [
    "Parte Superior, Pés", "Dedos, Pés", "Linha Boxer", "Umbigo Inferior", "Umbigo Superior", "Peito",
    "Mamilos", "Sovacos", "Linha Ante-Boxer", "Gémeos", "Coxa Superior", "Coxa Inferior", "Pênis Superior",
    "Pênis Laterais", "Pênis Coxas", "Pênis Base", "Tomate Direito", "Tomate Esquerdo", "Entre Pênis e Anús",
    "Nadegas", "Anús", "Braços"
]

estilos = ["Rapado", "Aparado", "Natural"]

# Opções especiais para "Pênis Superior" quando "Aparado" ou "Natural"
penis_superior_opcoes = [
    "Triangulo, Centro", "Quadrado, Centro", "Forma em V", "Forma em T",
    "Dentes Laterais", "Linha no meio (com pelos)", "Linha no meio (sem pelos)",
    "Linha no meio e com linha sobre os tomates (com pelos)", "Linha no meio e com linha sobre os tomates (sem pelos)"
]

# Função para verificar se é verão (21 de Junho a 21 de Setembro no Hemisfério Norte)
def is_verao():
    hoje = datetime.now()
    ano = hoje.year
    inicio_verao = datetime(ano, 6, 21)
    fim_verao = datetime(ano, 9, 21)
    return inicio_verao <= hoje <= fim_verao

# Função para determinar o estilo com base nas regras
def determinar_estilo(opcao):
    estilo = random.choice(estilos)

    # Regras especiais
    if opcao == "Gémeos" and is_verao() and estilo == "Rapado":
        estilo = random.choice(["Aparado", "Natural"])

    if opcao == "Pênis Superior" and estilo in ["Aparado", "Natural"]:
        estilo = random.choice(penis_superior_opcoes)

    return estilo

# Gerar e mostrar o resultado para cada opção
resultados = {}
for opcao in opcoes:
    estilo = determinar_estilo(opcao)
    resultados[opcao] = estilo

# Exibir os resultados em letras maiúsculas
print("Resultados da Roleta:")
for opcao, estilo in resultados.items():
    print(f"{opcao.upper()}: {estilo.upper()}")
