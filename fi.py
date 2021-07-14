import os,math
clear = lambda: os.system('cls')

print(">> Hi.. Baby !!")
print("-- Welcome to the Terminal <<")

# Calculate functions :

def fi():
    i = int(input("Enter initial Amount : "))
    p = float(input("Enter % interest : "))
    t = int(input("Enter the number of cycles : "))
    sum = i
    per = p/100
    for i in range(1, t + 1):
       change = math.floor(sum)
       sum += sum * per
       profit = math.floor(sum - change)
       print(str(i) + " Cycles >> Compounded Sum : " + str(sum) + ", Profit : " + str(profit) + " <<")

def fa():
    x = int(input("Buy Price : "))
    y = int(input("Sell Price : "))
    n = int(input("Number of Shares : "))
    res = n * (y - x)
    print("The Gain/Loss is : ", res)

def fd():
    x = int(input(">> Enter first Number : "))
    y = int(input(">> Enter second Number : "))
    res = ((y - x)/x)*100
    print(">> The difference is ", str(res), "% --")

def fp():
    x = int(input(">> Enter current Price : "))
    y = float(input(">> Enter % change : "))
    per = y/100
    res = (x + (x * per))
    print(">> The final price may be : ", res)

##Info functions :

def fiInfo():
    print("\nFI stands for Find Interest:"
    "\nUsing this method you can find Componded value for an Amount"
    "\nYou just have to put Initial Amount, % Interest and Total no. of Compunding cycles.\n")

def faInfo():
    print("\nFA stands for Find Amount:"
    "\nUsing this method you can find the Amount you Gained or Lost in a trade."
    "\nYou just have to put Buy Price, Sell Price and Quantity.")

def fdInfo():
    print("\nFD stands for Find Difference:"
    "\nUsing this method you can find the % difference between two prices"
    "\nYou just have to put Initial Price and Final Price.")

def fpInfo():
    print("\nFP stands for Find Price:" 
    "\nUsing this method you can find what will the Price after given % change"
    "\nYou just have to put Current Price % Change for this price")

def allInfo():
    fiInfo()
    faInfo()
    fdInfo()
    fpInfo()

while 1:
    print("\n>> What do you want to Run --\n\n>>Type :")

    Methods = {
        'fi' : "-To Find Compounded Growth",
        'fa' : "-To Find exact Gain/Loss",
        'fd' : "-To Find % Difference",
        'fp' : "-To Find % Price Gain/Loss",
    }

    print("\n",Methods,"\n-help : for help")

    opt = input()
    opt = opt.lower()
    print("You selected",opt)

    if(opt == "fi"):
        fi()
    elif(opt == "fi -in"):
        fiInfo()
    elif(opt == "fd"):
        fd()
    elif(opt == "fd -in"):
        fdInfo()
    elif(opt == "fp"):
        fp()
    elif(opt == "fp -in"):
        fpInfo()
    elif(opt == "fa"):
        fa()
    elif(opt == "fa -in"):
        faInfo()
    elif(opt == "all -in"):
        allInfo()
    elif(opt == "clear" or opt == "cls" or opt == "clr"):
        clear()
    elif(opt == "exit" or opt == "ext"):
        print("\nGood Bye..\n>> I Love You...!!")
        exit()
    elif(opt == "rs" or opt == "restart" or opt == "rst"):
        clear()
        exit()
        execfile(fi.py)
    elif(opt == "-help"):
        print("\nType 'clear', 'cls', or 'clr' to clear the console"
        "\nType 'exit' or 'ext ' to exit the program"
        "\nType '[option] -in' to know more about any option"
        "\nFor Example: 'fa -in' for more info about: 'fa' "
        "\n type 'all in' to know about all methods")
    else:
        print(">> Wrong Input \n Kindly choose a correct option --")
