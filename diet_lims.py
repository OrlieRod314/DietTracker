''' File: diet_lims.py
    Author: Orlando Rodriguez
    Purpose: Defines data structure for ideal intake per sex and age
'''
class Lim:
    '''
        Lays out the structure for a recommended diet dependent on age and sex.
        
        Data from https://health.gov/our-work/food-nutrition/2015-2020-dietary-guidelines/guidelines/appendix-7/
            Macro limits based on grams
        Fat macro calculated converting %kcal to grams, assuming 9 calories per gram of fat
            See: https://healthyeating.sfgate.com/many-grams-fat-per-day-should-children-have-5467.html
            
            get_profile():    -gets the age and sex correspondent to limit
            get_lims():       -gets the lim as a list
    '''
    def __init__(self, age, sex):
        try:
            assert age > 0
        except:
            print("Age cannot be 0 or negative")
        try:
            assert sex is 'm' or sex is 'f'
        except:
            print("Sex must be either male or female")
        
        if sex == 'm': 
            sex_string = 'Male'
        else:
            sex_string = 'Female'
        self._profile = [age, sex_string]
        
        if sex == 'm':
            if age < 4:
                self._lims = [1_000, 130, 13, 44]
            elif age < 9:
                self._lims = [1_600, 130, 19, 62]
            elif age < 14:
                self._lims = [1_800, 130, 34, 70]
            elif age < 19:
                self._lims = [3_200, 130, 52, 124]
            elif age < 31:
                self._lims = [3_000, 130, 56, 116]
            elif age < 51:
                self._lims = [2_200, 130, 56, 85]
            else:
                self._lims = [2_000, 130, 56, 77]
        else:
            if age < 4:
                self._lims = [1_000, 130, 13, 44]
            elif age < 9:
                self._lims = [1_200, 130, 19, 46]
            elif age < 14:
                self._lims = [1_600, 130, 34, 62]
            elif age < 19:
                self._lims = [1_800, 130, 34, 70]
            elif age < 31:
                self._lims = [2_000, 130, 46, 77]
            elif age < 51:
                self._lims = [1_800, 130, 46, 70]
            else:
                self._lims = [2_000, 130, 46, 77]
    
    # Getters for profile and lims
    
    def get_profile(self):
        return self._profile
    
    def get_lims(self):
        return self._lims