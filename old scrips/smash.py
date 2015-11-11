records = {"matt":{'total games': [], 'kills': [], 'sds': [], 'placement':[]},
           "kevin":{'total games': [], 'kills': [], 'sds': [], 'placement':[]},
           "karel":{'total games': [], 'kills':[], 'sds': [], 'placement':[]}}

class smash(object):
    
    def __init__(self):

        global records
        
        self.records = records
        
    def collectdata(self):

        
        for player in self.records:
            
            print()
            
            for key in self.records[player].keys():
                
                val = int(input("Enter {}'s {}:".format(player, key)))
                
                self.records[player][key].append(val)
                
    
    def displaydata(self):

        for player in self.records:
            print('\n{}\'s stats: \n'.format(player))
            for key in self.records[player]:
                print("{}: {}"
                      .format(key, self.records[player][key]))
            


def test():
    tester = smash()
    tester.collectdata()
    tester.displaydata()

def collect():
    pass







            
                            
                
                
        

    
    
    
        
