import time as tm
from datetime import timedelta
import tkinter as tk

from json_functions import init_race_session, start_procedure, boat_list_add, boat_list_del



if __name__ == "__main__":


    ### TESTING

    race_name = "Critérium Manche 1"
    boat_dict = [{"Name": "Melges 24", "Sail": "SUI 1459", "Category": "B"}, {"Name": "Nemo", "Sail": "SUI 102", "Category": "A"}]

    init_race_session(race_name, boat_dict)

    tm.sleep(2)

    boat_list_add(race_name, {"Name": "Whooo", "Sail": "SUI 1004", "Category": "B"})

    tm.sleep(2)

    start_procedure(race_name)