import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql



def menu_pantalla():
    """
        la funcion sirve para crear la pantalla inicial
        paran string ():no tiene entrada pero permite ver la pantalla  el registro del usuario
        :return:no retorna
        """
    global pantalla
    pantalla=Tk()
    pantalla.geometry("300x380")
    pantalla.title("Bienvenidos")
    #pantalla.iconbitmap("ICONO.ico")

    #image=PhotoImage(file="ICONO.gif")
    #image=image.subsample(2,2)
    #label=Label(image=image)
    #label.pack()


    Label(text="Acceso al sistema",bg="navy",fg="white",width="300",height="3",font=("calibri",15)).pack()
    Label(text="").pack()

    Button(text="iniciar sesion",height="3", width="30",command=inicio_sesion ).pack()
    Label(text="").pack()

    Button(text="registrar", height="3", width="30",command=registrar).pack()
    Label(text="").pack()

    pantalla.mainloop()

def inicio_sesion():
    """
        la funcion sirve para crear el usuario y contraseña o acceder al mismo si ya esta registrado
        paran string ():no tiene entrada
        :return: no retorna
        """
    global pantalla1
    pantalla1= Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de sesion")
    #pantalla1.iconbitmap("ICONO.ico")

    Label(pantalla1,text="Por favor ingrese su usuario y contraseña\n a continuacion",bg="navy",fg="white",width="300",height="3",font=("calibri",16)).pack()
    Label(pantalla1,text="").pack()

    global nombreusuario_verify
    global contraseñausuario_verify

    nombreusuario_verify= StringVar()
    contraseñausuario_verify= StringVar()

    global nombreusuario_entry
    global contraseñausuario_entry

    Label(pantalla1, text="Usuario").pack()
    nombreusuario_entry=Entry(pantalla1, textvariable=nombreusuario_verify)
    nombreusuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contraseñausuario_entry = Entry(pantalla1,show="*", textvariable=contraseñausuario_verify)
    contraseñausuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1,text="Iniciar sesion",command=validacion_datos).pack()

def registrar():
    """
            la funcion sirve para decirle al usuario la opcion de regitro
            paran string ():no tiene entrada
            :return: no retorna
            """
    global pantalla2
    pantalla2=Toplevel(pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("Registro")
    #pantalla2.iconbitmap("ICONO.ico")

    global nombreusuario_entry
    global contrasena_entry

    nombreusuario_entry=StringVar()
    contrasena_entry=StringVar()

    Label(pantalla2, text="Por favor ingrese un Usuario y Contraseña,\n para el registro al sistema",bg="navy",fg="white",width="300",height="3",font=("calibri",16))
    Label(pantalla2,text="").pack()

    Label(pantalla2, text="Usuario").pack()
    nombreusuario_entry = Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Contraseña").pack()
    contrasena_entry = Entry(pantalla2,show="*")
    contrasena_entry.pack()
    Label(pantalla2).pack()

    Button(pantalla2, text="Registrar", command=insertardatos).pack()

def insertardatos():
    """
            la funcion sirve para validar si el usuario tuvo un registro exitoso o no
            paran string ():no tiene entrada
            :return: fcursor
            """
    bd=pymysql.connect (
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
        )
    fcursor=bd.cursor()

    sql="INSERT INTO login (usuario, contrasena) VALUES ('{0}', '{1}')".format(nombreusuario_entry.get(), contrasena_entry.get())
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")

    except:
        bd.rollback()
        messagebox.showinfo(message="No registrado",title="Aviso")
    bd.close()
def validacion_datos():
    """
                la funcion sirve para validar si el usuario logra o no iniciar sesion
                paran string ():no tiene entrada
                :return: fcursor
                """
    bd = pymysql.connect (
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
        )

    fcursor=bd.cursor()

    fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+nombreusuario_verify.get()+"' and contrasena='"+contraseñausuario_verify.get()+"'")
    if fcursor.fetchall():
        messagebox.showinfo(title="Inicio de sesion Correcto",message="Usuario y/o contraseña correcta")
        intro_preguntas()
        pantalla1.withdraw()
    else:
        messagebox.showinfo(title="Inicio de sesion Incorrecto",message="Usuario y/o contraseña incorrecta")
    return fcursor
    bd.close()


def intro_preguntas():
    """
                la funcion sirve para preguntarle al usuario que quiere realzar en el primer paso
                paran string ():no tiene entrada
                :return: no retorno
                """

    preg_intro = tk.Toplevel()
    preg_intro.geometry('500x500')
    preg_intro.title("Nombre Proyecto")

    titulo_pestaña2 = tk.Label(preg_intro, text="Bienvenid@", font=('Arial bold', 20))
    titulo_pestaña2.grid(column=0, row=0, padx=50, pady=10)

    contenido_2 = tk.Label(preg_intro, text="Por favor selccione cual es su inquietud", font=('Arial bold', 10))
    contenido_2.grid(column=0, row=1, pady=10)

    pregunta1_intro = tk.Label(preg_intro, text="¿Desea aprender a sembrar?", font=('Arial bold', 10))
    pregunta1_intro.grid(column=0, row=2, pady=10)

    boton_preg1_intro = tk.Button(preg_intro,
                                  command=lambda: intro_2preguntas(
                                      preg_intro),
                                  text='SI',
                                  bg="green",
                                  fg="white")
    boton_preg1_intro.grid(column=1, row=2, padx=5)

    pregunta2_intro = tk.Label(preg_intro, text="""¿Tiene una planta sembrada por ud
    y no sabe si asi deberia crecer?""", font=('Arial bold', 10))
    pregunta2_intro.grid(column=0, row=3, pady=10)

    boton_preg2_intro = tk.Button(preg_intro,
                                  command=lambda: intro_2preguntas(
                                      preg_intro),
                                  text='SI',
                                  bg="green",
                                  fg="white")
    boton_preg2_intro.grid(column=1, row=3, padx=5)

    boton2 = tk.Button(preg_intro,
                       text='SALIR',
                       fg="red",
                       command=preg_intro.destroy)
    boton2.grid(column=0, row=4)


