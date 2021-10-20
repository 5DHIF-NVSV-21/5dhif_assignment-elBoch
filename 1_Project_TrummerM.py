class Menu:
    def __init__(self):
        self.total = 0
        self.order_options = [('Pizza', 8), ('Burger', 7), ('Wiener Schnitzel', 10)]
        self.order = {}
        pass

    def main_menu(self):
        option = 0
        print('-----MENU-----')
        print('(0) Menu')
        print('(1) Show Order')
        print('(2) Confirm Order')
        print('(3) Cancle Order\n')

        while True:
            try:
                option = int(input('Choose Option: '))
                if option < 0 or option > 3:
                    raise ValueError()
                break
            except ValueError:
                print('Invalid Answer. Please enter a number shown on screen')
                
        
        if option == 0:
            self.actual_menu()

        elif option == 1:
            self.print_order()

        elif option == 2:
            self.confirm_order()

        elif option == 3:
            self.cancle_order()


        pass

    def actual_menu(self):
        option = 0
        print('-----MENU-----')
        for i in range(len(self.order_options)):
            name, price = self.order_options[i]
            print(f'({i}) {name} - {price}€')

        print(f'({len(self.order_options)}) Never mind')
        print('--------------')
        while True:
            try:
                option = int(input('Choose Option: '))
                if option < 0 and option > len(self.order_options):
                    print(f'option: {option}')
                    raise ValueError()

                elif option == len(self.order_options):
                    self.main_menu()

                else:
                    name, price = self.order_options[option]
                    try:
                        self.order.update({name: self.order[name]+1})

                    except KeyError:
                        print('exception')
                        self.order.update({name: 1})
                    
                break
            except ValueError:
                print('Invalid Answer. Please enter a number shown on screen')
            
        self.main_menu()
        pass

    def print_order(self):
        self.total = 0
        for item in self.order.keys():
            print(f'{item} - {self.order[item]}x')
            for item2 in self.order_options:
                name, price = item2
                if name == item:
                    self.total += price * self.order[item]

        print(f'Your total amount is {self.total}€')

        self.main_menu()
        pass

    def confirm_order(self):
        self.total = 0
        for item in self.order.keys():
            print(f'{item} - {self.order[item]}x')
            for item2 in self.order_options:
                name, price = item2
                if name == item:
                    self.total += price * self.order[item]

        print(f'Your total amount is {self.total}€')
        while True:
            answer = input('Confirm Order? (y/n): ').lower()
            if answer == 'y':
                print('Thank you, enjoy your meal!')
                break

            elif answer == 'n':
                self.main_menu()
                break
            
    def cancle_order(self):
        self.total = 0
        for item in self.order.keys():
            print(f'{item} - {self.order[item]}x')
            for item2 in self.order_options:
                name, price = item2
                if name == item:
                    self.total += price * self.order[item]

        print(f'Your total amount is {self.total}€')
        while True:
            answer = input('Cancel Order? (y/n): ').lower()
            if answer == 'y':
                print('Thank you anyways')
                break

            elif answer == 'n':
                self.main_menu()
                break

if __name__ == "__main__":
    m = Menu()
    m.main_menu()
    pass