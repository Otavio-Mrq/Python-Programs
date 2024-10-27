def selecionar():
  ativo=True
  while(ativo):
    
    resposta=  input("Digite a operação: ")
    
    if(resposta=="mais"):
      somar()
    if(resposta=="menos"):
      subtrair()  
    if(resposta=="dividir"):
      dividir()
    if(resposta=="multiplicar"):
      multiplicar()
    if(resposta=="sair"):
      break
      
def somar():
  a = int(input("Digite o primeiro numero"))
  
  b = int(input("Digite o segundo numero"))
  
  resultado = a+b
  print(resultado)
def subtrair():
   a = int(input("Digite o primeiro numero"))
  
   b = int(input("Digite o segundo numero"))
   resultado=a-b
   print(resultado)

def dividir():
   a = int(input("Digite o primeiro numero"))
  
   b = int(input("Digite o segundo numero"))
   resultado=a/b
   print(resultado)

def multiplicar():
   a = int(input("Digite o primeiro numero"))
  
   b = int(input("Digite o segundo numero"))
   resultado=a*b
   print(resultado)
selecionar()