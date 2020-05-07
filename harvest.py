############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        return self.pairings

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        return 


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', '1998', 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', '2003', 'orange', False, False, 'Casaba')
    cas.add_pairing('mint')
    cas.add_pairing('strawberry')
    all_melon_types.append(cas)

    cren = MelonType('cren', '1996', 'green', False, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', '2013', 'yello', False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types
    

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
        print(f'{melon_type.name} pairs with')
        for pairing in melon_type.pairings:
            print(f'- {pairing}')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_dict = {}

    for melon_type in melon_types:
        melon_type_dict[melon_type.code] = melon_type

    return melon_type_dict

    
############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    def __init__ (self, melon_type, shape_rating, color_rating, harvested_from, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from != 3:
            return True
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons = []

    melon_by_id = make_melon_type_lookup(melon_types)
    
    melon_1 = Melon(melon_by_id['yw'], 8, 7, 2,'Shiela')
    melons.append(melon_1)

    melon_2 = Melon(melon_by_id['yw'], 3, 4,2,'Shiela')
    melons.append(melon_2)

    melon_3 = Melon(melon_by_id['yw'], 9, 8,3,'Shiela')
    melons.append(melon_3)

    melon_4 = Melon(melon_by_id['cas'], 10, 6,35,'Shiela')
    melons.append(melon_4)

    melon_5 = Melon(melon_by_id['cren'], 8, 9, 35,'Michael')
    melons.append(melon_5)

    melon_6 = Melon(melon_by_id['cren'], 8, 2, 35,'Michael')
    melons.append(melon_6)

    melon_7 = Melon(melon_by_id['cren'], 2,3, 4, 'Michael')
    melons.append(melon_7)

    melon_8 = Melon(melon_by_id['musk'], 6, 7, 4, 'Michael')
    melons.append(melon_8)

    melon_9 = Melon(melon_by_id['yw'], 7, 10, 3,'Shiela')
    melons.append(melon_9)

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            sellable = '(CAN BE SOLD)'
        else:
            sellable = '(NOT SELLABLE)'

        print(f'Harvested by {melon.harvested_by} \
              from Field {melon.harvested_from} {sellable}')

def make_melons_from_file(melon_types, filename):
    with open('harvest.txt') as data_file:
        
        melons = []

        for line in data_file:
            line = line.strip().split()

            melon_type = make_melon_type_lookup(melon_types)[line[5]]
            shape_rating = line[1]
            color_rating = line[3]
            harvested_from = line[11]
            harvested_by = line[8]

            new_melon = Melon(melon_type, shape_rating, color_rating,
                              harvested_from, harvested_by)
            melons.append(new_melon)

        return melons



melon_types = make_melon_types()
pairings = print_pairing_info(melon_types)
make_melon_type_lookup(melon_types)
melons = make_melons(melon_types)
get_sellability_report(melons)
make_melons_from_file(melon_types, 'harvest.txt')