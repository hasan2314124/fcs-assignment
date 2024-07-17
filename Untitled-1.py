class Driver:
    def __init__(self, worker_id, name, start_city):
        self.worker_id = worker_id
        self.name = name
        self.start_city = start_city
   
class City:
     def __init__(self, city_name, reachable_cities):
        self.city_name = city_name
        self.reachable_cities = reachable_cities
        
