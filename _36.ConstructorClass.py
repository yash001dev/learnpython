#Constructor IN Python
class ClientEmail:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self):
        print("draw")
    
clientEmail=ClientEmail(10,20)
print(clientEmail.x)