def intro_2preguntas(preg_intro):
    """
                    la funcion sirve para saber el interes del usuario  en horticultura o la jardineria o si su planta es comestible
                    paran string (): entrada preg_intro
                    :return: no retorno
                    """
    preg_intro.withdraw()
    preg_2intro = tk.Toplevel()
    preg_2intro.geometry('500x500')
    preg_2intro.title("Nombre Proyecto")

    titulo_pestaña3 = tk.Label(preg_2intro, text="¿Que desea?", font=('Arial bold', 20))
    titulo_pestaña3.grid(column=0, row=0, padx=50, pady=10)

    pregunta1_intro2 = tk.Label(preg_2intro, text="¿Su planta es comentible?", font=('Arial bold', 10))
    pregunta1_intro2.grid(column=0, row=1, pady=10)

    boton_preg1_intro2 = tk.Button(preg_2intro,
                                   command=lambda: solucion_comida(
                                       preg_2intro),
                                   text='SI',
                                   bg="green",
                                   fg="white")
    boton_preg1_intro2.grid(column=1, row=1, padx=5)

    pregunta2_intro2 = tk.Label(preg_2intro, text="¿Su objetivo es la horticultura o la jardineria?",
                                font=('Arial bold', 10))
    pregunta2_intro2.grid(column=0, row=2, pady=10)

    boton_preg2_intro2 = tk.Button(preg_2intro,
                                   command=lambda: solucion_jardineria(
                                       preg_2intro),
                                   text='SI',
                                   bg="green",
                                   fg="white")
    boton_preg2_intro2.grid(column=1, row=2, padx=5)


def solucion_jardineria(preg_2intro):
    """
                        la funcion sirve para saber si el usuario escoje horticultura
                        paran string ():entrada preg_2intro
                        :return: no retorno
                        """
    preg_2intro.withdraw()
    jardineria = tk.Toplevel()
    jardineria.geometry('500x500')
    jardineria.title("Nombre Proyecto")

    texto_jardineria = tk.Label(jardineria, text="Jardineria:", font=('Arial bold', 20))
    texto_jardineria.grid(column=0, row=0, pady=10)

    boton1_jardineria = tk.Button(jardineria,
                                  command=lambda: q_es_jardineria(),
                                  text='¿Que es jardineria?',
                                  bg="blue",
                                  fg="white")
    boton1_jardineria.grid(column=0, row=1, pady=5)

    boton2_jardineria = tk.Button(jardineria,
                                  command=lambda: fotos_jardineria(
                                      jardineria),
                                  text='¿Desea ver fotos?',
                                  bg="yellow")
    boton2_jardineria.grid(column=1, row=1, padx=10)

    texto_horilcultura = tk.Label(jardineria, text="Horilcultura:", font=('Arial bold', 20))
    texto_horilcultura.grid(column=0, row=2, pady=10)

    boton1_horilcultura = tk.Button(jardineria,
                                    command=lambda: q_es_horticultura(),
                                    text='¿Que es horicutura?',
                                    bg="blue",
                                    fg="white")
    boton1_horilcultura.grid(column=0, row=3, pady=5)

    boton2_horilcultura = tk.Button(jardineria,
                                    command=lambda: fotos_hortilcultura(
                                        jardineria),
                                    text='¿Desea ver fotos?',
                                    bg="yellow")
    boton2_horilcultura.grid(column=1, row=3, padx=10)


def solucion_comida(preg_2intro):
    def solucion_comida(preg_2intro):
        """
            la funcion sirve para saber el interes del usuario  en el caso en que escoja ¿que desea sembrar? se le daran todas las opciones para que escoja
                              paran string ():entrada preg_2intro
                              :return: no retorno
                              """
        preg_2intro.withdraw()
        cultivar = tk.Toplevel()
        cultivar.geometry('500x500')
        cultivar.title("Nombre Proyecto")

        texto_comida = tk.Label(cultivar, text="¿Que desea sembrar?", font=('Arial bold', 20))
        texto_comida.grid(column=0, row=0, pady=10)

        opcion1 = tk.Button(cultivar,
                            command=lambda: tomates(),
                            text="Tomates",
                            bg="tomato",
                            fg="white")
        opcion1.grid(column=0, row=1, pady=5)

        opcion2 = tk.Button(cultivar,
                            command=lambda: zanahorias(),
                            text="Zanahorias",
                            bg="orange",
                            fg="white")
        opcion2.grid(column=0, row=2, pady=5)

        opcion3 = tk.Button(cultivar,
                            command=lambda: pimientos(),
                            text="Pimientos",
                            bg="firebrick4",
                            fg="white")
        opcion3.grid(column=0, row=3, pady=5)

        opcion4 = tk.Button(cultivar,
                            command=lambda: espinacas(),
                            text="Espinacas",
                            bg="green4",
                            fg="white")
        opcion4.grid(column=0, row=4, pady=5)


def q_es_jardineria():
    """
                            la funcion sirve para que el usuario sepa que es la jardineria
                            paran string (): no tiene entrada
                            :return: no retorno
                            """
    definicion_jardineria = tk.Toplevel()
    definicion_jardineria.geometry('500x500')
    definicion_jardineria.title("Nombre Proyecto")

    titulo_jardineria = tk.Label(definicion_jardineria, text="Jardineria", font=('Arial bold', 20))
    titulo_jardineria.grid(column=0, row=0, pady=20)

    texto_definicion = tk.Label(definicion_jardineria, text="""  La jardinería es el arte y la práctica de cultivar los jardines. Consiste en cultivar, 
    tanto en un espacio abierto como cerrado, flores, árboles, hortalizas, o verduras, 
    ya sea por estética, por gusto o para la alimentación, y en cuya consecución el 
    objetivo económico es algo secundario""", font=('Arial bold', 10))
    texto_definicion.grid(column=0, row=1)


