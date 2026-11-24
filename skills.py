from pyscript import document

nonmetals = {
    "Hydrogen": ("H", "Hydrogen", 1, 1.008),
    "Nitrogen": ("N", "Nitrogen", 7, 14.007),
    "Oxygen": ("O", "Oxygen", 8, 15.999),
    "Fluorine": ("F", "Fluorine", 9, 18.998),
    "Chlorine": ("Cl", "Chlorine", 17, 35.45),
    "Bromine": ("Br", "Bromine", 35, 79.904),
    "Iodine": ("I", "Iodine", 53, 126.90),
    "Carbon": ("C", "Carbon", 6, 12.011),
    "Sulphur": ("S", "Sulphur", 16, 32.06),
    "Phosphorous": ("P", "Phosphorous", 15, 30.974),
    "Silicon": ("Si", "Silicon", 14, 28.085),
}
#references: https://www.periodictable.com/ https://byjus.com/chemistry/non-metals/

def search_element(e):
    document.getElementById('result').innerHTML = ""
    element1 = document.getElementById('search-input').value.strip().title()

    # Using .get() - no if statement
    symbol, element, atomic_number, atomic_mass = nonmetals.get(
        element1,
        ("-", "Element not found", "-", "-")
    )

    document.getElementById('result').innerHTML = f"""
    <b>Symbol :</b> {symbol} <br>
    <b>Element :</b> {element} <br>
    <b>Atomic Number :</b> {atomic_number} <br>
    <b>Atomic Mass :</b> {atomic_mass}
    """