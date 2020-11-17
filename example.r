plebiscitoAR = read.csv("data/Plebiscito Apruebo-Rechazo.csv", header=TRUE, sep=";", dec=",")
plebiscitoC = read.csv("data/Plebiscito convención.csv", header=TRUE, sep=";", dec=",")
presidencial = read.csv("data/resultadosComuna.csv", header=TRUE)


print(summary(plebiscitoAR))
print(summary(plebiscitoC))
print(summary(presidencial))