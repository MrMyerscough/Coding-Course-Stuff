class Element:
    def __init__(self, name, atomic_symbol, atomic_number, atomic_weight, charges):
        self.name = name
        self.atomic_symbol = atomic_symbol
        self.atomic_number = atomic_number
        self.atomic_weight = atomic_weight
        self.charges = charges

    def __str__(self):
        return f"""Name: {self.name} 
Atomic Number: {self.atomic_number} 
Atomic Weight: {self.atomic_weight} 
Ionic Charges: {self.charges}"""

class Chemistry:
    def __init__(self):
        print("Hey this worked")

    act_series = ('Li', 'Rb', 'K', 'Ba', 'Ca', 'Na', 'Mg', 'Al', 'Mn', 'Zn', 'Cr', 'Fe', 'Co', 'Ni', 'Sn', 'Pb', 'H', 'Cu', 'Ag', 'Hg', 'Pt', 'Au')
    halogen_series = ('F', 'Cl', 'Br', 'I')
    always_soluble = ('Li', 'Na', 'K', 'Rb', 'Cs', 'NH4', 'NO3', 'ClO3', 'ClO4', 'CH3COO', 'C2H3O2')
    f_exceptions = ('Mg', 'Ca', 'Sr', 'Ba', 'Pb')
    halogen_exceptions = ('Ag', 'Hg', 'Pb')
    sulfate_exceptions = ('Sr', 'Ba', 'Pb')
    insoluble = ('CO3', 'PO4', 'C2O4', 'CrO4', 'S', 'OH', 'O')

    @staticmethod
    def activity_series(element_1, element_2):
        first_element = Chemistry.act_series.index(element_1)
        second_element = Chemistry.act_series.index(element_2)

        if first_element < second_element:
            print("There is a reaction!", element_1, "will replace", element_2 + ".")
        else:
            print("There is no reaction!", element_1, "will not replace", element_2 + ".")

    @staticmethod
    def halogen_replacement(element_1, element_2):
        first_element = Chemistry.halogen_series.index(element_1)
        second_element = Chemistry.halogen_series.index(element_2)

        if first_element < second_element:
            print("There is a reaction!", element_1, "will replace", element_2 + ".")
        else:
            print("There is no reaction!", element_1, "will not replace", element_2 + ".")
 
    @staticmethod
    def is_it_soluble(cation, anion):
        if cation in Chemistry.always_soluble:
            print("The compound of", cation, "and", anion, "is soluble.")
        elif anion in Chemistry.always_soluble:
            print("The compound of", cation, "and", anion, "is soluble.")
        elif anion in "F" and cation not in Chemistry.f_exceptions:
            print("The compound of", cation, "and", anion, "is soluble.")
        elif (anion in 'Cl' or anion in 'Br' or anion in 'I') and cation not in Chemistry.halogen_exceptions:
            print("The compound of", cation, "and", anion, "is soluble.")
        elif anion in "SO4" and cation not in Chemistry.sulfate_exceptions:
            print("The compound of", cation, "and", anion, "is soluble.")
        else:
            print("The compound of", cation, "and", anion, "is insoluble.")

    p_table = {"Hydrogen" : Element('Hydrogen', 'H', 1, '1.008 g/mol', ['1+', '1-']), 
    "Helium": Element('Helium', 'He', 2, '4.003 g/mol', [0]), 
    "Lithium" : Element('Lithium', 'Li', 3, '6.94 g/mol', ['1+']), 
    "Beryllium" : Element('Beryllium', 'Be', 4, '9.0122 g/mol', ['2+']), 
    "Boron" : Element('Boron', 'B', 5, '10.81 g/mol', ['3+']), 
    "Carbon" : Element('Carbon', 'C', 6, '12.01 g/mol', ['4+', '4-']), 
    "Nitrogen" : Element('Nitrogen', 'N', 7, '14.007 g/mol', ['3-']), 
    "Oxygen" : Element('Oxygen', 'O', 8, '15.999 g/mol', ['2-']), 
    "Fluorine" : Element('Fluorine', 'F', 9, '18.998 g/mol', ['1-']), 
    "Neon" : Element('Neon', 'Ne', 10, '20.18 g/mol', ['0']),
    "Sodium" : Element('Sodium', 'Na', 11, '22.99 g/mol', ['1+']),
    "Magnesium" : Element('Magnesium', 'Mg', 12, '24.305', ['2+']),
    "Aluminum" : Element('Aluminum', 'Al', 13, '26.982 g/mol', ['3+']),
    "Silicon" : Element('Silicon', 'Si', 14, '28.085 g/mol', ['4+', '4-']),
    "Phosphorus" : Element('Phosphorus', 'P', 15, '30.974 g/mol', ['3-']),
    "Sulfur" : Element('Sulfur', 'S', 16, '32.06 g/mol', ['2-']),
    "Chlorine" : Element('Chlorine', 'Cl', 17, '35.45 g/mol', ['1-']),
    "Argon" : Element('Argon', 'Ar', 18, '39.948 g/mol', [0]),
    "Potassium" : Element('Potassium', 'K', 19, '39.098 g/mol', ['1+']),
    "Calcium" : Element('Calcium', 'Ca', 20, '40.078 g/mol', ['2+']),
    "Scandium" : Element('Scandium', 'Sc', 21, '44.956 g/mol', []),
    "Titanium" : Element('Titanium', 'Ti', 22, '47.867 g/mol', []),
    "Vanadium" : Element('Vanadium', 'V', 23, '50.942', []),
    "Chromium" : Element('Chromium', 'Cr', 24, '51.996 g/mol', []),
    "Manganese" : Element('Manganese', 'Mn', 25, '54.938 g/mol', []),
    "Iron" : Element('Iron', 'Fe', 26, '55.845 g/mol', []),
    "Cobalt" : Element('Cobalt', 'Co', 27, '58.933 g/mol', []),
    "Nickel" : Element('Nickel', 'Ni', 28, '58.693 g/mol', []),
    "Copper" : Element('Copper', 'Cu', 29, '63.546 g/mol', []),
    "Zinc" : Element('Zinc', 'Zn', 30, '65.38 g/mol', ['2+']),
    "Gallium" : Element('Gallium', 'Ga', 31, '69.723 g/mol', ['3+']),
    "Germanium" : Element('Germanium', 'Ge', 32, '72.63 g/mol', ['4+', '4-']),
    "Arsenic" : Element('Arsenic', 'As', 33, '74.922 g/mol', ['3-']),
    "Selenium" : Element('Selenium', 'Se', 34, '78.971 g/mol', ['2-']),
    "Bromine" : Element('Bromine', 'Br', 35, '79.904 g/mol', ['1-']),
    "Krypton" : Element('Krypton', 'Kr', 36, '83.798 g/mol', [0]),
    }


