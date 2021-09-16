lhc = [71, 65, 63, 66, 68]
sumUp1 = sum(lhc) / 5
sed = [62, 47, 45, 51, 56]
sumUp2 = sum(sed)/5
cg = [76, 69, 60, 64, 69]
sumUp3 = sum(cg)/5
flg = [46, 35, 33, 40, 44]
sumUp4 = sum(flg)/5
chn = [77, 68, 61, 65, 67]
sumUp5 = sum(chn)/5


def display():
    print("Welcome to city temperature check")
    print("I will show you the sequence of city and their average dailu temperature:")
    cName = ["1. Sedona","2. Flagstaff","3. Lake Havasu City", "4. Casa Grande", "5. Chandler", "0. To know best city to visit"]
    for b in cName:
        print(b)
def chooseCity():
    while True:
        choose = int(input("\nEnter City No. to check temperature:\n"))
        if choose in [0,1,2,3,4,5]:
            if choose == 1:
                Lhc()
            elif choose == 2:
                Sedona()
            elif choose == 3:
                Chn()
            elif choose == 4:
                Flg()
            elif choose == 5:
                Cg()
            elif choose == 0:
                city_temp_list = [sumUp1,sumUp2,sumUp3,sumUp4,sumUp5]
                best_city = min(city_temp_list)
                print("Best city to visit => Flagstaff:", best_city,end = '°C')
                break
        else:
            print("Invalid city input")

def Sedona():
    sed
    sed.sort()
    print("\nSedona Temperature: ", sed)
    print("Average daily temp:", sumUp2, end=" °C")
def Lhc():
    lhc
    lhc.sort()
    print("\nLake Havasu City Temperature: ", lhc)
    print("Average daily temp:", sumUp1, end=" °C")
def Cg():
    cg
    cg.sort()
    print("\nCasa Grande Temperature: ", cg)
    print("Average daily temp:", sumUp3, end=" °C")
def Flg():
    flg
    flg.sort()
    print("\nFlagstaff Temperature: ", flg)
    print("Average daily temp:", sumUp4, end=" °C")
def Chn():
    chn
    chn.sort()
    print("\nChandler Temperature: ", chn)
    print("Average daily temp:", sumUp5, end=" °C")

display()
chooseCity()
