from datetime import date

#Creo los productos, creo el carrito , cuando vaya a consolidar le mando el carrito a la orden y devuelvo la orden

class User():
    def __init__(self,id,user_name,balance):
        self.id=int(id)
        self.user_name=str(user_name)
        self.balance=float(balance)
        
        self.order_list=[]
        self.car=[]
    
    #Se agrega el carrito
    def add_product_to_car(self,product):
        self.car.append(product)

    #añadimos la compra al historial
    def consolidate_order(self,order_id):

        for i in self.car:
            order_id.total+=i.price
        if order_id.total>self.balance:
            print(f" NO TIENE SALDO SUFICIENTE \n El valor total de su compra es de {order_id.total} y su saldo es de {self.balance}$ ")
        else:
            print(f" La orden se ha realizado con exito.\nEl valor a pagar es de {order_id.total}")
            order_id.product_list.append(self.car)
            self.order_list.append(order_id)
    

    #añadir saldo al usuario
    def add_to_balance(self,amount):
        if type(amount)==int:
            self.balance+=amount
        else:
            print("digite un número valido")

    #Graficacion 
    def plot_order_history(self):
        pass

class Order():
    def __init__(self,id,date,status=False,total=0):
        self.id=int(id)
        self.product_list=[]
        self.date=date
        self.status=status
        self.total=total
        
class Product():
    def __init__(self, id, name, price, dict):
        self.id=int(id)
        self.name=str(name)
        self.price=float(price)
        self.price_history=dict

    def update_price(self,date,price):
        self.price=float(price)
        self.price_history[date]=price

papa=Product(1,"papa",123,{date(2022,1,12):123})
yuca=Product(2,"yuca",12,{date(2022,1,19):12})
platano=Product(3,"platano",34,{date(2022,1,2):34})
zapote=Product(4,"zapote",42,{date(2022,1,5):42})
coco=Product(5,"coco",54,{date(2022,1,4):54})

papa.update_price(date(2022,3,12),2)

juan=User(1,"juan maria",13.12)
juan.add_product_to_car(yuca)
juan.add_product_to_car(platano)
juan.add_product_to_car(zapote)
for i in range (len(juan.car)):
    print(juan.car[i].name)

mercado=Order(1,date(2022,1,2))
juan.consolidate_order(mercado)

juan.add_to_balance(3123123)
mercado=Order(1,date(2022,1,2))
juan.consolidate_order(mercado)

juan.plot_order_history()