def q_es_horticultura():
    """
     la funcion sirve para que el usuario sepa que es la horticultura
     paran string (): no tiene entrada
     :return: no retorno
     """
    definicion_horticultura = tk.Toplevel()
    definicion_horticultura.geometry('500x500')
    definicion_horticultura.title("Nombre Proyecto")

    titulo_horticultura = tk.Label(definicion_horticultura, text="Horicultura", font=('Arial bold', 20))
    titulo_horticultura.grid(column=0, row=0, pady=20)

    texto_horticultura = tk.Label(definicion_horticultura, text="""  La horticultura es la ciencia, la tecnología y los negocios envueltos en la producción 
    de hortalizas con destino al consumo. La horticultura es la técnica del cultivo de 
    plantas que se desarrollan en huertos. El término proviene etimológicamente de 
    las palabras latinas hortus y cultura, es decir ‘cultivo en huertas’.""", font=('Arial bold', 10))
    texto_horticultura.grid(column=0, row=1)


def tomates():
    """
    la funcion sirve para que el usuario sepa dentro de las opciones sobre el tomate
    paran string (): no tiene entrada
    :return: no retorno
    """
    tomate = tk.Toplevel()
    tomate.geometry('500x500')
    tomate.title("Tomates")

    texto_tomates = tk.Label(tomate, text="Tomates: ", fg="tomato", font=('Arial bold', 20))
    texto_tomates.grid(column=0, row=0, pady=10)

    tomate_pregunta1 = tk.Button(tomate,
                                 command=lambda: tomate_hogar(),
                                 text="¿El fin de su sembrado es decorar su hogar?",
                                 bg="tomato",
                                 fg="white")
    tomate_pregunta1.grid(column=0, row=1, pady=5)

    tomate_pregunta2 = tk.Button(tomate,
                                 command=lambda: tomate_curiosidades(),
                                 text="¿Le gustaría ver curiosidades de la  planta?",
                                 bg="tomato",
                                 fg="white")
    tomate_pregunta2.grid(column=0, row=2, pady=5)

    tomate_pregunta3 = tk.Button(tomate,
                                 command=lambda: tomate_iniciar(),
                                 text="¿como iniciar?",
                                 bg="tomato",
                                 fg="white")
    tomate_pregunta3.grid(column=0, row=3, pady=5)

    tomate_pregunta4 = tk.Button(tomate,
                                 command=lambda: tomate_primera_produccion(),
                                 text="¿cuanto tiempo se estima para la primera producción?",
                                 bg="tomato",
                                 fg="white")
    tomate_pregunta4.grid(column=0, row=4, pady=5)

    tomate_pregunta5 = tk.Button(tomate,
                                 command=lambda: tomate_beneficios(),
                                 text="beneficios y propiedades ",
                                 bg="tomato",
                                 fg="white")
    tomate_pregunta5.grid(column=0, row=5, pady=5)

    tomate_pregunta6 = tk.Button(tomate,
                                 command=lambda: tomate_fotos(),
                                 text="¿Desea ver fotos?",
                                 bg="tomato",
                                 fg="white")
    tomate_pregunta6.grid(column=0, row=6, pady=5)


def zanahorias():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre la zanahoria
        paran string (): no tiene entrada
        :return: no retorno
        """
    zanahoria = tk.Toplevel()
    zanahoria.geometry('500x500')
    zanahoria.title("Zanahoria")

    texto_comida = tk.Label(zanahoria, text="Zanahoria: ", fg="orange", font=('Arial bold', 20))
    texto_comida.grid(column=0, row=0, pady=10)

    zanahoria_pregunta1 = tk.Button(zanahoria,
                                    command=lambda: zanahoria_hogar(),
                                    text="¿El fin de su sembrado es decorar su hogar?",
                                    bg="orange",
                                    fg="white")
    zanahoria_pregunta1.grid(column=0, row=1, pady=5)

    zanahoria_pregunta2 = tk.Button(zanahoria,
                                    command=lambda: zanahoria_curiosidades(),
                                    text="¿Le gustaría ver curiosidades de la  planta?",
                                    bg="orange",
                                    fg="white")
    zanahoria_pregunta2.grid(column=0, row=2, pady=5)

    zanahoria_pregunta3 = tk.Button(zanahoria,
                                    command=lambda: zanahoria_iniciar(),
                                    text="¿como iniciar?",
                                    bg="orange",
                                    fg="white")
    zanahoria_pregunta3.grid(column=0, row=3, pady=5)

    zanahoria_pregunta4 = tk.Button(zanahoria,
                                    command=lambda: zanahoria_primera_produccion(),
                                    text="¿cuanto tiempo se estima para la primera producción?",
                                    bg="orange",
                                    fg="white")
    zanahoria_pregunta4.grid(column=0, row=4, pady=5)

    zanahoria_pregunta5 = tk.Button(zanahoria,
                                    command=lambda: zanahoria_beneficios(),
                                    text="beneficios y propiedades ",
                                    bg="orange",
                                    fg="white")
    zanahoria_pregunta5.grid(column=0, row=5, pady=5)

    zanahoria_pregunta6 = tk.Button(zanahoria,
                                    command=lambda: zanahoria_fotos(),
                                    text="¿Desea ver fotos?",
                                    bg="orange",
                                    fg="white")
    zanahoria_pregunta6.grid(column=0, row=6, pady=5)


def pimientos():
    """
    la funcion sirve para que el usuario sepa dentro de las opciones sobre los pimientos
    paran string (): no tiene entrada
    :return: no retorno
    """
    pimiento = tk.Toplevel()
    pimiento.geometry('500x500')
    pimiento.title("Pimiento")

    texto_pimiento = tk.Label(pimiento, text="Pimiento: ", fg="firebrick4", font=('Arial bold', 20))
    texto_pimiento.grid(column=0, row=0, pady=10)

    pimiento_pregunta1 = tk.Button(pimiento,
                                   command=lambda: pimiento_hogar(),
                                   text="¿El fin de su sembrado es decorar su hogar?",
                                   bg="firebrick4",
                                   fg="white")
    pimiento_pregunta1.grid(column=0, row=1, pady=5)

    pimiento_pregunta2 = tk.Button(pimiento,
                                   command=lambda: pimiento_curiosidades(),
                                   text="¿Le gustaría ver curiosidades de la  planta?",
                                   bg="firebrick4",
                                   fg="white")
    pimiento_pregunta2.grid(column=0, row=2, pady=5)

    pimiento_pregunta3 = tk.Button(pimiento,
                                   command=lambda: pimiento_iniciar(),
                                   text="¿como iniciar?",
                                   bg="firebrick4",
                                   fg="white")
    pimiento_pregunta3.grid(column=0, row=3, pady=5)

    pimiento_pregunta4 = tk.Button(pimiento,
                                   command=lambda: pimiento_primera_produccion(),
                                   text="¿cuanto tiempo se estima para la primera producción?",
                                   bg="firebrick4",
                                   fg="white")
    pimiento_pregunta4.grid(column=0, row=4, pady=5)

    pimiento_pregunta5 = tk.Button(pimiento,
                                   command=lambda: pimiento_beneficios(),
                                   text="beneficios y propiedades ",
                                   bg="firebrick4",
                                   fg="white")
    pimiento_pregunta5.grid(column=0, row=5, pady=5)

    pimiento_pregunta6 = tk.Button(pimiento,
                                   command=lambda: pimiento_fotos(),
                                   text="¿Desea ver fotos?",
                                   bg="firebrick4",
                                   fg="white")
    pimiento_pregunta6.grid(column=0, row=6, pady=5)


def espinacas():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre las espinacas
        paran string (): no tiene entrada
        :return: no retorno
        """
    espinaca = tk.Toplevel()
    espinaca.geometry('500x500')
    espinaca.title("Espinaca")

    texto_espinaca = tk.Label(espinaca, text="Espinaca: ", fg="green4", font=('Arial bold', 20))
    texto_espinaca.grid(column=0, row=0, pady=10)

    espinaca_pregunta1 = tk.Button(espinaca,
                                   command=lambda: espinaca_hogar(),
                                   text="¿El fin de su sembrado es decorar su hogar?",
                                   bg="green4",
                                   fg="white")
    espinaca_pregunta1.grid(column=0, row=1, pady=5)

    espinaca_pregunta2 = tk.Button(espinaca,
                                   command=lambda: espinaca_curiosidades(),
                                   text="¿Le gustaría ver curiosidades de la  planta?",
                                   bg="green4",
                                   fg="white")
    espinaca_pregunta2.grid(column=0, row=2, pady=5)

    espinaca_pregunta3 = tk.Button(espinaca,
                                   command=lambda: espinaca_iniciar(),
                                   text="¿como iniciar?",
                                   bg="green4",
                                   fg="white")
    espinaca_pregunta3.grid(column=0, row=3, pady=5)

    espinaca_pregunta4 = tk.Button(espinaca,
                                   command=lambda: espinaca_primera_produccion(),
                                   text="¿cuanto tiempo se estima para la primera producción?",
                                   bg="green4",
                                   fg="white")
    espinaca_pregunta4.grid(column=0, row=4, pady=5)

    espinaca_pregunta5 = tk.Button(espinaca,
                                   command=lambda: espinaca_beneficios(),
                                   text="beneficios y propiedades ",
                                   bg="green4",
                                   fg="white")
    espinaca_pregunta5.grid(column=0, row=5, pady=5)

    espinaca_pregunta6 = tk.Button(espinaca,
                                   command=lambda: espinaca_fotos(),
                                   text="¿Desea ver fotos?",
                                   bg="green4",
                                   fg="white")
    espinaca_pregunta6.grid(column=0, row=6, pady=5)


