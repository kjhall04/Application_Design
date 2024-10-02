#! python3

class Printer():
    def __init__(self, material, brand):
        self.material = material
        self.brand = brand

    def start_print(self):
        print('All ready to print.')

class Resin_Printer(Printer):
    def __init__(self, material, brand, size):
        super().__init__(material, brand)
        self.size = size

    def start_print(self, button):
        if button.lower() == 'on':
            print('All ready to print.')
        else:
            print('The printer is not on.')

    def end_print(self, stop):
        if stop:
            print('The print will end immediatly.')
        else:
            print('The print was unable to stop.')

if __name__ == '__main__':

    # create a printer object through the resin printer sub class
    printer = Resin_Printer('resin', 'Elegoo', '190 x 100 x 200')
    
    # print a statement showing the printer brand through the brand parameter
    print('Your printer is made by ' + printer.brand)
    
    # calling the start_print function and passing the string 'on'
    printer.start_print('on')
    
    # calling the end_print funcion, but giving the stop attribute the False value
    printer.end_print(stop = False)