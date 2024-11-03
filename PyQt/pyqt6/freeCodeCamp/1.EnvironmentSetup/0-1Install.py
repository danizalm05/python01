# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:26:32 2024

@author: gilfm
"""

from PySide6.QtWidgets import QApplication, QWidget

import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()