def tipo_acl(lista_de_acceso):
    if lista_de_acceso >= 1 and lista_de_acceso <= 99:
        return "Estándar"
    elif lista_de_acceso >= 100 and lista_de_acceso <= 199:
        return "Extendida"
    else:
        return "El número no corresponde a una lista de acceso"
while True:
    try:
       lista_de_acceso = int(input("Por favor, ingresa el número de ACL IPv4: "))
       tipo = tipo_acl(lista_de_acceso)
       print("Tipo de ACL:", tipo)
       break
    except ValueError:
                     print("Error: Ingresa un número válido para la ACL IPv4.")
