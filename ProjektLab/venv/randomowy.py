import random
import time

listaImion = [ "Arek", "Kamila", "Piotr", "Robert", "Marian", "Marcin", "Zenon", "Ala", "Lidia"]


random.seed(time.time())
liczba = random.randrange(0,5)
print(liczba)
print(random.choice(listaImion))