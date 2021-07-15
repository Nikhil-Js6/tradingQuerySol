import os,jwt,math,webbrowser
clear = lambda: os.system('cls')

print("\n>> Hi.. Baby !!")
print("-- Welcome to the Terminal <<\n")

def op():
    print(">>Type : \n"
          "\n  >>1, fi : -To Find Compounded Growth\n",
          " >>2, fn : -To Find Net Gain/Loss\n",
          " >>3, fc : -To Find % of Change in price\n",
          " >>4, fp : -To Find Price after a given % of Change\n",
          " >>5, fr : -To Find Return and % Return\n",
          " -help : for help")
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
s = "ikNo"
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
e = "wYou"
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
c="rSec"
encmsg = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrZXkiOiJleUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpJVXpJMU5pSjkuZXlKclpYa2lPaUptWlhScGMyZ2lMQ0p6YVhSbElqb2ljRzl5Ym10NUluMC53OWdOaVpqbUpUc0I4ZFlpbWVUYzlCYWVPbjhvTzlwbTJFem5YcDFfOEh3In0.s_-06vPfDe574QzzKnzUMv7ox-uDYj7XmDOdqvYk6Ew'

##Info functions :

def onHelp():
    print("\n>> Type '[option] -in' to know more about any option"
    "\n>> For Example: 'fa -in' or 'fa -info' for more info about: 'fa' "
    "\n>> Type 'op' to see options list"
    "\n>> Type 'all -in' to know about all methods"
    "\n>> Type 'clear', 'cls', or 'clr' to clear the console"
    "\n>> Type 'rs' or 'restart' or 'rst' to restart"
    "\n>> Type 'exit' or 'ext ' to exit the program")

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

    if(opt == "fi" or opt =="1"):
        fi()
    elif(opt == "fi -in" or opt == "fi -info"):
        fiInfo()
    elif(opt == "fn" or opt =="2"):
        fn()
    elif(opt == "fn -in" or opt == "fn -info"):
        fnInfo()
    elif(opt == "fc" or opt =="3"):
        fc()
    elif(opt == "fc -in" or opt == "fc -info"):
        fcInfo()
    elif(opt == "fp" or opt =="4"):
        fp()
    elif(opt == "fp -in" or opt == "fp -info"):
        fpInfo()
    elif(opt == "fr" or opt =="5"):
        fr()
    elif(opt == "fr -in" or opt == "fr -info"):
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
    elif(opt == "help" or opt == "-help"):
        onHelp()
    else:
        print(">> Wrong Input \n Kindly choose a correct option >>")
