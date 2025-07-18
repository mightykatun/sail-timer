import json
import os
import time as tm



def init_race_session(race_name: str, boat_list: list):
    '''
    Initialize the race_name.json file that will serve as data storage for the whole race

    Args:
        race_name (str): Name of the race, e.g. "Critérium Manche 1"
        boat_dict (dict): A list containing [{"Name": "Little Nemo II", "Sail number": "SUI 102", "Category": "Lestés A"}, ...]
    
    Returns:
        False: If a race already exists
        True: Otherwise
    '''

    # check if race exists
    if os.path.exists(f"./{race_name}.json"):
        return False
    
    # create the race's json file
    else:
        with open(f"./{race_name}.json", "w") as race_file:
            init_dict = {"Race name": race_name, "Participants": boat_list, "Started": False}
            json.dump(init_dict, race_file, indent=4)
        return True
    


def boat_list_add(race_name: str, boat_info_to_add: dict):
    '''
    Adds one boat to the list

    Args:
        race_name (str): Name of the race, e.g. "Critérium Manche 1"
        boat_info_to_add (dict): {"Name": "Little Nemo II", "Sail number": "SUI 102", "Category": "Lestés A"}
    
    Returns:
        False: If race is started
        True: Otherwise
    '''
    # check if the race is already started
    with open(f"./{race_name}.json", "r") as race_file:
        race_dict = json.load(race_file)
    if race_dict["Started"] != False:
        return False
    
    # update the boat list
    else:
        with open(f"./{race_name}.json", "w") as race_file:
            race_dict["Participants"].append(boat_info_to_add)
            json.dump(race_dict, race_file, indent=4)
        return True



def boat_list_del(race_name: str, boat_to_delete: str):
    '''
    '''

    # check if the race is already started
    with open(f"./{race_name}.json", "r") as race_file:
        race_dict = json.load(race_file)
    if race_dict["Started"] != False:
        return False
    pass



def start_procedure(race_name: str):
    '''
    Write the time the procedure started (5 mins) at to the json file

    Args:
        race_name (str): Name of the race, e.g. "Critérium Manche 1"
    
    Returns:
        False: If procedure already started
        True: Otherwise
    '''

    # check if the race is already started
    with open(f"./{race_name}.json", "r") as race_file:
        race_dict = json.load(race_file)
    if race_dict["Started"] != False:
        return False
    
    # start the race
    else:
        with open(f"./{race_name}.json", "w") as race_file:
            race_dict["Started"] = tm.time()
            json.dump(race_dict, race_file, indent=4)
        return True