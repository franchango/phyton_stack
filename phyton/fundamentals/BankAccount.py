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
        print("1. Depósito fijo de lectura y escritura")
        print("2. Depósito recurrente de lectura y escritura")
        print("3. salir")
        
        n=int(input("\nSeleccione su elección: "))
        if n==1:
            self.readWriteFixedDeposit()
        elif n==2:
            self.readWriteRecurringDeposit()
        elif n==3:
            print("¡¡¡Gracias!!!")
            exit()
        else:
            print("¡opción inválida! \ n inténtalo de nuevo \ n")
            self.bankOptions() 
    
    def readWriteFixedDeposit(self):        
        print("\ nDar detalles de depósito fijo \ n")
        j=0
        while(j==0):
            try:
                accountNumber = int(input("Ingrese el número de cuenta:").strip())
                j=1
            except:
                print("Inténtalo de nuevo")
        name =input("Ingrese el nombre de la cuenta:").strip()
        j=0
        while(j==0):
            try:
                duration = int(input("Duración:").strip())
                j=1
            except:
                print("Inténtalo de nuevo")
        j=0
        while(j==0):
            try:
                amount = float(input("Monto: ").strip())
                j=1
            except:
                print("Inténtalo de nuevo")
        
        j=0
        while(j==0):
            try:
                rateOfInterest = float(input("Tipo de interés:").strip())
                j=1
            except:
                print("Inténtalo de nuevo")
       
        
        fd = FixedDeposit(accountNumber, name, duration, amount, rateOfInterest)
        
        print("\n Los detalles del depósito fijo son ... \n")
        print("\n Número de cuenta: ", fd.get_account_number())
        print("Nombre de la cuenta:", fd.get_name())   
        print("Duración:", fd.get_duration())
        print("Monto: ", fd.get_amount())
        print("Tipo de interés: ", fd.get_rate_of_interest())
        
    def readWriteRecurringDeposit(self):
        print("\n Dar detalles de depósitos recurrentes \n")
        j=0
        while(j==0):
            try:
                accountNumber = int(input("Ingrese el número de cuenta: ").strip())
                j=1
            except:
                print("Inténtalo de nuevo ")
        name =input("Ingrese el nombre de la cuenta: ").strip()
        j=0
        while(j==0):
            try:
                duration = int(input("Duración: ").strip())
                j=1
            except:
                print("Inténtalo de nuevo")
        j=0
        while(j==0):
            try:
                monthlyPayment = float(input("Mensualidad:").strip())
                j=1
            except:
                print("Inténtalo de nuevo")
        
        j=0
        while(j==0):
            try:
                rateOfInterest = float(input("Tasa de interés:").strip())
                j=1
            except:
                print("Inténtalo de nuevo")   
      
                
        rd = RecurringDeposit(accountNumber, name, duration, monthlyPayment, rateOfInterest)
        
        print("\n Los detalles del depósito recurrente son ... \n")
        print("\nNúmero de cuenta: ", rd.get_account_number())
        print("Nombre de la cuenta: ", rd.get_name())   
        print("Duración:", rd.get_duration())
        print("Mensualidad: ", rd.get_monthly_payment())
        print("Tipo de interés: ", rd.get_rate_of_interest())    
        
    def gotooptions(self):
        if self.n!=3:
            ch=input("\n¿Desea continuar (s / n)?").strip()
            if(ch[0]=='y' or ch[0]=='Y'):
                BankDemo.bankOptions(self)
            else:
                print("¡Gracias!")
                exit()        
        
demoObject = BankDemo()
demoObject.bankOptions()
demoObject.gotooptions()