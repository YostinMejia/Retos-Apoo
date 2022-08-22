class User():
    def __init__(self,id,user_name,balance,order_list):
        self.id=int(id)
        self.user_name=str(user_name)
        self.balance=float(balance)
        self.order_list=list(order_list)
    
    #Se envia a orden
    def add_product_to_car(self,id_product):
        self.order_list.append(str(id_product))

    #no se     
    def consolidate_order(self,order_id):
        return 

    #añadir saldo al usuario
    def add_to_balance(self,amount):
        if type(amount)==int:
            self.balance+=amount
        else:
            print("digite un número valido")

    #no se
    def plot_order_history(self):
        pass

juan=User(2,"juan marinilla",1231.123,[])
juan.add_product_to_car(123)
juan.add_to_balance(12)
print(juan.balance)

class Order():
    def __init__(self,usuario,id,date,total,status):
        self.usuario=usuario
        self.id=int(id)
        self.product_list=usuario.order_list     #tomamos la lista del usuario
        self.date=date
        self.total=float(total)
        self.status=status

ca112d=Order(juan,1,"12/23/2222",123123,True)
print(ca112d.product_list)

class Product():
    def __init__(self, id, name, price, dict):
        self.id=int(id)
        self.name=str(name)
        self.price=float(price)
        self.price_history=dict

    def update_price(self,date,price):
        self.price=float(price)
        self.price_history[date]=price

papa=Product(2,"papa",12.3,{})
print(papa.price)
print(papa.price_history)

papa.update_price("12/321/3",123)
print(papa.price)
print(papa.price_history)