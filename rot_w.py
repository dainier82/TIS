# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rot_w.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(520, 300)
        self.SB_az = QtGui.QDoubleSpinBox(Form)
        self.SB_az.setGeometry(QtCore.QRect(40, 80, 71, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SB_az.setFont(font)
        self.SB_az.setMaximum(360.0)
        self.SB_az.setObjectName(_fromUtf8("SB_az"))
        self.SB_el = QtGui.QDoubleSpinBox(Form)
        self.SB_el.setGeometry(QtCore.QRect(230, 80, 71, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SB_el.setFont(font)
        self.SB_el.setObjectName(_fromUtf8("SB_el"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(220, 50, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 130, 201, 28))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(220, 150, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.L_az = QtGui.QLabel(Form)
        self.L_az.setGeometry(QtCore.QRect(20, 180, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.L_az.setFont(font)
        self.L_az.setObjectName(_fromUtf8("L_az"))
        self.L_el = QtGui.QLabel(Form)
        self.L_el.setGeometry(QtCore.QRect(220, 180, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.L_el.setFont(font)
        self.L_el.setObjectName(_fromUtf8("L_el"))
        self.PB_conec = QtGui.QPushButton(Form)
        self.PB_conec.setGeometry(QtCore.QRect(330, 210, 85, 27))
        self.PB_conec.setObjectName(_fromUtf8("PB_conec"))
        self.W_Ti_data_3 = QtGui.QLabel(Form)
        self.W_Ti_data_3.setGeometry(QtCore.QRect(20, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.W_Ti_data_3.setFont(font)
        self.W_Ti_data_3.setWordWrap(False)
        self.W_Ti_data_3.setObjectName(_fromUtf8("W_Ti_data_3"))
        self.W_Ti_data_r = QtGui.QLabel(Form)
        self.W_Ti_data_r.setGeometry(QtCore.QRect(150, 240, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.W_Ti_data_r.setFont(font)
        self.W_Ti_data_r.setWordWrap(False)
        self.W_Ti_data_r.setObjectName(_fromUtf8("W_Ti_data_r"))
        self.CB_sat = QtGui.QComboBox(Form)
        self.CB_sat.setGeometry(QtCore.QRect(360, 170, 131, 31))
        self.CB_sat.setObjectName(_fromUtf8("CB_sat"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(370, 140, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.PB_Set = QtGui.QPushButton(Form)
        self.PB_Set.setGeometry(QtCore.QRect(350, 80, 85, 27))
        self.PB_Set.setObjectName(_fromUtf8("PB_Set"))
        self.PB_close = QtGui.QPushButton(Form)
        self.PB_close.setGeometry(QtCore.QRect(410, 10, 85, 27))
        self.PB_close.setObjectName(_fromUtf8("PB_close"))
        self.PB_desco = QtGui.QPushButton(Form)
        self.PB_desco.setGeometry(QtCore.QRect(420, 210, 85, 27))
        self.PB_desco.setObjectName(_fromUtf8("PB_desco"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">Azimut</p></body></html>", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\">Elevación</p></body></html>", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\">Posición en la antena</p></body></html>", None))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\">Azimut</p></body></html>", None))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\">Elevación</p></body></html>", None))
        self.L_az.setText(_translate("Form", "<html><head/><body><p align=\"center\">#####</p></body></html>", None))
        self.L_el.setText(_translate("Form", "<html><head/><body><p align=\"center\">####</p></body></html>", None))
        self.PB_conec.setText(_translate("Form", "Conectar", None))
        self.W_Ti_data_3.setText(_translate("Form", "Tiempo(UTC):", None))
        self.W_Ti_data_r.setText(_translate("Form", "#############", None))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\">Satélite</p></body></html>", None))
        self.PB_Set.setText(_translate("Form", "Ajustar", None))
        self.PB_close.setText(_translate("Form", "Cerrar", None))
        self.PB_desco.setText(_translate("Form", "Desconectar", None))


class Form(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

