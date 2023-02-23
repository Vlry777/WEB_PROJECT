class Trolley:
    def __init__(self, request):
        self.request = request
        self.session= request.session
        trolley= self.session.get('trolley')
        if not trolley:
            trolley = self.session['trolley'] = {} 
        else:
            self.trolley= trolley

    def add(self, product):
        id = str(product.id)
        if id not in self.trolley.keys():
            self.trolley[id]={
                'product_id': product.id,
                'name': product.name,
                'subtotal': product.price,
                'amount': 1,
                
            }
        else:
            for key,value in self.trolley.items():
                if key == id:
                    value['amount'] = value['amount'] +1
                break
        self.save_trolley()
       

    def save_trolley(self):
        self.session['Trolley']= self.trolley
        self.session.modified = True

    def delete(self, product):
        id = str(product.id)
        if id in self.trolley:
            del self.trolley[id]
            self.save_trolley()

    def subtract_product(self,product):
        for key,value in self.trolley.items():
                if key == id:
                    value['amount'] = value['amount'] -1
                if value['amount'] <1:
                    self.delete(product)
                break
        self.save_trolley()

    def clear_trolley(self):
        self.session['trolley'] = {}
        self.session.modified = True



    



