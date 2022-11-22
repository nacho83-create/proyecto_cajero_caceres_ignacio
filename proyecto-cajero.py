def cajero():
    print("Hola Bienvenido al cajero de codo a codo")
    idioma = int(input("ingresa \n 1 para elegir el idioma en español \n 2 para ingles \n 3 para portugues: "))
    if idioma == 1:
        print("has seleccionado el idioma español")
        print("ingresa tu clave para acceder a tu cuenta \n la clave es 1234 ")
        clave = int(input("ingresa tu clave: "))
        nombre = str(input("ingresa tu nombre: "))
        
        
        if clave == 1234:
            def menu_principal():
                saldoDolar = float(1000)
                saldo = float(85200)
                print("#########################################")
                print("Bienvenido a tu cuenta", nombre, "!!")
                print("#########################################")
                print("seleciona una opcion y presiona lo siguiente: ")
                print("#########################################")
                print("     #1  consultar saldo")
                print("     #2  depositar dinero")
                print("     #3  extraer dinero")
                print("     #4  transferir dinero")
                print("     #5  comprar dolares")
                print("     #6  vender dolares")
                print("     #7  crear plazo fijo en dolares")
                print("     #8  crear plazo fijo en pesos")
                print("     #9  salir de la cuenta")
                print("#########################################")
                opcion = int(input("ingresa tu opcion: "))
            #1consultar saldo
                if  opcion == 1:
                    print("tu saldo actual en pesos es de: $" ,saldo)
                    def menu_salida():
                        print("""si desea vovlver al menu principal presione 0 
                        si desea salir presione 9""")
                        opcion_menu = int(input("ingresa la opcion desada: "))
                        if opcion_menu==0:
                            menu_principal()
                        elif opcion_menu==9:
                            print("""usted a salido con exito!!!
                            muchas gracias por usar nuestros servicios""")
                        else :
                            print("ha ingresado una opcion invalida, por favor imgrese la opcion correcta") 
                            menu_salida() 
                    menu_salida()              
            #2depositar dinero
                elif opcion == 2:
                    print("#########################################")
                    ingreso = int(input("digite por teclado el monto de su dinero a ingresar y luego inserte su dinero: "))
                    print("#########################################")
                    saldoActual = saldo + ingreso
                    print("--Gracias por ingresar su dinero, su saldo actual es de: $",saldoActual, "--")
                    def menu_salida():
                        print("""si desea vovlver al menu principal presione 0 
                        si desea salir presione 9""")
                        opcion_menu = int(input("ingresa la opcion desada: "))
                        if opcion_menu==0:
                            menu_principal()
                        elif opcion_menu==9:
                            print("""usted a salido con exito!!!
                            muchas gracias por usar nuestros servicios""")
                        else :
                            print("ha ingresado una opcion invalida, por favor imgrese la opcion correcta") 
                            menu_salida() 
                    menu_salida()              
            #3extraer dinero
                elif opcion == 3:
                    extraccion = int(input("ingresa el monto a extraer: "))
                    saldoActual = saldo - extraccion
                    print("gracias por extraer, tu saldo restante es: $" , saldoActual)
                    def menu_salida():
                        print("""si desea vovlver al menu principal presione 0 
                        si desea salir presione 9""")
                        opcion_menu = int(input("ingresa la opcion desada: "))
                        if opcion_menu==0:
                            menu_principal()
                        elif opcion_menu==9:
                            print("""usted a salido con exito!!!
                            muchas gracias por usar nuestros servicios""")
                        else :
                            print("ha ingresado una opcion invalida, por favor imgrese la opcion correcta") 
                            menu_salida() 
                    menu_salida()              
            #4transferir dinero
                elif opcion == 4:
                    tranferir = int(input("ingrese el cbu de la cuenta a la cual deseas tranferir: "))
                    monto = int(input("ingresa el monto a tranferir: "))
                    print("#########################################################")
                    print("Estas por realizar una transferencia al numero de cuenta ", tranferir , "con el siguiente monto: ", monto, "estas seguro que deseas realizar esta accion ?")
                    print("#########################################################")
                    saldoActual = saldo - monto
                    confirmar = str(input("ingresa: \n     # si para confirmar la transferencia. \n     # no para cancelar: \n "))
                    if confirmar == "si":
                        print("gracias tu tranferencia ha sido realizada!, tu saldo actual es de: $" , saldoActual )
                    elif confirmar == "no":
                        print("has cancelado tu transferencia")
                    else:
                        print("has ingresado un valor invalido")
                    def menu_salida():
                        print("""si desea vovlver al menu principal presione 0 
                        si desea salir presione 9""")
                        opcion_menu = int(input("ingresa la opcion desada: "))
                        if opcion_menu==0:
                            menu_principal()
                        elif opcion_menu==9:
                            print("""usted a salido con exito!!!
                            muchas gracias por usar nuestros servicios""")
                        else :
                            print("ha ingresado una opcion invalida, por favor imgrese la opcion correcta") 
                            menu_salida() 
                    menu_salida()                  
            #5comprar dolares
                elif opcion == 5:
                    print("#####################################")
                    print("    el precio del dolar es de $160")
                    print("    tu saldo es el siguiente: " , saldo)
                    print("#####################################")
                    compraDolar = float(input("ingresa el monto de dolares a comprar: "))
                    print("#####################################")
                    print("estas seguro de comprar : u$s" , compraDolar, " dolares ?")
                    confirma  = str(input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
                    print("#####################################")
                    if confirma == "si":
                        conversion = compraDolar * 160
                        saldoActual = saldo - conversion
                        saldoDolar = saldoDolar + compraDolar
                        print("#####################################################")
                        print("tu saldo en tu cuenta pesos es de: $" , saldoActual)
                        print("tu saldo en tu cuenta dolares es de: u$s" , saldoDolar )
                        print("#####################################################")
                    elif confirma == "no":
                        print("has cancelado tu compra") 
                    else:
                        print("has ingresado una opcion incorrecta")    
                    def menu_salida():
                        print("""si desea vovlver al menu principal presione 0 
                        si desea salir presione 9""")
                        opcion_menu = int(input("ingresa la opcion desada: "))
                        if opcion_menu==0:
                            menu_principal()
                        elif opcion_menu==9:
                            print("""usted a salido con exito!!!
                            muchas gracias por usar nuestros servicios""")
                        else :
                            print("ha ingresado una opcion invalida, por favor imgrese la opcion correcta") 
                            menu_salida() 
                    menu_salida()                          
            #6vender dolares
                elif opcion == 6:
                    print("#####################################")
                    print("    el precio del dolar es de $160")
                    print("    tu saldo es el siguiente: " , saldo)
                    print("    tu saldo en dolares es el siguiente:", saldoDolar)
                    print("#####################################")
                    ventaDolar = float(input("ingresa el monto de dolares a vender: "))
                    print("#####################################")
                    print("estas seguro de vender : u$s" , ventaDolar, " dolares ?")
                    confirma  = str(input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
                    print("#####################################")
                    if confirma == "si":
                        
                        if saldoDolar<=0 or saldoDolar<=ventaDolar :
                            print("####################################################")
                            print("usted no posee saldo suficiente")
                            print("####################################################")
                        elif saldoDolar>=ventaDolar:
                            conversion = ventaDolar * 160
                            saldoActual = saldo + conversion
                            saldoDolar = saldoDolar - ventaDolar
                            
                            print("#####################################################")
                            print("tu saldo en tu cuenta pesos es de: $" , saldoActual)
                            print("tu saldo en tu cuenta dolares es de: u$s" , saldoDolar )
                            print("#####################################################")
                    elif confirma == "no":
                
                        print("has cancelado tu venta en dolares")
                    def menu_salida():
                        print("""si desea vovlver al menu principal presione 0 
                        si desea salir presione 9""")
                        opcion_menu = int(input("ingresa la opcion desada: "))
                        if opcion_menu==0:
                            menu_principal()
                        elif opcion_menu==9:
                            print("""usted a salido con exito!!!
                            muchas gracias por usar nuestros servicios""")
                        else :
                            print("ha ingresado una opcion invalida, por favor imgrese la opcion correcta") 
                            menu_salida() 
                    menu_salida()              


            #7crear plazo fijo en dolares
                elif opcion == 7:
                    def mifuncion():
                        print("#####################################")
                        print("    plazo fijo en dolares por 365 dias ofrece taza del 2%")
                        print("    plazo fijo en dolares a 180 dias ofrece taza de 0.7%" )
                        print("    plazo fijo en dolares a 120 dias ofrece taza de 0.3%")
                        print("    plazo fijo en dolares a 60 dias ofrece taza de 0.2%")
                        print("    plazo fijo en dolares a 30 dias ofrece taza de 0.11%")
                        print("#####################################")
                        print("    tu saldo en dolares es el siguiente:", saldoDolar)
                        print("#####################################")
                        print("#####################################")
                        plazoFijoDolar = float(input("ingresa el monto de dolares a plazo fijo que deseas colocar: "))
                        dias_plazo_fijo_dolar= int(input("ingrese los dias que desea colocar su plazo fijo en dolares: "))
                        print("#####################################")
                        print("estas seguro de colocar en plazo fijo : u$s" , plazoFijoDolar, "a",dias_plazo_fijo_dolar,  "dias?")
                        confirma  = str(input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
                        print("#####################################")
                        if confirma == "si":
                    
                    
                            if dias_plazo_fijo_dolar == 30:
                                plazo_dolar_30 =(plazoFijoDolar * 0.11)/100 + plazoFijoDolar
                                print("####################################################")
                                print("usted recibira en 30 dias un  total de: u$s" , plazo_dolar_30)
                                print("####################################################")
                            elif dias_plazo_fijo_dolar == 60:
                                plazo_dolar_60 =(plazoFijoDolar * 0.2)/100 + plazoFijoDolar
                                print("####################################################")
                                print("usted recibira en 60 dias un  total de: u$s" , plazo_dolar_60)
                                print("####################################################")
                            elif dias_plazo_fijo_dolar == 120:
                                plazo_dolar_120 =(plazoFijoDolar * 0.3)/100 + plazoFijoDolar
                                print("####################################################")
                                print("usted recibira en 120 dias un  total de: u$s" , plazo_dolar_120)
                                print("####################################################")
                            elif dias_plazo_fijo_dolar == 180:
                                plazo_dolar_180 =(plazoFijoDolar * 0.7)/100 + plazoFijoDolar
                                print("####################################################")
                                print("usted recibira en 180 dias un  total de: u$s" , plazo_dolar_180)
                                print("####################################################") 
                            elif dias_plazo_fijo_dolar == 365:
                                plazo_dolar_365 =(plazoFijoDolar * 2)/100 + plazoFijoDolar
                                print("####################################################")
                                print("usted recibira en 365 dias un  total de: u$s" , plazo_dolar_365)
                                print("####################################################") 
                            else:
                                print("######################################")
                                print ("seleccion incorrecta por favor vuelve a ingresar una opcion correcta!!!!!!") 
                                print("#######################################")
                                mifuncion()          
                        elif confirma == "no":
                    
                                print("has cancelado tu plazo fijo en dolares")  
                        else :
                                print("######################################")
                                print ("seleccion incorrecta por favor vuelve a ingresar una opcion correcta!!!!!!") 
                                print("#######################################")
                    
                    mifuncion()
                    def menu_salida():
                        print("""si desea vovlver al menu principal presione 0 
                        si desea salir presione 9""")
                        opcion_menu = int(input("ingresa la opcion desada: "))
                        if opcion_menu==0:
                            menu_principal()
                        elif opcion_menu==9:
                            print("""usted a salido con exito!!!
                            muchas gracias por usar nuestros servicios""")
                        else :
                            print("ha ingresado una opcion invalida, por favor imgrese la opcion correcta") 
                            menu_salida() 
                    menu_salida()                   
                
            #8ver plazo fijo en pesos
                elif opcion == 8:
                    def mifuncion():
                        print("#####################################")
                        print("    plazo fijo en pesos por 365 dias ofrece taza del 75%")
                        print("    plazo fijo en pesos a 180 dias ofrece taza de 36.98%" )
                        print("    plazo fijo en pesos a 120 dias ofrece taza de 18.4%")
                        print("    plazo fijo en pesos a 60 dias ofrece taza de 12.33%")
                        print("    plazo fijo en pesos a 30 dias ofrece taza de 6.174%")
                        print("#####################################")
                        print("    tu saldo en pesos es el siguiente:", saldo)
                        print("#####################################")
                        print("#####################################")
                        plazoFijoPesos = float(input("ingresa el monto en pesos a plazo fijo que deseas colocar: "))
                        dias_plazo_fijo_pesos= int(input("ingrese los dias que desea colocar su plazo fijo en pesos: "))
                        print("#####################################")
                        print("estas seguro de colocar en plazo fijo : $" , plazoFijoPesos, "a",dias_plazo_fijo_pesos,  "dias?")
                        confirma  = str(input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
                        print("#####################################")
                        if confirma == "si":
                    
                    
                            if dias_plazo_fijo_pesos == 30:
                                plazo_pesos_30 =(plazoFijoPesos * 6.174)/100 + plazoFijoPesos
                                print("####################################################")
                                print("usted recibira en 30 dias un  total de: $" , plazo_pesos_30)
                                print("####################################################")
                            elif dias_plazo_fijo_pesos == 60:
                                plazo_pesos_60 =(plazoFijoPesos *12.33 )/100 + plazoFijoPesos
                                print("####################################################")
                                print("usted recibira en 60 dias un  total de: $" , plazo_pesos_60)
                                print("####################################################")
                            elif dias_plazo_fijo_pesos == 120:
                                plazo_pesos_120 =(plazoFijoPesos *18.4 )/100 + plazoFijoPesos
                                print("####################################################")
                                print("usted recibira en 120 dias un  total de: $" , plazo_pesos_120)
                                print("####################################################")
                            elif dias_plazo_fijo_pesos == 180:
                                plazo_pesos_180 =(plazoFijoPesos * 36.98)/100 + plazoFijoPesos
                                print("####################################################")
                                print("usted recibira en 180 dias un  total de: $" , plazo_pesos_180)
                                print("####################################################") 
                            elif dias_plazo_fijo_pesos == 365:
                                plazo_pesos_365 =(plazoFijoPesos * 75)/100 + plazoFijoPesos
                                print("####################################################")
                                print("usted recibira en 365 dias un  total de: $" , plazo_pesos_365)
                                print("####################################################") 
                            else:
                                print("######################################")
                                print ("seleccion incorrecta por favor vuelve a ingresar una opcion correcta!!!!!!") 
                                print("#######################################")
                                mifuncion()  
                        elif confirma == "no":
                    
                                print("has cancelado tu plazo fijo en pesos")  
                        else :
                                print("######################################")
                                print ("seleccion incorrecta por favor vuelve a ingresar una opcion correcta!!!!!!") 
                                print("#######################################")
                                mifuncion()
                    mifuncion()
                    def menu_salida():
                        print("""si desea vovlver al menu principal presione 0 
                        si desea salir presione 9""")
                        opcion_menu = int(input("ingresa la opcion desada: "))
                        if opcion_menu==0:
                            menu_principal()
                        elif opcion_menu==9:
                            print("""usted a salido con exito!!!
                            muchas gracias por usar nuestros servicios""")
                        else :
                            print("ha ingresado una opcion invalida, por favor imgrese la opcion correcta") 
                            menu_salida() 
                    menu_salida()           
            menu_principal()   
            #9salir de la cuenta
            def menu_salida():
                        print("""si desea vovlver al menu principal presione 0 
                        si desea salir presione 9""")
                        opcion_menu = int(input("ingresa la opcion desada: "))
                        if opcion_menu==0:
                            menu_principal()
                        elif opcion_menu==9:
                            print("""usted a salido con exito!!!
                            muchas gracias por usar nuestros servicios""")
                        else :
                            print("ha ingresado una opcion invalida, por favor imgrese la opcion correcta") 
                            menu_salida() 
            menu_salida()           
        else:
            print("clave incorrecta")
    elif idioma == 2:
        print("has seleccionado ingles")
    elif idioma == 3:
        print("has seleccionado portugues")
    else:
        print("opcion incorrecta")
cajero()