def tomate_hogar():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre como decorar con  tomate
        paran string (): no tiene entrada
        :return: no retorno
        """
    hogar_tomate = tk.Toplevel()
    hogar_tomate.geometry('500x500')
    hogar_tomate.title("Tomate para decorar")

    texto_hogar_tomate = tk.Label(hogar_tomate, text="!Decora con tomates¡", font=('Arial bold', 20))
    texto_hogar_tomate.grid(column=0, row=0, pady=10)

    contenido_hogar_tomate = tk.Label(hogar_tomate, text="""Si esta es tu finalidad déjame decirte que en cuestión de 2 a 3 semanas ya estarás 
    viendo tus platicas bonitas y con un olor inconfundible, eso si tienes que regar 
    la planta cada dos días o cuando veas la tierra muy seca, ten en cuenta que para 
    este punto la planta no necesitara mucha agua así que no te apresures a echarle 
    demasiada.""", font=('Arial bold', 10))
    contenido_hogar_tomate.grid(column=0, row=1)


def tomate_curiosidades():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre las curiosidades de tomate
        paran string (): no tiene entrada
        :return: no retorno
        """
    curiosidad_tomate = tk.Toplevel()
    curiosidad_tomate.geometry('500x500')
    curiosidad_tomate.title("Curiosidad de Tomates")

    texto_curiosidad_tomate = tk.Label(curiosidad_tomate, text="¿Si sabias que el tomate?", font=('Arial bold', 20))
    texto_curiosidad_tomate.grid(column=0, row=0, pady=10)

    contenido_curiosidad_tomate = tk.Label(curiosidad_tomate, text="""1. No llegó a Europa hasta el siglo XVI de la mano de Hernán Cortés.
    2. Los primeros tomates europeos no eran rojos sino amarillo.
    3. Fue considerado durante mucho tiempo un fruto tóxico.
    4.  Existen más de 10.000 variedades.
    5. Su nombre proviene del azteca.
    6.Es en un 94% agua.
    7.Contiene un potente antioxidante llamado licopeno.""", font=('Arial bold', 10))
    contenido_curiosidad_tomate.grid(column=0, row=1)


