from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel, QMessageBox
)
from core import network


class DhcpTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        title = QLabel("Switch to DHCP (Automatic)")
        title.setObjectName("SectionTitle")
        layout.addWidget(title)

        self.adapter = QComboBox()
        layout.addWidget(self.adapter)

        self.apply_btn = QPushButton("Switch to DHCP")
        self.apply_btn.setObjectName("Primary")
        self.apply_btn.clicked.connect(self.apply)
        layout.addWidget(self.apply_btn)
        layout.addStretch()

        self.status = QLabel("")
        self.status.setObjectName("Subtitle")
        layout.addWidget(self.status)

        self.reload_adapters()

    def reload_adapters(self):
        self.adapter.clear()
        self.adapter.addItems(network.list_adapters())

    def apply(self):
        if not self.adapter.currentText():
            QMessageBox.warning(self, "No adapter", "Please select a network adapter.")
            return
        result = network.set_dhcp(self.adapter.currentText())
        if result["ok"]:
            self.status.setText("DHCP enabled successfully.")
        else:
            self.status.setText("Failed: " + result["out"][:200])
