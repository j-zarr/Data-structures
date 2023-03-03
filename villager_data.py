"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    # TODO: replace this with your code

    file_name = open(filename, 'r')
    
    for line in file_name:
        villager_info = line.rstrip().split("|")
        species_name = villager_info[1]
        species.add(species_name)

    file_name.close()

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    # TODO: replace this with your code
    file_name = open(filename, "r")

    if search_string != "All":
        for line in file_name:
            line = line.rstrip().split("|")
            if search_string == line[1]:
                name = line[0]
                villagers.append(name)
    else:
        for line in file_name:
            line = line.rstrip().split("|")
            name = line[0]
            villagers.append(name)
            
    file_name.close()
   
    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    hobbies = []
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []


    file_name = open(filename, "r")

    for line in file_name:
        line = line.rstrip().split("|")
        hobby = line[3]
        name = line[0]
        if hobby == "Fitness":
            fitness.append(name)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Music":
            music.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "Play":
            play.append(name)


    hobbies = [sorted(fitness), sorted(nature), sorted(education), 
                sorted(music), sorted(fashion), sorted(play)]

    return hobbies


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    file_name = open(filename)

    for line in file_name:
        split_string = line.rstrip().split("|")
        data_tuple = tuple(split_string)
        
        all_data.append(data_tuple)
            
    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code

print(all_data("villagers.csv"))

