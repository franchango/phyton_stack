from sys import displayhook


class User:
    def __init__(self, username, email_address):# ahora nuestro método tiene 2 parametros!
        self.name = username			#y usamos los valores pasados para establecer el atributo de nombre
        self.email = email_address		# y el atributo email
        self.account_balance = 0		# el saldo de la cuenta se establece en $ 0, así que no es necesario un tercer parámetro
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal (self, amount):
        self.account_balance -= amount
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
    def display_user_balance(self):
        print(f"Usuario: {self.name}, Balance: {self.account_balance}")


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
jose = User("Jose Santamaria", "santamaria@ambato.com")
print(guido.name)	# salida: Guido van Rossum
print(monty.name)	# salida: Monty Python
print(jose.name)
guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(100)
guido.make_withdrawal(50)
print("Saldo Cuenta de Guido")
print(guido.account_balance)	
monty.make_deposit(150)
monty.make_deposit(750)
monty.make_withdrawal(25)
monty.make_withdrawal(52)
print("Saldo Cuenta de Monty")
print(monty.account_balance)	
jose.make_deposit(150)
jose.make_withdrawal(50)
jose.make_withdrawal(32)
jose.make_withdrawal(12)
print("Saldo Cuenta de Jose")
print(jose.account_balance)	    

print("------------Transferencia entre Usuarios--------------")
guido.transfer_money(jose, 5).display_user_balance()
jose.display_user_balance()
guido.display_user_balance()
guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50)
monty.display_user_balance()
