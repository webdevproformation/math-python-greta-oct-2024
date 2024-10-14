class Article :
    def __init__(self, p_auteur, p_contenu, p_like , p_titre):
        self.auteur = p_auteur
        self.contenu = p_contenu
        self.like = p_like
        self.titre = p_titre

    def render(self):
        texte = f"""
            <h1>{self.titre}</h1>
            <p>{self.contenu}</p>
            <ul>
                <li>écrit par : {self.auteur}</li>
                <li>like : {self.like}</li>
            </ul>
        """
        print(texte)

article1 = Article("moi" , "lorem ipsum" ,10 , "mon premier article")
article2 = Article("un étudiant" , "exemple article" , 15 , "utiliser une class au quotidien")

article1.render()
article2.render()