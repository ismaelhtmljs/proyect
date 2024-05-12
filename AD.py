#Importaciones
import time
import pyfiglet
from colorama import Fore, Style, init

#Activación de codigos
figlet = pyfiglet.Figlet(font='big')
init()

#Titulo
print(figlet.renderText('Leectura'))
print(figlet.renderText('espacial'))
print(figlet.renderText('Peru'))
print("\n")
print("-"*209)

#descripcion
descripcion = "Esta es una página(proyecto) en python sobre Leectura(astronómicas) en Perú(no necesariamente),SE RECOVENTMIENDA TENER LA PANTALLA ABIERTA(VENTANA COMPLETA) "
mensaje = "Para entrar a los links(enlaces) haga CTRL + CLICK"
mensaje = mensaje.replace('CTRL',f'{Fore.CYAN}CTRL{Style.RESET_ALL}')
mensaje = mensaje.replace('CLICK',f'{Fore.RED}CLICK{Style.RESET_ALL}')
mensaje = mensaje.replace('+',f'{Fore.MAGENTA}+{Style.RESET_ALL}')
descripcion = descripcion.replace('(proyecto)', f'{Fore.CYAN}(proyecto){Style.RESET_ALL}')
descripcion = descripcion.replace('Leectura',f'{Fore.BLUE}Leectura{Style.RESET_ALL}')
descripcion = descripcion.replace('Perú',f'{Fore.LIGHTRED_EX}Perú{Style.RESET_ALL}')
descripcion = descripcion.replace('astronómicas',f'{Fore.CYAN}astronómicas{Style.RESET_ALL}')
descripcion = descripcion.replace('no necesariamente',f'{Fore.LIGHTMAGENTA_EX}no necesariamente{Style.RESET_ALL}')
descripcion = descripcion.replace('VENTANA COMPLETA',f'{Fore.YELLOW}VENTANA COMPLETA{Style.RESET_ALL}')

print(descripcion)
print(mensaje)
print("\n")

#Mensaje de inicio de sesión
time.sleep(2)
print("Coloque los Datos(ya estan guardados)")
print("\n")
nombre = input("Coloque el nombre : ")
contraseña = input("Coloque la contraseña : ")
print("\n")

#Datos guardados
R_nombre = "ismael"
R_contraseña = "123456789"

#Carga de Datos
time.sleep(2)
print("-"*100)
print("espere unos segundos, esto puede tardar un poco")
time.sleep(0.9)

#Animación de puntos
for _ in range(10):
    print(".", end="", flush=True)
    time.sleep(1)

print("\n")


