# rappels

## objet

=> variable dans laquelle on peut stocker plusieurs valeurs ET des fonctions 
=> valeurs => propriétés de l'objet 
=> fonctions => méthodes de l'objet
=> syntaxe 

```js
let tableau = []

let nom_objet = {
    // 5 propriétés
    cle : 10 ,
    nom_propriete : "bonjour",
    test : true ,
    tableau : [1,2],
    obj : { a : 1  }
    // 
    nom_method : function(){
        // traitement
        nom_objet.tableau // utiliser une propriété de l'objet
        // dans une méthode du même objet 
        let toto = 10 ; // ici toto est une variable LOCALE
        // utilisable UNIQUEMENT dans la méthode
        return toto ;
    }
} ;

// toto => ERREUR 
let valeur = nom_objet.nom_method()

// this 
```

## dom

=> Document Object Model 
=> objet qui est créé automatiquement par javascript AVANT la balise <script>
=> cet objet a comme nom => `document`
=> contient TOUT ce que vous voyez à l'écran 

=> je veux accéder à la première balise h1 dans la page 

```js
let h1 = document.querySelector("#h1") ;  // => très flexible ! 
// <p id="h1"></p>
let h1 = document.querySelector(".h1") ;
// <p class="h1"></p>
let h1 = document.querySelector("h1") ;
// <h1></h1>
let h1 = document.getElementById("h1") ; // ancienne manière 
let h1 = {
    innerText : "....", // text dans la balise
    parent : {
        innerText : "....",
        style : {},
        addEventListener : function(){},
        parent : {}
    }
    style : { // mise en forme
        color : "black"
        textAlign : "center"
    },
    addEventListener : function("click"){}, // événements
    onclick : function(){} // js pur (moins à la mode)
                            // React / Angular / VueJS => ce qu'il faut faire 
}
```