# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newpatient.ui'
#
# Created: Mon Jun 15 13:57:41 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(679, 489)
        self.verticalLayout_7 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_11.addWidget(self.label_2)
        self.txtPatientId = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPatientId.sizePolicy().hasHeightForWidth())
        self.txtPatientId.setSizePolicy(sizePolicy)
        self.txtPatientId.setMaximumSize(QtCore.QSize(125, 16777215))
        self.txtPatientId.setObjectName("txtPatientId")
        self.horizontalLayout_11.addWidget(self.txtPatientId)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.txtName = QtGui.QLineEdit(Dialog)
        self.txtName.setObjectName("txtName")
        self.horizontalLayout_2.addWidget(self.txtName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.txtSurname = QtGui.QLineEdit(Dialog)
        self.txtSurname.setObjectName("txtSurname")
        self.horizontalLayout_3.addWidget(self.txtSurname)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.cbxSex = QtGui.QComboBox(Dialog)
        self.cbxSex.setObjectName("cbxSex")
        self.cbxSex.addItem("")
        self.cbxSex.addItem("")
        self.cbxSex.addItem("")
        self.horizontalLayout_4.addWidget(self.cbxSex)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.dateDob = QtGui.QDateEdit(Dialog)
        self.dateDob.setObjectName("dateDob")
        self.horizontalLayout_5.addWidget(self.dateDob)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.txtPhone = QtGui.QLineEdit(Dialog)
        self.txtPhone.setObjectName("txtPhone")
        self.horizontalLayout_6.addWidget(self.txtPhone)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.spnHeight = QtGui.QSpinBox(Dialog)
        self.spnHeight.setObjectName("spnHeight")
        self.horizontalLayout_7.addWidget(self.spnHeight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.spnWeight = QtGui.QDoubleSpinBox(Dialog)
        self.spnWeight.setObjectName("spnWeight")
        self.horizontalLayout_8.addWidget(self.spnWeight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.txtBmi = QtGui.QLineEdit(Dialog)
        self.txtBmi.setObjectName("txtBmi")
        self.horizontalLayout.addWidget(self.txtBmi)
        self.btnCalculateBmi = QtGui.QPushButton(Dialog)
        self.btnCalculateBmi.setObjectName("btnCalculateBmi")
        self.horizontalLayout.addWidget(self.btnCalculateBmi)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.spnEpsworth = QtGui.QSpinBox(Dialog)
        self.spnEpsworth.setObjectName("spnEpsworth")
        self.horizontalLayout_10.addWidget(self.spnEpsworth)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.txtBriefAssessment = QtGui.QTextEdit(Dialog)
        self.txtBriefAssessment.setObjectName("txtBriefAssessment")
        self.verticalLayout_2.addWidget(self.txtBriefAssessment)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_13.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.btnSave = QtGui.QPushButton(Dialog)
        self.btnSave.setObjectName("btnSave")
        self.verticalLayout_6.addWidget(self.btnSave)
        self.btnSaveAddNew = QtGui.QPushButton(Dialog)
        self.btnSaveAddNew.setObjectName("btnSaveAddNew")
        self.verticalLayout_6.addWidget(self.btnSaveAddNew)
        self.btnReset = QtGui.QPushButton(Dialog)
        self.btnReset.setObjectName("btnReset")
        self.verticalLayout_6.addWidget(self.btnReset)
        self.btnCancel = QtGui.QPushButton(Dialog)
        self.btnCancel.setObjectName("btnCancel")
        self.verticalLayout_6.addWidget(self.btnCancel)
        self.horizontalLayout_13.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.label_2.setBuddy(self.txtPatientId)
        self.label_3.setBuddy(self.txtName)
        self.label_4.setBuddy(self.txtSurname)
        self.label_5.setBuddy(self.cbxSex)
        self.label_6.setBuddy(self.dateDob)
        self.label_7.setBuddy(self.txtPhone)
        self.label_8.setBuddy(self.spnHeight)
        self.label_9.setBuddy(self.spnWeight)
        self.label_10.setBuddy(self.txtBmi)
        self.label_11.setBuddy(self.spnEpsworth)
        self.label_12.setBuddy(self.txtBriefAssessment)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.txtPatientId, self.txtName)
        Dialog.setTabOrder(self.txtName, self.txtSurname)
        Dialog.setTabOrder(self.txtSurname, self.cbxSex)
        Dialog.setTabOrder(self.cbxSex, self.dateDob)
        Dialog.setTabOrder(self.dateDob, self.txtPhone)
        Dialog.setTabOrder(self.txtPhone, self.spnHeight)
        Dialog.setTabOrder(self.spnHeight, self.spnWeight)
        Dialog.setTabOrder(self.spnWeight, self.txtBmi)
        Dialog.setTabOrder(self.txtBmi, self.btnCalculateBmi)
        Dialog.setTabOrder(self.btnCalculateBmi, self.spnEpsworth)
        Dialog.setTabOrder(self.spnEpsworth, self.txtBriefAssessment)
        Dialog.setTabOrder(self.txtBriefAssessment, self.btnSave)
        Dialog.setTabOrder(self.btnSave, self.btnSaveAddNew)
        Dialog.setTabOrder(self.btnSaveAddNew, self.btnReset)
        Dialog.setTabOrder(self.btnReset, self.btnCancel)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Add a new patient record</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Patient ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Surname:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Sex:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxSex.setItemText(0, QtGui.QApplication.translate("Dialog", " ", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxSex.setItemText(1, QtGui.QApplication.translate("Dialog", "Male", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxSex.setItemText(2, QtGui.QApplication.translate("Dialog", "Female", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Date of Birth:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Phone:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Height (cm):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Weight (kg):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "BMI:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCalculateBmi.setText(QtGui.QApplication.translate("Dialog", "Calculate BMI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "Epsworth Scale:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog", "Brief Assessment:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("Dialog", "Save Record", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSaveAddNew.setText(QtGui.QApplication.translate("Dialog", "Save && Add New", None, QtGui.QApplication.UnicodeUTF8))
        self.btnReset.setText(QtGui.QApplication.translate("Dialog", "Reset Fields", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

