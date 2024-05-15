#Importaciones
import time
import pyfiglet
from colorama import Fore, Style, init
from rich.console import Console
import os
import sys

#Activación de codigos
figlet = pyfiglet.Figlet(font='big')
console = Console()
init()
#animacion
for _ in range(5):
    mensaje = print(".", end="", flush=True)
    time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
#Titulo
print(figlet.renderText('Leectura'))
print(figlet.renderText('espacial'))
print(figlet.renderText('Peru'))
print("\n")
print("-"*209)

#descripcion
advertencia = "se recomienda leer esto antes que se borre : "
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
advertencia = advertencia.replace('se recomienda leer esto antes que se borre',f'{Fore.RED}{Style.BRIGHT}se recomienda leer esto antes que se borre{Style.RESET_ALL}')

#impresiones en colores
print(advertencia)
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
print("\n")
time.sleep(0.9)

#Animación de puntos
for _ in range(10):
    mensaje = print(".", end="", flush=True)
    time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("\n")


#If and Else
while True:
    #Separacion
    if nombre == R_nombre and contraseña == R_contraseña:
        print("\n")
        print(figlet.renderText('EXITO'))
        print("Inicio de sesión completada con éxito")
        time.sleep(1.6)
        
        #animacion
        for _ in range(5):
            print(".", end="", flush=True)
            time.sleep(1)
        
        #eliminar animacion y lo de arriba
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n")
        print("\n")
        print(f"Bienvenido {R_nombre}, la página aun esta en desarrollo, solo puede ver esto usted.")
        
        #tiempo
        time.sleep(2)
        
        print("\n")
        print(figlet.renderText('Desarrollo'))
        print(figlet.renderText(f'{R_nombre}'))
        print("\n")
        
        #Ya puro TXT para que sea de Noticias espaciales
        print(figlet.renderText('Espacio'))
        print("\n")
        print("esto se borra en 10 segundos")
        
        #tiempo
        time.sleep(1.5)
        
        #animacion
        for _ in range(10):
            print(".", end="", flush= True)
            time.sleep(1)

        #eliminar animacion y lo de arriba
        os.system('cls' if os.name == 'nt' else 'clear')
        
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
        
        #tiempo
        time.sleep(2)

        #animacion de espera de puntos
        for _ in range(5):
            print(".", end="", flush=True)
            time.sleep(1)
        
        #eliminacion de la animacion de puntos
        sys.stdout.write("\r" + " "*10 + "\r")
        sys.stdout.flush()
        
        #datos curiosos
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
        print("\n")
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
        print("Muchas estrellas en el universo existen como parte de sistemas binarios, donde dos estrellas orbitan entre sí, devido a la gravedad. Algunas de estas estrellas binarias pueden experimentar fenómenos \n como eclipses mutuos cuando una estrella pasa frente a la otra desde nuestra perspectiva en la tierra.")
        
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
        print("Según la teoría del Big Bang, el universo comenzó como una singularidad hace aproximadamente 13.8 mil millones de años y ha estado expandiéndose desde entonces. Esta expansión se puede observar a través \n del corrimiento al rojo de la luz de objetos distantes, lo que indica que están alejándose de nosotros.")
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
        enlace_nebulosa_águila = "ver foto(Nebulosa Águila) : https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Eagle_Nebula_from_ESO.jpg/800px-Eagle_Nebula_from_ESO.jpg"
        enlace_nebulosa_águila = enlace_nebulosa_águila.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Eagle_Nebula_from_ESO.jpg/800px-Eagle_Nebula_from_ESO.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Eagle_Nebula_from_ESO.jpg/800px-Eagle_Nebula_from_ESO.jpg{Style.RESET_ALL}') 
        print(enlace_nebulosa_águila)
        
        #separacion
        print("\n")
        
        #nebulosa de orión
        enlace_nebulosa_orión = "ver foto(Nebulosa de Orión) : https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Orion_Nebula_-_Hubble_2006_mosaic_18000.jpg/1200px-Orion_Nebula_-_Hubble_2006_mosaic_18000.jpg"
        enlace_nebulosa_orión = enlace_nebulosa_orión.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Orion_Nebula_-_Hubble_2006_mosaic_18000.jpg/1200px-Orion_Nebula_-_Hubble_2006_mosaic_18000.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Orion_Nebula_-_Hubble_2006_mosaic_18000.jpg/1200px-Orion_Nebula_-_Hubble_2006_mosaic_18000.jpg{Style.RESET_ALL}')
        print(enlace_nebulosa_orión)

        #separacion
        print("\n")

        #rayos cosmicos
        mensaje = "15.Rayos cósmicos"
        mensaje = mensaje.replace('Rayos cósmicos',f'{Fore.LIGHTBLUE_EX}Rayos cósmicos{Style.RESET_ALL}')
        print(mensaje)
        print("\n")
        print("Son partículas de alta energía que viajan a través del espacio a velocidades cercanas a la de la luz. Se originan en eventos cataclísmicos como las explosiones de supernovas o agujeros negros activos.")
        #separacion
        print("\n")
        
        #imagen
        enlace_rayos_cosmicos = "ver foto : https://static.nationalgeographic.es/files/styles/image_3200/public/five-hundred-meter-spherical-aperture-telescope-fast-.adapt_.1900.1.jpg?w=1900&h=2664"
        enlace_rayos_cosmicos = enlace_rayos_cosmicos.replace('https://static.nationalgeographic.es/files/styles/image_3200/public/five-hundred-meter-spherical-aperture-telescope-fast-.adapt_.1900.1.jpg?w=1900&h=2664',f'{Fore.CYAN}https://static.nationalgeographic.es/files/styles/image_3200/public/five-hundred-meter-spherical-aperture-telescope-fast-.adapt_.1900.1.jpg?w=1900&h=2664{Style.RESET_ALL}')
        print(enlace_rayos_cosmicos)
        
        #separacion
        print("\n")
        
        #agujeros de gusanos
        agujero_gusano = "16.Agujeros de gusanos"
        agujero_gusano = agujero_gusano.replace('Agujeros de gusanos',f'{Fore.CYAN}Agujeros de gusanos{Style.RESET_ALL}')
        print(agujero_gusano)
        print("\n")
        print("Son hipotéticas estructura en el espacio-tiempo que podrían conectar diferentes regiones del universo o incluso universos paralelos. Aunque todavía son teóricos, los agujeros de gusanos son un tema fasinante \n en la ciencia ficción y la fisica teórica.")
        print("\n")
        #imagenes
        enlace_agujero_gusano = "ver foto : https://d7lju56vlbdri.cloudfront.net/var/ezwebin_site/storage/images/_aliases/img_1col/noticias/dos-grupos-de-fisicos-teoricos-se-adentran-en-los-agujeros-de-gusano/8865364-6-esl-MX/Dos-grupos-de-fisicos-teoricos-se-adentran-en-los-agujeros-de-gusano.jpg"
        enlace_agujero_gusano = enlace_agujero_gusano.replace('https://d7lju56vlbdri.cloudfront.net/var/ezwebin_site/storage/images/_aliases/img_1col/noticias/dos-grupos-de-fisicos-teoricos-se-adentran-en-los-agujeros-de-gusano/8865364-6-esl-MX/Dos-grupos-de-fisicos-teoricos-se-adentran-en-los-agujeros-de-gusano.jpg',f'{Fore.CYAN}https://d7lju56vlbdri.cloudfront.net/var/ezwebin_site/storage/images/_aliases/img_1col/noticias/dos-grupos-de-fisicos-teoricos-se-adentran-en-los-agujeros-de-gusano/8865364-6-esl-MX/Dos-grupos-de-fisicos-teoricos-se-adentran-en-los-agujeros-de-gusano.jpg{Style.RESET_ALL}')
        print(enlace_agujero_gusano)
        
        #separacion
        print("\n")

        #radiacion cosmica
        radiacion_cosmica = "17.Radiación cósmica de fondo"
        radiacion_cosmica = radiacion_cosmica.replace('Radiación cósmica de fondo',f'{Fore.RED}Radiación cósmica de fondo{Style.RESET_ALL}')
        print(radiacion_cosmica)
        print("\n")
        print("Es una radiación electromagnética que llena todo el universo y es remanente del big bang. Esta radiación es unirforme en todas las direcciones y proporciona una ventana hacia los primeros momentos del \n universo.")
        #separacion
        print("\n")
        #imagenes
        enlace_radiacion_cosmica = "ver foto : https://www.iaea.org/sites/default/files/styles/original_image_size/public/solar-radiation-1140x640.png?itok=mzv1I2O3"
        enlace_radiacion_cosmica = enlace_radiacion_cosmica.replace('https://www.iaea.org/sites/default/files/styles/original_image_size/public/solar-radiation-1140x640.png?itok=mzv1I2O3',f'{Fore.CYAN}https://www.iaea.org/sites/default/files/styles/original_image_size/public/solar-radiation-1140x640.png?itok=mzv1I2O3{Style.RESET_ALL}')
        print(enlace_radiacion_cosmica)

        #separacion
        print("\n")

        #pulsares
        pulsares = "18.Pulsares"
        print("\n")
        print("Son estrellas de neutrones altamente magnéticas que emiten 'haces' de radiación electromagnética desde sus polos magnéticos. cuando estos 'haces' se alinean con la tierra, se detectan como pulsos periódicos de radiación, de ahí su nombre")
        print("\n")
        #imagen
        enlace_pulsares = "ver foto : https://www.ngenespanol.com/wp-content/uploads/2023/04/que-son-los-pulsares-como-se-forman-y-que-los-hace-especiales.jpg"
        enlace_pulsares = enlace_pulsares.replace('https://www.ngenespanol.com/wp-content/uploads/2023/04/que-son-los-pulsares-como-se-forman-y-que-los-hace-especiales.jpg',f'{Fore.CYAN}https://www.ngenespanol.com/wp-content/uploads/2023/04/que-son-los-pulsares-como-se-forman-y-que-los-hace-especiales.jpg{Style.RESET_ALL}')
        print(enlace_pulsares)

        #sepracion
        print("\n")
        
        #nebulosas planetarias 
        nebulosas_planetarias = "19.Nebulosas Planetarias"
        nebulosas_planetarias = nebulosas_planetarias.replace('Nebulosas Planetarias',f'{Fore.LIGHTGREEN_EX}Nebulosas Planetarias{Style.RESET_ALL}')
        print(nebulosas_planetarias)
        print("\n")
        print("Son nebulosas formadas por la eyección de material estelar por parte de estrellas en la etapa final de su evolución. Estas nebulosas suelen tener formas fascinantes y son el resultado de procesos astronómicos complejos")
        print("\n")
        #imagenes
        enlace_nebulosa_planetaria = "ver foto : https://concepto.de/wp-content/uploads/2019/10/nebulosa-helice-planetaria-e1570990002852-800x400.jpg"
        enlace_nebulosa_planetaria = enlace_nebulosa_planetaria.replace('https://concepto.de/wp-content/uploads/2019/10/nebulosa-helice-planetaria-e1570990002852-800x400.jpg',f'{Fore.CYAN}https://concepto.de/wp-content/uploads/2019/10/nebulosa-helice-planetaria-e1570990002852-800x400.jpg{Style.RESET_ALL}')
        print(enlace_nebulosa_planetaria)
        
        #separacion
        print("\n")

        #clusters galacticos
        clusters_galacticos = "20.Clusters galácticos"
        clusters_galacticos = clusters_galacticos.replace('Clusters galácticos',f'{Fore.LIGHTMAGENTA_EX}Clusters galácticos{Style.RESET_ALL}')
        print(clusters_galacticos)
        print("\n")
        print("Son agrupaciones masivas de galaxias que están unidas por la gravedad. Estos clusters pueden contener cientos o mu¿iles de galaxias y son objetos de estudio para comprender la formación y evolución de las estructuras a gran escala en el universo.")
        print("\n")
        #imagen 
        enlace_clusters_galacticos = "ver foto : https://cordis.europa.eu/docs/results/images/2019-07/396750.jpg"
        enlace_clusters_galacticos = enlace_clusters_galacticos.replace('https://cordis.europa.eu/docs/results/images/2019-07/396750.jpg',f'{Fore.CYAN}https://cordis.europa.eu/docs/results/images/2019-07/396750.jpg{Style.RESET_ALL}')
        print(enlace_clusters_galacticos)
        
        #sepracion
        print("\n")
        print("-"*209)
        
        #subtitulo : galaxias
        sub_galaxias = "*Galaxias*"
        sub_galaxias = sub_galaxias.replace('Galaxias',f'{Fore.LIGHTBLUE_EX}Galaxias{Style.RESET_ALL}')
        ancho_titulo_galaxias = 200
        print(sub_galaxias.center(ancho_titulo_galaxias))
        print("\n")
        #galaxia via-lactea
        via_lactea = "1.Vía Láctea"
        via_lactea = via_lactea.replace('Vía Láctea',f'{Fore.LIGHTRED_EX}Vía Láctea{Style.RESET_ALL}')
        print(via_lactea)
        print("\n")
        print("Nuestra galaxia, la Vía Láctea, es una espiral barrada que contiene entre 100 mil millones y 400 mil millones de estrellas. Estamos ubicados en uno de sus brazos, llamado el 'Brazo de Orión'.")
        print("\n")
        #imagen
        enlace_via_lactea = "ver foto : https://img.europapress.es/fotoweb/fotonoticia_20130603202748_1200.jpg"
        enlace_via_lactea = enlace_via_lactea.replace('https://img.europapress.es/fotoweb/fotonoticia_20130603202748_1200.jpg',f'{Fore.CYAN}https://img.europapress.es/fotoweb/fotonoticia_20130603202748_1200.jpg{Style.RESET_ALL}')
        print(enlace_via_lactea)
        
        #separacion
        print("\n")
        
        #andromeda 
        andromeda = "2.Andrómeda(M31)"
        andromeda = andromeda.replace('Andrómeda(M31)',f'{Fore.LIGHTMAGENTA_EX}Andrómeda(M31){Style.RESET_ALL}')
        print(andromeda)
        print("\n")
        print("La galaxia de Andrómeda es la galaxia espiral más cercana a la Vía LLáctea y se está acercando a nosotros a unos 110 kilómetros por segundo. Se espera que colisione con nuestra galaxia en unos \n 4 mil millones de años.")
        print("\n")
        #imagen
        enlace_andromeda = "ver foto : https://upload.wikimedia.org/wikipedia/commons/5/57/M31bobo.jpg"
        enlace_andromeda = enlace_andromeda.replace('https://upload.wikimedia.org/wikipedia/commons/5/57/M31bobo.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/5/57/M31bobo.jpg{Style.RESET_ALL}')
        print(enlace_andromeda)

        #separacion
        print("\n")

        #galaxia de remolino
        galaxia_remolino = "3.Galaxia de Remolino(M51)"
        galaxia_remolino = galaxia_remolino.replace('Galaxia de Remolino(M51)',f'{Fore.LIGHTBLUE_EX}Galaxia de Remolino(M51){Style.RESET_ALL}')
        print(galaxia_remolino)
        print("\n")
        print("Es una galaxia espiral situada a unos 23 millones de años luz de la Tierra. Es famosa por su estructura en espiral y su interracción con una galaxia más pequeña que ha causado distorsiones en sus brazos")
        print("\n")
        #imagen
        enlace_galaxia_remolino = "ver foto : https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Messier51.jpg/1200px-Messier51.jpg"
        enlace_galaxia_remolino =enlace_galaxia_remolino.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Messier51.jpg/1200px-Messier51.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Messier51.jpg/1200px-Messier51.jpg{Style.RESET_ALL}')
        print(enlace_galaxia_remolino)
        
        #separacion
        print("\n")

        #galaxia del sombrero
        galaxia_sombrero = "4.Galaxia del Sombrero(M104)"
        galaxia_sombrero = galaxia_sombrero.replace('Galaxia del Sombrero(M104)',f'{Fore.LIGHTMAGENTA_EX}Galaxia del Sombrero(M104){Style.RESET_ALL}')
        print(galaxia_sombrero)
        print("\n")
        print("Conocida por su apariencia similar a un sombrero, esta galaxia elíptica está a unos 28 millones de años luz de distancia. Contiene un agujero negro supermasivo en su centro")
        print("\n")
        #imagen
        enlace_galaxia_sombrero = "ver foto : https://www.iaa.csic.es/sites/default/files/sombrero_starstream2p.jpg"
        enlace_galaxia_sombrero = enlace_galaxia_sombrero.replace('https://www.iaa.csic.es/sites/default/files/sombrero_starstream2p.jpg',f'{Fore.CYAN}https://www.iaa.csic.es/sites/default/files/sombrero_starstream2p.jpg{Style.RESET_ALL}')
        print(enlace_galaxia_sombrero)
        
        #separacion
        print("\n")
        
        #galaxia de cigarro
        galaxia_cigarro = "5.Galaxia de Cigarro(M82)"
        galaxia_cigarro = galaxia_cigarro.replace('Galaxia de Cigarro(M82)',f'{Fore.LIGHTBLUE_EX}Galaxia de Cigarro(M82){Style.RESET_ALL}')
        print(galaxia_cigarro)
        print("\n")
        print("Es una galaxia irregular con intensa actividad de formación estelar. Su nombre proviene de su forma alargada y su apariencia brillante en longitudes de onda infrarrojas.")
        print("\n")
        #imagen
        enlace_galaxia_cigarro = "ver foto : https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2019/03/16/15527473482186.jpg"
        enlace_galaxia_cigarro = enlace_galaxia_cigarro.replace('https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2019/03/16/15527473482186.jpg',f'{Fore.CYAN}https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2019/03/16/15527473482186.jpg{Style.RESET_ALL}')
        print(enlace_galaxia_cigarro)
        
        #separacion
        print("\n")

        #galaxia del triangulo 
        galaxia_triangulo = "6.Galaxia del triángulo(M33)"
        galaxia_triangulo = galaxia_triangulo.replace('Galaxia del triángulo(M33)',f'{Fore.LIGHTRED_EX}Galaxia del triángulo(M33){Style.RESET_ALL}')
        print(galaxia_triangulo)
        print("\n")
        print("Esta galaxia espiral está a unos 3 millones de años luz de la Tierra y es parte del Grupo Local, al que también pertenecen la Vía Láctea y Andrómeda")
        print("\n")
        #imagen
        enlace_galaxia_triangulo = "ver foto : https://astronomiaparatodos.com/wp-content/uploads/2022/10/m33-01_10_2022-querol_a.jpg"
        enlace_galaxia_triangulo = enlace_galaxia_triangulo.replace('https://astronomiaparatodos.com/wp-content/uploads/2022/10/m33-01_10_2022-querol_a.jpg',f'{Fore.CYAN}https://astronomiaparatodos.com/wp-content/uploads/2022/10/m33-01_10_2022-querol_a.jpg{Style.RESET_ALL}')
        print(enlace_galaxia_triangulo)
        
        #separacion
        print("\n")

        #galaxia del sombrero de copa
        galaxia_sombrero_copa = "7.Galaxia del Sombrero de Copa(NGC 474)"
        galaxia_sombrero_copa = galaxia_sombrero_copa.replace('Galaxia del Sombrero de Copa(NGC 474)',f'{Fore.LIGHTWHITE_EX}Galaxia del Sombrero de Copa(NGC 474){Style.RESET_ALL}')
        print(galaxia_sombrero_copa)
        print("\n")
        print("Ubicada en la constelación de Piscis, esta galaxia elíptica tiene un aspecto peculiar que se asemeja a un sombrero de copa debido a sus regiones exteriores en forma de anillo.")
        print("\n")
        #imagen
        enlace_galaxia_sombrero_copa= "ver foto : https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/NGC_474_Hubble_WikiSky.jpg/1200px-NGC_474_Hubble_WikiSky.jpg"
        enlace_galaxia_sombrero_copa = enlace_galaxia_sombrero_copa.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/NGC_474_Hubble_WikiSky.jpg/1200px-NGC_474_Hubble_WikiSky.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/NGC_474_Hubble_WikiSky.jpg/1200px-NGC_474_Hubble_WikiSky.jpg{Style.RESET_ALL}')
        print(enlace_galaxia_sombrero_copa)
        
        #separacion
        print("\n")
        print("-"*209)
        historias = "Historias"
        historias = historias.replace('Historias',f'{Fore.LIGHTMAGENTA_EX}Historias{Style.RESET_ALL}')
        ancho_historias = 200
        print(historias.center(ancho_historias))
        print("\n")
        
        #apollo 11
        apollo11 = "*Apollo 11 y la llegada a la luna"
        apollo11 = apollo11.replace('*Apollo 11 y la llegada a la luna',f'{Fore.LIGHTRED_EX}*Apollo 11 y la llegada a la luna{Style.RESET_ALL}')
        print(apollo11)
        print("\n")
        print("La misión Apollo 11 fue un hito histórico en la exploración espacial. En julio de 1969, Neil Armstrong se convirtió en el primer ser humano en caminar sobre la luna, seguido por Bluzz Aldrin.")
        print("\n")
        #imagen
        enlace_neil_armstrong = "Neil Armstrong : https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Neil_Armstrong_pose.jpg/1200px-Neil_Armstrong_pose.jpg"
        enlace_neil_armstrong = enlace_neil_armstrong.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Neil_Armstrong_pose.jpg/1200px-Neil_Armstrong_pose.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Neil_Armstrong_pose.jpg/1200px-Neil_Armstrong_pose.jpg{Style.RESET_ALL}')
        print(enlace_neil_armstrong)
        print("\n")
        enlace_buzz_aldrin = "Buzz Aldrin : https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Buzz_Aldrin_%28S69-31743%29.jpg/640px-Buzz_Aldrin_%28S69-31743%29.jpg"
        enlace_buzz_aldrin = enlace_buzz_aldrin.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Buzz_Aldrin_%28S69-31743%29.jpg/640px-Buzz_Aldrin_%28S69-31743%29.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Buzz_Aldrin_%28S69-31743%29.jpg/640px-Buzz_Aldrin_%28S69-31743%29.jpg{Style.RESET_ALL}')
        print(enlace_buzz_aldrin)
        print("\n")
        print("Esta hazaña marcó un momento crucial en la carrera espacial entre Estados Unidos y la Unión Soviética durante la Guerra Fría")
        
        #separacion
        print("\n")

        #Sally Ride
        sally_ride = "Sally Ride, primera mujer en llegar al espacio"
        sally_ride = sally_ride.replace('Sally Ride, primera mujer en llegar al espacio',f'{Fore.RED}Sally Ride, primera mujer en llegar al espacio{Style.RESET_ALL}')
        print(sally_ride)
        print("\n")
        print("En 1983, Sally Ride se convirtió en la primera mujer estadounidense en viajar al espacio a bordo del transbordador espacial Challenger. Su contribución significativa abrió nuevas oportunidades para las mujeres en la exploración espacial.")
        print("\n")
        #imagen
        enlace_sally_ride = "Sally Ride : https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Sally_Ride_in_1984.jpg/1200px-Sally_Ride_in_1984.jpg"
        enlace_sally_ride = enlace_sally_ride.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Sally_Ride_in_1984.jpg/1200px-Sally_Ride_in_1984.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Sally_Ride_in_1984.jpg/1200px-Sally_Ride_in_1984.jpg{Style.RESET_ALL}')
        print(enlace_sally_ride)
        print("\n")
        enlace_challenger = "Challenger : https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/S83-35803_%28cropped%29.jpg/1200px-S83-35803_%28cropped%29.jpg"
        enlace_challenger = enlace_challenger.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/S83-35803_%28cropped%29.jpg/1200px-S83-35803_%28cropped%29.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/S83-35803_%28cropped%29.jpg/1200px-S83-35803_%28cropped%29.jpg{Style.RESET_ALL}')
        print(enlace_challenger)

        #separacion
        print("\n")

        #la tragedia del challenger
        tragredia_challenger = "La tragedia del Challenger"
        tragredia_challenger = tragredia_challenger.replace('La tragedia del Challenger',f'{Fore.LIGHTMAGENTA_EX}La tragedia del Challenger{Style.RESET_ALL}')
        print(tragredia_challenger)
        print("\n")
        print("En 1986, el transbordador espacial Challenger sufrió un trágico accidente poco después de su lanzamiento, causando la muerte de sus siete tripulantes, incluida Christa McAuliffe, quien habría sido la primera maestra en viajar al espacio.")
        print("\n")
        #imagen
        enlace_tragedia_challenger = "Tragedia del Challenger : https://cnnespanol.cnn.com/wp-content/uploads/2021/01/200128114911-01-space-shuttle-challenger-restricted-super-169.jpg?quality=100&strip=info"
        enlace_tragedia_challenger = enlace_tragedia_challenger.replace('https://cnnespanol.cnn.com/wp-content/uploads/2021/01/200128114911-01-space-shuttle-challenger-restricted-super-169.jpg?quality=100&strip=info',f'{Fore.CYAN}https://cnnespanol.cnn.com/wp-content/uploads/2021/01/200128114911-01-space-shuttle-challenger-restricted-super-169.jpg?quality=100&strip=info{Style.RESET_ALL}')
        print(enlace_tragedia_challenger)
        print("\n")
        enlace_christa_mcauliffe = "Christa McAuliffe : https://upload.wikimedia.org/wikipedia/commons/a/aa/ChristaMcAuliffe.jpg"
        enlace_christa_mcauliffe = enlace_christa_mcauliffe.replace('https://upload.wikimedia.org/wikipedia/commons/a/aa/ChristaMcAuliffe.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/a/aa/ChristaMcAuliffe.jpg{Style.RESET_ALL}')
        print(enlace_christa_mcauliffe)
       
        #separacion
        print("\n")

        #Expedicion a la estacion espacial internacional(iss)
        iss = "Expedicion a la Estacion Espacial Internacional(ISS)"
        iss = iss.replace('Expedicion a la Estacion Espacial Internacional(ISS)',f'{Fore.LIGHTYELLOW_EX}Expedicion a la Estacion Espacial Internacional(ISS){Style.RESET_ALL}')
        print(iss)
        print("\n")
        print("La ISS ha sido un proyecto emblemático de cooperación internacional en el espacio. Desde su lanzamiento en 1998, ha albergado a astronautas de diferentes países, realizando investigaciones científicas y experimentos en microgravedad.")
        print("\n")
        enlace_iss = "ISS : https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2010/06/iss2/18901111-1-eng-GB/ISS.jpg"
        enlace_iss = enlace_iss.replace('https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2010/06/iss2/18901111-1-eng-GB/ISS.jpg',f'{Fore.CYAN}https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2010/06/iss2/18901111-1-eng-GB/ISS.jpg{Style.RESET_ALL}')
        print(enlace_iss)

        #separacion
        print("\n")

        #El astronauta Chris Hadfield y su versión de "Space Oddity":
        chris_hadfield = "El astronauta Chris Hadfield y su versión de 'Space Oddity'"
        chris_hadfield = chris_hadfield.replace("El astronauta Chris Hadfield y su versión de 'Space Oddity'",f"{Fore.LIGHTMAGENTA_EX}El astronauta Chris Hadfield y su versión de 'Space Oddity'{Style.RESET_ALL}")
        print(chris_hadfield)
        print("\n")
        print("En 2013, Chris Hadfield, astronauta de la Agencia Espacial Canadiense, grabó una versión de la canción 'Space Oddity' de David Bowie mientras estaba a bordo de la ISS, El video se volvió viral y destacó la vida cotidiana de los astronautas en el espacio.")
        print("\n")
        #imagen y video
        enlace_chris_hadfield = "Chris Hadfield : https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Chris_Hadfield_2011.jpg/1200px-Chris_Hadfield_2011.jpg"
        enlace_chris_hadfield = enlace_chris_hadfield.replace('https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Chris_Hadfield_2011.jpg/1200px-Chris_Hadfield_2011.jpg',f'{Fore.CYAN}https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Chris_Hadfield_2011.jpg/1200px-Chris_Hadfield_2011.jpg{Style.RESET_ALL}')
        print(enlace_chris_hadfield)
        print("\n")
        enlace_space_oddity = "Space Oddity : https://youtu.be/iYYRH4apXDo?si=udmzI1H7fuelRG7S"
        enlace_space_oddity = enlace_space_oddity.replace('https://youtu.be/iYYRH4apXDo?si=udmzI1H7fuelRG7S',f'{Fore.CYAN}https://youtu.be/iYYRH4apXDo?si=udmzI1H7fuelRG7S{Style.RESET_ALL}')
        print(enlace_space_oddity)
        print("\n")
        enlace_video_chris_hadfield = "video grabado : https://youtu.be/KaOC9danxNo?si=7_kG41YMhGy3v9fB"
        enlace_video_chris_hadfield = enlace_video_chris_hadfield.replace('https://youtu.be/KaOC9danxNo?si=7_kG41YMhGy3v9fB',f'{Fore.CYAN}https://youtu.be/KaOC9danxNo?si=7_kG41YMhGy3v9fB{Style.RESET_ALL}')
        print(enlace_video_chris_hadfield)

        #separacion
        print("\n")
        #separacion
        print("\n")
        console.print(figlet.renderText("beta"),style='bold green')

        #Tiempo para que no se cierre de golpe
        while True:
            time.sleep(1231320)
    else:
        console.print(figlet.renderText('error'),style='bold red')
        print("No se pudo iniciar sesión")
        print("Vuelva a intentarlo")
        time.sleep(2)
        print("\n")
        print("El programa se cerrará en 5 segundos")
        time.sleep(0.6)
        #animacion
        for _ in range(5):
            print(".", end="", flush=True)  # Imprime un punto sin saltar de línea
            time.sleep(1)
        break  # Esto detiene el bucle después de un intento fallido de inicio de sesión