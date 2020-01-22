import folium
import webbrowser
import os
import csv
import pandas as pd
from folium.plugins import MarkerCluster
import numpy as np


myMap = folium.Map(location=[38.423733, 27.142826], zoom_start= 5)





with open('aliaga_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Aliaga</strong>", tooltip= "Aliaga", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('aliaga_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Aliaga</strong>", tooltip= "Aliaga", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('aliaga_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Aliaga</strong>", tooltip= "Aliaga", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('balcova_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Balcova</strong>", tooltip= "Balcova", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('balcova_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Balcova</strong>", tooltip= "Balcova", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('balcova_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Balcova</strong>", tooltip= "Balcova", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('bayindir_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Bayindir</strong>", tooltip= "Bayindir", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('bayindir_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Bayindir</strong>", tooltip= "Bayindir", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('bayindir_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Bayindir</strong>", tooltip= "Bayindir", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('bayrakli_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Bayrakli</strong>", tooltip= "Bayrakli", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('bayrakli_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Bayrakli</strong>", tooltip= "Bayrakli", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('bayrakli_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Bayrakli</strong>", tooltip= "Bayrakli", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('beydag_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Beydag</strong>", tooltip= "Beydag", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('beydag_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Beydag</strong>", tooltip= "Beydag", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('beydag_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Beydag</strong>", tooltip= "Beydag", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('bornova_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Bornova</strong>", tooltip= "Bornova", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('bornova_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Bornova</strong>", tooltip= "Bornova", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('bornova_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Bornova</strong>", tooltip= "Bornova", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('buca_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Buca</strong>", tooltip= "Buca", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('buca_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Buca</strong>", tooltip= "Buca", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('buca_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Buca</strong>", tooltip= "Buca", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('cesme_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Cesme</strong>", tooltip= "Cesme", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('cesme_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Cesme</strong>", tooltip= "Cesme", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('cesme_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Cesme</strong>", tooltip= "Cesme", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('cigli_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Cigli</strong>", tooltip= "Cigli", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('cigli_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Cigli</strong>", tooltip= "Cigli", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('cigli_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Cigli</strong>", tooltip= "Cigli", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('dikili_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Dikili</strong>", tooltip= "Dikili", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('dikili_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Dikili</strong>", tooltip= "Dikili", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('dikili_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Dikili</strong>", tooltip= "Dikili", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('dikili_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Dikili</strong>", tooltip= "Dikili", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('foca_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Foca</strong>", tooltip= "Foca", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('foca_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Foca</strong>", tooltip= "Foca", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('foca_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Foca</strong>", tooltip= "Foca", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('gaziemir_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Gaziemir</strong>", tooltip= "Gaziemir", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('gaziemir_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Gaziemir</strong>", tooltip= "Gaziemir", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('gaziemir_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Gaziemir</strong>", tooltip= "Gaziemir", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('guzelbahce_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Guzelbahce</strong>", tooltip= "Guzelbahce", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('guzelbahce_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Guzelbahce</strong>", tooltip= "Guzelbahce", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('guzelbahce_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Guzelbahce</strong>", tooltip= "Guzelbahce", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('karabaglar_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Karabaglar</strong>", tooltip= "Karabaglar", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('karabaglar_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Karabaglar</strong>", tooltip= "Karabaglar", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('karabaglar_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Karabaglar</strong>", tooltip= "Karabaglar", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('karaburun_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Karaburun</strong>", tooltip= "Karaburun", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('karaburun_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Karaburun</strong>", tooltip= "Karaburun", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('karaburun_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Karaburun</strong>", tooltip= "Karaburun", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('karsiyaka_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Karsiyaka</strong>", tooltip= "Karsiyaka", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('karsiyaka_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Karsiyaka</strong>", tooltip= "Karsiyaka", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('karsiyaka_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Karsiyaka</strong>", tooltip= "Karsiyaka", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)



with open('kemalpasa_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Kemalpasa</strong>", tooltip= "Kemalpasa", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('kemalpasa_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Kemalpasa</strong>", tooltip= "Kemalpasa", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('kinik_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Kinik</strong>", tooltip= "Kinik", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('kinik_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Kinik</strong>", tooltip= "Kinik", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('kinik_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Kinik</strong>", tooltip= "Kinik", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('kiraz_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Kiraz</strong>", tooltip= "Kiraz", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)




with open('kiraz_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Kiraz</strong>", tooltip= "Kiraz", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('konak_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Konak</strong>", tooltip= "Konak", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('konak_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Konak</strong>", tooltip= "Konak", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('konak_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Konak</strong>", tooltip= "Konak", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('menderes_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Menderes</strong>", tooltip= "Menderes", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('menderes_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Menderes</strong>", tooltip= "Menderes", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('menderes_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Menderes</strong>", tooltip= "Menderes", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('menemen_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Menemen</strong>", tooltip= "Menemen", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('menemen_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Menemen</strong>", tooltip= "Menemen", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('menemen_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Menemen</strong>", tooltip= "Menemen", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('narlidere_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Narlidere</strong>", tooltip= "Narlidere", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('narlidere_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Narlidere</strong>", tooltip= "Narlidere", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('narlidere_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Narlidere</strong>", tooltip= "Narlidere", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('odemis_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Odemis</strong>", tooltip= "Odemis", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('odemis_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Odemis</strong>", tooltip= "Odemis", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('odemis_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Odemis</strong>", tooltip= "Odemis", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('seferihisar_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Seferihisar</strong>", tooltip= "Seferihisar", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('seferihisar_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Seferihisar</strong>", tooltip= "Seferihisar", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('seferihisar_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Seferihisar</strong>", tooltip= "Seferihisar", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)


with open('selcuk_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Selcuk</strong>", tooltip= "Selcuk", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('selcuk_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Selcuk</strong>", tooltip= "Selcuk", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('selcuk_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Selcuk</strong>", tooltip= "Selcuk", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('tire_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Tire</strong>", tooltip= "Tire", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('tire_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Tire</strong>", tooltip= "Tire", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('tire_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Tire</strong>", tooltip= "Tire", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('torbali_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Torbali</strong>", tooltip= "Torbali", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('torbali_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Torbali</strong>", tooltip= "Torbali", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('torbali_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Torbali</strong>", tooltip= "Torbali", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('urla_ortaokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Urla</strong>", tooltip= "Urla", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('urla_ilkokul.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Urla</strong>", tooltip= "Urla", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('urla_lise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Urla</strong>", tooltip= "Urla", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)



state_geo = "turkiye-ilceler.geojson" #coordinat
state_numberesoo = 'OkulDagilim.csv' #values with id 
state_data = pd.read_csv(state_numberesoo)


folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['ilce', 'number'],
    key_on='properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=5,
    legend_name='NumberOfEsso',

).add_to(myMap)



myMap.save("myMap.html")



