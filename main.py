from src.a import A
from src.h1 import H1
from src.img import Img
from src.HTML import HTML

if __name__=="__main__":
    print("___votre image__")
    img=Img()
    img.ajouter_info()
    print("___votre link__")
    a=A()
    a.ajouter_info()
    print("___votre titre__")
    h1=H1()
    h1.ajouter_info()
    print("________")
    html=HTML()
    html.ajouter_balise(img)
    html.ajouter_balise(h1)
    html.ajouter_balise(a)
    html.cree_page_html()
    
    print(html)








    