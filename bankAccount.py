

from cardHolder import card_holder

class ATM_Menu():

        def __init__(self):

            self.card_holders = [
                {"firstname": "Mariam","lastname": "Tamer","card_number": 1234567890123456,"pin" : 1234,"balance": 1000}, 
                {"firstname": "Menna","lastname": "Tamer","card_number": 11111111111111,"pin" : 5555,"balance": 2200}, 
                {"firstname": "Amany","lastname": "Ali","card_number": 987654321987654,"pin" : 2514,"balance": 4500}, 
                {"firstname": "Omar","lastname": "Omar","card_number": 5554567890123456,"pin" : 6500,"balance": 2000}, 
            ]
        

        def menu(self): 
                        print("------------------------------")
                        print("------------------------------")
                        print("Welcome to the ATM_Menu")
                        print("------------------------------")
                        print("------------------------------")
                        print("1. Deposit")
                        print("2. Withdrawal")
                        print("3. Check Balance")
                        print("4. Exit")
                        print("------------------------------")
                       

        def deposit(self, card_holder):
                
                try:
                     deposit = float(input("Enter the deposit amount: ").strip())

                    # new = old + change 
                    # set = get + change aka deposit
                    #  card_holder.set_balance( card_holder.get_balance() + deposit )
                     new_balance = card_holder.get_balance() + deposit
                     card_holder.set_balance(new_balance)
    
                     print(" Your balance now is " + card_holder.get_balance())  
                    #  return " Your balance now is " + card_holder.get_balance()  

                except:
                        print("Invalid Iption")


        def withdraw(self,card_holder):
                
                try:
                      withdraw = float(input(" ").strip())
                      if card_holder.get_balance() < withdraw : 
                              print("Insufficient amount to withdraw")
                      else:
                        card_holder.set_balance( card_holder.get_balance() - withdraw )
                        print(" Your balance now is " + card_holder.get_balance())   

                except:
                        print("Invalid Iption")




        def check_balance(self, card_holder):
                print(" Your balance is " + card_holder.get_balance())


        def run(self):
               
               while True : 
                      
                      self.menu()
                      option = int(input(" ").strip())
                      if option == 1:
                            card_number = int(input("PLease enter your card number : ").strip())
                            pin = int(input(" Please enter your pin : ").strip())
                            flag = False
                            for i in self.card_holders:
                                   if i["card_number"] == card_number and i["pin"] == pin:
                                                        self.deposit(i)
                                                        flag = True
                                                        break
                                   if not flag: 
                                          print("Invalid card number or pin")
                                          continue
                                                
                      elif option == 2:
                            card_number = int(input("PLease enter your card number : ").strip())
                            pin = int(input(" Please enter your pin : ").strip())
                            flag = False
                            for i in self.card_holders:
                                   if i["card_number"] == card_number and i["pin"] == pin:
                                                        self.withdraw(i)
                                                        flag = True
                                                        break
                                   if not flag: 
                                          print("Invalid card number or pin")
                                          continue
                            
                      elif option == 3:
                            card_number = int(input("PLease enter your card number : ").strip())
                            pin = int(input(" Please enter your pin : ").strip())
                            flag = False
                            for i in self.card_holders:
                                   if i["card_number"] == card_number and i["pin"] == pin:
                                                        self.check_balance(i)
                                                        flag = True
                                                        break
                                   if not flag: 
                                          print("Invalid card number or pin")
                                          continue
                            
                      elif option == 4:
                            break 
                      else:
                            print("Invalid option")






# if this is running, and if this is the main method here, 
# then instantiate a new object user from the card holder class

if __name__ == "__main__":
       current_user = card_holder("","","","","")  # blank so we could use our database
       
       current_menu = ATM_Menu()
       current_menu.run()
       current_user.run()



