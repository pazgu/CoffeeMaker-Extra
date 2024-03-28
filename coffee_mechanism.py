# decorator wrapper
def my_decorator(run_main):
    def wrapper():
        print("Welcome to CoffeeMaker Extra!")
        func = run_main()
        make_run = func()
        print("Thank you for using CoffeeMaker Extra! Have a great day!")
        return make_run
    return wrapper

##################################################################################### 
        
def are_resources_sufficient(selected_beverage, availables_ingredients, beverages):
                    
    match selected_beverage:
        case "espresso":
            counter_item = 0   
        case "latte":
            counter_item = 1   
        case "cappuchino":
            counter_item = 2   
            
    if beverages[counter_item][selected_beverage][counter_item] > availables_ingredients[counter_item]:
        print(f"We run out of coffee. Our sincere apology")
        return False
        
    beverages = [{"espresso": (50, 20, 5)}, {"latte": (20, 20, 30)}, {"cappuchino": (30, 20, 20)}]    
    # tupple organize as: water, coffee, milk  
    availables_ingredients = [70, 50, 80]
    #list contains quantities water, coffee, and milk
    
    return True   
   
#####################################################################################           

def process_coins(price):

    user_input = {
        "Q": 0.25,
        "D": 0.1,
        "N": 0.05,
        "P": 0.01
    }
    
    user_payment = 0.0
    change = 0.0
    print("For payment we recieve- quarters, dimes, nickels, and pennies")
    while (user_payment < price):
        print("""Please choose the kind of coin you want to insert:
            for quarters type Q
            for dimes type D
            for nickels type N
            and for pennies type P""")
        selected_coin = input(">> ").upper()
        
        if selected_coin not in user_input:
            print("Invalid coin. Please insert a valid coin.")
            continue
        
        user_payment += user_input[selected_coin]
        if user_payment > price:
            change = user_payment- price
            print(f"Here is your {round(change, 2)} dollars in change")
            break
        elif user_payment == price:
            print(f"Thank you and enjoy your beverage!")
            break
        else:    
            print(f"you are left to pay {round(abs(user_payment- price), 2)} dollars")
    return user_payment        
    
######################################################################################

def is_transaction_successful(money_received, drink_cost):
    profit = 0
    if (money_received >= drink_cost):
        profit += money_received
        print("Payment is successful")
        return True
    return False
######################################################################################


def make_coffee(input_beverage, beverages, availables_ingredients):

    match input_beverage:
        case "espresso":
            counter_item = 0   
        case "latte":
            counter_item = 1   
        case "cappuchino":
            counter_item = 2 
            
    availables_ingredients[counter_item] -= beverages[counter_item][input_beverage][counter_item]

    # tupple organize as: water, coffee, milk  
    #list contains quantities water, coffee, and milk
    prices = {"espresso": 9, "latte": 12, "cappuchino":15}
######################################################################################       

def run_main():
   
    beverages = [{"espresso": (50, 20, 5)}, {"latte": (20, 20, 30)}, {"cappuchino": (30, 20, 20)}]    
    # tupple organize as: water, coffee, milk 
     
    # print(beverages[0]["espresso"][0])  
     
    availables_ingredients = [70, 50, 80]
    #list contains quantities water, coffee, and milk
    prices = {"espresso": 9, "latte": 12, "cappuchino":15}
    
    print("""Please choose your prefered beverage:
            for cappuchino type C
            for latte type L
            for espresso type E
            if you want to cancel action type Q""")
    
    user_input = {
        "C": "cappuchino",
        "L": "latte",
        "E": "espresso"
    }
    
    while True:
        input_beverage = input(">> ").upper()
        if input_beverage in user_input:
            break
        elif input_beverage == 'Q':
            return False
        else:
            print("Invalid option. Please choose again.")
            
    print(user_input[input_beverage])
    selected_beverage = are_resources_sufficient(user_input[input_beverage], availables_ingredients, beverages)
    if selected_beverage == True:
        print ("For the payment part:")
        user_payment = process_coins(prices[user_input[input_beverage]])
        transaction_successful = is_transaction_successful(user_payment, prices[user_input[input_beverage]])
        if transaction_successful:
            make_coffee(user_input[input_beverage], beverages, availables_ingredients)
    else:
        print("Have a good day!")
        
my_decorator(run_main())