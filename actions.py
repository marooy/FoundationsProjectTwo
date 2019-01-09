# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart
from components import Store

site_name = "www.achoo.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)
    


def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    print()
    print("our Stores:")
    for store in stores:
        print(store.name)
    

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for store in stores:
        if store.name.lower() == store_name.lower():
            print(store.print_products())
            return store

            
            # return store.name
            

        
            
            
def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """

    
    print("Pick a store by typing its name or type'checkout' to pay your bills")
    storeName = ''

    while(storeName != 'checkout'):
        storeName = input()
        if( storeName != 'checkout'):
            if(get_store(storeName)):
                return pick_products(Cart(), storeName)
                
            else:
                print("Store Doesn't Exit: " + storeName) 
                print("Would you like to Pick Another store or checkout")  
    return Cart().checkout() 
               


                

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    
    print()
    order = ''
    print("Pick the items that you would like to buy by typing the product name exactly as it spelled")
    print("type 'back' to go back to the main menu where you can checkout")
    while(order != "back"):
        order = input()
        if(order != 'back'):
            for store in stores:
                if(store.name.lower() == picked_store.lower()):
                    for p in store.products:
                        
                        if(order.lower() == p.name.lower()):
                            cart.add_to_cart(p.price)
                            print(order + ' been Added to the cart')

                        # else: 
                        #     print("PRODUCT DOESN'T EXIT: " + order)
                        #     order = input()
    pick_store()            



def shop():
    """
    The main shopping functionality
    """
    # cart = Cart()
    # your code goes here!
    print_stores()
    pick_store()
    # pick_products(cart, picked_store)
    
    

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
