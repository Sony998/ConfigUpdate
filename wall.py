import os 
import random

user = os.getenv('USER')
directorio = "/home/{}/Pictures/".format(user)
def mezclar():
    misarchivos = os.listdir(directorio)
    sacado = random.choice(misarchivos)
    srtfinal = 'feh --bg-fill {}{}'.format(directorio,sacado) 
    print(srtfinal)
    os.system(srtfinal)

mezclar()
