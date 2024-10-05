import qtawesome as qta

from pyside6_imports import QLabel, QIcon
from utils.qss_file_loader import load_stylesheet

class Label(QLabel):
    """
    Custom label with text, optional icon (local or QtAwesome), and optional CSS styles.

    Args:
        text (str): The label text.
        icon_path (str, optional): Path to the local icon. Defaults to None.
        icon_name (str, optional): Name of the QtAwesome icon (e.g., 'fa5s.info-circle'). Defaults to None.
        theme_name (str, optional): CSS class name for styling (e.g., 'primary', 'danger').
    """

    def __init__(self, text, icon_path=None, icon_name=None, theme_name="primary"):
        super().__init__()
        self.setup_label(text, icon_path, icon_name)
        style = load_stylesheet("styles/label.qss")
        self.setProperty("class", theme_name)
        self.setStyleSheet(style)

    def setup_label(self, text, icon_path, icon_name):
        """
        Sets up the label with text and optional icon.

        Args:
            text (str): The label text.
            icon_path (str, optional): Path to the local icon. Defaults to None.
            icon_name (str, optional): Name of the QtAwesome icon. Defaults to None.
        """
        self.setText(text)

        if icon_path:
            icon = QIcon(icon_path)
            self.setPixmap(icon.pixmap(24, 24))  # Set icon with fixed size
        elif icon_name:
            # Use QtAwesome to set the icon
            icon = qta.icon(icon_name)
            self.setPixmap(icon.pixmap(24, 24))  # Set icon with fixed size

    def set_text(self, text):
        """
        Sets the text of the label.

        Args:
            text (str): The new text for the label.
        """
        self.setText(text)

    def get_widget(self):
        """
        Returns the main widget (self).

        Returns:
            QLabel: The label widget.
        """
        return self
