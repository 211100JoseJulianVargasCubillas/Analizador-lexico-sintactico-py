import ply.yacc as yacc
from analizador_lexico import tokens
from analizador_lexico import analizador

# resultado del analisis
resultado_gramatica = []

def p_init(p):
    '''init : inicio
            | opcion2
            | opcion3
            | opcion4'''
            
def p_inicio(p):
    '''inicio : PARAQOQUE LPAREN variable ID ASSIGN NUMBER PUNTCOM ID operador NUMBER PUNTCOM ID INCREMENT PUNTCOM RPAREN LBRACE  cualquier RBRACE
              | PARAQOQUE LPAREN variable ID PUNTCOM ID operador NUMBER PUNTCOM ID INCREMENT PUNTCOM RPAREN LBRACE  cualquier RBRACE'''
    
def p_opcion2(p):
    '''opcion2 : AGUSTICIDAD variable ID ASSIGN ident
               | AGUSTICIDAD variable ID'''

def p_opcion3(p):
    '''opcion3 : VASIR LPAREN ID operador ident RPAREN LBRACE cualquier RBRACE NOVASIR LBRACE cualquier RBRACE'''    

def p_opcion4(p):
    '''opcion4 : VUELAOQUE SIONO LPAREN  RPAREN LBRACE cualquier RBRACE
               | VUELAOQUE ID LPAREN variable ID RPAREN LBRACE cualquier RBRACE'''
def p_cualquier(p):
    '''cualquier : opcion2
                | opcion4
                | ident
                | CONTENIDO'''
def p_variable(p):
    '''variable : UBUBUE
                | PAN'''

def p_operador(p):
    '''operador : GREATER
                | IGUALMA
                | IGUALMENO
                | DOBLEIGUAL
                | MENOR
                | DESIGUAL
                | ASSIGN'''
def p_ident(p):
    '''ident : ID  
             | NUMBER'''

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico EOF".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)



# instanciamos el analizador sistactico
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else: print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica

if __name__ == '__main__':
    while True:
        try:
            s = input(' ingresa dato >>> ')
        except EOFError:
            continue

        prueba_sintactica(s)