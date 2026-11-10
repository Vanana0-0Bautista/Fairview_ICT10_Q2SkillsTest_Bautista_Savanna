from pyscript import document

#Non-metals
#Dictionary with information about Non-metals
#Non-metal name: non-metal details, order from non-metal, and # of non-metals

Non_metals = {
    "HYDROGEN": ("H", "hydrogen", 1, 1),
    "HELIUM": ("He", "helium", 2, 4),
    "CARBON": ("C", "carbon", 6, 12),
    "NITROGEN": ("N", "nitrogen", 7, 14),
    "OXYGEN": ("O", "oxygen", 8, 16),
    "FLUORINE": ("F", "fluorine", 9, 19),
    "NEON": ("Ne", "neon", 10, 20),
    "PHOSPHORUS": ("P", "phosphorus", 15, 31),
    "SULFUR": ("S", "sulfur", 16, 32),
    "CHLORINE": ("Cl", "chlorine", 17, 35),
    "ARGON": ("Ar", "argon", 18, 40),
    "SELENIUM": ("Se", "selenium", 34, 79),
    "BROMINE": ("Br", "bromine", 35, 80),
    "KRYPTON": ("Kr", "krypton", 36, 84),
    "IODINE": ("I", "iodine", 53, 127),
    "XENON": ("Xe", "xenon", 54, 131),
    "RADON": ("Rn", "radon", 86, 222)
}

#create a function to search a non-metal

def search_element(e):
    #get the input value from HTML
    Element1 = document.getElementById("nonmetal1").value
    #retrieve information from the dictionary
    result = Non_metals.get(Element1, ("Element not found", "-", "-", "-"))
    #display the result
    document.getElementById("code").innerText = result[0]
    document.getElementById("name").innerText = Element1
    document.getElementById("order").innerText = result[2]
    document.getElementById("count").innerText = result[3]

 

