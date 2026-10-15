####################################
# 1. Import Modules
####################################
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout



####################################
# 2. Main App Objects and Settings
####################################
app = QApplication([])              # 'app' is the QApplication([]) class with empty list
main_window = QWidget()             # 'main_window' is the QWidget() class's object which is the application window    
main_window.setWindowTitle("Random Word Generator")
main_window.resize(400, 300)



####################################
# 3. Create All Widgets/App Objects needed for the App
####################################



####################################
# 4. Design your Layout, add your widgets to the screen(All Design Happens here)
####################################



####################################
# 5. Events (Set final Layout to main window)
####################################



####################################
# 6. Show/Run the GUI App
####################################
main_window.show()      # this line shows up the GUI
app.exec_()             # this line executes the GUI application
#app.exec()