def tomate_iniciar():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre como iniciar la plantacion de tomates
        paran string (): no tiene entrada
        :return: no retorno
        """
    iniciar_tomate = tk.Toplevel()
    iniciar_tomate.geometry('500x500')
    iniciar_tomate.title("Iniciar Tomates")

    texto_iniciar_tomate = tk.Label(iniciar_tomate, text="¿Como iniciar?", font=('Arial bold', 20))
    texto_iniciar_tomate.grid(column=0, row=0, pady=10)

    contenido_iniciar_tomate = tk.Label(iniciar_tomate, text="""La semilla de tomate se encuentra en el interior del fruto. Para recolectarlas, 
    se recomienda elegir tomates grandes y maduros; ya que algunas 
    personas creen que existe  un 90% de probabilidad de que los 
    futuros frutos sean de las mismas características. 

    Una vez elegidas, se deben poner en un lugar fresco, seco y 
    alejado de la luz solar durante tres días. Cuando haya pasado 
    el tiempo aconsejado, se almacenan en una bolsa hermética 
    hasta el momento de la siembra.

    Según el siguiente  artículo publicado por el Instituto Nacional 
    de Investigaciones Agropecuarias (INIAP) , se aconseja plantar 
    tomate en suelos arenosos, ya que este se desarrolla con una 
    mayor facilidad en suelos fértiles y drenados.

    La profundidad del terreno no debe ser inferior a 18 pulgadas 
    (45 cm), y se debe lograr que adquiera las condiciones físicas 
    adecuadas: suave, drenado y ventilado. Además, es importante  
    abonarlo con abundante materia orgánica. Asimismo, si quieres 
    cultivar tomate, hazlo en un lugar donde puedas recibir el sol
    mínimo 8 horas diarias. No obstante, recuerda que el verano 
    favorece la aparición de las plagas en el huerto, así que ten 
    precaución para no perder la cosecha.  """, font=('Arial bold', 10))
    contenido_iniciar_tomate.grid(column=0, row=1)


def tomate_primera_produccion():
    """
    la funcion sirve para que el usuario sepa dentro de las opciones sobre la primera produccion de tomate
    paran string (): no tiene entrada
    :return: no retorno
    """
    produccion_tomate = tk.Toplevel()
    produccion_tomate.geometry('500x500')
    produccion_tomate.title("Tomate para producir")

    texto_produccion_tomate = tk.Label(produccion_tomate, text="!Comienza desde ya¡", font=('Arial bold', 20))
    texto_produccion_tomate.grid(column=0, row=0, pady=10)

    contenido_produccion_tomate = tk.Label(produccion_tomate, text="""Aunque el tiempo depende de la variedad de tomate cultivada, 
    la primera  cosecha  suele comenzar unos 65 o 100 días. 
    Se recomienda llevar a cabo la recolección cuando estén "pintones" (ni verdes ni 
    demasiado maduros) para evitar que las plagas se adelanten a la cosecha""", font=('Arial bold', 10))
    contenido_produccion_tomate.grid(column=0, row=1)


def tomate_beneficios():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre los beneficios del tomate
        paran string (): no tiene entrada
        :return: no retorno
        """
    beneficios_tomate = tk.Toplevel()
    beneficios_tomate.geometry('500x500')
    beneficios_tomate.title("Beneficios del tomate")

    texto_beneficios_tomate = tk.Label(beneficios_tomate, text="¿Porque es bueno para ti?", font=('Arial bold', 20))
    texto_beneficios_tomate.grid(column=0, row=0, pady=10)

    contenido_beneficios_tomate = tk.Label(beneficios_tomate, text="""El tomate es rico en vitaminas y minerales : esta hortaliza aporta vitamina
    C, un potente antioxidante natural, además de vitamina A, K, hierro y potasio.

    El tomate protege la vista:  contiene vitamina A, la cual ayuda a proteger 
    nuestros ojos de enfermedades degenerativas o ceguera nocturna. La vitamina 
    A mejora nuestra visión.

    El tomate cuida de tu piel:  al poseer grandes propiedades antioxidantes, 
    es un remedio natural contra el envejecimiento y un gran aliado para el 
    cuidado, no sólo del aspecto de nuestra piel, sino también de nuestro pelo 
    y nuestros dientes. De hecho, muchos componentes relacionados con el 
    cuidado estético, contienen tomate en su composición.

    El tomate evita el estreñimiento:  esto es debido a su contenido en fibra 
    que cuida del tránsito intestinal y evita la aparición de enfermedades 
    que tienen que ver con los órganos gastrointestinales.

    El tomate es un diurético natural : es otra de las propiedades beneficiosas 
    para la salud que posee el tomate y que debemos destacar. El tomate contiene 
    potasio y bajos niveles de sodio, lo que favorece a evitar la retención de 
    líquidos y la eliminación de toxinas.""", font=('Arial bold', 10))
    contenido_beneficios_tomate.grid(column=0, row=1)


def zanahoria_hogar():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre como decorar con zanahoria
        paran string (): no tiene entrada
        :return: no retorno
        """
    hogar_zanahoria = tk.Toplevel()
    hogar_zanahoria.geometry('500x500')
    hogar_zanahoria.title("zanahoria para decorar")

    texto_hogar_zanahoria = tk.Label(hogar_zanahoria, text="!Decora con zanahoria¡", font=('Arial bold', 20))
    texto_hogar_zanahoria.grid(column=0, row=0, pady=10)

    contenido_hogar_zanahoria = tk.Label(hogar_zanahoria, text="""si esta es tu finalidad te recomendamos cortar la parte alta de las zanahorias 
    y sembrarlas, junto con buena tierra y agua, espera un plazo de 3 a 4 semanas y 
    veras tus zanahorias crecer y comenzar  a tomar su forma particular.

    Te recomendamos ver nuestra sección de ¿como iniciar? para mas información. """, font=('Arial bold', 10))
    contenido_hogar_zanahoria.grid(column=0, row=1)


def zanahoria_curiosidades():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre las curiosidades de la zanahoria
        paran string (): no tiene entrada
        :return: no retorno
        """
    curiosidad_zanahoria = tk.Toplevel()
    curiosidad_zanahoria.geometry('500x500')
    curiosidad_zanahoria.title("Curiosidad de zanahorias")

    texto_curiosidad_zanahoria = tk.Label(curiosidad_zanahoria, text="¿Si sabias que las zanahorias?",
                                          font=('Arial bold', 20))
    texto_curiosidad_zanahoria.grid(column=0, row=0, pady=10)

    contenido_curiosidad_zanahoria = tk.Label(curiosidad_zanahoria, text="""1 Las zanahorias empezaron a cultivarse alrededor del año 3,000 a. C, 
    en lo que ahora es Afganistan.

    2 Una zanahoria aporta más de la dosis de vitamina A recomendada que 
    tu cuerpo necesita (este nutrimento ayuda a prevenir la ceguera, las 
    cataratas y otros problemas visuales.

    3 Su color se debe a su alto contenido de betacarotenos y alfacarotenos, 
    pigmentos vegetales que el hígado transforma en vitamina A. Por eso comer 
    zanahoria en exceso puede hacer que la piel, principalmente las palmas 
    de las manos, adquiera un color entre anaranjado y amarillo.

    4 Está compuesta 80% por agua.

    5 La zanahoria pertenece a la misma familia del apio y el perejil (la 
    Apiaceae).

    6 Existen varios tipos de zanahorias y no todas son anaranjadas: ¡hay 
    amarillas rojas y moradas!.""", font=('Arial bold', 10))
    contenido_curiosidad_zanahoria.grid(column=0, row=1)


