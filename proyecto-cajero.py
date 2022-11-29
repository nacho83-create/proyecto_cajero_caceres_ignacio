def cajero():
        print("///////////////////////////////////////////")
        print("Hola Bienvenido al cajero de codo a codo")
        print("///////////////////////////////////////////")
        usuario=input("Por favor ingrese su usuario:")
        a=0
        print("///////////////////////////////////////////")
        opcion_incorrecta="opcion incorrecta!!!"    
        while a<3:
            a=a+1
            if str(usuario)==usuario:
                print("BIENVENIDO", usuario)
                print("clave por defecto 1234")
                print("///////////////////////////////////////////")
                print("Importante=Recuerde que posee 3 intentos")
                print("///////////////////////////////////////////")
                clave=int(input("por favor ingrese su clave:"))
                if clave==1234:
                    print("=================================")
                    print(usuario,"tu clave es correcta")
                    break        
                else:
                    print("=======================================================================")
                    print(usuario,"Tu clave ingresada es incorrecta, tiene", a,"intento realizado.")
                    print("=======================================================================")
                    if a==3:
                        print("=================================================================")
                        print("Intentos agotados, su tarjeta fue retenida")
                        print("Por favor para recuperar su tarjeta comuniquese al 0800-222-1234")
                        print("=================================================================")        
                        break

        if clave == 1234:
    
                def menu_principal():
                    saldoDolar = float(1000)
                    saldo = float(85200)
                    print("#########################################")
                    print("Bienvenido a tu cuenta",usuario, "!!")
                    print("#########################################")
                    print("Seleciona una opcion y presiona lo siguiente: ")
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
                    opcion = int(input("Ingresa tu opcion: "))
                #1consultar saldo
                    if  opcion == 1:
                        print("#########################################")
                        print("Tu saldo actual en pesos es de: $" ,saldo)
                        def menu_salida():
                            print("#########################################")
                            print("""Si desea vovlver al menu principal presione 0 
                            si desea salir presione 9""")
                            print("#########################################")
                            opcion_menu = int(input("Ingresa la opcion desada: "))
                            if opcion_menu==0:
                                menu_principal()
                            elif opcion_menu==9:
                                print("#########################################")
                                print("""Usted a salido con exito!!!
                                Muchas gracias por usar nuestros servicios""")
                            else :
                                print("#########################################")
                                print(opcion_incorrecta.upper())
                                print("Ingrese la opcion correcta")  
                                menu_salida() 
                        menu_salida()              
                #2depositar dinero
                    elif opcion == 2:
                        print("#########################################")
                        ingreso = int(input("Digite por teclado el monto de su dinero a ingresar y luego inserte su dinero: "))
                        print("#########################################")
                        saldoActual = saldo + ingreso
                        print("--Gracias por ingresar su dinero, su saldo actual es de: $",saldoActual, "--")
                        def menu_salida():
                            print("#########################################")
                            print("""Si desea vovlver al menu principal presione 0 
                            si desea salir presione 9""")
                            print("#########################################")
                            opcion_menu = int(input("Ingresa la opcion desada: "))
                            if opcion_menu==0:
                                menu_principal()
                            elif opcion_menu==9:
                                print("#########################################")
                                print("""Usted a salido con exito!!!
                                Muchas gracias por usar nuestros servicios""")
                            else :
                                print("#########################################")
                                print(opcion_incorrecta.upper())
                                print("Ingrese la opcion correcta")  
                                menu_salida() 
                        menu_salida()              
                #3extraer dinero
                    elif opcion == 3:
                        print("#########################################")
                        extraccion = int(input("Ingresa el monto a extraer: "))
                        saldoActual = saldo - extraccion
                        print("#########################################")
                        print("Gracias por extraer, tu saldo restante es: $" , saldoActual)
                        def menu_salida():
                            print("#########################################")
                            print("""Si desea volver al menu principal presione 0 
                            si desea salir presione 9""")
                            print("#########################################")
                            opcion_menu = int(input("Ingresa la opcion desada: "))
                            if opcion_menu==0:
                                menu_principal()
                            elif opcion_menu==9:
                                print("#########################################")
                                print("""Usted a salido con exito!!!
                                Muchas gracias por usar nuestros servicios""")
                            else :
                                print("#########################################")
                                print(opcion_incorrecta.upper())
                                print("Ingrese la opcion correcta")  
                                menu_salida() 
                        menu_salida()              
                #4transferir dinero
                    elif opcion == 4:
                        print("#########################################")
                        tranferir = int(input("Ingrese el cbu de la cuenta a la cual deseas tranferir: "))
                        print("#########################################")
                        monto = int(input("Ingresa el monto a tranferir: "))
                        print("#########################################################")
                        print("Estas por realizar una transferencia al numero de cuenta ", tranferir , "con el siguiente monto: ", monto, "estas seguro que deseas realizar esta accion ?")
                        print("#########################################################")
                        saldoActual = saldo - monto
                        confirmar = str(input("Ingresa: \n     # si para confirmar la transferencia. \n     # no para cancelar: \n "))
                        if confirmar == "si":
                            print("#########################################")
                            print("Gracias tu tranferencia ha sido realizada!, tu saldo actual es de: $" , saldoActual )
                        elif confirmar == "no":
                            print("#########################################")
                            print("Has cancelado tu transferencia")
                        else:
                            print("#########################################")
                            print(opcion_incorrecta.upper())
                            print("Ingrese la opcion correcta") 
                        def menu_salida():
                            print("#########################################")
                            print("""Si desea vovlver al menu principal presione 0 
                            si desea salir presione 9""")
                            print("#########################################")
                            opcion_menu = int(input("Ingresa la opcion desada: "))
                            if opcion_menu==0:
                                menu_principal()
                            elif opcion_menu==9:
                                print("#########################################")
                                print("""Usted a salido con exito!!!
                                Muchas gracias por usar nuestros servicios""")
                            else :
                                print("#########################################")
                                print(opcion_incorrecta.upper())
                                print("Ingrese la opcion correcta")  
                                menu_salida() 
                        menu_salida()                  
                #5comprar dolares
                    elif opcion == 5:
                        print("#####################################")
                        print("    El precio del dolar es de $160")
                        print("    Tu saldo es el siguiente: " , saldo)
                        print("#####################################")
                        compraDolar = float(input("ingresa el monto de dolares a comprar: "))
                        print("#####################################")
                        print("Estas seguro de comprar : u$s" , compraDolar, " dolares ?")
                        confirma  = str(input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
                        print("#####################################")
                        if confirma == "si":
                            conversion = compraDolar * 160
                            saldoActual = saldo - conversion
                            saldoDolar = saldoDolar + compraDolar
                            print("#####################################################")
                            print("Tu saldo en tu cuenta pesos es de: $" , saldoActual)
                            print("Tu saldo en tu cuenta dolares es de: u$s" , saldoDolar )
                            print("#####################################################")
                        elif confirma == "no":
                            print("#########################################")
                            print("Has cancelado tu compra") 
                        else:
                            print("#########################################")
                            print(opcion_incorrecta.upper())
                            print("Ingrese la opcion correcta")     
                        def menu_salida():
                            print("#########################################")
                            print("""Si desea vovlver al menu principal presione 0 
                            si desea salir presione 9""")
                            print("#########################################")
                            opcion_menu = int(input("Ingresa la opcion desada: "))
                            if opcion_menu==0:
                                menu_principal()
                            elif opcion_menu==9:
                                print("#########################################")
                                print("""Usted a salido con exito!!!
                                Muchas gracias por usar nuestros servicios""")
                            else :
                                print("#########################################")
                                print(opcion_incorrecta.upper())
                                print("Ingrese la opcion correcta") 
                                menu_salida() 
                        menu_salida()                          
                #6vender dolares
                    elif opcion == 6:
                        print("#####################################")
                        print("    El precio del dolar es de $160")
                        print("    Tu saldo es el siguiente: " , saldo)
                        print("    Tu saldo en dolares es el siguiente:", saldoDolar)
                        print("#####################################")
                        ventaDolar = float(input("Ingresa el monto de dolares a vender: "))
                        print("#####################################")
                        print("Estas seguro de vender : u$s" , ventaDolar, " dolares ?")
                        confirma  = str(input("Ingresa \n     #si para confirmar. \n     #no para cancelar "))
                        print("#####################################")
                        if confirma == "si":
                            
                            if saldoDolar<=0 or saldoDolar<=ventaDolar :
                                print("####################################################")
                                print("Usted no posee saldo suficiente")
                                print("####################################################")
                            elif saldoDolar>=ventaDolar:
                                conversion = ventaDolar * 160
                                saldoActual = saldo + conversion
                                saldoDolar = saldoDolar - ventaDolar
                                
                                print("#####################################################")
                                print("Tu saldo en tu cuenta pesos es de: $" , saldoActual)
                                print("Tu saldo en tu cuenta dolares es de: u$s" , saldoDolar )
                                print("#####################################################")
                        elif confirma == "no":
                            print("#########################################")
                            print("Has cancelado tu venta en dolares")
                        def menu_salida():
                            print("#########################################")
                            print("""Si desea vovlver al menu principal presione 0 
                            Si desea salir presione 9""")
                            print("#########################################")
                            opcion_menu = int(input("Ingresa la opcion desada: "))
                            if opcion_menu==0:
                                menu_principal()
                            elif opcion_menu==9:
                                print("#########################################")
                                print("""Usted a salido con exito!!!
                                Muchas gracias por usar nuestros servicios""")
                            else :
                                print("#########################################")
                                print(opcion_incorrecta.upper())
                                print("Ingrese la opcion correcta") 
                                menu_salida() 
                        menu_salida()              


                #7crear plazo fijo en dolares
                    elif opcion == 7:
                        def mifuncion():
                            print("#####################################")
                            print("    Plazo fijo en dolares por 365 dias ofrece taza del 2%")
                            print("    plazo fijo en dolares a 180 dias ofrece taza de 0.7%" )
                            print("    plazo fijo en dolares a 120 dias ofrece taza de 0.3%")
                            print("    plazo fijo en dolares a 60 dias ofrece taza de 0.2%")
                            print("    plazo fijo en dolares a 30 dias ofrece taza de 0.11%")
                            print("#####################################")
                            print("    Tu saldo en dolares es el siguiente:", saldoDolar)
                            print("#####################################")
                            print("#####################################")
                            plazoFijoDolar = float(input("ingresa el monto de dolares a plazo fijo que deseas colocar: "))
                            dias_plazo_fijo_dolar= int(input("ingrese los dias que desea colocar su plazo fijo en dolares: "))
                            print("#####################################")
                            print("Estas seguro de colocar en plazo fijo : u$s" , plazoFijoDolar, "a",dias_plazo_fijo_dolar,  "dias?")
                            confirma  = str(input("Ingresa \n     #si para confirmar. \n     #no para cancelar "))
                            print("#####################################")
                            if confirma == "si":
                        
                        
                                if dias_plazo_fijo_dolar == 30:
                                    plazo_dolar_30 =(plazoFijoDolar * 0.11)/100 + plazoFijoDolar
                                    print("####################################################")
                                    print("Usted recibira en 30 dias un  total de: u$s" , plazo_dolar_30)
                                    print("####################################################")
                                elif dias_plazo_fijo_dolar == 60:
                                    plazo_dolar_60 =(plazoFijoDolar * 0.2)/100 + plazoFijoDolar
                                    print("####################################################")
                                    print("Usted recibira en 60 dias un  total de: u$s" , plazo_dolar_60)
                                    print("####################################################")
                                elif dias_plazo_fijo_dolar == 120:
                                    plazo_dolar_120 =(plazoFijoDolar * 0.3)/100 + plazoFijoDolar
                                    print("####################################################")
                                    print("Usted recibira en 120 dias un  total de: u$s" , plazo_dolar_120)
                                    print("####################################################")
                                elif dias_plazo_fijo_dolar == 180:
                                    plazo_dolar_180 =(plazoFijoDolar * 0.7)/100 + plazoFijoDolar
                                    print("####################################################")
                                    print("Usted recibira en 180 dias un  total de: u$s" , plazo_dolar_180)
                                    print("####################################################") 
                                elif dias_plazo_fijo_dolar == 365:
                                    plazo_dolar_365 =(plazoFijoDolar * 2)/100 + plazoFijoDolar
                                    print("####################################################")
                                    print("Usted recibira en 365 dias un  total de: u$s" , plazo_dolar_365)
                                    print("####################################################") 
                                else:
                                    print("######################################")
                                    print(opcion_incorrecta.upper())
                                    print("Ingrese la opcion correcta")  
                                    print("#######################################")
                                    mifuncion()          
                            elif confirma == "no":
                                    print("#########################################")
                                    print("Has cancelado tu plazo fijo en dolares")  
                            else :
                                    print("######################################")
                                    print(opcion_incorrecta.upper())
                                    print("Ingrese la opcion correcta")  
                                    print("#######################################")
                        
                        mifuncion()
                        def menu_salida():
                            print("#########################################")
                            print("""Si desea vovlver al menu principal presione 0 
                            si desea salir presione 9""")
                            print("#########################################")
                            opcion_menu = int(input("Ingresa la opcion desada: "))
                            if opcion_menu==0:
                                menu_principal()
                            elif opcion_menu==9:
                                print("#########################################")
                                print("""Usted a salido con exito!!!
                                Muchas gracias por usar nuestros servicios""")
                            else :
                                print("#########################################")
                                print(opcion_incorrecta.upper())
                                print("Ingrese la opcion correcta")  
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
                            print("    Plazo fijo en pesos a 30 dias ofrece taza de 6.174%")
                            print("#####################################")
                            print("    Tu saldo en pesos es el siguiente:", saldo)
                            print("#####################################")
                            print("#####################################")
                            plazoFijoPesos = float(input("Ingresa el monto en pesos a plazo fijo que deseas colocar: "))
                            dias_plazo_fijo_pesos= int(input("Ingrese los dias que desea colocar su plazo fijo en pesos: "))
                            print("#####################################")
                            print("Estas seguro de colocar en plazo fijo : $" , plazoFijoPesos, "a",dias_plazo_fijo_pesos,  "dias?")
                            confirma  = str(input("Ingresa \n     #si para confirmar. \n     #no para cancelar "))
                            print("#####################################")
                            if confirma == "si":
                        
                        
                                if dias_plazo_fijo_pesos == 30:
                                    plazo_pesos_30 =(plazoFijoPesos * 6.174)/100 + plazoFijoPesos
                                    print("####################################################")
                                    print("Usted recibira en 30 dias un  total de: $" , plazo_pesos_30)
                                    print("####################################################")
                                elif dias_plazo_fijo_pesos == 60:
                                    plazo_pesos_60 =(plazoFijoPesos *12.33 )/100 + plazoFijoPesos
                                    print("####################################################")
                                    print("Usted recibira en 60 dias un  total de: $" , plazo_pesos_60)
                                    print("####################################################")
                                elif dias_plazo_fijo_pesos == 120:
                                    plazo_pesos_120 =(plazoFijoPesos *18.4 )/100 + plazoFijoPesos
                                    print("####################################################")
                                    print("Usted recibira en 120 dias un  total de: $" , plazo_pesos_120)
                                    print("####################################################")
                                elif dias_plazo_fijo_pesos == 180:
                                    plazo_pesos_180 =(plazoFijoPesos * 36.98)/100 + plazoFijoPesos
                                    print("####################################################")
                                    print("Usted recibira en 180 dias un  total de: $" , plazo_pesos_180)
                                    print("####################################################") 
                                elif dias_plazo_fijo_pesos == 365:
                                    plazo_pesos_365 =(plazoFijoPesos * 75)/100 + plazoFijoPesos
                                    print("####################################################")
                                    print("Usted recibira en 365 dias un  total de: $" , plazo_pesos_365)
                                    print("####################################################") 
                                else:
                                    print("######################################")
                                    print(opcion_incorrecta.upper())
                                    print("Ingrese la opcion correcta")  
                                    print("#######################################")
                                    mifuncion()  
                            elif confirma == "no":
                        
                                    print("Has cancelado tu plazo fijo en pesos")  
                            else :
                                    print("######################################")
                                    print(opcion_incorrecta.upper())
                                    print("Ingrese la opcion correcta") 
                                    print("#######################################")
                                    mifuncion()
                        mifuncion()
                        def menu_salida():
                            print("#########################################")
                            print("""Si desea vovlver al menu principal presione 0 
                            si desea salir presione 9""")
                            print("#########################################")
                            opcion_menu = int(input("Ingresa la opcion desada: "))
                            if opcion_menu==0:
                                menu_principal()
                            elif opcion_menu==9:
                                print("#########################################")
                                print("""usted a salido con exito!!!
                                Muchas gracias por usar nuestros servicios""")
                            else :
                                print("#########################################")
                                print(opcion_incorrecta.upper())
                                print("Ingrese la opcion correcta") 
                                menu_salida() 
                        menu_salida()           
                
                #9salir de la cuenta
                    elif opcion == 9:
                        def menu_retorno():
                            print("""Esta seguro de salir?
                            Presione s para confirmar y n para retornar al menu principal""")
                            print("#########################################")
                            opcion_menu = str(input("Ingresa la opcion desada: "))
                            print("#########################################")
                            if opcion_menu=="s":
                                print("#########################################")
                                print("""Usted a salido con exito!!!
                                Muchas gracias por usar nuestros servicios""")
                            elif opcion_menu=="n":
                                menu_principal()
                            else :
                                print("#########################################")
                                print(opcion_incorrecta.upper())
                                
                                
                                menu_retorno()
                        menu_retorno()
                menu_principal()               
cajero()