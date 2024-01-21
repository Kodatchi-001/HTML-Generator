import webbrowser
class HTML:
    def __init__(self):
        self.list_balise=[]
    
    def ajouter_balise(self,balise):
        self.list_balise.append(balise)
    
    def cree_page_html(self):
        with open ("index.html","w") as fichier :
            fichier.write(str(self))
            webbrowser.open("index.html")
    
    def __str__(self) :
     html=""
     for balise in self.list_balise :
        html=html+str(balise)+"\n"
     return f'<html>\n<head>\n<title>Document</title>\n<link rel="stylesheet" href="./assets/style.css">\n</head>\n<body>\n{html}</body>\n</html>'
    

