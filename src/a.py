class A:
    def __init__(self,href="",contenue=""):
        self.__href=""
        self.__contenue=""
    
    def get_href(self):
        return self.__href
    def set_href(self,new_href):
        self.__href=new_href
    
    def get_contenue (self):
        return self.__contenue
    def set_contenue(self,new_contenue):
        self.__contenue=new_contenue
    
    def ajouter_info(self):
       href_utilisateur=input("entrez votre lien:")
       contenue_utilisatuer=input("entrz votre contenue:")
       self.set_href(href_utilisateur)
       self.set_contenue(contenue_utilisatuer) 

    def __str__(self):
        return f'<a href="{self.__href}">{self.__contenue}</a>'
"""
href_utilisateur=input("entrez votre lien :")
contenue_utilisatuer=input("entrz votre contenue:")


mon_choix=A(href_utilisateur,contenue_utilisatuer)

print(str(mon_choix))
"""