def zanahoria_iniciar():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre como iniciar la siembra de zanahoria
        paran string (): no tiene entrada
        :return: no retorno
        """
    iniciar_zanahoria = tk.Toplevel()
    iniciar_zanahoria.geometry('500x500')
    iniciar_zanahoria.title("Inicia Zanahoria")

    texto_iniciar_zanahoria = tk.Label(iniciar_zanahoria, text="¿Como iniciar?", font=('Arial bold', 20))
    texto_iniciar_zanahoria.grid(column=0, row=0, pady=10)

    contenido_iniciar_zanahoria = tk.Label(iniciar_zanahoria, text="""Necesitas: 
    1. 5 zanahorias
    2. Un envase o maceta de 30 cm de profundidad y 50 cm de longitud.
    3. Tierra enriquecida con sustrato ecológico (composta)
    4. Abono líquido

    Lo primero que vamos a hacer es tomar las zanahorias y cortar la parte de 
    arriba. Cuando vayas a utilizarlas para cocinar, basta con que te acuerdes 
    de reservar esta parte del inicio del vegetal en lugar de tirarlo a la 
    basura orgánica.

    Colocar los tallos de zanahoria en un recipiente con agua.La idea es que 
    germinen, y lo harán al cabo de unas semanas.

    Una vez hayan germinado, ya podemos proceder a plantarlas en nuestra maceta.

    Recuerda crear un adecuado drenaje en la misma, con pequeñas piedras de 
    gravilla.

    A las zanahorias les gusta el sol, así que no tengas miedo de dejar la 
    maceta en el balcón durante todo el día.

    Puedes regarlas un poco, pero basta con una o dos veces por semana. Recuerda 
    incluir en esta agua unas gotas de abono líquido. De este modo, las 
    zanahorias crecerán fuertes y sanas.""", font=('Arial bold', 10))
    contenido_iniciar_zanahoria.grid(column=0, row=1)


def zanahoria_primera_produccion():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre la primera produccion de zanahoria
        paran string (): no tiene entrada
        :return: no retorno
        """
    produccion_zanahoria = tk.Toplevel()
    produccion_zanahoria.geometry('500x500')
    produccion_zanahoria.title("Producir zanahoria")

    texto_produccion_zanahoria = tk.Label(produccion_zanahoria, text="!Comienza desde ya¡", font=('Arial bold', 20))
    texto_produccion_zanahoria.grid(column=0, row=0, pady=10)

    contenido_produccion_zanahoria = tk.Label(produccion_zanahoria, text="""Hay que señalar que en ocasiones, no tienen la típica forma alargada, sino 
    que pueden salir algo más abombadas y con volúmenes algo caprichosos.

    las zanahorias tardan unos dos meses en formarse.""", font=('Arial bold', 10))
    contenido_produccion_zanahoria.grid(column=0, row=1)


def zanahoria_beneficios():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre los beneficios de la zanahoria
        paran string (): no tiene entrada
        :return: no retorno
        """
    beneficios_zanahoria = tk.Toplevel()
    beneficios_zanahoria.geometry('500x500')
    beneficios_zanahoria.title("Beneficios del zanahoria")

    texto_beneficios_zanahoria = tk.Label(beneficios_zanahoria, text="¿Porque es bueno para ti?",
                                          font=('Arial bold', 20))
    texto_beneficios_zanahoria.grid(column=0, row=0, pady=10)

    contenido_beneficios_zanahoria = tk.Label(beneficios_zanahoria, text="""*Buenas para la dentadura.

    *Indicadas para mejorar problemas intestinales.

    *Diuréticas.

    *Energía para nuestro cerebro.

    *Buenas para la vista.

    *Buenas para las uñas y el cabello.""", font=('Arial bold', 10))
    contenido_beneficios_zanahoria.grid(column=0, row=1)


def pimiento_hogar():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre como decorar con pimientos su hogar
        paran string (): no tiene entrada
        :return: no retorno
        """
    hogar_pimiento = tk.Toplevel()
    hogar_pimiento.geometry('500x500')
    hogar_pimiento.title("pimiento para decorar")

    texto_hogar_pimiento = tk.Label(hogar_pimiento, text="!Decora con pimiento¡", font=('Arial bold', 20))
    texto_hogar_pimiento.grid(column=0, row=0, pady=10)

    contenido_hogar_pimiento = tk.Label(hogar_pimiento, text="""La planta de pimientos cuenta con una forma en las hojas bastante comunes en 
    nuestra cuidad, tiene una hojas grandes y  simétricas perfectas para 
    decorar tu hogar. """, font=('Arial bold', 10))
    contenido_hogar_pimiento.grid(column=0, row=1)


