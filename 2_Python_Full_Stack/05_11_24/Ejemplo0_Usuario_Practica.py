class Usuario:
    def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0

    def hacer_compra(self, monto):  
       self.saldo_pagar += monto   
    
    def pagar_saldo(self,monto):
        if monto > self.saldo_pagar:
           print("El monto a pagar es mayor al saldo pendiente")
        else:
            self.saldo_pagar -= monto
    def mostrar_saldo_usuario(self):
        print(f"El saldo a pagar del usuario {self.nombre} {self.apellido} es de {self.saldo_pagar}")
    
    def transferir_deuda(self, otro_usuario, monto):
        otro_usuario.hacer_compra(monto)
        self.pagar_saldo(monto)


kevin = Usuario("Kevin", "duque", "kduque@codingdojo.la")
jose = Usuario("Jose", "Perez", "jperez@codingdojo.la")
everardo = Usuario("Everardo", "Gonzalez", "egonzales@codingdojo.la")



kevin.hacer_compra(1000)
kevin.hacer_compra(500)
kevin.pagar_saldo(1500)
kevin.mostrar_saldo_usuario()

jose.hacer_compra(2000)
jose.pagar_saldo(1500)
jose.pagar_saldo(200)
jose.mostrar_saldo_usuario()



jose.transferir_deuda(kevin, 300)

jose.mostrar_saldo_usuario()
kevin.mostrar_saldo_usuario()




##########Encadenar metodos
print("Ejemplo de encadenar metodos xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
class Usuario:
    def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0

    def hacer_compra(self, monto):  
       self.saldo_pagar += monto  
       return self

    def pagar_saldo(self,monto):
        if monto > self.saldo_pagar:
           print("El monto a pagar es mayor al saldo pendiente")
        else:
            self.saldo_pagar -= monto
        return self
    
    def mostrar_saldo_usuario(self):
        print(f"El saldo a pagar del usuario {self.nombre} {self.apellido} es de {self.saldo_pagar}")
        return self
    
    def transferir_deuda(self, otro_usuario, monto):
        otro_usuario.hacer_compra(monto)
        self.pagar_saldo(monto)
        return self

kevin = Usuario("Kevin", "duque", "kduque@codingdojo.la")

kevin.hacer_compra(1000).hacer_compra(500).pagar_saldo(1500).mostrar_saldo_usuario()

