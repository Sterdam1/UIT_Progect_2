import re

class Valid:
    
    def __init__(self):
        pass

    def isLike(self, text, name):
        if name == 'цена товара':
            return True if re.fullmatch(pattern=r'\d+\.\d', string=text) else False
        else:
            return None
        
    

Validator = Valid()
