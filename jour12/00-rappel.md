# rappel

## boucle 

```py
for i in range(min, max_non_inclu, pas) :
    // traitement
```

```js
for(let i = min ; i < max_non_inclu ; i += pas){
    // traitement
}
```

## condition

```py
if comparaison :
    // traitement
```

```js
if( comparaison ){
    // traitement
}
```

vous pouvez enchainer les if via la syntaxe suivante :

```js
if( comparaison1 ){
    // traitement
}else if( comparaison2 ){
    // traitement
}else if( comparaison3 ){
    // traitement
}else{
    // traitement par défaut 
}
```

=> la partie INTELLIGENTE de tous les programmes 

## fonction

=> définition : variable qui stocke un bloc de code / des traitements 

```py
def nom_fonction(param1, param2) :
    // traitement 
```

```js
function nom_fonction(param1,param2){
    // traitement 
}
```

dans une fonction il y a un mot clé essentiel => `return`

```js
function nom_fonction(param1,param2){
    // traitement 
    let a = 10 ;
    let b = 30 ;
    let c = a / b ;
    return c ; 
}

// let d  = c + 2; // ERREUR car c n'existe PLUS

// par contre si je veux récupérer la valeur stockée dans c alors je dois utiliser la syntaxe suivante :

let variable = nom_fonction(1,2); 
```

tous les traitements stockés dans une fonction SONT LOCALES => DISPONIBLE QUE DANS la fonction 


## tableau 

```py
# liste 

elements = [1,2,3,4]
```

```js

let elements = [1,2,3,4] ; 
```

opération que l'on peut réaliser sur un tableau => CRUD 

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
```js
let elements = [1,2,3,4] ; 

// Create => ajouter une valeur au tableau 
elements.push(5) ; // ajouter à la fin du tableau 

// ajouter 10 après le chiffre 1
elements.splice(1, 0, 10); 

// Read => récupérer la 2ème valeur du tableau 
elements[1];
// elements[1:3]; n'existe pas en JS
elements.slice(0, 2); // récupérer les 2 premières valeurs du tableau 

// Update => modifier la valeur du deuxième élément => 2 => 99
elements[1] = 99 ; 

// Delete => supprimer le chiffre 4 du tableau 
elements.splice(3,1); 
```


## objet et DOM (aujourd'hui)