FONT_FAMILY = "Segoe UI, Ubuntu, sans-serif"
FONT_MONO = "Cascadia Code, Consolas, monospace"

COLORS = {
    "gray_50": "#f9fafb",
    "gray_100": "#f3f4f6",
    "gray_200": "#e5e7eb",
    "gray_300": "#d1d5db",
    "gray_400": "#9ca3af",
    "gray_500": "#6b7280",
    "gray_600": "#4b5563",
    "gray_700": "#374151",
    "gray_800": "#1f2937",
    "gray_900": "#111827",
    "blue_50": "#eff6ff",
    "blue_200": "#bfdbfe",
    "blue_500": "#3b82f6",
    "blue_600": "#2563eb",
    "blue_700": "#1d4ed8",
    "green_600": "#059669",
    "red_50": "#fef2f2",
    "red_600": "#dc2626",
}


def stylesheet() -> str:
    c = COLORS
    return f"""
    * {{
        font-family: {FONT_FAMILY};
        font-size: 13px;
        color: {c['gray_800']};
    }}
    QMainWindow, QWidget {{
        background-color: {c['gray_50']};
    }}
    QLabel#Title {{
        font-size: 18px;
        font-weight: 600;
        color: {c['gray_900']};
    }}
    QLabel#Subtitle {{
        font-size: 12px;
        color: {c['gray_500']};
    }}
    QLabel#SectionTitle {{
        font-size: 15px;
        font-weight: 500;
        color: {c['gray_900']};
    }}
    QTabWidget::pane {{
        border: 1px solid {c['gray_200']};
        background: white;
        border-radius: 8px;
    }}
    QTabBar::tab {{
        background: {c['gray_100']};
        color: {c['gray_600']};
        padding: 8px 18px;
        border: 1px solid {c['gray_200']};
        border-bottom: none;
        border-top-left-radius: 6px;
        border-top-right-radius: 6px;
        margin-right: 4px;
    }}
    QTabBar::tab:selected {{
        background: white;
        color: {c['blue_700']};
        font-weight: 500;
    }}
    QPushButton {{
        background-color: white;
        color: {c['gray_700']};
        border: 1px solid {c['gray_300']};
        border-radius: 5px;
        padding: 6px 14px;
        font-weight: 500;
    }}
    QPushButton:hover {{
        background-color: {c['gray_50']};
        border-color: {c['gray_400']};
    }}
    QPushButton#Primary {{
        background-color: {c['blue_600']};
        border-color: {c['blue_600']};
        color: white;
    }}
    QPushButton#Primary:hover {{
        background-color: {c['blue_700']};
        border-color: {c['blue_700']};
    }}
    QPushButton#Danger {{
        color: {c['red_600']};
        border-color: {c['red_200'] if 'red_200' in c else '#fca5a5'};
    }}
    QPushButton#Danger:hover {{
        background-color: {c['red_50']};
    }}
    QLineEdit, QComboBox {{
        background: white;
        border: 1px solid {c['gray_300']};
        border-radius: 5px;
        padding: 6px 10px;
        min-height: 22px;
    }}
    QLineEdit:focus, QComboBox:focus {{
        border-color: {c['blue_500']};
    }}
    QLineEdit[invalid="true"] {{
        border-color: {c['red_600']};
        background-color: {c['red_50']};
    }}
    QTableWidget {{
        background: white;
        border: 1px solid {c['gray_200']};
        border-radius: 6px;
        gridline-color: {c['gray_200']};
    }}
    QHeaderView::section {{
        background-color: {c['gray_50']};
        color: {c['gray_600']};
        padding: 8px;
        border: none;
        border-bottom: 1px solid {c['gray_200']};
        font-weight: 500;
    }}
    QPlainTextEdit {{
        background-color: {c['gray_900']};
        color: {c['gray_300']};
        border: 1px solid {c['gray_800']};
        border-radius: 6px;
        padding: 10px;
        font-family: {FONT_MONO};
        font-size: 12px;
    }}
    """
