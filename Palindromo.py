def palindromo(oracion):
    oracion = oracion.replace(" ","")
    if str(oracion)==str(oracion)[::-1]:
      print("La oración sí es un palíndromo")
    else:
      print("La oración no es un palíndromo")

      
def ingresar_oracion():  
    while True:
        error = False
        oracion = input("Escriba una oración: ")
        for letra in oracion:
            if letra.isdigit() == True:
                print("Ingrese una oración que no contenga números")
                error = True
                break
        if error == False:
            break

    return oracion

def menu():
    while True:
        oracion = ingresar_oracion()
        palindromo(oracion)
        while True:
            opc = input("¿Desea ingresar otra oración? si/no: ")
            if opc != "si" and opc != "no":
                print("Ingrese alguna de las opciones")
                continue
            elif opc == "si":
                break
            else:
                print("¡Hasta luego!")
                quit()

menu()

# Interfaz grafica 

class pantalla :

    titulos          = ["Bienvenidos al detector de palindromos"]
    texto_simple     = ["Ingrese el palindromo:"]
    texto_rango      = ["Ingrese el primer límite:", "Ingrese el segundo límite:"]
    texto_menu       = ["¿Desea implementar otra oracion?", "Salir"]
    texto_error      = "Porfavor ingresar una oracion que no contenga numeros"
    texto_retornar   = "Presione cualquier tecla para regresar al menú principal"

    def __init__(self, stdscr):
        self.stdscr = stdscr
    # Método para imprimir el menú del detector de palindromos
    def pantalla_menu(self, fila_seleccionada): 
        
        #Inicializar paleta de colores
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        altura, ancho = self.stdscr.getmaxyx()
        #curses.textpad.rectangle(win, uly, ulx, lry, lrx)

        rectangle(self.stdscr, 3, 3, altura-3, ancho-3) 
        #Print del título principal
        self.stdscr.addstr(0, ancho//2-len(self.titulos[0])//2, self.titulos[0])
        self.stdscr.addstr(2, ancho//2-len(self.titulos[1])//2, self.titulos[1])

        #Print de las opciones
        for indice, i in enumerate(self.texto_menu):
            x = ancho//2 - len(i)//2
            y = altura//2 - len(self.texto_menu)//2 + indice

            if indice == fila_seleccionada:
              
                self.stdscr.attron(curses.color_pair(1))
                self.stdscr.addstr(y, x, i)
                self.stdscr.attroff(curses.color_pair(1))

            else:
                self.stdscr.addstr(y, x, i)

        self.stdscr.refresh()
    #Método para imprimir las pantallas para el palindrpomo

    def pantalla_palindromo(self, palindromo, simple = False): 
        self.stdscr.clear()
        altura, ancho = self.stdscr.getmaxyx()

        #Elección de los títulos
        if simple == True:
            titulo = self.titulos[2]
        else:
            titulo = self.titulos[3]

        self.stdscr.addstr(0, ancho//2-len(titulo)//2, titulo)
        self.stdscr.refresh()

        #Creando ventana
        window = curses.newwin(altura-5, ancho-5, 3, 3) #newwin(int nlines, int ncols, int begin_y, int begin_x)
        window.border()
        _, ancho_W = window.getmaxyx()

        i = 0

        while i < 2:

            #Elección texto input
            if simple == True:
                t = self.texto_simple[i]

            else:
                t = self.texto_rango[i]

            long_cuadro = 4

            posh_texto = ancho_W//2-len(t)//2- long_cuadro      #Posicion horizontal del texto
            posv_texto = 5
            posh1_rect = ancho_W//2+len(t)//2- long_cuadro + 1  #1ra posición horizontal del rectángulo
            posh2_rect = posh1_rect + long_cuadro               #2da posición horizontal del rectángulo

            #Creando ventana para la textbox
            win_text = curses.newwin(1, posh2_rect - posh1_rect, 8, posh1_rect+4) #newwin(int nlines, int ncols, int begin_y, int begin_x)
            box = Textbox(win_text)

            #Creando rectángulo para la textbox
            rectangle(window, posv_texto - 1, posh1_rect, posv_texto + 1, posh2_rect + 1 ) #curses.textpad.rectangle(win, uly, ulx, lry, lrx)
            
            window.addstr(posv_texto, posh_texto, t)
            window.refresh()

            #Input del usuario
            box.edit()

            try:
                texto = int(box.gather())
                
            except ValueError:
                window.addstr(posv_texto + 5, posh_texto, self.texto_error)
                window.refresh()
                win_text.clear()
                continue
            
            if texto <= 0:
                window.addstr(posv_texto + 5, posh_texto, self.texto_error)
                window.refresh()
                win_text.clear()
                continue

            if i == 0:
                num_1 = int(texto)
            else:
                num_2 = int(texto)
            
            i += 1
            
            window.clear()
            window.border()
        
        #Print del resultado en pantalla
        window.addstr(10, ancho_W//2-len(resultado)//2, resultado)
        window.addstr(20, ancho_W//2-len(self.texto_retornar)//2, self.texto_retornar)
        window.refresh()

        window.getch()
    
    def len_menu(self): #Método para retornar la longitud del menú

        return len(self.texto_menu)

    #Función principal

    def palindromo(oracion):
        oracion = oracion.replace(" ","")
    if str(oracion)==str(oracion)[::-1]:
      print("La oración sí es un palíndromo")
    else:
      print("La oración no es un palíndromo")

    while True:
        key = stdscr.getch()
        stdscr.clear()        

        #Verificando cambio o elección de opción en el menú
        if key == curses.KEY_UP and fila_actual > 0:
            fila_actual -= 1

        elif key == curses.KEY_DOWN and fila_actual < scr.len_menu()-1:
            fila_actual += 1

        elif key == curses.KEY_ENTER or key in [10,13]:

            #Salir
            if fila_actual == scr.len_menu() - 1:
                break

            scr.pantalla_menu(fila_actual)

curses.wrapper(main)

        




