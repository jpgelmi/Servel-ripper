import urllib.request
import os

class Descarga_padrones:

    root = os.path.abspath("./")
    pdf_path = "https://cdn.servel.cl/padrondefinitivo/"
    
    #Antes los padrones estaban acá -> https://cdn.servel.cl/padron/
    #https://servel.cl/padron-electoral-definitivo-y-nomina-de-inhabilitados-elecciones-generales-2021/
    #https://cdn.servel.cl/padrondefinitivo/

    def get_id():
        ID = []
        f = open(Descarga_padrones.root + "/Ripper/id.txt", "r")
        for i in f:
            i = i.strip()
            if len(i) == 4:
                i = "A0" + i
            else:
                i = "A" + i
            ID.append(i)
        Descarga_padrones.download_file(Descarga_padrones.root + "/Ripper/Padrones/",ID)

    def download_file(filename, ID):
    
        for i in ID:
            link = Descarga_padrones.pdf_path + i + ".pdf"
            try:
                response = urllib.request.urlopen(Descarga_padrones.pdf_path + i + ".pdf")    
                file = open(filename + i +".pdf", 'wb')
                file.write(response.read())
                file.close()
                
            except:
                print("No existe la URL")
                print(link)
            filename = Descarga_padrones.root + "/Ripper/Padrones/"