class ChemGetters:
    def get_name_from_number(self, num):
        for i in Chemistry.p_table:
            if Chemistry.p_table[i].atomic_number == num:
                return Chemistry.p_table[i].name

    def get_name_from_symbol(self, symb):
        for i in Chemistry.p_table:
            if Chemistry.p_table[i].atomic_symbol == symb:
                return Chemistry.p_table[i].name

    def get_name_from_mass(self, mass):
        for i in Chemistry.p_table:
            if Chemistry.p_table[i].atomic_weight == mass:
                return Chemistry.p_table[i].name

    def get_symbol_from_name(self, name):
        for i in Chemistry.p_table:
            if Chemistry.p_table[i].name == name:
                return Chemistry.p_table[i].atomic_symbol

    def get_symbol_from_number(self, num):
        for i in Chemistry.p_table:
            if Chemistry.p_table[i].atomic_number == num:
                return Chemistry.p_table[i].atomic_symbol

    def get_symbol_from_mass(self, mass):
        for i in Chemistry.p_table:
            if Chemistry.p_table[i].atomic_weight == mass:
                return Chemistry.p_table[i].atomic_symbol

    def get_number_from_name(self, name):
        for i in Chemistry.p_table:
            if Chemistry.p_table[i].name == name:
                return Chemistry.p_table[i].atomic_number

    def get_number_from_symbol(self, symb):
        for i in Chemistry.p_table:
            if Chemistry.p_table[i].atomic_symbol == symb:
                return Chemistry.p_table[i].atomic_number

    def get_number_from_mass(self, mass):
        for i in Chemistry.p_table:
            if Chemistry.p_table[i].atomic_weight == mass:
                return Chemistry.p_table[i].atomic_number

    def get_mass_from_name(self, name):
        for i in Chemistry.p_table:
            if Chemistry.p_table[i].name == name:
                return Chemistry.p_table[i].atomic_weight

    def get_mass_from_symbol(self, symb):
        for i in Chemistry.p_table:
            if Chemistry.p_table[i].atomic_symbol == symb:
                return Chemistry.p_table[i].atomic_weight

    def get_mass_from_number(self, num):
        for i in Chemistry.p_table:
            if Chemistry.p_table[i].atomic_number == num:
                return Chemistry.p_table[i].atomic_weight

# Chemistry.activity_series('Li', 'Au')
# Chemistry.halogen_replacement('Cl', 'Br')
# Chemistry.is_it_soluble('Ca', 'SO4')

# print(Chemistry.p_table["Hydrogen"])
# print(f"Helium's atomic weight is {Chemistry.p_table['Helium'].atomic_weight}")
# print(f"The cations that make Fluoride's insoluble are {Chemistry.f_exceptions}")

# getter = ChemGetters()
# print(f'The atomic number of Zinc is {getter.get_number_from_name("Zinc")}')
#isaiah was here
