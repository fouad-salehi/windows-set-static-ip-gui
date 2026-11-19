from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QLabel
)
from PyQt6.QtCore import Qt
from ui.theme import stylesheet
from ui.view_tab import ViewTab
from ui.setip_tab import SetIpTab
from ui.dhcp_tab import DhcpTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Static IP Configuration Tool")
        self.resize(820, 620)
        self.setStyleSheet(stylesheet())

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.setContentsMargins(24, 20, 24, 20)
        layout.setSpacing(10)

        header = QVBoxLayout()
        header.setSpacing(2)
        title = QLabel("Static IP Configuration Tool")
        title.setObjectName("Title")
        subtitle = QLabel("by Fouad Salehi — github.com/fouad-salehi")
        subtitle.setObjectName("Subtitle")
        header.addWidget(title)
        header.addWidget(subtitle)
        layout.addLayout(header)

        tabs = QTabWidget()
        tabs.addTab(ViewTab(), "View Current IP")
        tabs.addTab(SetIpTab(), "Set Static IP")
        tabs.addTab(DhcpTab(), "Set DHCP")
        layout.addWidget(tabs, 1)

        self.setCentralWidget(central)
