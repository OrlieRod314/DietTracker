''' File: entry.py
    Author: Orlando Rodriguez
    Purpose: Defines data structure for an entry
'''
class Entry:
    ''' Lays out the structure for an entry. Contains fields for nutrients.
        
            make_entries():     -makes list of entry objects
    '''
    def __init__(self, data):
        self._name = data[0]
        self._cals = data[1]
        self._carbs = data[2]
        self._prot = data[3]
        self._fat = data[4]
    
    # Getters for macros
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
        ''' Converts entry object to a string
        '''
        info = f"{self.get_name()}\t{self.get_cals()}\t{self.get_carbs()}\t{self.get_prot()} \
        \t{self.get_fat()}"
        return info
    
def make_entries(entry_data_lists):
    ''' Makes the list of entries
        Argument: List of data for entries
        Returns: List of entries
    '''
    entries = []
    for entry_data in entry_data_lists:
        entries.append(Entry(entry_data))
    return entries