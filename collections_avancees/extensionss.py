
fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document Word"),
                            ("exe", "Executable"),
                            ("txt", "Document texte"),
                            ("jpeg", "Image JPEG"))


definition_extensions_dict = {
                    "doc" : "Document Word",
                    "exe" : "Executable",
                    "txt" : "Document texte",
                    "jpeg" : "Image JPEG"
                }

def extraire_extension(nom_fichier):
    nom_fichier_split = nom_fichier.split(".")
    if len(nom_fichier_split) > 1:
        return nom_fichier_split[-1]
    return None

def obternir_def_extension(extension, definitions):
    for d in definitions:
        if d[0].lower() == extension.lower():
            return d[1]
    return None

for fichier in fichiers:
    ext = extraire_extension(fichier)
    if ext:
        definition = obternir_def_extension(ext, definition_extensions)
        # Avec un dictionnaire : 
        # definition = definition_extensions_dict.get(ext.lower())
        if not definition:
            definition = "Extension non connue"
    else:
        definition = "Aucune extension"
    print(fichier + "(" + definition + ")")



