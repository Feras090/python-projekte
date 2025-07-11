import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import pyshorteners

class URLShortenerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("URL Shortener")
        self.setGeometry(100, 100, 400, 250)
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Enter the URL you want to shorten: ")
        layout.addWidget(self.label)
        
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter your URL here...")
        layout.addWidget(self.url_input)
        
        self.shorten_button = QPushButton("Shorten URL")
        self.shorten_button.clicked.connect(self.shorten_url)
        layout.addWidget(self.shorten_button)
        
        self.short_url_label = QLabel()
        layout.addWidget(self.short_url_label)
        
        self.copy_button = QPushButton("Copy to Clipboard")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.copy_button.setEnabled(False)
        layout.addWidget(self.copy_button)
        
        self.setLayout(layout)
        
        self.setStyleSheet(""" 
            QWidget {background-color: #f7f9fc;}
            QLabel { color: #003366; font-size: 14px; font-weight: bold; }
            QLineEdit { border: 2px solid #007BFF; border-radius: 5px; padding: 8px; font-size: 14px; }
            QPushButton { background-color: #007BFF; color: white; border-radius: 5px; padding: 10px; font-size: 14px; font-weight: bold; }
            QPushButton:hover { background-color: #0056b3; }
        """)

    def shorten_url(self):
        long_url = self.url_input.text().strip()
        if not long_url:
            QMessageBox.warning(self, "Input ERROR", "Please enter a URL to shorten.")
            return
        try:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(long_url)
            
            self.short_url_label.setText(f"Short URL: <a href='{short_url}' style='color:#007BFF;'>{short_url}</a>")
            self.short_url_label.setOpenExternalLinks(True)
            self.copy_button.setEnabled(True)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to shorten URL: {str(e)}")

    def copy_to_clipboard(self):
        short_url = self.short_url_label.text().replace("Short URL:", "").strip()
        if short_url:
            QApplication.clipboard().setText(short_url)
            QMessageBox.information(self, "Copied", "Short URL copied to clipboard!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = URLShortenerApp()
    window.show()
    sys.exit(app.exec_())