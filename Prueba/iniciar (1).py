import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QWidget, QPushButton, QMessageBox,QMainWindow
from PyQt5.uic import loadUi
class login(QDialog):
    def __init__(self):
        super(login,self).__init__()
        loadUi("login.ui",self)
        self.boton_iniciar.clicked.connect(self.loginfuncion)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.crearcuenta.clicked.connect(self.gotcreate)
    def loginfuncion(self):
        email=self.email.text()
        password=self.password.text()
        datos_user = open("datos.txt", "r")
        lineas=datos_user.readlines()
        lineas=diccionario(lineas)
        datos_user.close()
        global nombre
        nombre=email
        if lineas[email]==password:
            print("Usuario Correcto: ",email,"y contraseña",password)
            registro = open(f"{email}", "a")
            registro.write(f"{email}")
            registro.close
            c=inicio()
            widget.addWidget(c)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            c=error()
            a.addWidget(c)
            a.setCurrentIndex(widget.currentIndex() + 1)
    def gotcreate(self):
        create=CreateAcc()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)
class inicio(QDialog):
    def __init__(self):
        super(inicio,self).__init__()
        loadUi("postlogin.ui",self)
        self.bienvenido.setText(f"Bienvenido {nombre}")
        self.boton_nuevo.clicked.connect(self.menue)
    def menue(self):
        menu=menuh()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+ 1)
class menuh(QDialog):
    def __init__(self):
        super(menuh,self).__init__()
        loadUi("hortalizas_menu.ui",self)
        self.boton_zana.clicked.connect(self.zanahoriae)
        self.boton_tomate.clicked.connect(self.tomatee)
        self.boton_pimiento.clicked.connect(self.pimientoe)
        self.boton_espinaca.clicked.connect(self.espianacae)
        self.boton_atras.clicked.connect(self.atras)

    def espianacae(self):
        espinaca = espinacas()
        widget.addWidget(espinaca)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def tomatee(self):
        tomate = tomates()
        widget.addWidget(tomate)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def pimientoe(self):
        pimiento = pimientos()
        widget.addWidget(pimiento)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def zanahoriae(self):
        zanahoria = zanahorias()
        widget.addWidget(zanahoria)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def atras(self):
        log=inicio()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)
class tomates(QDialog):
     def __init__(self):
        super(tomates, self).__init__()
        loadUi("Tomate inicio.ui", self)
        self.boton_cultivar.clicked.connect(self.cultivot)
        self.boton_jardineria.clicked.connect(self.jardint)
        self.boton_atras.clicked.connect(self.atras)
     def atras(self):
        log=menuh()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)
     def jardint(self):
         log = jardinto()
         widget.addWidget(log)
         widget.setCurrentIndex(widget.currentIndex() + 1)

     def cultivot(self):
         log = cultivoto()
         widget.addWidget(log)
         widget.setCurrentIndex(widget.currentIndex() + 1)
class jardinto(QDialog):
    def __init__(self):
        super(jardinto,self).__init__()
        loadUi("Jardin tomates.ui",self)
        self.boton_atras.clicked.connect(self.atras)
    def atras(self):
        log=tomates()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)
class cultivoto(QDialog):
    def __init__(self):
        super(cultivoto,self).__init__()
        loadUi("cultivar tomates.ui",self)
        self.boton_atras.clicked.connect(self.atras)
    def atras(self):
        log=tomates()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)
class zanahorias(QDialog):
    def __init__(self):
        super(zanahorias, self).__init__()
        loadUi("Zanahoria inicio.ui", self)
        self.boton_atras.clicked.connect(self.atras)
        self.botonJ.clicked.connect(self.jardinz)
        self.botonC.clicked.connect(self.cultivoz)
    def atras(self):
        log = menuh()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def jardinz(self):
        log = jardinza()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def cultivoz(self):
        log = cultivoza()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex() + 1)
class jardinza(QDialog):
    def __init__(self):
        super(jardinza,self).__init__()
        loadUi("Jardineria zanahoria.ui",self)
        self.boton_atras.clicked.connect(self.atras)
    def atras(self):
        log=zanahorias()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)
class cultivoza(QDialog):
    def __init__(self):
        super(cultivoza,self).__init__()
        loadUi("Cultivar zanahoria.ui",self)
        self.boton_atras.clicked.connect(self.atras)
    def atras(self):
        log=zanahorias()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)
class pimientos(QDialog):
    def __init__(self):
        super(pimientos, self).__init__()
        loadUi("Pimientos inicio.ui", self)
        self.boton_atras.clicked.connect(self.atras)
        self.pimiento_cultivar.clicked.connect(self.cultivop)
        self.pimiento_jardin.clicked.connect(self.jardinp)
    def atras(self):
        log = menuh()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def jardinp(self):
        log = jardinpi()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def cultivop(self):
        log = cultivopi()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex() + 1)
class jardinpi(QDialog):
    def __init__(self):
        super(jardinpi,self).__init__()
        loadUi("jardin pimiento.ui",self)
        self.boton_atras.clicked.connect(self.atras)
    def atras(self):
        log=pimientos()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)
class cultivopi(QDialog):
    def __init__(self):
        super(cultivopi,self).__init__()
        loadUi("cultivar pimientos.ui",self)
        self.boton_atras.clicked.connect(self.atras)
    def atras(self):
        log=pimientos()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)
class espinacas(QDialog):
    def __init__(self):
        super(espinacas, self).__init__()
        loadUi("Espinaca inicio.ui", self)
        self.espinaca_jardin.clicked.connect(self.jardine)
        self.cultivar_cultivar.clicked.connect(self.jardine)
        self.boton_atras.clicked.connect(self.atras)
    def atras(self):
        log = menuh()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def jardine(self):
        log = jardines()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def cultivoe(self):
        log = cultivoes()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex() + 1)
class jardines(QDialog):
    def __init__(self):
        super(jardines,self).__init__()
        loadUi("jardin espinaca.ui",self)
        self.boton_atras.clicked.connect(self.atras)
    def atras(self):
        log=espinacas()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)
class cultivoes(QDialog):
    def __init__(self):
        super(cultivoes,self).__init__()
        loadUi("cultivar espinaca.ui",self)
        self.boton_atras.clicked.connect(self.atras)
    def atras(self):
        log=espinacas()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)
class error(QMessageBox):
    def __init__(self):
        super(error,self).__init__()
        loadUi("mensaje0.ui",self)
class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("registrar.ui",self)
        self.boton_iniciar.clicked.connect(self.createfuncion)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)
    def createfuncion(self):
        email=self.email.text()
        if self.password.text()==self.password_2.text():
            password=self.password.text()
            print("Cuenta creada correctamente con usuario",email,"y contraseña",password)
            datos_user = open("datos.txt", "a")
            datos_user.write(f"{email}:{password}\n")
            datos_user.close()
            log=login()
            widget.addWidget(log)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            print("Cuenta creada correctamente con usuario", email, "y contraseña", )
def diccionario(lineas):
    lista=[]
    for i in lineas:
        users=i.split(":")
        lista.append([users[0],users[1][:-1]])
    dic={}
    for i in lista:
        dic[i[0]]=i[1]
    return  dic
app=QApplication(sys.argv)
mainwindow=login()
a=QtWidgets.QStackedWidget()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec()

