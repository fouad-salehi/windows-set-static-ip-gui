import sys
from PyQt6.QtWidgets import QApplication
from core.admin import require_admin
from ui.main_window import MainWindow


def main():
    require_admin()
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()