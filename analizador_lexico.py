import ply.lex as lex

# resultado del analisis
resultado_lexema = []

reservada = (
    'PAN',
    'PARAQOQUE',
    'AGUSTICIDAD',
    'UBUBUE',
    'VASIR',
    'NOVASIR',
    'VUELAOQUE',
    'SIONO',
    'CONTENIDO'
)
tokens = reservada + (
    'ID',
    'ENTERO',
    'LPAREN',
    'ID',
    'ASSIGN',
    'NUMBER',
    'SEMI',
    'GREATER',
    'INCREMENT',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'STRING',
    'MENOS',
    'MAS',
    'MULTI',
    'DIV',
    'IGUALMA',
    'IGUALMENO',
    'DOBLEIGUAL',
    'PUNTCOM',
    'MENOR',
    'DESIGUAL',
    'COMILLA'
)

# Reglas de Expresiones Regualres para token de Contexto simple

t_LPAREN = r'\('
t_ASSIGN = r'='
t_GREATER = r'>'
t_INCREMENT = r'\+\+'
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTI = r'\*'
t_DIV = r'\\'
t_IGUALMA = r'=>'
t_IGUALMENO = r'=<'
t_DOBLEIGUAL = r'=='
t_PUNTCOM = r';'
t_MENOR = r'<'
t_DESIGUAL = r'=!'
t_COMILLA = r'"'


def t_PAN(t):
    r'pan'
    return t

def t_PARAQOQUE(t):
    r'paraqoque'
    return t

def t_AGUSTICIDAD(t):
    r'agusticidad'
    return t

def t_CONTENIDO(t):
    r'contenido'
    return t

def t_UBUBUE(t):
    r'ububue'
    return t

def t_VASIR(t):
    r'vasir'
    return t

def t_NOVASIR(t):
    r'novasir'
    return t

def t_VUELAOQUE(t):
    r'vuelaoque'
    return t

def t_SIONO(t):
    r'siono'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"(?:\\"|[^"])*"'
    return t


t_ignore = ' \t\n'

def t_error( t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                      str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema

 # instanciamos el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("ingrese: ")
        prueba(data)
        print(resultado_lexema)