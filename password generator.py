import sys
import random
import string
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QCheckBox, QMessageBox
)
from PyQt5.QtGui import QClipboard


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Password Generator")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Password length
        length_layout = QHBoxLayout()
        length_label = QLabel("Password Length:")
        self.length_input = QLineEdit()
        self.length_input.setText("12")
        length_layout.addWidget(length_label)
        length_layout.addWidget(self.length_input)

        # Checkboxes
        self.letters_checkbox = QCheckBox("Include Letters")
        self.letters_checkbox.setChecked(True)
        self.numbers_checkbox = QCheckBox("Include Numbers")
        self.numbers_checkbox.setChecked(True)
        self.symbols_checkbox = QCheckBox("Include Symbols")
        self.symbols_checkbox.setChecked(True)

        # Generate Button
        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)

        # Password output
        self.password_output = QLineEdit()
        self.password_output.setReadOnly(True)

        # Copy Button
        self.copy_button = QPushButton("Copy to Clipboard")
        self.copy_button.clicked.connect(self.copy_to_clipboard)

        # Add widgets to layout
        layout.addLayout(length_layout)
        layout.addWidget(self.letters_checkbox)
        layout.addWidget(self.numbers_checkbox)
        layout.addWidget(self.symbols_checkbox)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.password_output)
        layout.addWidget(self.copy_button)

        self.setLayout(layout)

    def generate_password(self):
        try:
            length = int(self.length_input.text())
        except ValueError:
            QMessageBox.critical(self, "Error", "Password length must be a number.")
            return

        characters = ""
        if self.letters_checkbox.isChecked():
            characters += string.ascii_letters
        if self.numbers_checkbox.isChecked():
            characters += string.digits
        if self.symbols_checkbox.isChecked():
            characters += string.punctuation

        if not characters:
            QMessageBox.critical(self, "Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_output.setText(password)

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_output.text())
        QMessageBox.information(self, "Copied", "Password copied to clipboard!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())
