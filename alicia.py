def brd(arc):
    try:
        with open(arc, 'r') as f:
            line = f.readlines()
            for lin in line:
                if 'ip route 0.0.0.0 0.0.0.0' in lin:
                    return True
        return False
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return False
arc = "RT01.cfg"
if brd(arc):
    print("Entrada de ruta por defecto.")
else:
    print("No contiene entrada de ruta por defecto.")
