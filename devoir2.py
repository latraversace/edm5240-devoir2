# coding: utf-8

import json
import csv
import requests

fichier = "banq.csv"

lien = "http://collections.banq.qc.ca/api/service-notice?handle=52327/1000"

entete = {
	"User-Agent":"Julien Latraverse", 
	"From":"j.lat@hotmail.ca"
}

l1 = range(1000,2001)
for a in l1:
	
	url = lien + str(a)
	# print(url)
	req = requests.get(url,headers=entete)
	# print(req)
	if req.status_code == 200:
		infos = req.json()
		# print(infos)
		s = []
		if infos["type"] == "audio":
			s.append(a)
			s.append(infos["titre"][:(x.find("/"))])
			s.append(infos["createur"][0])
			s.append(infos["sujets"])
			s.append(infos["dateCreation"])
			s.append(infos["descriptionMat"])
			s.append(infos["url"][0])
			print(infos["titre"][:(x.find("/"))])
			print(infos["createur"][0])
			print(infos["sujets"][0])
			print(infos["dateCreation"])
			print(infos["descriptionMat"])
			print(infos["lien"][0]["url"])
			print("~"*80)
f2 = open(fichier,"a")
marche = csv.writer(f2)
marche.writerow(s)































