class Img:
    def __init__(self,src="",whith=0,height=0):
        self.__src=""
        self.__whith=0
        self.__height=0
    
    def get_src(self):
        return self.__src
    def set_src(self,new_src):
        self.__src=new_src
    
    def get_whith(self):
        return self.__whith
    def set_width(self,new_whith):
        self.__whith=new_whith
    
    def get_height(self):
        return self.__height
    def set_height(self,new_height):
        self.__height=new_height
    
    def ajouter_info(self):
       src_utilisateur=input("entrez votre lien de img:")
       width_utilisatuer=input("entrz whith de img:")
       height_utilisateur=input("entrz height de img:")
       self.set_src(src_utilisateur)
       self.set_width(int(width_utilisatuer)) 
       self.set_height(int(height_utilisateur))  

    def __str__(self):
        return f'<img src="{self.__src}" whith="{self.__whith}vw" height="{self.__height}vh">'


"""
mon_choix=Img()
mon_choix.ajouter_info()
print(str(mon_choix))
"""