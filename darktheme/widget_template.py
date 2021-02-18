
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QFrame, QInputDialog, QLabel, QMessageBox, QWidget
from PySide6.QtGui import QColor, QCursor, QPalette


class DarkPalette(QPalette):
    """A Dark palette meant to be used with the Fusion theme."""
    def __init__(self, *__args):
        super().__init__(*__args)
        
        self.setColor(QPalette.Window, QColor(53, 53, 53))          #dark grey (normal background widgets and main)
        self.setColor(QPalette.WindowText, QColor(255, 255, 255))   #white
        self.setColor(QPalette.Base, QColor(25, 25, 25))            #darker grey (selected text in pop up)
        self.setColor(QPalette.AlternateBase, QColor(53, 53, 53))   #dark grey (not used far as i can see)
        self.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))  #white
        self.setColor(QPalette.ToolTipText, QColor(255, 255, 255))  #white
        self.setColor(QPalette.Text, QColor(255, 255, 255))         #white
        self.setColor(QPalette.Button, QColor(53, 53, 53))          #dark grey (drop down arrow colour and tabs)
        self.setColor(QPalette.ButtonText, QColor(255, 255, 255))   #white
        self.setColor(QPalette.BrightText, QColor(255, 0, 0))       #red
        self.setColor(QPalette.Link, QColor(42, 130, 218))          #blue
        self.setColor(QPalette.Highlight, QColor(42, 130, 218))     #blue
        self.setColor(QPalette.HighlightedText, QColor(0, 0, 0))    #black

        # If item is disabled, use alternative colours
        self.setColor(QPalette.Disabled, QPalette.Button, QColor(53, 53, 53))       #dark grey
        self.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(25, 25, 25))   #darker grey

class DarkApplication(QApplication):
    """A Dark styled application."""
    def __init__(self, *__args):
        super().__init__(*__args)
        
        self.setStyle("Fusion")
        self.setPalette(DarkPalette())
        # self.setFont(QFont("schoensperger", 20))
        self.setStyleSheet("QToolTip { color: #ffffff; background-color: grey; border: 1px solid white; }")
