import os 
os.system("cls")

menu = """\nbienvenido a Creativos.cl \nmenu de entradas para Michael Jam \n1.comprar entradas \n2.mostrar ubicaciones disponibles \n3.ver listado de asistentes \n4.mostrar ganancias totales \n5.salir \ningrese opcion: """

ubicaciondis= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
ubicacionven= []
valoren ="""valor de entradas \n1.platinum $120.000 \n2.gold $80.000 \n3.silver $50.000"""
platinum = []
gold = []
silver = []
while True: 
    try:
        nom = input("ingrese su nombre: ")
        apell = input("ingrese su apellido: ")
        opc = int(input(menu))
        if opc == 1:
            rut = input("porfavor ingrese rut sin puntos ni digito verificador: ")
            if len(rut) != 8:
                print("error, rut no ingresado correctamente")
                break
            else:
                print("bienvenido")
            canten = int(input("cantidad de entradas a comprar [1-3]: "))
            if canten < 1  or  canten > 3:
                print("error, debe seleccionar un numero del 1-3")
            elif canten == 1:
                print(valoren)
                c = 1
            elif canten == 2:
                print(valoren)
                c = 2
            elif canten == 3:
               c=3
               print(valoren)
            
            for i in range (0,(c)):
                t = int(input("ingrese numero a comprar"))
                ubicaciondis.remove(t)
                ubicacionven.append(t)
                if t == 1-20:
                    platinum.append(t)
                elif t == 21-50:
                    gold.append(t)
                elif t == 51-100:
                    silver.append(t)
                print(gold,platinum,silver)
            print(f"numeros ocupados {ubicacionven}")
            #holass

        elif opc == 2:
            print(f"a continuacion se muestran los asientos disponibles: {ubicaciondis} y los asientos reservados {ubicacionven}")
        elif opc == 3:
            print("jaja")
        elif opc == 4:
            print("mu")
        elif opc == 5:
            print(f"hasta pronto {nom} {apell}! , 10/07/2023")
            break
        else :
            print("porfavor seleccione una opcion de la lista")
    except:
        print("ha ocurrido una excepcion")

print("alojaaa")