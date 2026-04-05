nome = "Geraldo"

""" 
dicas python early return
 """
""" 
def saudacao(nome=None):
  if not nome:    
    return "Ola visitante"
  
  return f"Ola, {nome}"

#res = saudacao()
#print(res)
def calc(x, y, action='+'):
  if not action:
    return "definir uma action"
  
  if(action == '+'):
    return x + y
  if(action == '*'):
    return x * y

  return 'action invalid'


print(calc(2, 5, 'vegege')) """
# EXE2
def pode_executar(allow_manual):

  if not isinstance(allow_manual, bool):
    return "Valor inválido para allow_manual"

  if(allow_manual):
      return "Execução manual permitida"

  return "Execução manual bloqueada"

#print(pode_executar(1212))

# 🧩 Exercício 3 — Timeout válido

def validar_timeout(timeout):
  if not timeout:
      return "definir um timeout"
  if not isinstance(timeout, int):
      return "valor invalido para timeout"

  if(timeout <= 0):
    return "timeout invalido"
  
  if(timeout > 60):
    return "timeout muito alto"
  
  return "timeout OK"

print(validar_timeout(100))