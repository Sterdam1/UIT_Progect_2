import re

class Valid:
    
    def __init__(self):
        pass

    def isLike(self, text, name):
        if name.lower() in ['цена товара', "масса"]:
            return True if re.fullmatch(pattern=r'^(?!0\d)(\d+)(\.\d*[1-9])?$', string=text) else False
        elif name.lower() == 'свойства в формате json':
            return True if re.fullmatch(pattern=r'.+\.json$', string=text) else False
        elif name.lower() == 'дата истечения срока годности':
            return True if re.fullmatch(pattern=r'^\d{4}-\d{2}-\d{2}$', string=text) else False
        elif name.lower() == 'артикул':
            return True if re.fullmatch(pattern=r'^\d{4}$', string=text) else False
        else:
            return None
        
    

Validator = Valid()
# print(Validator.isLike('5.10' ,'цена товара'))
