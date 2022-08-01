class Remote:
    def __init__(self):
        self.channel_list = [0, 2, 5, 7, 10]
        self.channel = self.channel_list[0]
        self.volume = 3
        self.power_status = False
        self.cnt = 0
        self.status = ""

    def change_channel(self, channel=None):
        if self.power_status:
            if not channel:
                self.channel = self.channel_list[self.channel_list.index(self.channel) + 1]
            else:
                if channel in self.channel_list:
                    self.channel = channel
                else:
                    self.status = "Channel Not Found"
        else:
            self.status = "Power is Off Channel Cannot be Changed"


    def change_volume(self, volume=None):
        if self.power_status:
            if not volume:
                self.volume += 1
            else:
                self.volume += volume
        else:
            self.status = "Power is Off volume Cannot be changed"
    
    def power(self):
        self.cnt += 1
        if self.cnt % 2 != 0:
            self.power_status = True
        else:
            self.power_status = False



    def info(self):
        if not self.status:
            if self.power_status:
                print("Power is On")
            else:
                print("Power is Off")
            print(f"Channel: {self.channel}")
            print(f"Volume: {self.volume}")
        else:
            print(self.status)
            if self.power_status:
                print("Power is On")
            else:
                print("Power is Off")
            print(f"Channel: {self.channel}")
            print(f"Volume: {self.volume}")

remote = Remote()
remote.power()
remote.change_channel(3)
remote.info()
