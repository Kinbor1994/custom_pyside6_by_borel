from pyside6_custom_widgets import Dashboard

from utils.utils import set_app_icon

from qt_material import apply_stylesheet

class MainWindow(Dashboard):
    
    def __init__(self):
        super().__init__(menus=self.setup_menu(),sidebar_buttons=self.setup_sidebar())
        self.setWindowTitle("Gestionnaire de caisse") 
        apply_stylesheet(self, theme="default_light.xml")
        set_app_icon(self)
        self.setup_pages()
        
        
    def setup_menu(self):
        menus = [
            ("File", [("Fermer", self.close), ("Actualiser", lambda: print("Actualisation..."))])
        ]
        return menus
    
    def setup_sidebar(self):
        sidebar_buttons = [
            ("Accueil", "fa.home", lambda: print("Home...")),
            ("Paramètres", 'fa.cog', "",[("Fermer",'fa.close', self.close), ("Actualiser",'fa.star', lambda: print("Actualisation..."))]),
            ("About", 'fa.info-circle', lambda: print("Apropos...")),
            ("Déconnection", 'fa.power-off', self.open_signin)
        ]
        return sidebar_buttons

    def open_signin(self):
        """Affiche le formulaire de connexion et cache le Dashboard."""
        from authentication.sign_in import SignIn
        self.signin_form = SignIn()   
        self.signin_form.show()
        self.close()

    def setup_pages(self):
        # self.income_category_widget = IncomeCategoryList()
        # self.add_content_page(self.income_category_widget, "Bienvenue sur la page des catégories des recettes")
        pass
        
    
    @property
    def get_pages_index(self):
        index = {
            
        }
        return index
        
if __name__ == "__main__":
    import sys
    from pyside6_imports import QApplication
    app = QApplication([])
    win = MainWindow()
    win.show()
    
    sys.exit(app.exec())