def pimiento_curiosidades():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre las curiosidades del pimiento
        paran string (): no tiene entrada
        :return: no retorno
        """
    curiosidad_pimiento = tk.Toplevel()
    curiosidad_pimiento.geometry('500x500')
    curiosidad_pimiento.title("Curiosidad de pimientos")

    texto_curiosidad_pimiento = tk.Label(curiosidad_pimiento, text="¿Si sabias que los pimientos?",
                                         font=('Arial bold', 20))
    texto_curiosidad_pimiento.grid(column=0, row=0, pady=10)

    contenido_curiosidad_pimiento = tk.Label(curiosidad_pimiento, text="""*Son muy ricos en fibra, y esto hace que el consumo de esta hortaliza 
    ofrezca una sensación de saciedad enorme. Por ello es muy útil en dietas 
    de control de peso.

    *Contribuye a reducir las tasas de colesterol en sangre y al control de 
    la glucemia en personas que padecen diabetes.

    *El pimiento dulce es muy bueno para personas con estómago delicado. Las 
    variedades picantes resultan irritantes y pueden llegar a convertirse 
    en laxantes.

    *La capsaicina es un componente característico en los pimientos picantes 
    y posee un doble efecto: por un lado tiene acción antibiótica natural y 
    por otro son analgésicos pues reducen la disponibilidad del mensajero 
    químico del dolor, llamado sustancia P

    *Los pimientos de color rojo son muy ricos en vitamina C. Contienen más 
    del doble de la que se encuentra en frutas como las naranjas, las 
    fresas o el kiwi.

    *60 gramos de pimientos contienen la cantidad diaria recomendada de 
    vitamina C.""", font=('Arial bold', 10))
    contenido_curiosidad_pimiento.grid(column=0, row=1)


def pimiento_iniciar():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre como iniciar el sembrado de pimiento
        paran string (): no tiene entrada
        :return: no retorno
        """
    iniciar_pimiento = tk.Toplevel()
    iniciar_pimiento.geometry('500x500')
    iniciar_pimiento.title("Inicia pimiento")

    texto_iniciar_pimiento = tk.Label(iniciar_pimiento, text="¿Como iniciar?", font=('Arial bold', 20))
    texto_iniciar_pimiento.grid(column=0, row=0, pady=10)

    contenido_iniciar_pimiento = tk.Label(iniciar_pimiento, text="""¿Cuándo?  Entre Abril y Mayo.

    ¿Dónde ?  Zona que Recibe Mucha Luz Solar. Al menos 7 horas diarias.. 

    ¿Cómo preparamos la tierra?  Removida con motoazada, pH entre 6,5-7. 
    Ideal que haya habido siembra de guisantes anteriormente.

    ¿Cómo abonamos? Son exigentes. Con materia orgánica descompuesta como 
    estiércol, bien removido con la tierra. También humus de lombriz. 
    Utilizar compostera en caso de que tengamos.

    ¿Cada cuánto regamos? Son exigentes con el agua. En verano caluroso, 
    a diario unos 30-40 minutos. En caso contrario cada 2-3 días unos 
    30-40 minutos. Fijarse en las hojas para determinar si necesitan más 
    agua.  

    ¿Cómo sembramos?  Con semilla, enterramos a unos 3mm. Dejamos un 
    espacio de entre semillas de 2,5cm aproximadamente. 

    Con planteles dejamos un poco más de espacio. """, font=('Arial bold', 10))
    contenido_iniciar_pimiento.grid(column=0, row=1)


def pimiento_primera_produccion():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre la primera produccion de pimiento
        paran string (): no tiene entrada
        :return: no retorno
        """
    produccion_pimiento = tk.Toplevel()
    produccion_pimiento.geometry('500x500')
    produccion_pimiento.title("Producir pimiento")

    texto_produccion_pimiento = tk.Label(produccion_pimiento, text="!Comienza desde ya¡", font=('Arial bold', 20))
    texto_produccion_pimiento.grid(column=0, row=0, pady=10)

    contenido_produccion_pimiento = tk.Label(produccion_pimiento, text="""¿Tiempo de cosecha? Unos 30 días desde el plantel o de que la semilla 
    haya germinado.""", font=('Arial bold', 10))
    contenido_produccion_pimiento.grid(column=0, row=1)


def pimiento_beneficios():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre los beneficios del pimiento
        paran string (): no tiene entrada
        :return: no retorno
        """
    beneficios_pimiento = tk.Toplevel()
    beneficios_pimiento.geometry('500x500')
    beneficios_pimiento.title("Beneficios del pimiento")

    texto_beneficios_pimiento = tk.Label(beneficios_pimiento, text="¿Porque es bueno para ti?", font=('Arial bold', 20))
    texto_beneficios_pimiento.grid(column=0, row=0, pady=10)

    contenido_beneficios_pimiento = tk.Label(beneficios_pimiento, text="""Son  ricos en vitamina C, vitamina A,  y además poseen vitamina E, 
    vitaminas B6, B3, B2, B1 y ácido fólico. Entre los minerales que 
    contienen los distintos tipos de pimientos se destacan el potasio 
    en mayor proporción seguido por fósforo y calcio. Tienen una buena 
    cantidad de hidratos de carbono y una gran concentración de 
    carotenos (750 mg / 100 g).""", font=('Arial bold', 10))
    contenido_beneficios_pimiento.grid(column=0, row=1)


def espinaca_hogar():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre como decorar el hogar con espinaca
        paran string (): no tiene entrada
        :return: no retorno
        """
    hogar_espinaca = tk.Toplevel()
    hogar_espinaca.geometry('500x500')
    hogar_espinaca.title("espinaca para decorar")

    texto_hogar_espinaca = tk.Label(hogar_espinaca, text="!Decora con espinaca¡", font=('Arial bold', 20))
    texto_hogar_espinaca.grid(column=0, row=0, pady=10)

    contenido_hogar_espinaca = tk.Label(hogar_espinaca, text="""Las hojas de las espinacas son grandes, redondas y llamativas perfectas para 
    decorar tu hogar en cuestión de dos a tres semanas.   """, font=('Arial bold', 10))
    contenido_hogar_espinaca.grid(column=0, row=1)


def espinaca_curiosidades():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre las curiosidades de la espinaca
        paran string (): no tiene entrada
        :return: no retorno
        """
    curiosidad_espinaca = tk.Toplevel()
    curiosidad_espinaca.geometry('500x500')
    curiosidad_espinaca.title("Curiosidad de pimientos")

    texto_curiosidad_espinaca = tk.Label(curiosidad_espinaca, text="¿Si sabias que las espinacas?",
                                         font=('Arial bold', 20))
    texto_curiosidad_espinaca.grid(column=0, row=0, pady=10)

    contenido_curiosidad_espinaca = tk.Label(curiosidad_espinaca, text="""1. Ayuda a combatir el estrés oxidativo.
    2. Buena para el sistema cardiovascular
    3. Mejora la salud ósea
    4. Previene la diabetes
    5. Contra la anemia
    6. Es buena para la vista
    7. Pérdida de peso
    8. Buena salud gastrointestinal
    9. Previene el envejecimiento prematuro""", font=('Arial bold', 10))
    contenido_curiosidad_espinaca.grid(column=0, row=1)


