def process(self, username, password, dialog):
    if username == '123' and password == '123': 
        print('your in')
        self.table()
        dialog.close()