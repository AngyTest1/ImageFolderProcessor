import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QFileDialog, QListWidget, QDialog, QMessageBox
from core_processing import process_folder
from utils import get_folders_in_directory

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        
        # Example label to show text
        label = QLabel(self)
        label.setText("Hello from PyQt6!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        # Folder selection section
        folder_button = QPushButton("Select Folder", self)
        folder_button.clicked.connect(self.open_folder_dialog)
        
        version_management_layout = QVBoxLayout()
        self.version_list_widget = QListWidget()
        version_management_layout.addWidget(self.version_list_widget)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(folder_button)
        layout.addLayout(version_management_layout)
        self.setCentralWidget(container)

    def open_folder_dialog(self):
        folder_path, _ = QFileDialog.getExistingDirectory(None, "Select Folder")
        if folder_path:
            try:
                versions = get_folders_in_directory(folder_path)
                for version in versions:
                    process_folder(os.path.join(folder_path, version))
                    self.version_list_widget.addItem(f"Processed Version: {version}")
                QMessageBox.information(self, "Success", "All processing completed successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

class CreateVersionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Version Dialog")
        
        # Example label to show text
        label = QLabel(self)
        label.setText("Hello from Create Version Dialog!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec())