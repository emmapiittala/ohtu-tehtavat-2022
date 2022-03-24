from urllib import request
from project import Project
import toml
content = ""

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        lista = toml.loads(content)
        nimi = lista['tool']['poetry']['name']
        kuvaus = lista['tool']['poetry']['description']
        riippuvuudet = lista['tool']['poetry']['dependencies']
        dev_riippuvuudet = lista['tool']['poetry']['dev-dependencies']
        
        print('')
        #print (content[0],"ripuli", type(content))
        #print(content[1])
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(nimi, kuvaus, riippuvuudet, dev_riippuvuudet)
        