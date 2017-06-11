class Queque(object):
    def __init__(self):
        self.vals=[]
    
    def insert(self,e):
        self.vals.append(e)
        
    def __del__(self):
        try:
            element=self.vals[0]
            self.vals.remove(self.vals[0])
            return element
        except:
            raise ValueError()