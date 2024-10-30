# module natif de python
# functool
# https://docs.python.org/3/library/functools.html
# module natif MAIS qu'il faut importer même si il est disponible dans le langage Python

# Quel est le but des décorateurs de mise en cache comme functools.lru_cache ou functools.cache ?

from functools import cache, lru_cache
import time

@cache
def addition(minimum, maximum):
    total = 0
    for i in range(minimum, maximum + 1):
        total+= i 

    return total

start = time.time()
print(addition(1, 10_000_000))
end = time.time()
print(end - start)

start = time.time()
print(addition(1, 10_000_000))
end = time.time()
print(end - start)