with open("calles_de_medellin_con_acoso.csv") as archivo:
    lines = archivo.readlines( )
    array = []
for i in lines:
    array.append(i.split(";"))
