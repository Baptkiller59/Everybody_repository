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
tps = #tps

#afficher un logo pendant le démarage

#liste des méthodes
def time()
    debut = time.time() # On attend quelques secondes avant de taper la commande suivante
    fin = time.time()
    tps = fin - debut # Combien de secondes entre debut et fin ?
    
def position() #GPS - ne marche pas (v1)
  Name  = "ISS (ZARYA)"
  Line1 = "1 25544U 98067A   18008.29516252  .00001521  00000-0  30072-4 0  9994"
  Line2 = "2 25544  51.6425  95.8146 0003157 351.7539  71.6709 15.54270870 93659"

  Iss = ephem.readtle(name, line1, line2)

  While True: #eviter une boucle infini
    Iss.computer()
    Print("Lat: %s – Long: %s" % (iss.sublat, iss.sublong))
    Time.sleep(1)

def infrarouge() #photo + heure - à tester v1
  camera = PiCamera()
  camera.start_preview() #il manque la prise de date
  sleep(60)
  camera.stop_preview()

time()
while tps <= 118800: #condition à trouver -> s'execute pendant 3heures (118 800 secondes)
  time()
  position()
  infrarouge()
