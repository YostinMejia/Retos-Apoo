

class User():
    def __init__(self,id,user_name,balance,order_list):
        self.id=int(id)
        self.user_name=str(user_name)
        self.balance=float(balance)
        self.order_list=list(order_list)
    
    #Se envia a orden
    def add_product_to_car(self,id_product):
        self.order_list.append(str(id_product))

    #Terminar orden
    def consolidate_order(self,order_id):
        return self 

    def add_to_balance(self,amount):
        if type(amount)==int:
            self.balance+=amount
        else:
            print("digite un número valido")

    def plot_order_history(self):
        return self.order_list

juan=User(2,"juan marinilla",1231.123,[])
juan.add_product_to_car(123)
juan.add_to_balance(12)
print(juan.balance)
print(juan.consolidate_order(2))

class Order(User):
    def __init__(self,id,product,date,total,status):
        self.id=int(id)
        self.product_list=list(product)
        self.date=date
        self.total=float(total)
        self.status=status



class Product(Order):
    def __init__(self, id, name, price, dict):
        self.id=int(id)
        self.name=str(name)
        self.price=float(price)
        self.price_history=dict

    def update_prince(self,date,price):
        self.price=float(price)
        self.price_history.uppdate({date:price})
