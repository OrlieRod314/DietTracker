class Entry:
    def __init__(self, data):
        # name, calories, carbs, prot, fat, water
        self._name = data[0]
        self._cals = data[1]
        self._carbs = data[2]
        self._prot = data[3]
        self._fat = data[4]
    
    def get_name(self):
        return self._name
    def get_cals(self):
        return self._cals
    def get_carbs(self):
        return self._carbs
    def get_prot(self):
        return self._prot
    def get_fat(self):
        return self._fat

    
    def __str__(self):
        header = "Name\t\tCalories\tCarbohydrates\tProtein\tFat\n"
        info = f"{self.get_name()}\t\t{self.get_cals()}\t{self.get_carbs()}\t{self.get_prot()} \
        \t{self.get_fat()}"
        
        return header + info
    

def make_entries(entry_data_lists):
    entries = []
    for entry_data in entry_data_lists:
        entries.append(Entry(entry_data))
    return entries
    
