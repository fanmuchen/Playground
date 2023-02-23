import os
import sys
import pikepdf
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QVBoxLayout


class PDFUnlocker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the UI components
        self.file_label = QLabel(
            'Select a password-protected PDF file to unlock:')
        self.file_button = QPushButton('Select File')
        self.file_button.clicked.connect(self.showFileDialog)
        self.status_label = QLabel('')

        # Set up the layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.file_label)
        vbox.addWidget(self.file_button)
        vbox.addWidget(self.status_label)
        self.setLayout(vbox)

        # Set up the window properties
        self.setWindowTitle('PDF Unlocker')
        self.setGeometry(100, 100, 400, 150)

    def showFileDialog(self):
        # Open a file dialog and get the selected file path
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self, 'Select File', '', 'PDF Files (*.pdf)')

        # Call the unlockPDF function with the selected file path
        self.unlockPDF(file_path)

    def unlockPDF(self, input_file):
        # Check if the input file exists and is a PDF file
        if not os.path.isfile(input_file):
            self.status_label.setText('Error: Invalid file path.')
        elif not input_file.endswith('.pdf'):
            self.status_label.setText('Error: Invalid file type.')
        else:
            # Open the input file with pikepdf and remove the password protection
            output_file = os.path.splitext(input_file)[0] + '_unlocked.pdf'
            try:
                with pikepdf.open(input_file, password='') as pdf:
                    pdf.save(output_file)
                    self.status_label.setText(
                        'Password protection removed and file saved as ' + output_file + '.')
            except pikepdf._qpdf.PasswordError:
                self.status_label.setText('Error: Password-protected file.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pdf_unlocker = PDFUnlocker()
    pdf_unlocker.show()
    sys.exit(app.exec_())
