direction = 1
items = []
main1 = False
main2 = False
main3 = False
main4 = False
curent_room = None

def run(rooms,names):
    global curent_room
    rooms_dic = {}
    for room_ind,room in enumerate(rooms):
        rooms_dic[names[room_ind]] = room
    curent_room = names[0]
    while True:
        rooms_dic[curent_room].main_loop()

def switch(bol):
    if bol:
        bol = False
    else:
        bol = True
    return bol

class room:
    def __init__(self,dir1,dir2,dir3,dir4):
        self.dir = (dir1,dir2,dir3,dir4)
        self.done1 = False
        self.done2 = False
        self.done3 = False
        self.done4 = False
        
    def done(self,done):
        global main1
        global main2
        global main3
        global main4
        
        if done == "1":
            self.done1 = switch(self.done1)
        elif done == "2":
            self.done2 = switch(self.done2)
        elif done == "3":
            self.done3 = switch(self.done3)
        elif done == "4":
            self.done4 = switch(self.done4)
        elif done == "main1":
            main1 = switch(main1)
        elif done == "main2":
            main2 = switch(main2)
        elif done == "main3":
            main3 = switch(main3)
        elif done == "main4":
            main4 = switch(main4)
    
    def foword(self,data):
        print(data)
        for dat in data[:1]:
            try:
                datx = dat[3][0]
            except:
                pass
            else:
                if datx != "always":
                    if not dat[3][1]:
                        if datx == "1" and not self.done1:
                            pass
                        elif datx == "2" and not self.done2:
                            pass
                        elif datx == "3" and not self.done3:
                            pass
                        elif datx == "4" and not self.done4:
                            pass
                        elif datx == "main1" and not main1:
                            pass
                        elif datx == "main2" and not main2:
                            pass
                        elif datx == "main3" and not main3:
                            pass
                        elif datx == "main4" and not main4:
                            pass
                        else:
                            data.remove(dat)
                    else:
                        if datx == "1" and self.done1:
                            pass
                        elif datx == "2" and self.done2:
                            pass
                        elif datx == "3" and self.done3:
                            pass
                        elif datx == "4" and self.done4:
                            pass
                        elif datx == "main1" and main1:
                            pass
                        elif datx == "main2" and main2:
                            pass
                        elif datx == "main3" and main3:
                            pass
                        elif datx == "main4" and main4:
                            pass
                        else:
                            data.remove(dat)
        
        if len(data) > 2:
            global direction
            global curent_room
            choises = data[1][0]
            for option in data[2:]:
                choises += ", " + option[0]
            l = False
            while True:
                comand = input(data[0], " (", choises, ") ")
                for dat in data[1:]:
                    if dat[0] == comand:
                        if len(dat[-1]) >1:
                            for line in dat[-1][:-1]:
                                print(line)
                                i = input()
                        print(dat[-1][-1],"\n")
                        direction = dat[2]
                        curent_room = dat[1]
                        l = True
                if l:
                    break
                else:
                    print("\n", comand.capitalize(), " is not valid input.")
        else:
            if len(data[1][-1]) >1:
                for line in data[1][-1][:-1]:
                    print(line)
                    i = input()
            print(data[1][-1][-1],"\n")
            curent_room = data[1][1]
            direction = data[1][2]
            
    
    def use(self,data):
        global items
        
        for dat in data:
            datx = dat[2][0]
            if datx != "always":
                if not dat[2][1]:
                    if datx == "1" and not self.done1:
                        pass
                    elif datx == "2" and not self.done2:
                        pass
                    elif datx == "3" and not self.done3:
                        pass
                    elif datx == "4" and not self.done4:
                        pass
                    elif datx == "main1" and not main1:
                        pass
                    elif datx == "main2" and not main2:
                        pass
                    elif datx == "main3" and not main3:
                        pass
                    elif datx == "main4" and not main4:
                        pass
                    else:
                        data.remove(dat)
                else:
                    if datx == "1" and self.done1:
                        pass
                    elif datx == "2" and self.done2:
                        pass
                    elif datx == "3" and self.done3:
                        pass
                    elif datx == "4" and self.done4:
                        pass
                    elif datx == "main1" and main1:
                        pass
                    elif datx == "main2" and main2:
                        pass
                    elif datx == "main3" and main3:
                        pass
                    elif datx == "main4" and main4:
                        pass
                    else:
                        data.remove(dat)
        
        used = input("Wich item do you want to use? ")
        if used in items:
            for dat in data:
                if dat[0] == used:
                    if len(dat[0]) >1:
                        for line in dat[0][:-1]:
                            print(line)
                            i = input()
                    print(dat[-1])
                    if dat[3][0]:
                        items.append(dat[4][1])
                        print(dat[3][1][0].capitalize(), "was added to your inventory")
                    done(dat[3][1][1])
                    if dat[4]:
                        items.remove(dat)
                    else:
                        print(used.capitalize()," is not in your inventory.")
        
    def interaction(self,data):
        global items
        print("")
        if len(data[1]) >1:
            for line in data[1][:-1]:
                print(line, end = "")
                i = input()
        print(data[1][-1], "\n")
        if data[3][0]:
            items.append(data[3][1][0])
            print(data[3][1][0].capitalize(), "was added to your inventory")
        switch(data[3][1][1])
        
    def interact(self,data):
        for dat in data[1:]:
            try:
                datx = dat[2][0]
            except:
                pass
            else:
                if datx != "always":
                    if not dat[2][1]:
                        if datx == "1" and not self.done1:
                            pass
                        elif datx == "2" and not self.done2:
                            pass
                        elif datx == "3" and not self.done3:
                            pass
                        elif datx == "4" and not self.done4:
                            pass
                        elif datx == "main1" and not main1:
                            pass
                        elif datx == "main2" and not main2:
                            pass
                        elif datx == "main3" and not main3:
                            pass
                        elif datx == "main4" and not main4:
                            pass
                        else:
                            data.remove(dat)
                    else:
                        if datx == "1" and self.done1:
                            pass
                        elif datx == "2" and self.done2:
                            pass
                        elif datx == "3" and self.done3:
                            pass
                        elif datx == "4" and self.done4:
                            pass
                        elif datx == "main1" and main1:
                            pass
                        elif datx == "main2" and main2:
                            pass
                        elif datx == "main3" and main3:
                            pass
                        elif datx == "main4" and main4:
                            pass
                        else:
                            data.remove(dat)
        if len(data) > 2:
            choises = data[1][0]
            for option in data[2:]:
                choises += ", " + option[0]
            l = False
            while True:
                comand = input(data[0] + " (" + choises + ") ")
                for dat in data[1:]:
                    if dat[0] == comand:
                        self.interaction(dat)
                        l=True
                if l:
                    break
                else:
                    print("\n", comand.capitalize(), " is not valid input.")
        else:
            self.interaction(data[1])
            
    def main_loop(self):
        global direction
        while True:
            comand = input("What do you want to do? (Left, Right, Foword, Interact, Use, iNventory) ")
            if comand.capitalize() == "Left" or comand.capitalize() == "L":
                direction -=1
                if direction == 0:
                    direction = 4
                if len(self.dir[direction-1][0]) >1:
                    for line in self.dir[direction-1][0][:-1]:
                        print(line, end="")
                        i = input()
                print(self.dir[direction-1][0][-1], "\n")
            elif comand.capitalize() == "Right" or comand.capitalize() == "R":
                direction +=1
                if direction == 5:
                    direction = 1
                if len(self.dir[direction-1][0]) >1:
                    for line in self.dir[direction-1][0][:-1]:
                        print(line, end="")
                        i = input()
                print(self.dir[direction-1][0][-1], "\n")
            elif comand.capitalize() == "Foword" or comand.capitalize() == "F":
                try:
                    if self.dir[direction-1][1][0][0] == "!":
                        replace = ""
                        for symbol_ind,symbol in enumerate(self.dir[direction-1][1][0]):
                            if symbol_ind != 0:
                                replace += symbol
                        new_list = list(self.dir[direction-1][1])
                        new_list[0] = replace
                        if len(new_list[0]) >1:
                            for line in new_list[:-1]:
                                print(line, end = "")
                                i = input()
                        print(new_list[-1], "\n")
                    else:
                        self.foword(self.dir[direction-1][1])
                        break
                except:
                    self.foword(self.dir[direction-1][1])
                    break
                    
            elif comand.capitalize() == "Ineract" or comand.capitalize() == "I":
                self.interact(self.dir[direction-1][2])
            elif comand.capitalize() == "Use" or comand == "U":
                self.use(self.dir[direction-1][3])
            elif comand.capitalize() == "Inventory" or comand.capitalize() == "N":
                print("Your inventory contains: ", end = "")
                if len(items) !=0:
                    print(items[0])
                else:
                    print("nothing")
                if len(items) > 1:
                    for item in items[1:]:
                        print(", ", item, end = "")
            else:
                print(comand.capitalize(), " is not valid input.")           