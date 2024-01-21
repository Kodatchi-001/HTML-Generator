class H1:
    def __init__(self,style="",contenue=""):
        self.__style=""
        self.__contenue=""
    
    def get_style(self):
        return self.__style
    def set_style(self,new_style):
        self.__style=new_style
    
    def get_contenue (self):
        return self.__contenue
    def set_contenue(self,new_contenue):
        self.__contenue=new_contenue
    
    def ajouter_info(self):
       style_utilisateur=input("entrez votre style:")
       contenue_utilisatuer=input("entrz votre contenue:")
       self.set_style(style_utilisateur)
       self.set_contenue(contenue_utilisatuer) 


    def __str__(self):
        return f'<h1 style="{self.__style}">{self.__contenue}</h1>'
"""
titre_utilisateur=input("entrez votre titre:")
style_utilisatuer=input("entrz votre style (color-position...):")

mon_choix=H1(style_utilisatuer,titre_utilisateur)

print(str(mon_choix))
"""  