#If and Else
while True:
    if nombre == R_nombre and contraseña == R_contraseña:
        print("\n")
        print("-"*209)
        print(figlet.renderText('EXITO'))
        print("Inicio de sesión completada con éxito")
        time.sleep(3)
        print("\n")
        print("\n")
        print(f"Bienvenido {R_nombre}, la página aun esta en desarrollo, solo puede ver esto usted.")
        time.sleep(5)
        print("\n")
        print(figlet.renderText('Desarrollo'))
        print(figlet.renderText(f'{R_nombre}'))
        print("\n")
        
        #Ya puro TXT para que sea de Noticias espaciales
        print(figlet.renderText('Espacio'))
        print("\n")
        time.sleep(5)
        
        #Titulo de espcaio y separacion para que se vea bonito
        print("-"*209)
        print("\n")
        espacio = "*El espacio*"
        ancho_total = 200
        espacio = espacio.replace('El espacio',f'{Fore.LIGHTRED_EX}El espacio{Style.RESET_ALL}')
        print(espacio.center(ancho_total))
        
        #Separacion
        print("\n")
        
        #Descripcion de espacio
        print("El espacio, en el contexto astronómico, se refiere al vasto y aparentamente infinito vacío que contiene todo lo que existe: planetas, estrellas, galaxias y mucho más.")
        
        #Separación
        print("\n")
        
        #Datos curiosos
        print("\n")
        print("-"*209)
        print("\n")
        print(figlet.renderText('Datos'))
        print(figlet.renderText('Curuosos'))
        time.sleep(1)
        
        #Escaleras astronómicas
        escaleras_astronomicas = "1.Escaleras astronómicas:"
        escaleras_astronomicas = escaleras_astronomicas.replace("1.Escaleras astronómicas:",f"{Fore.BLUE}1.Escaleras astronómicas:{Style.RESET_ALL}")
        print(escaleras_astronomicas)
        print("\n")
        print("El espacio es extremadamente vasto y las distancias se miden en unidades como añoz luz(la distancia que la luz viaja en un año),parsecs, y unidades astronómicas(la distancia media entre la Tierra y el Sol).")
        #enlace de la foto
        enlace = ""
        enlace = enlace.replace('https://upload.wikimedia.org/wikipedia/commons/2/23/Cosmic_distance_ladder.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/2/23/Cosmic_distance_ladder.jpg{Style.RESET_ALL}')
        
        #Separacion
        print("\n")
        
        #Galaxias
        galaxias = "2.Galaxias :"
        galaxias = galaxias.replace("2.Galaxias :",f"{Fore.BLUE}2.Galaxias :{Style.RESET_ALL}")
        print(galaxias)
        print("\n")
        print("Se estima que hay más de 100 mil millones de galaxias en el universo observable. Nuestra galaxia,'la Via Láctea',contiene al menos 100 mil millones de estrellas.")
        #enlace de la foto
        print("\n")
        enlace = "ver foto : https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_qnTageO9OQh0kEq_F3iN4HfmbZ7NFAOPnSanC5x4iA&s"
        enlace = enlace.replace('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_qnTageO9OQh0kEq_F3iN4HfmbZ7NFAOPnSanC5x4iA&s',f'{Fore.CYAN}https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_qnTageO9OQh0kEq_F3iN4HfmbZ7NFAOPnSanC5x4iA&s{Style.RESET_ALL}')
        print(enlace)
        
        #Separacion
        print("\n")
        
        #Agujeros negros
        agujero_negro = "3.Agujeros negros"
        agujero_negro = agujero_negro.replace('Agujeros negros',f'{Fore.LIGHTBLUE_EX}Agujeros negros{Style.RESET_ALL}')
        print(agujero_negro)
        print("\n")
        print("Son regiones del espacio donde la gravedad es tan intensa que nada, ni siquiera la luz, puede escapar. Los agujeros negros pueden formarse a partir de la muerte de estrellas masivas")
        #Separacion
        print("\n")
        #enlace de la foto
        enlace = "ver imagen : https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyBbIr8rGyyJetXoUwR8ONVnUExtOpUALjRE6lViIHZA&s"
        enlace = enlace.replace('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyBbIr8rGyyJetXoUwR8ONVnUExtOpUALjRE6lViIHZA&s',f'{Fore.CYAN}https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyBbIr8rGyyJetXoUwR8ONVnUExtOpUALjRE6lViIHZA&s{Style.RESET_ALL}')
        print(enlace)
        
        #separacion
        print("\n")

        #Estrellas
        estrellas = "4.Estrellas"
        estrellas = estrellas.replace('Estrellas',f'{Fore.LIGHTYELLOW_EX}Estrellas{Style.RESET_ALL}')
        print(estrellas)
        print("\n")
        print("Hay una increible variedad de estrellas en el universo, desde estrellas enanas rojas, las más comunes, hasta estrellas gigantes azules,que son extremadamente calientes y luminosas")
        print("\n")
        enlace = "ver foto : https://upload.wikimedia.org/wikipedia/commons/2/23/Cosmic_distance_ladder.jpg"
        enlace = enlace.replace('https://upload.wikimedia.org/wikipedia/commons/2/23/Cosmic_distance_ladder.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/2/23/Cosmic_distance_ladder.jpg{Style.RESET_ALL}')
        print(enlace)

        #separacion
        print("\n")

        #exoplanetas
        exoplanetas = "5.Exoplanetas"
        exoplanetas = exoplanetas.replace("Exoplanetas",f"{Fore.LIGHTRED_EX}Exoplanetas{Style.RESET_ALL}")
        print(exoplanetas)
        print("\n")
        print("Se han descubierto miles de planetas orbitando estrellas fuera de nuestro sistema solar. Algunos de ellos podrían tener condiciones similares a la de la tierra y ser potencialmente habitables.")
        print("\n")
        enlace = "ver foto : https://image.slidesharecdn.com/exoplanetas-110311145254-phpapp01/85/Exoplanetas-2-320.jpg"
        enlace = enlace.replace('https://image.slidesharecdn.com/exoplanetas-110311145254-phpapp01/85/Exoplanetas-2-320.jpg',f'{Fore.CYAN}https://image.slidesharecdn.com/exoplanetas-110311145254-phpapp01/85/Exoplanetas-2-320.jpg{Style.RESET_ALL}')
        print(enlace)

        #separacion
        print("\n")

        #cosmologia 
        cosmologia = "6.Cosmología"
        cosmologia = cosmologia.replace("Cosmología",f"{Fore.LIGHTMAGENTA_EX}Cosmología{Style.RESET_ALL}")
        print(cosmologia)
        print("\n")
        print("El estudio del origen, la evalucación y la estructura del universo se conoce como Cosmología, Teoriás como el Big Bang intentan explicar el comienzo del universo y su desarrollo a lo largo del tiempo")
        print("\n")
        enlace = "ver foto : https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Hubble_ultra_deep_field_high_rez_edit1.jpg/250px-Hubble_ultra_deep_field_high_rez_edit1.jpg"
        enlace = enlace.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Hubble_ultra_deep_field_high_rez_edit1.jpg/250px-Hubble_ultra_deep_field_high_rez_edit1.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Hubble_ultra_deep_field_high_rez_edit1.jpg/250px-Hubble_ultra_deep_field_high_rez_edit1.jpg{Style.RESET_ALL}')
        print(enlace)

        #separacion
        print("\n")

        #exploracion espacial
        exploracion_espacial = "7.Exploración espacial"
        exploracion_espacial = exploracion_espacial.replace('Exploración espacial',f'{Fore.LIGHTGREEN_EX}Exploración espacial{Style.RESET_ALL}')
        print(exploracion_espacial)
        print("\n")
        print("La exploración del espacio ha llevado a la humanidad a enviar sondas y misiones a planetas, lunas y otros objetos celestes en nuestro sistema solar y más allá.")
        print("\n")
        enlace = "ver foto : https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/EdWhiteFirstAmericanSpacewalker.1965.ws.jpg/1200px-EdWhiteFirstAmericanSpacewalker.1965.ws.jpg"
        enlace = enlace.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/EdWhiteFirstAmericanSpacewalker.1965.ws.jpg/1200px-EdWhiteFirstAmericanSpacewalker.1965.ws.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/EdWhiteFirstAmericanSpacewalker.1965.ws.jpg/1200px-EdWhiteFirstAmericanSpacewalker.1965.ws.jpg{Style.RESET_ALL}')
        print(enlace)

        #separacion 
        print("\n")

        #Materia oscura y energia oscura
        materia_oscura = "8.Matería oscura y energía oscura"
        materia_oscura = materia_oscura.replace('Matería oscura y energía oscura',f'{Fore.RED}Matería oscura y enegía oscura{Style.RESET_ALL}')
        print(materia_oscura)
        print("\n")
        print("Aunque no se puede ver directamente, se cree que el universo que la matería oscura y la energía oscura constituyen la mayor parte del universo y tienen un papel fundamental en su evolución.")
        enlace = "ver foto : https://www.ngenespanol.com/wp-content/uploads/2022/10/ngc-1398-Grande.jpeg"
        enlace = enlace.replace('https://www.ngenespanol.com/wp-content/uploads/2022/10/ngc-1398-Grande.jpeg',f'{Fore.CYAN}https://www.ngenespanol.com/wp-content/uploads/2022/10/ngc-1398-Grande.jpeg{Style.RESET_ALL}')
        print(enlace)
        
        #separacion
        print("\n")
        
        #viaje espacial
        viaje_espacial = "9.Viaje espacial"
        viaje_espacial = viaje_espacial.replace('Viaje espacial',f'{Fore.LIGHTCYAN_EX}Viaje espacial{Style.RESET_ALL}')
        print(viaje_espacial)
        print("\n")
        print("La exploración ha llevado a la humanidad a enviar sondas,satélites y misiones tripuladas a planetas, lunas y otros objetos celestes en nuestro sistema solar y más allá.La luna, Marte y otros planetas como \n Júpiter y Saturno han sido objetos de interés en la exploración espacial")
        print("\n")
        enlace = "ver foto : https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTbz2xYlOwHkJR1yKjCxXOhxFswAK8hJGguzikvRZbeA&s"
        enlace = enlace.replace('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTbz2xYlOwHkJR1yKjCxXOhxFswAK8hJGguzikvRZbeA&s',f'{Fore.CYAN}https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTbz2xYlOwHkJR1yKjCxXOhxFswAK8hJGguzikvRZbeA&s{Style.RESET_ALL}')
        print(enlace)
        
        #separacion
        print("\n")
        
        #estrellas fugaces y meteoritos
        estrellas_meteoritos = "10.Estrellas fugaces y meteoritos"
        estrellas_meteoritos = estrellas_meteoritos.replace('Estrellas fugaces y meteoritos',f'{Fore.LIGHTMAGENTA_EX}Estrellas fugaces y meteoritos{Style.RESET_ALL}')
        print(estrellas_meteoritos)
        print("\n")
        print("Cada año, la Tierra atraviesa varias corrientes de meteoroides, lo que resulta en la observación de estrellas fugaces o meteoros. Algunos de estos meteoroides entran en la atmósfera terrestre y se queman, \n creando lo que conocemos como meteoritos cuando alcanzan la superficie.")
        print("\n")
        enlace = "ver foto :https://estaticos.elcolombiano.com/binrepository/1073x565/147c0/780d565/none/11101/QRRW/meteoro_39636767_20220314185837.jpg"
        enlace = enlace.replace('https://estaticos.elcolombiano.com/binrepository/1073x565/147c0/780d565/none/11101/QRRW/meteoro_39636767_20220314185837.jpg',f'{Fore.CYAN}https://estaticos.elcolombiano.com/binrepository/1073x565/147c0/780d565/none/11101/QRRW/meteoro_39636767_20220314185837.jpg{Style.RESET_ALL}')
        print(enlace)

        #separacion
        print("\n")
        
        #constelaciones
        constelaciones = "11.Constelaciones"
        constelaciones = constelaciones.replace('Constelacione',f'{Fore.LIGHTCYAN_EX}Constelacione{Style.RESET_ALL}')
        print(constelaciones)
        print("\n")
        print("Las constelaciones son grupos aparentes de estrellas en el cielo nocturno que han sido nombradas y utilizadas para la navegacion desde la antigüedad. Ejemplos famosos incluyen Orión, la Osa Mayor y \n la Osa Menor")
        #las tres fotos
        
        #separacion
        print("\n")
        
        #orion
        orion = "ver foto(Orión): https://www.teidebynight.com/wp-content/uploads/2023/09/orion-constellation-2.jpg"
        orion = orion.replace('https://www.teidebynight.com/wp-content/uploads/2023/09/orion-constellation-2.jpg',f'{Fore.CYAN}https://www.teidebynight.com/wp-content/uploads/2023/09/orion-constellation-2.jpg{Style.RESET_ALL}')
        print(orion)
        
        #separacion
        print("\n")

        #osa mayor
        osa_meyor = "ver foto(Osa mayor): https://lh4.googleusercontent.com/proxy/hPg4y7bBuUyaZO4fpSBs3c5wQk7zJRjVPXbPctJ3zyS-sRmFGXkYV8rWYpqBimsSOfAkwd9CmYd91cEZ038LMMT-xyTDkgVa6pVog6GMs0xKacrP"
        osa_meyor = osa_meyor.replace('https://lh4.googleusercontent.com/proxy/hPg4y7bBuUyaZO4fpSBs3c5wQk7zJRjVPXbPctJ3zyS-sRmFGXkYV8rWYpqBimsSOfAkwd9CmYd91cEZ038LMMT-xyTDkgVa6pVog6GMs0xKacrP',f'{Fore.CYAN}https://lh4.googleusercontent.com/proxy/hPg4y7bBuUyaZO4fpSBs3c5wQk7zJRjVPXbPctJ3zyS-sRmFGXkYV8rWYpqBimsSOfAkwd9CmYd91cEZ038LMMT-xyTDkgVa6pVog6GMs0xKacrP{Style.RESET_ALL}')
        print(osa_meyor)
        
        #separacion
        print("\n")

        #osa menor
        osa_menor = "ver foto(Osa menor): https://historiasdeastronomia.es/vistas/images/artistic/ursa-minor.jpg"
        osa_menor = osa_menor.replace('https://historiasdeastronomia.es/vistas/images/artistic/ursa-minor.jpg',f'{Fore.CYAN}https://historiasdeastronomia.es/vistas/images/artistic/ursa-minor.jpg{Style.RESET_ALL}')
        print(osa_menor)        
        
        #separacion
        print("\n")

        #estrellas binarias
        estrellas_binarias = "12.Estrellas Binarias"
        estrellas_binarias = estrellas_binarias.replace('Estrellas Binarias',f'{Fore.LIGHTRED_EX}Estrellas Binarias{Style.RESET_ALL}')
        print(estrellas_binarias)
        print("\n")
        print("Muchas estrellas en el universo existen como parte de sistemas binarios, donde dos estrellas orbitan entre sí, devido a la gravedad. Algunas de estas estrellas binarias pueden experimentar fenómenos como eclipses mutuos cuando una estrella pasa frente a la otra desde nuestra perspectiva en la tierra.")
        
        #separacion
        print("\n")

        #imagen
        enlace_estrellas_binarias = "ver foto : https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Orbit5.gif/350px-Orbit5.gif"
        enlace_estrellas_binarias = enlace_estrellas_binarias.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Orbit5.gif/350px-Orbit5.gif',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Orbit5.gif/350px-Orbit5.gif{Style.RESET_ALL}')
        print(enlace_estrellas_binarias)

        #separacion
        print("\n")

        #expansion del universo
        espancion_universo = "13.Expansión del universo"
        espancion_universo = espancion_universo.replace('Expansión del universo',f'{Fore.LIGHTMAGENTA_EX}Expansión del universo{Style.RESET_ALL}')
        print(espancion_universo)
        print("\n")
        print("Según la teoría del Big Bang, el universo comenzó como una singularidad hace aproximadamente 13.8 mil millones de años y ha estado expandiéndose desde entonces. Esta expansión se puede observar a través del corrimiento al rojo de la luz de objetos distantes, lo que indica que están alejándose de nosotros.")
        #separacion
        print("\n")
        
        #imagen
        enlace_espancion_universo = "ver foto : https://www.ngenespanol.com/wp-content/uploads/2023/07/la-expansion-del-universo-podria-ser-una-ilusion-segun-estudio-espacio.jpg"
        enlace_espancion_universo = enlace_espancion_universo.replace('https://www.ngenespanol.com/wp-content/uploads/2023/07/la-expansion-del-universo-podria-ser-una-ilusion-segun-estudio-espacio.jpg',f'{Fore.CYAN}https://www.ngenespanol.com/wp-content/uploads/2023/07/la-expansion-del-universo-podria-ser-una-ilusion-segun-estudio-espacio.jpg{Style.RESET_ALL}')
        print(enlace_espancion_universo)
        
        #separacion
        print("\n")

        #nebulosas
        nebulosas = "14.Nebulosas"
        nebulosas = nebulosas.replace('Nebulosas',f'{Fore.LIGHTBLACK_EX}Nebulosas{Style.RESET_ALL}')
        print(nebulosas)
        print("\n")
        print("Son grandes nubes de gas y polvo en el espacio que pueden ser el lugar de formación de nuevas estrellas. Las Nebulosas del Águila o la Nebulosa de Orión.")
        print("\n")
        
        #imagenes
        #nebulosa del águila
        enlace_nebulosa_águila = "ver foto : https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Eagle_Nebula_from_ESO.jpg/800px-Eagle_Nebula_from_ESO.jpg"
        enlace_nebulosa_águila = enlace_nebulosa_águila.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Eagle_Nebula_from_ESO.jpg/800px-Eagle_Nebula_from_ESO.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Eagle_Nebula_from_ESO.jpg/800px-Eagle_Nebula_from_ESO.jpg{Style.RESET_ALL}') 
        print(enlace_nebulosa_águila)
        
        #separacion
        print("\n")
        
        #nebulosa de orión
        enlace_nebulosa_orión = "ver foto(Nebulosa de Orión) : https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Eagle_Nebula_from_ESO.jpg/800px-Eagle_Nebula_from_ESO.jpg"
        enlace_nebulosa_orión = enlace_nebulosa_orión.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Eagle_Nebula_from_ESO.jpg/800px-Eagle_Nebula_from_ESO.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Eagle_Nebula_from_ESO.jpg/800px-Eagle_Nebula_from_ESO.jpg{Style.RESET_ALL}')
        print(enlace_nebulosa_orión)
        
        #separacion
        print("\n")
        #separacion
        print("\n")
        #Tiempo para que no se cierre de golpe
        while True:
            time.sleep(1231320)
    else:
        print("No se pudo iniciar sesión")
        print("Vuelva a intentarlo")
        time.sleep(2)
        print("\n")
        print("El programa se cerrará en 5 segundos")
        time.sleep(0.6)
        for _ in range(5):
            print(".", end="", flush=True)  # Imprime un punto sin saltar de línea
            time.sleep(1)
        break  # Esto detiene el bucle después de un intento fallido de inicio de sesión