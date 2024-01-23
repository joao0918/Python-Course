a = 'A'   # tudo em py são objetos 
b = 'B'
c = 1.1
string = 'a={0} b={1} c={:.2f}' #podemos usar pegando o indice, ou parametro argumento nome_1=a
formato = string.format(a, b, c)

print(formato) 