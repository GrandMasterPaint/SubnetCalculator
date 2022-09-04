import itertools

from PIL import Image as PILImage

class IpAddress(object):
    
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


    def PrintIp(self):
        print(f"The IP address is: {self.first}.{self.second}.{self.third}.{self.fourth}")


class MaskIpAddress(IpAddress):
    
    def PrintMask(self):
        print(f"The subnet mask is: {self.first}.{self.second}.{self.third}.{self.fourth}")
        
def BroadNet(Octet, Mask):
    global BroadcastIP
    global NetworkIP
    global BinaryMaths
    
    MaskBinary = []
    MaskBinary2 = []

    for num in BinaryMaths:
        if Octet >= num:
            MaskBinary = MaskBinary + list("1")
            Octet = Octet - num
        else:
            MaskBinary = MaskBinary + list("0")
    #print(MaskBinary)

    for num in BinaryMaths:
        if Mask >= num:
            MaskBinary2 = MaskBinary2 + list("1")
            Mask = Mask - num
        else:
            MaskBinary2 = MaskBinary2 + list("0")
    #print(MaskBinary2)
            
            
    for (val1, val2, num) in zip(MaskBinary, MaskBinary2, BinaryMaths):
            if val1 == str(1) and val2 == str(1):
                NetworkIP = NetworkIP + num
                
        
    for (val1, val2, num) in zip(MaskBinary, MaskBinary2, BinaryMaths):
            if val1 == str(0) and val2 == str(1):
                continue
            else:
                BroadcastIP = BroadcastIP + num
        
PlaceTup = ("First", "Second", "Third", "Fourth")

PossibleMasks = [int(255), int(254), int(252), int(248), int(240), int(224), int(192), int(128), int(0)]

BinaryMaths = [int(128), int(64), int(32), int(16), int(8), int(4), int(2), int(1)]

IpDict = {1: '', 2: '', 3: '', 4: ''}
MaskDict = {1: '', 2: '', 3: '', 4:''}

BroadcastIP = int()
NetworkIP = int()

PlaceCounter = 0

CIDR = int(0)

for key, value in IpDict.items():
    IpDict[key] = input(f"Enter a valid number between 0 and 255 for your IP address' {PlaceTup[PlaceCounter]} octet:")
    while not IpDict[key].isdecimal():
        print("Error: Character value detected. Please enter a valid number between 0 and 255:")
        IpDict[key] = input("Enter a valid number between 0 and 255:")
    while int(IpDict[key]) < 0 or int(IpDict[key]) > 255:
        print("Error: Number out or range. Type a number between 0 and 255:")
        IpDict[key] = input("Enter a valid number between 0 and 255:")
    PlaceCounter+= 1

PlaceCounter = 0

for key, value in MaskDict.items():
    MaskDict[key] = input(f"Enter a valid number for your {PlaceTup[PlaceCounter]} Subnet Mask Value:")
    while not MaskDict[key].isdecimal():
        print("Error: Character value detected. Please enter a valid number for the subnet mask value:")
        MaskDict[key] = input(f"Enter a valid number for your {PlaceTup[PlaceCounter]} Subnet Mask Value:") 
    if int(MaskDict[key]) in PossibleMasks:
        pass
    else:
         print("Invalid subnet mask value. Remember, in binary a subnet mask must be a continuous string of 1's followed by a continuous string of 0's. Please reformat the current value accordingly.")
         while int(MaskDict[key]) not in PossibleMasks:
            MaskDict[key] = input(f"Enter a valid number for your {PlaceTup[PlaceCounter]} Subnet Mask Value:") 
    if key == 1:
        pass
    elif MaskDict[int(key) - 1] != str(255) and MaskDict[key] != str(0):
        print("Invalid subnet mask value. Remember, in binary a subnet mask must be a continuous string of 1's followed by a continuous string of 0's. Please reformat the current value accordingly.")
        while MaskDict[key] != str(0):
            MaskDict[key] = input(f"Enter a valid number for your {PlaceTup[PlaceCounter]} Subnet Mask Value:")
    PlaceCounter+= 1
    

#print(IpDict)          
#print(MaskDict)

FirstOctet = IpDict[1]
SecondOctet = IpDict[2]
ThirdOctet = IpDict[3]
FourthOctet = IpDict[4]

FirstMask = MaskDict[1]
SecondMask = MaskDict[2]
ThirdMask = MaskDict[3]
FourthMask = MaskDict[4]

MaskList = [FirstMask, SecondMask, ThirdMask, FourthMask]    
NewIP = IpAddress(FirstOctet, SecondOctet, ThirdOctet, FourthOctet)
NewMask = MaskIpAddress(FirstMask, SecondMask, ThirdMask, FourthMask)


NewIP.PrintIp()
NewMask.PrintMask()

for mask in MaskList:
    if mask == str(255):
        CIDR += int(8)  
    else:
        for num in BinaryMaths:
            if int(mask) >= num:
                CIDR += int(1)
                mask = int(mask) - num
                #BroadcastIP = int(BroadcastIP + num)
            else:
                #BroadcastIP = BroadcastIP - 1
                break
print("or " + "/" + str(CIDR) + " In CIDR notation")

if int(FirstMask) < 255:
    BroadNet(int(FirstOctet), int(FirstMask))
    print("The Broadcast Address is: " + str(BroadcastIP) + "." + "255" + "." + "255" + "." + "255")
    print("The Network Address is: " + str(BroadcastIP) + "." +  + "." + "0" + "." + "0")
elif int(SecondMask) < 255:
    BroadNet(int(SecondOctet), int(SecondMask))
    print("The Broadcast Address is: " + FirstOctet + "." + str(BroadcastIP) + "." + "255" + "." + "255")
    print("The Network Address is: " + FirstOctet + "." + str(NetworkIP) + "." + "0" + "." + "0")
elif int(ThirdMask) < 255:
    BroadNet(int(ThirdOctet), int(ThirdMask))
    print("The Broadcast Address is: " + FirstOctet + "." + SecondOctet + "." + str(BroadcastIP) + "." + "255")
    print("The Network Address is: " + FirstOctet + "." + SecondOctet + "." + str(NetworkIP) + "." + "0")
else:
    BroadNet(int(FourthOctet), int(FourthMask))
    print("The Broadcast Address is: " + FirstOctet + "." + SecondOctet + "." + ThirdOctet + "." + str(BroadcastIP))
    print("The Network Address is: " + FirstOctet + "." + SecondOctet + "." + ThirdOctet + "." + str(NetworkIP))


input("You may exit the program now")
#Subnet Calculator by Brandon "Paint" Epperson