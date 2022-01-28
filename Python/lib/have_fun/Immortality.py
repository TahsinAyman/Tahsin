class Immortality():
    power = 0

    def __init__(self):
        pass
    
    
    def kill_hecker(self):
        command = 'print("$sudo kill hekcer")'
        eval('print("$sudo kill hekcer")')
        if command == 'print("$sudo kill hekcer")':
            while True:
                self.power -= 1
                print('Hecker Power', self.power)

    def revive_Tahsin(self):
        command = 'print("$sudo revive Tahsin")'
        eval('print("$sudo revive Tahsin")')
        if command == 'print("$sudo revive Tahsin")':
            while True:
                self.power += 1
                print('Tahsin Power', self.power)

    def beluga_gf_noob(self):
        command = 'print("$sudo ban beluga_gf")'
        death = bool()
        
        eval('print("$sudo ban beluga_gf")')
        if command == print("$sudo ban beluga_gf"):
            death = True
            if death:
                print('belug_bf Died')

if __name__ == '__main__':
    immportality = Immortality()
    while True:
        print('0. Exit')
        print('1. Kill Hecker')
        print('2. Revive Tahsin')
        print('3. Beluga GF Noob')
        choice = input('Enter your choice: ')
        if choice == 'Kill Hecker':
            immportality.kill_hecker()
        elif choice == 'Revive Tahsin':
            immportality.revive_Tahsin()
        elif choice == 'Beluga GF Noob':
            immportality.beluga_gf_noob()
        elif choice == 'Exit':
            exit()
        else:
            print('Wrong Command')
