import time as tm
from datetime import timedelta
import tkinter as tk

from json_functions import init_race_session, start_procedure, boat_list_add, boat_list_del



if __name__ == "__main__":
    race_name = "Critérium Manche 1"
    boat_dict = {"melges 24": {"Sail": "SUI 1459", "Category": "B"}, "little": {"Sail": "SUI 102", "Category": "A"}}

    init_race_session(race_name, boat_dict)

    tm.sleep(2)

    start_procedure(race_name)