# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_W_p1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1268, 588)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Map_sat = QtGui.QWidget(self.centralwidget)
        self.Map_sat.setGeometry(QtCore.QRect(0, 0, 751, 491))
        self.Map_sat.setObjectName(_fromUtf8("Map_sat"))
        self.PB_nex = QtGui.QPushButton(self.centralwidget)
        self.PB_nex.setGeometry(QtCore.QRect(780, 329, 151, 27))
        self.PB_nex.setObjectName(_fromUtf8("PB_nex"))
        self.PB_Ruta = QtGui.QPushButton(self.centralwidget)
        self.PB_Ruta.setGeometry(QtCore.QRect(940, 329, 111, 27))
        self.PB_Ruta.setObjectName(_fromUtf8("PB_Ruta"))
        self.PB_Tabla = QtGui.QPushButton(self.centralwidget)
        self.PB_Tabla.setGeometry(QtCore.QRect(1080, 329, 131, 27))
        self.PB_Tabla.setObjectName(_fromUtf8("PB_Tabla"))
        self.W_Ti_data = QtGui.QLabel(self.centralwidget)
        self.W_Ti_data.setGeometry(QtCore.QRect(910, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.W_Ti_data.setFont(font)
        self.W_Ti_data.setWordWrap(False)
        self.W_Ti_data.setObjectName(_fromUtf8("W_Ti_data"))
        self.W_Ti_data_3 = QtGui.QLabel(self.centralwidget)
        self.W_Ti_data_3.setGeometry(QtCore.QRect(780, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.W_Ti_data_3.setFont(font)
        self.W_Ti_data_3.setWordWrap(False)
        self.W_Ti_data_3.setObjectName(_fromUtf8("W_Ti_data_3"))
        self.Sat_tab = QtGui.QWidget(self.centralwidget)
        self.Sat_tab.setGeometry(QtCore.QRect(760, 90, 480, 218))
        self.Sat_tab.setObjectName(_fromUtf8("Sat_tab"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(790, 452, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(790, 508, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Lab_lati = QtGui.QLabel(self.centralwidget)
        self.Lab_lati.setGeometry(QtCore.QRect(910, 396, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Lab_lati.setFont(font)
        self.Lab_lati.setObjectName(_fromUtf8("Lab_lati"))
        self.Lab_long = QtGui.QLabel(self.centralwidget)
        self.Lab_long.setGeometry(QtCore.QRect(910, 424, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Lab_long.setFont(font)
        self.Lab_long.setObjectName(_fromUtf8("Lab_long"))
        self.Lab_al = QtGui.QLabel(self.centralwidget)
        self.Lab_al.setGeometry(QtCore.QRect(910, 480, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Lab_al.setFont(font)
        self.Lab_al.setObjectName(_fromUtf8("Lab_al"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(910, 508, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.Lab_azi = QtGui.QLabel(self.centralwidget)
        self.Lab_azi.setGeometry(QtCore.QRect(910, 452, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Lab_azi.setFont(font)
        self.Lab_azi.setObjectName(_fromUtf8("Lab_azi"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(790, 396, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(790, 424, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(790, 480, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.Lab_sat_name = QtGui.QLabel(self.centralwidget)
        self.Lab_sat_name.setGeometry(QtCore.QRect(790, 370, 231, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Lab_sat_name.setFont(font)
        self.Lab_sat_name.setObjectName(_fromUtf8("Lab_sat_name"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.M_Bar = QtGui.QMenuBar(MainWindow)
        self.M_Bar.setGeometry(QtCore.QRect(0, 0, 1268, 27))
        self.M_Bar.setObjectName(_fromUtf8("M_Bar"))
        self.menuBnb = QtGui.QMenu(self.M_Bar)
        self.menuBnb.setObjectName(_fromUtf8("menuBnb"))
        self.menuAntena = QtGui.QMenu(self.menuBnb)
        self.menuAntena.setObjectName(_fromUtf8("menuAntena"))
        self.menuEdici_n = QtGui.QMenu(self.M_Bar)
        self.menuEdici_n.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.menuEdici_n.setObjectName(_fromUtf8("menuEdici_n"))
        self.menuActualizar = QtGui.QMenu(self.menuEdici_n)
        self.menuActualizar.setObjectName(_fromUtf8("menuActualizar"))
        MainWindow.setMenuBar(self.M_Bar)
        self.actionArchivo = QtGui.QAction(MainWindow)
        self.actionArchivo.setObjectName(_fromUtf8("actionArchivo"))
        self.actionNuevo = QtGui.QAction(MainWindow)
        self.actionNuevo.setObjectName(_fromUtf8("actionNuevo"))
        self.actionRed = QtGui.QAction(MainWindow)
        self.actionRed.setObjectName(_fromUtf8("actionRed"))
        self.actionSatelites = QtGui.QAction(MainWindow)
        self.actionSatelites.setObjectName(_fromUtf8("actionSatelites"))
        self.actionObservador = QtGui.QAction(MainWindow)
        self.actionObservador.setObjectName(_fromUtf8("actionObservador"))
        self.actionReloj = QtGui.QAction(MainWindow)
        self.actionReloj.setObjectName(_fromUtf8("actionReloj"))
        self.actionControl = QtGui.QAction(MainWindow)
        self.actionControl.setObjectName(_fromUtf8("actionControl"))
        self.actionRed_2 = QtGui.QAction(MainWindow)
        self.actionRed_2.setObjectName(_fromUtf8("actionRed_2"))
        self.menuAntena.addAction(self.actionControl)
        self.menuAntena.addAction(self.actionRed_2)
        self.menuBnb.addSeparator()
        self.menuBnb.addSeparator()
        self.menuBnb.addAction(self.actionSatelites)
        self.menuBnb.addAction(self.actionObservador)
        self.menuBnb.addAction(self.menuAntena.menuAction())
        self.menuActualizar.addAction(self.actionRed)
        self.menuEdici_n.addAction(self.menuActualizar.menuAction())
        self.menuEdici_n.addAction(self.actionReloj)
        self.M_Bar.addAction(self.menuBnb.menuAction())
        self.M_Bar.addAction(self.menuEdici_n.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.PB_nex.setText(_translate("MainWindow", "Gráfica de ángulos", None))
        self.PB_Ruta.setText(_translate("MainWindow", "Ruta del satélite", None))
        self.PB_Tabla.setText(_translate("MainWindow", "Tabla de ángulos", None))
        self.W_Ti_data.setText(_translate("MainWindow", "#############", None))
        self.W_Ti_data_3.setText(_translate("MainWindow", "Tiempo(UTC):", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Azimut(°):</p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Distancia(Km):</p></body></html>", None))
        self.Lab_lati.setText(_translate("MainWindow", "TextLabel", None))
        self.Lab_long.setText(_translate("MainWindow", "TextLabel", None))
        self.Lab_al.setText(_translate("MainWindow", "TextLabel", None))
        self.label_11.setText(_translate("MainWindow", "TextLabel", None))
        self.Lab_azi.setText(_translate("MainWindow", "TextLabel", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Latitud(°):</p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Longitud(°):</p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Elevación(°):</p></body></html>", None))
        self.Lab_sat_name.setText(_translate("MainWindow", "TextLabel", None))
        self.menuBnb.setTitle(_translate("MainWindow", "Archivo", None))
        self.menuAntena.setTitle(_translate("MainWindow", "Antena", None))
        self.menuEdici_n.setTitle(_translate("MainWindow", "Edición", None))
        self.menuActualizar.setTitle(_translate("MainWindow", "Actualizar", None))
        self.actionArchivo.setText(_translate("MainWindow", "Abrir", None))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo", None))
        self.actionRed.setText(_translate("MainWindow", "Red ", None))
        self.actionSatelites.setText(_translate("MainWindow", "Satélites", None))
        self.actionObservador.setText(_translate("MainWindow", "Observador", None))
        self.actionReloj.setText(_translate("MainWindow", "Hora", None))
        self.actionReloj.setIconText(_translate("MainWindow", "Reloj", None))
        self.actionReloj.setToolTip(_translate("MainWindow", "Reloj", None))
        self.actionControl.setText(_translate("MainWindow", "PC", None))
        self.actionRed_2.setText(_translate("MainWindow", "Red", None))


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)

        self.setupUi(self)

