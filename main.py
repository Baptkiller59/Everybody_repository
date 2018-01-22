# -- ceci est notre code principal --

#commandes d'initialisation
from sense_hat import SenseHat
from time import sleep
from picamera import PiCamera
import os
import ephem
import time
import math

sense = SenseHat()
debut = time.time()

##definition des couleurs

y = [255, 255, 0]  
g = [0, 255, 0]
b = [0,150, 255]   
a = [0, 0, 255]
v = [165, 0, 245]
r = [250, 0, 0]
o = [255, 130, 0] 
p = [215, 0, 230]
w = [255, 255, 255]
e = [0, 0, 0] 

imgcamerainfra = [  
e, e, e, e, y, y, e, e,
e, e, e, e, e, y, e, e,  
y, y, y, y, y, y, y, y,  
y, e, e, r, r, e, y, y,   
y, e, r, e, e, r, e, y,  
y, e, r, e, e, r, e, y,  
y, e, e, r, r, e, e, y,   
y, y, y, y, y, y, y, y,  
]


#afficher un logo pendant le démarage

#liste des méthodes
def temps()
    fin = time.time()
    tps = fin - debut # Combien de secondes entre debut et fin ?
    
def position() #GPS - ! ne marche pas (v1) !
  Name  = "ISS (ZARYA)"
  Line1 = "1 25544U 98067A   18008.29516252  .00001521  00000-0  30072-4 0  9994"
  Line2 = "2 25544  51.6425  95.8146 0003157 351.7539  71.6709 15.54270870 93659"

  Iss = ephem.readtle(name, line1, line2)

  While True: # ! eviter une boucle infini !
    Iss.computer()
    Print("Lat: %s – Long: %s" % (iss.sublat, iss.sublong))
    Time.sleep(1)

def infrarouge() #photo + heure - à tester v1 + manque la sauvergarde
  camera = PiCamera()
  camera.start_preview()
  sleep(60)
  camera.stop_preview()
  temps()

temps()

while tps <= 10800: #condition à vérifier -> s'execute pendant 3heures (10 800 secondes)
  if lum > #test de la luminosité
    sense.set_pixels(imgcamerainfra)  
    infrarouge()
    position()
  temps()
