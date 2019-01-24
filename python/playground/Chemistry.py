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




Chemistry.activity_series('Li', 'Au')
Chemistry.halogen_replacement('Cl', 'Br')
Chemistry.is_it_soluble('Ca', 'SO4')

hey = Chemistry()