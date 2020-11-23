with open("data/comunas.csv", "r") as file:
    comu = []
    file.readline()
    for line in file:
        comu.append(line.strip())
comunas = []
dictIngresos = dict()
with open("data/ingresos.csv", "r") as file:
    file.readline()
    for line in file:
        comuna = line.strip().split(";")[2]
        porcentaje = float(line.strip().split(";")[4].replace(",","."))
        dictIngresos[comuna] = porcentaje


with open("data/porcentajePobreza.csv","w") as file:
    file.write("comuna,porcentaje,categoria\n")
    for co in comu:
        file.write(co+","+str(dictIngresos[co])+","+str(int(dictIngresos[co]*10))+"\n")