class Driver:
    def __init__(self, worker_id, name, start_city):
        self.worker_id = worker_id
        self.name = name
        self.start_city = start_city
   
class City:
     def __init__(self, city_name, reachable_cities):
        self.city_name = city_name
        self.reachable_cities = reachable_cities
        
class wedeliversystem:  
    def __init__(self) :
        self.driver = {
         "ID001": {"name": "max verstappen","start_city":"beirut"},
         "iD002": {"name": "Charles Leclerc,","start_city":"tripoli"},
         "iD003": {"name": "lando Norris","start_city":"zahle"},
         "iD004": {"name": "Sebstian Vettal","start_city":"saida"},
         "ID005": {"name": "lewis hamilton","start_city":"Byblos"},
        }
self.cities ={
            "beirut":["saida","byblos"],
            "tripoli":["beirut","jounieh"],
            "zahle":["chtoura","saoufar"],
            "saida":["sour","jeye"],
            "byblos":["jounieh","amchit"],
            }
def run(self):
    print=("hello Welcome to the web delivery system ")
    while True:
            print("1 Drivers Menu")
            print("2 Cities Menu")
            print("3 Exit")
            choice = input("Enter your choice here ")
            if choice == '1':
                self.add_driver()
            elif choice == '2':
                self.view_drivers()
            elif choice == '3':
                print("Going back to main menu.")
                break
            else:
                print("wrong choice Please enter 1, 2, or 3")
            

        

        