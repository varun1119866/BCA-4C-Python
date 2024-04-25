from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QVBoxLayout
app = QApplication([])
Window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton(&#39;Top&#39;))
layout.addWidget(QPushButton(&#39;Bottom&#39;))
Window.setLayout(layout)
Window.show()
app.exec_()
