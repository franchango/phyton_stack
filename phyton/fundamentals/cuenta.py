
if __name__ == '__main__':
    class Usuario:
        def __init__(self, users, email):
            self.name = users
            self.email = email

        def make_deposit(self, monto, b):
            b.deposito(monto)
            print(self.name, '- Cuenta', b.type, '-> Deposito por:', '$', monto)
            return self

        def make_withdrawal(self, retiro, b):
            b.retiro(retiro)
            print(self.name, '- Cuenta', b.type, '-> Retiro por:', '$', retiro)
            return self

        def display_user_balance(self, b):
            print('*' * 45, '\n Usuario:', self.name)
            b.account_info()
            return self

        def transfer_money(self, b, b_tercero, monto):
            b.retiro(monto)
            b_tercero.deposito(monto)
            return self

    class Cuenta:
        def __init__(self, tipo, interes, u):
            self.type = tipo
            self.interes = interes
            self.saldo = 0
            self.users = Usuario(u.name, u.email)

        def deposito(self, monto):
            self.saldo += monto
            return self

        def retiro(self, monto):
            if self.saldo >= monto:
                self.saldo -= monto
            elif monto > self.saldo:
                print('Fondos insuficientes: cobrar una tarifa de $5')
                self.saldo -= 5
            return self

        def account_info(self):
            print('\n Tipo Cuenta:', self.type, '\n Interés:', self.interes,
                  '%' '\n Saldo: $', self.saldo, '\n', '*' * 44)
            return self

        def tasa_interes(self):
            self.saldo = self.saldo + self.saldo * self.interes / 100
            return self


    u1 = Usuario('user1202', 'francisco@gmail.com')
    u2 = Usuario('user1203', 'israel@gmail.com')

    # Cuentas de Usuario N1
    b11 = Cuenta('A', 2, u1)
    b12 = Cuenta('B', 3, u1)

    # Cuentas de Usuario N2
    b21 = Cuenta('A', 2, u2)
    b22 = Cuenta('B', 3, u2)

    u1.make_deposit(3000, b11).make_withdrawal(8000, b11).display_user_balance(b11)
    u1.make_deposit(2000, b12).make_withdrawal(400, b12).display_user_balance(b12)