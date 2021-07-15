import os,math
clear = lambda: os.system('cls')

def op():
   Methods = {
        'fi' : ">To Find Compounded Growth",
        'fn' : ">To Find Net Gain/Loss",
        'fc' : ">To Find % of Change in price",
        'fp' : ">To Find Price after a given % of Change",
        'fr' : ">To Find Return and % Return"
   }
   
   print(">> Hi.. Baby !!")
   print("-- Welcome to the Terminal <<\n\n>>Type :")
   print("\n",Methods,"\n-help : for help")
op()

# Calculate functions :

def fi():
    print("Calculate Compounded Amount :")
    i = int(input("Initial Amount : "))
    p = float(input("Percent interest : "))
    t = int(input("Number of Time Cycles : "))
    sum = i
    per = p/100
    for i in range(1, t + 1):
       change = int(math.floor(sum))
       sum += sum * per
       profit = int(math.floor(sum - change))
       print(str(i) + " Cycles >> Compounded Sum : " + str(sum) + ", Profit : " + str(profit))

def fn():
    print("Calculate Net Gain : ")
    x = float(input(">> Buy Price : "))
    y = float(input(">> Sell Price : "))
    n = int(input(">> Number of Shares : "))
    res = n * (y - x)
    print(">> The Net Gain is : ", res)

def fc():
    print("Calculate % Gain : ")
    x = float(input(">> Buy Price : "))
    y = float(input(">> Sell Price : "))
    res = ((y - x)/x)*100
    print(">> The % change is ", res, "%")

def fp():
    print("Calculate Future Price : ")
    x = float(input(">> Current Price : "))
    y = float(input(">> Percent Change : "))
    per = y/100
    res = (x + (x * per))
    print(">> The final price may be : ", res)
   
def fr():
    print("Calculate Net Return : ")
    n = int(input(">> Amount : "))
    x = float(input(">> Buy Price : "))
    y = float(input(">> Sell Price : "))
    quant = math.floor((n/x))
    ret = (quant * y)
    print(">> Net Value :", ret)
    pret = (((ret - n)/n)*100)
    print(">> Return(%) :", pret, "%")
    gain = (quant * (y - x))
    print(">> Net Gain : ", gain)   


##Info functions :

def fiInfo():
    print("\nFI stands for Find Interest: \nUsing this method you can find Compounded value for an Amount"
    "\nYou just have to put Initial Amount, % Interest and Total no. of Compunding cycles.\n")

def fnInfo():
    print("\nFA stands for Find Net Amount: \nUsing this method you can find the Net Gain/Lost in a trade."
    "\nYou just have to put Buy Price, Sell Price and Quantity.")

def fcInfo():
    print("\nFC stands for Find Change: \nUsing this method you can find the % of Change in prices"
    "\nYou just have to put Initial Price and Final Price.")

def fpInfo():
    print("\nFP stands for Find Price: \nUsing this method you can find how much the price will be,after given % change"
    "\nYou just have to put Current Price % Change for this Price.")
     
def frInfo():
    print("\nFR stands for Find Return: \nUsing this method you can find the Net Value, %Return and Net Gain in a trade"
    "\nYou just have to put the Investment Amount, Buy Price and Sell Price.")
   
def allInfo():
    fiInfo()
    fnInfo()
    fcInfo()
    fpInfo()

while 1:
    print("\n>> What do you want to Run >>")
    opt = input()
    opt = opt.lower()

    if(opt == "fi"):
        fi()
    elif(opt == "fi -in"):
        fiInfo()
    elif(opt == "fn"):
        fn()
    elif(opt == "fn -in"):
        fnInfo()
    elif(opt == "fc"):
        fc()
    elif(opt == "fc -in"):
        fcInfo()
    elif(opt == "fp"):
        fp()
    elif(opt == "fp -in"):
        fpInfo()
    elif(opt == "fr"):
        fr()
    elif(opt == "fr -in"):
        frInfo()
    elif(opt == "all -in"):
        allInfo()
    elif(opt == "clear" or opt == "cls" or opt == "clr"):
        clear()
    elif(opt == "op" or opt == "options"):
        op()
    elif(opt == "exit" or opt == "ext"):
        print("\nGood Bye..\n>> I Love You...!!")
        exit()
    elif(opt == "rs" or opt == "restart" or opt == "rst"):
        clear()
        os.system('fi.py')
    elif(opt == "-help"):
        print("\nType '[option] -in' to know more about any option"
        "\nFor Example: 'fa -in' for more info about: 'fa' "
        "\nType 'op' to see options list"
        "\nType 'all -in' to know about all methods"
        "\nType 'clear', 'cls', or 'clr' to clear the console"
        "\nType 'rs' or 'restart' or 'rst' to restart"
        "\nType 'exit' or 'ext ' to exit the program")
    else:
        print(">> Wrong Input \n Kindly choose a correct option >>")
