# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appointmentview.ui'
#
# Created: Sun Aug  9 21:27:17 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(807, 677)
        self.horizontalLayout_20 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_12.addWidget(self.label_2)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.txtPatientId = QtGui.QLineEdit(Dialog)
        self.txtPatientId.setReadOnly(True)
        self.txtPatientId.setObjectName("txtPatientId")
        self.horizontalLayout_7.addWidget(self.txtPatientId)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.txtPatientName = QtGui.QLineEdit(Dialog)
        self.txtPatientName.setReadOnly(True)
        self.txtPatientName.setObjectName("txtPatientName")
        self.horizontalLayout_8.addWidget(self.txtPatientName)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.txtPatientSurname = QtGui.QLineEdit(Dialog)
        self.txtPatientSurname.setReadOnly(True)
        self.txtPatientSurname.setObjectName("txtPatientSurname")
        self.horizontalLayout_9.addWidget(self.txtPatientSurname)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.txtPatientSex = QtGui.QLineEdit(Dialog)
        self.txtPatientSex.setReadOnly(True)
        self.txtPatientSex.setObjectName("txtPatientSex")
        self.horizontalLayout_10.addWidget(self.txtPatientSex)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.txtPatientDob = QtGui.QLineEdit(Dialog)
        self.txtPatientDob.setReadOnly(True)
        self.txtPatientDob.setObjectName("txtPatientDob")
        self.horizontalLayout_11.addWidget(self.txtPatientDob)
        self.verticalLayout_10.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.txtPatientAssessment = QtGui.QTextBrowser(Dialog)
        self.txtPatientAssessment.setObjectName("txtPatientAssessment")
        self.horizontalLayout_12.addWidget(self.txtPatientAssessment)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_18.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_17.addWidget(self.label_8)
        self.txtPatientPhone = QtGui.QLineEdit(Dialog)
        self.txtPatientPhone.setReadOnly(True)
        self.txtPatientPhone.setObjectName("txtPatientPhone")
        self.horizontalLayout_17.addWidget(self.txtPatientPhone)
        self.verticalLayout_9.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_16.addWidget(self.label_9)
        self.txtPatientHeight = QtGui.QLineEdit(Dialog)
        self.txtPatientHeight.setAutoFillBackground(False)
        self.txtPatientHeight.setReadOnly(True)
        self.txtPatientHeight.setObjectName("txtPatientHeight")
        self.horizontalLayout_16.addWidget(self.txtPatientHeight)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_15.addWidget(self.label_10)
        self.txtPatientWeight = QtGui.QLineEdit(Dialog)
        self.txtPatientWeight.setReadOnly(True)
        self.txtPatientWeight.setObjectName("txtPatientWeight")
        self.horizontalLayout_15.addWidget(self.txtPatientWeight)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_14.addWidget(self.label_11)
        self.txtPatientBmi = QtGui.QLineEdit(Dialog)
        self.txtPatientBmi.setReadOnly(True)
        self.txtPatientBmi.setObjectName("txtPatientBmi")
        self.horizontalLayout_14.addWidget(self.txtPatientBmi)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.txtPatientEpsworth = QtGui.QLineEdit(Dialog)
        self.txtPatientEpsworth.setReadOnly(True)
        self.txtPatientEpsworth.setObjectName("txtPatientEpsworth")
        self.horizontalLayout_13.addWidget(self.txtPatientEpsworth)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_18.addLayout(self.verticalLayout_9)
        self.verticalLayout_11.addLayout(self.horizontalLayout_18)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.line = QtGui.QFrame(Dialog)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_12.addWidget(self.line)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.txtAppointmentDate = QtGui.QLineEdit(Dialog)
        self.txtAppointmentDate.setReadOnly(True)
        self.txtAppointmentDate.setObjectName("txtAppointmentDate")
        self.horizontalLayout_2.addWidget(self.txtAppointmentDate)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.txtAppointmentRegDate = QtGui.QLineEdit(Dialog)
        self.txtAppointmentRegDate.setReadOnly(True)
        self.txtAppointmentRegDate.setObjectName("txtAppointmentRegDate")
        self.horizontalLayout.addWidget(self.txtAppointmentRegDate)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.txtAppointmentDiagnosis = QtGui.QPlainTextEdit(Dialog)
        self.txtAppointmentDiagnosis.setObjectName("txtAppointmentDiagnosis")
        self.verticalLayout_2.addWidget(self.txtAppointmentDiagnosis)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_19 = QtGui.QLabel(Dialog)
        self.label_19.setObjectName("label_19")
        self.verticalLayout.addWidget(self.label_19)
        self.txtAppointmentNotes = QtGui.QPlainTextEdit(Dialog)
        self.txtAppointmentNotes.setObjectName("txtAppointmentNotes")
        self.verticalLayout.addWidget(self.txtAppointmentNotes)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_3.addWidget(self.label_18)
        self.txtAppointmentAhi = QtGui.QLineEdit(Dialog)
        self.txtAppointmentAhi.setObjectName("txtAppointmentAhi")
        self.horizontalLayout_3.addWidget(self.txtAppointmentAhi)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblPsgReport = QtGui.QLabel(Dialog)
        self.lblPsgReport.setObjectName("lblPsgReport")
        self.verticalLayout_4.addWidget(self.lblPsgReport)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.buttonAttachPsgReport = QtGui.QPushButton(Dialog)
        self.buttonAttachPsgReport.setObjectName("buttonAttachPsgReport")
        self.horizontalLayout_4.addWidget(self.buttonAttachPsgReport)
        self.buttonOpenPsgReport = QtGui.QPushButton(Dialog)
        self.buttonOpenPsgReport.setObjectName("buttonOpenPsgReport")
        self.horizontalLayout_4.addWidget(self.buttonOpenPsgReport)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblDocReport = QtGui.QLabel(Dialog)
        self.lblDocReport.setObjectName("lblDocReport")
        self.verticalLayout_3.addWidget(self.lblDocReport)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.buttonAttachDocReport = QtGui.QPushButton(Dialog)
        self.buttonAttachDocReport.setObjectName("buttonAttachDocReport")
        self.horizontalLayout_5.addWidget(self.buttonAttachDocReport)
        self.buttonShowDocReport = QtGui.QPushButton(Dialog)
        self.buttonShowDocReport.setObjectName("buttonShowDocReport")
        self.horizontalLayout_5.addWidget(self.buttonShowDocReport)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_12.addLayout(self.verticalLayout_7)
        self.horizontalLayout_19.addLayout(self.verticalLayout_12)
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_19.addWidget(self.line_2)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.buttonEditPatient = QtGui.QPushButton(Dialog)
        self.buttonEditPatient.setObjectName("buttonEditPatient")
        self.verticalLayout_8.addWidget(self.buttonEditPatient)
        self.buttonViewPreviousAppointments = QtGui.QPushButton(Dialog)
        self.buttonViewPreviousAppointments.setObjectName("buttonViewPreviousAppointments")
        self.verticalLayout_8.addWidget(self.buttonViewPreviousAppointments)
        self.buttonSave = QtGui.QPushButton(Dialog)
        self.buttonSave.setObjectName("buttonSave")
        self.verticalLayout_8.addWidget(self.buttonSave)
        self.buttonSaveAndAdd = QtGui.QPushButton(Dialog)
        self.buttonSaveAndAdd.setObjectName("buttonSaveAndAdd")
        self.verticalLayout_8.addWidget(self.buttonSaveAndAdd)
        self.buttonCancel = QtGui.QPushButton(Dialog)
        self.buttonCancel.setObjectName("buttonCancel")
        self.verticalLayout_8.addWidget(self.buttonCancel)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.horizontalLayout_19.addLayout(self.verticalLayout_8)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_19)
        self.label_3.setBuddy(self.txtPatientId)
        self.label_4.setBuddy(self.txtPatientName)
        self.label_5.setBuddy(self.txtPatientSurname)
        self.label_6.setBuddy(self.txtPatientSex)
        self.label_7.setBuddy(self.txtPatientDob)
        self.label_13.setBuddy(self.txtPatientAssessment)
        self.label_8.setBuddy(self.txtPatientPhone)
        self.label_9.setBuddy(self.txtPatientHeight)
        self.label_10.setBuddy(self.txtPatientWeight)
        self.label_11.setBuddy(self.txtPatientBmi)
        self.label_12.setBuddy(self.txtPatientEpsworth)
        self.label_15.setBuddy(self.txtAppointmentDate)
        self.label_16.setBuddy(self.txtAppointmentRegDate)
        self.label_17.setBuddy(self.txtAppointmentDiagnosis)
        self.label_19.setBuddy(self.txtAppointmentNotes)
        self.label_18.setBuddy(self.txtAppointmentAhi)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonCancel, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Appointment Details</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Patient Details</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Patient ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Surname:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Sex:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Date of Birth:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Dialog", "Assessment:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Phone:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Height:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Weight:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "BMI:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog", "Epsworth Score:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Appointment</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Dialog", "Appointment Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Dialog", "Registration Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Dialog", "Diagnosis:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Dialog", "Notes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Dialog", "AHI:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPsgReport.setText(QtGui.QApplication.translate("Dialog", "PSG Report", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAttachPsgReport.setText(QtGui.QApplication.translate("Dialog", "Attach Report", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOpenPsgReport.setText(QtGui.QApplication.translate("Dialog", "Show Report", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDocReport.setText(QtGui.QApplication.translate("Dialog", "Doctor\'s Report", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAttachDocReport.setText(QtGui.QApplication.translate("Dialog", "Attach Report", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonShowDocReport.setText(QtGui.QApplication.translate("Dialog", "Show Report", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonEditPatient.setText(QtGui.QApplication.translate("Dialog", "Edit Patient Details", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonViewPreviousAppointments.setText(QtGui.QApplication.translate("Dialog", "View Previous Appointments", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSave.setText(QtGui.QApplication.translate("Dialog", "Save Appointment Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSaveAndAdd.setText(QtGui.QApplication.translate("Dialog", "Book Another Appointment", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
