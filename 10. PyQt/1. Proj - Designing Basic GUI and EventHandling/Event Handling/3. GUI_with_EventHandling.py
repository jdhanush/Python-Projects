####################################
# 1. Import Modules
####################################
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from random import choice



####################################
# 2. Main App Objects and Settings
####################################
app = QApplication([])              # 'app' is the QApplication([]) class with empty list
main_window = QWidget()             # 'main_window' is the QWidget() class's object which is the application window    
main_window.setWindowTitle("Random Word Generator")
main_window.resize(300, 150)



####################################
# 3. Create All Widgets/App-Objects needed for the App
####################################
title_text = QLabel("Random Generator")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click Me 1")
button2 = QPushButton("Click Me 2")
button3 = QPushButton("Click Me 3")

my_words = ["Python", "Code", "PyQt", "Test", "GUI", "App", "Module", "Framework", "Class", "Widget", "Window", "Pushbutton"] 



####################################
# 4. Design your Layout, add your widgets to the screen(All Design Happens here)
####################################

# master layout for vertical line (this column forms the basis for the GUI on which rows will be held)
master_layout = QVBoxLayout()

# creating GUI row objects (rows form the GUI building blocks)
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

# Adding text to each row (row1 is the top-most row, row2 comes next and row3 is bottom row)
row1.addWidget(title_text, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

# Adding button to 3rd row
row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

# adding the row objects to the master column object
# These row objects must be added in the order that we want to see them (Python reads from top to bottom)
master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

# superimposing master_layout on Main widget
main_window.setLayout(master_layout)


# Functions for Generating Random word  
def random_word1():
    word = choice(my_words)
    text1.setText(word)
    
def random_word2():
    word = choice(my_words)
    text2.setText(word)
    
def random_word3():
    word = choice(my_words)
    text3.setText(word)    
    
    
    
####################################
# 5. Events (Set final Layout to main window)
####################################
button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)

####################################
# 6. Show/Run the GUI App
####################################
main_window.show()      # this line shows up the GUI
app.exec_()             # this line executes the GUI application
#app.exec()