def espinaca_iniciar():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre como iniciar el sembrado de espinaca
        paran string (): no tiene entrada
        :return: no retorno
        """
    iniciar_espinaca = tk.Toplevel()
    iniciar_espinaca.geometry('500x500')
    iniciar_espinaca.title("Inicia espinaca")

    texto_iniciar_espinaca = tk.Label(iniciar_espinaca, text="¿Como iniciar?", font=('Arial bold', 20))
    texto_iniciar_espinaca.grid(column=0, row=0, pady=10)

    contenido_iniciar_espinaca = tk.Label(iniciar_espinaca, text="""La espinaca es una planta que crece mejor en climas frescos o fríos. Las 
    semillas son esferas irregulares color café claro, entre 2-3mm de diámetro. 
    Antes de sembrar, debemos preparar nuestro semillero con una mezcla nutritiva 
    que tenga buen drenaje. Existen distintas maneras de sembrar las espinacas, 
    siembra directa o en semillero.

    La siembra directa, es en la que se realizan pequeños surcos con una separación
    aproximada de 8-10cm entre ellos y una profundidad aproximada de 1.5cm. Coloca 
    las semillas en los surcos con una distancia de 2-3cm entre semillas. Las plantas 
    crecerán muy cercanas y podremos cosecharlas con tijeras, obteniendo hojas de 
    espinaca “baby” u hojas tiernas, que tienen un sabor más sutil. """, font=('Arial bold', 10))
    contenido_iniciar_espinaca.grid(column=0, row=1)


def espinaca_primera_produccion():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre la primera produccion de espinaca
        paran string (): no tiene entrada
        :return: no retorno
        """
    produccion_espinaca = tk.Toplevel()
    produccion_espinaca.geometry('500x500')
    produccion_espinaca.title("Producir pimiento")

    texto_produccion_espinaca = tk.Label(produccion_espinaca, text="!Comienza desde ya¡", font=('Arial bold', 20))
    texto_produccion_espinaca.grid(column=0, row=0, pady=10)

    contenido_produccion_espinaca = tk.Label(produccion_espinaca, text="""A partir de unas seis semanas después de la siembra, podemos comenzar a 
    cosechar las hojas externas de nuestras espinacas. 

    Es importante observar el crecimiento de nuestras plantas, al principio sólo 
    podremos cosechar algunas hojas, ya que si cosechamos demasiadas tardará en 
    recuperarse y su crecimiento será lento. 

    El mejor momento para la cosecha es durante la mañana, las hojas tienen una 
    mayor concentración de humedad y se conservan mejor. Coloca las hojas en 
    una red o bolsa con orificios y colócalas en el refrigerador. Pueden 
    conservarse frescas hasta por 10 días.""", font=('Arial bold', 10))
    contenido_produccion_espinaca.grid(column=0, row=1)


def espinaca_beneficios():
    """
        la funcion sirve para que el usuario sepa dentro de las opciones sobre los beneficios de la espinaca
        paran string (): no tiene entrada
        :return: no retorno
        """
    beneficios_espinaca = tk.Toplevel()
    beneficios_espinaca.geometry('500x700')
    beneficios_espinaca.title("Beneficios del pimiento")

    texto_beneficios_espinaca = tk.Label(beneficios_espinaca, text="¿Porque es bueno para ti?", font=('Arial bold', 20))
    texto_beneficios_espinaca.grid(column=0, row=0, pady=10)

    contenido_beneficios_espinaca = tk.Label(beneficios_espinaca, text="""PRIOPEDADES NUTRICIONALES""", fg="green4",
                                             font=('Arial bold', 15))
    contenido_beneficios_espinaca.grid(column=0, row=1, pady=10)

    contenido2_beneficios_espinaca = tk.Label(beneficios_espinaca, text="""1. Es rica en fibra, vitamina A, B1, B2, C, K, calcio, fósforo, hierro, 
    ácido fólico, magnesio, zinc y betacarotenos, estos últimos poseen 
    potente actividad antioxidante.""", font=('Arial bold', 10))
    contenido2_beneficios_espinaca.grid(column=0, row=2, pady=5)

    contenido2_beneficios_espinaca = tk.Label(beneficios_espinaca, text="""PRIOPEDADES PARA TU SALUD""", fg="green4",font=('Arial bold', 15))
    contenido2_beneficios_espinaca.grid(column=0, row=3, pady=10)

    contenido2_beneficios_espinaca = tk.Label(beneficios_espinaca, text="""2. Las espinacas son buenísimas en dietas para adelgazar ya que producen 
    saciedad y sólo aportan 16 calorías por cada 100 gramos.

    3. Las espinacas son de los alimentos anticancerígenos más destacados, 
    propiedad atribuida a la importante cantidad de betacarotenos que 
    posee, ya que frena la acción de los radicales libres sobre las células.

    4. Es muy recomendable su consumo durante el embarazo, pues el zinc
    interviene en la formación de los huesos, y el ácido fólico previene 
    defectos en la columna vertebral, malformaciones en el feto, tales 
    como espina bífida y labio leporino.

    5. Favorece el funcionamiento del sistema inmunológico, así como el 
    control de la diabetes pues contiene un antioxidante conocido como 
    ácido alfalipoico, que aumenta la sensibilidad a la insulina.

    6. Las espinacas son altamente recomendadas en caso de padecer anemia 
    debido a su aporte en hierro que mejora la absorción con la vitamina C, 
    también presente en esta verdura.

    7. Contienen luteína y zeaxantina, sustancias que mejoran la visión y 
    previenen la ceguera causada por la degeneración macular.

    8. El consumo de espinacas crudas o cocidas ayuda a disminuir el 
    estreñimiento logrando regular el tránsito intestinal.""", font=('Arial bold', 10))
    contenido2_beneficios_espinaca.grid(column=0, row=4, pady=5)


menu_pantalla()



