#import sys;


class BankAccount:
    def __init__(self, accountNumber, name ):
        self.__accountNumber = accountNumber
        self.__name = name

    def get_account_number(self):
        return self.__accountNumber


    def get_name(self):
        return self.__name


    def set_account_number(self, value):
        self.__accountNumber = value


    def set_name(self, value):
        self.__name = value

class FixedDeposit(BankAccount):
    def __init__(self, accountNumber, name, duration, amount, rateOfInterest ):
        super().__init__(accountNumber,name)
        self.__duration = duration
        self.__amount = amount
        self.__rateOfInterest = rateOfInterest

    def get_duration(self):
        return self.__duration


    def get_amount(self):
        return self.__amount


    def get_rate_of_interest(self):
        return self.__rateOfInterest


    def set_duration(self, value):
        self.__duration = value


    def set_amount(self, value):
        self.__amount = value


    def set_rate_of_interest(self, value):
        self.__rateOfInterest = value
    
        
class RecurringDeposit(BankAccount):
    def __init__(self, accountNumber, name, duration, monthlyPayment, rateOfInterest ):
        super().__init__(accountNumber,name)
        self.__duration = duration
        self.__monthlyPayment = monthlyPayment
        self.__rateOfInterest = rateOfInterest

    def get_duration(self):
        return self.__duration


    def get_monthly_payment(self):
        return self.__monthlyPayment


    def get_rate_of_interest(self):
        return self.__rateOfInterest


    def set_duration(self, value):
        self.__duration = value


    def set_monthly_payment(self, value):
        self.__monthlyPayment = value


    def set_rate_of_interest(self, value):
        self.__rateOfInterest = value

class BankDemo:
    n=0
    ch='n'
    
    def bankOptions(self):
        print("******************************")
        print("  Banco Cuenta ")
        print("******************************")
        print("1. Dep??sito fijo de lectura y escritura")
        print("2. Dep??sito recurrente de lectura y escritura")
        print("3. salir")
        
        n=int(input("\nSeleccione su elecci??n: "))
        if n==1:
            self.readWriteFixedDeposit()
        elif n==2:
            self.readWriteRecurringDeposit()
        elif n==3:
            print("??????Gracias!!!")
            exit()
        else:
            print("??opci??n inv??lida! \ n int??ntalo de nuevo \ n")
            self.bankOptions() 
    
    def readWriteFixedDeposit(self):        
        print("\ nDar detalles de dep??sito fijo \ n")
        j=0
        while(j==0):
            try:
                accountNumber = int(input("Ingrese el n??mero de cuenta:").strip())
                j=1
            except:
                print("Int??ntalo de nuevo")
        name =input("Ingrese el nombre de la cuenta:").strip()
        j=0
        while(j==0):
            try:
                duration = int(input("Duraci??n:").strip())
                j=1
            except:
                print("Int??ntalo de nuevo")
        j=0
        while(j==0):
            try:
                amount = float(input("Monto: ").strip())
                j=1
            except:
                print("Int??ntalo de nuevo")
        
        j=0
        while(j==0):
            try:
                rateOfInterest = float(input("Tipo de inter??s:").strip())
                j=1
            except:
                print("Int??ntalo de nuevo")
       
        
        fd = FixedDeposit(accountNumber, name, duration, amount, rateOfInterest)
        
        print("\n Los detalles del dep??sito fijo son ... \n")
        print("\n N??mero de cuenta: ", fd.get_account_number())
        print("Nombre de la cuenta:", fd.get_name())   
        print("Duraci??n:", fd.get_duration())
        print("Monto: ", fd.get_amount())
        print("Tipo de inter??s: ", fd.get_rate_of_interest())
        
    def readWriteRecurringDeposit(self):
        print("\n Dar detalles de dep??sitos recurrentes \n")
        j=0
        while(j==0):
            try:
                accountNumber = int(input("Ingrese el n??mero de cuenta: ").strip())
                j=1
            except:
                print("Int??ntalo de nuevo ")
        name =input("Ingrese el nombre de la cuenta: ").strip()
        j=0
        while(j==0):
            try:
                duration = int(input("Duraci??n: ").strip())
                j=1
            except:
                print("Int??ntalo de nuevo")
        j=0
        while(j==0):
            try:
                monthlyPayment = float(input("Mensualidad:").strip())
                j=1
            except:
                print("Int??ntalo de nuevo")
        
        j=0
        while(j==0):
            try:
                rateOfInterest = float(input("Tasa de inter??s:").strip())
                j=1
            except:
                print("Int??ntalo de nuevo")   
      
                
        rd = RecurringDeposit(accountNumber, name, duration, monthlyPayment, rateOfInterest)
        
        print("\n Los detalles del dep??sito recurrente son ... \n")
        print("\nN??mero de cuenta: ", rd.get_account_number())
        print("Nombre de la cuenta: ", rd.get_name())   
        print("Duraci??n:", rd.get_duration())
        print("Mensualidad: ", rd.get_monthly_payment())
        print("Tipo de inter??s: ", rd.get_rate_of_interest())    
        
    def gotooptions(self):
        if self.n!=3:
            ch=input("\n??Desea continuar (s / n)?").strip()
            if(ch[0]=='y' or ch[0]=='Y'):
                BankDemo.bankOptions(self)
            else:
                print("??Gracias!")
                exit()        
        
demoObject = BankDemo()
demoObject.bankOptions()
demoObject.gotooptions()