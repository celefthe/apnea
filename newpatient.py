__author__ = 'Constantinos Eleftheriou'

"""
Copyright (C) 2015 Constantinos Eleftheriou
    
    This file is part of Apnea.

    Apnea is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Apnea is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Apnea.  If not, see <http://www.gnu.org/licenses/>.
"""

from decimal import Decimal
from PySide.QtGui import QDialog
import ui_newpatient


class NewPatientForm(QDialog,
                     ui_newpatient.Ui_Dialog):

    def __init__(self, parent=None):
        super(NewPatientForm, self).__init__(parent)
        self.setupUi(self)
        self.uiConnect()

    def uiConnect(self):
        # Map button clicked events to appropriate methods
        self.btnCalculateBmi.clicked.\
            connect(self.btnCalculateBmiClicked)
        self.btnReset.clicked.connect(self.btnResetClicked)
        self.btnSave.clicked.connect(self.btnSaveClicked)
        self.btnSaveAddNew.clicked.\
            connect(self.btnSaveAddNewClicked)
        self.spnHeight.setMaximum(999)

    def btnCalculateBmiClicked(self):
        # Calculate BMI using weight and height data
        weight = Decimal(self.spnWeight.value())
        height = Decimal(self.spnHeight.value()) / 100
        bmi = weight / (height * height)
        # Give answer in BMI textbox to 2 dp
        self.txtBmi.setText(str(round(bmi, 2)))

    def btnResetClicked(self):
        # Clear all fields
        self.txtPatientId.clear()
        self.txtName.clear()
        self.txtSurname.clear()
        self.txtPhone.clear()
        self.txtBriefAssessment.clear()
        self.txtBmi.clear()
        self.spnWeight.minimum()
        self.spnHeight.minimum()
        self.dateDob.minimumDate()
        self.cbxSex.clear()
        self.spnEpsworth.minimum()

    def btnSaveClicked(self):
        return

    def btnSaveAddNewClicked(self):
        return