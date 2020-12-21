
dictComunas = dict()
candidatos = []
regiones = dict()
# data/Resultados_Mesa_PRESIDENCIAL_2da.csv
# data/ResultadosMesas.csv 

with open("data/ResultadosMesas.csv", "r", encoding="utf-8") as file:
    file.readline()
    for i,line in enumerate(file):
        comuna = line.strip().split(";")[4]
        if comuna == "":
            continue
        comuna = comuna.lower()
        region = line.strip().split(";")[0]  
        if region not in regiones:
            regiones[region] = set()
        regiones[region].add(comuna)
        candidato = line.strip().split(";")[12]
        candidato = " ".join(i.capitalize() for i in candidato.split(" ") if i)
        if candidato not in candidatos:
            candidatos.append(candidato)
        votos = int(line.strip().split(";")[13])
        if comuna not in dictComunas:
            dictComunas[comuna] = dict()
        if candidato not in dictComunas[comuna]:
            dictComunas[comuna][candidato] = 0
        dictComunas[comuna][candidato] += votos
    
with open("data/comunas.csv", "r") as file:
    comu = []
    file.readline()
    for line in file:
        comu.append(line.strip())

with open("data/resultadosPresidencial1era.csv", "w", encoding="utf-8") as file:
    file.write("comuna,"+",".join(candidatos)+",ganador\n")
    for comuna in comu:
        file.write(comuna+","+",".join(str(dictComunas[comuna.lower()][candidato]) for candidato in candidatos)
        +","+str(candidatos.index(max(dictComunas[comuna.lower()], key=dictComunas[comuna.lower()].get))) +"\n")