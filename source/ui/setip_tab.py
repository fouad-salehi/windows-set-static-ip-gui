from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QComboBox, QLineEdit,
    QPushButton, QLabel, QMessageBox
)
from core import network, validators


class SetIpTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        title = QLabel("Set Static IP Address")
        title.setObjectName("SectionTitle")
        layout.addWidget(title)

        form = QFormLayout()
        form.setSpacing(10)

        self.adapter = QComboBox()
        self.ip = QLineEdit()
        self.ip.setPlaceholderText("192.168.1.10")
        self.mask = QLineEdit("255.255.255.0")
        self.gateway = QLineEdit()
        self.gateway.setPlaceholderText("192.168.1.1 (optional)")

        form.addRow("Network adapter", self.adapter)
        form.addRow("IP address", self.ip)
        form.addRow("Subnet mask", self.mask)
        form.addRow("Default gateway", self.gateway)
        layout.addLayout(form)

        self.apply_btn = QPushButton("Apply configuration")
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

    def _mark(self, w, ok):
        w.setProperty("invalid", "false" if ok else "true")
        w.style().unpolish(w)
        w.style().polish(w)

    def apply(self):
        ip_ok = validators.is_valid_ipv4(self.ip.text())
        mask_ok = validators.is_valid_subnet_mask(self.mask.text())
        gw_ok = validators.is_valid_gateway(self.gateway.text())
        self._mark(self.ip, ip_ok)
        self._mark(self.mask, mask_ok)
        self._mark(self.gateway, gw_ok)

        if not (ip_ok and mask_ok and gw_ok):
            self.status.setText("Please fix the highlighted fields.")
            return

        if not self.adapter.currentText():
            QMessageBox.warning(self, "No adapter", "Please select a network adapter.")
            return

        result = network.set_static(
            self.adapter.currentText(),
            self.ip.text().strip(),
            self.mask.text().strip(),
            self.gateway.text().strip(),
        )
        if result["ok"]:
            self.status.setText("Configuration applied successfully.")
        else:
            self.status.setText("Failed: " + result["out"][:200])
