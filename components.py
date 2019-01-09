# CLASSES AND METHODS
import numbers
class Store():
    
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name = name
        self.products = []
        
        
        
    
    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        # print(self.products)
        for i in self.products:
            print(i)


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        # your code goes here!
        return " Product Name: %s \n Description : %s \n Price: %s KD" %(self.name,self.description,self.price)


class Cart():
    products = []

    
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.products

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!

        self.products.append(product)
        # print(self.products) 


    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!

        total = 0
        
        list_2 = [num for num in self.products if isinstance(num, (int,float))]
        for x in list_2:
            total = total + x
            
            
        return total

        


        # for i in self.products:
        #     print(i)
        #     total = total + i
        # return total


    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        print( "the total price is %s" % str((self.get_total_price())))


    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
        confirms = ''
        self.print_receipt()   
        print("to preceed enter 'confirms' to cancel enter 'cancel'")
        confirms = input()

        if (confirms == 'confirms'):
            print("Your order has been placed")
        elif(confirms == 'cancel'):
            print('Your order has been cancelled')    

