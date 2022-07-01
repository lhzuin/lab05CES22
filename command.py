from tkinter import Tk, Button, messagebox, Text, Label
from abc import ABC, abstractmethod

class Comando(ABC): #classe abstrata (interface) para implementação dos botões
    @abstractmethod
    def executar(self):
        pass

class VerificarSaldo(Comando):
    def __init__(self, cliente):
        self.cliente = cliente
    def executar(self):
        messagebox.showinfo("Extrato", self.cliente.saldo)
        self.cliente.historico += "Saldo "

class VerificarExtrato(Comando):
    def __init__(self, cliente):
        self.cliente = cliente
    def executar(self):
        messagebox.showinfo("Extrato", self.cliente.extrato)
        self.cliente.historico += "Extrato "

class RealizarTransferencia(Comando):
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor
    def executar(self):
        self.cliente.saldo = self.cliente.saldo - self.valor
        self.cliente.extrato += f' / Transferência: {self.valor}'
        self.cliente.historico += "Transferência "
        messagebox.showinfo("Novo Saldo", self.cliente.saldo)


class Cliente: #Invoker
    def __init__(self, saldo):
        self.saldo = saldo
        self.extrato = ""
        self.historico = ""
        self.cmd = None
    def comando(self, cmd):
        self.cmd = cmd

    def executar(self):
        self.cmd.executar()


#Funções auxiliares para implementação dos botões
def transf(cliente):
    valor = int(inputtxt.get(1.0, "end-1c"))
    cliente.comando(RealizarTransferencia(cliente, valor))
    cliente.executar()

def saldo(cliente):
    cliente.comando(VerificarSaldo(cliente))
    cliente.executar()

def extrato(cliente):
    cliente.comando(VerificarExtrato(cliente))
    cliente.executar()


#Criação da interface

top = Tk()
cliente = Cliente(120)
cliente.extrato = "Depósito: 100 / Depósito: 50 / Saque: 30"
top.geometry("200x300")
d = Button(top, command = lambda: transf(cliente), text = 'Realizar Transferência') # Só deve ser pressionado após a inserção de um valor
d.pack()
b = Button(top, command = lambda: saldo(cliente), text = 'Verificar Saldo')
b.pack()
a = Button(top, command = lambda: extrato(cliente), text = 'Verificar Extrato')
a.pack()
inputtxt = Text(top)
inputtxt.pack()
top.mainloop()