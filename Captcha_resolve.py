from hashlib import md5
from random import randint

lista = []

def generate(tamanho):
    global lista
    retorno = ''
    carac = 'abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ0123456789'
    
    while (retorno in lista):
        priv_list = []
        for _ in range(0, tamanho):
            priv_list.append(carac[randint(0, len(carac) -1)])
        retorno = ''.join(priv_list)
    
    lista.append(retorno)
    return retorno

def main():
    a = raw_input('>>')
    crip = 'aaaaaa'
    while(crip[0:4] != a):
        gen = generate(randint(4, 6))
        crip = md5(gen.encode())
        crip = crip.hexdigest()
        print('GERADO: %s  HASH: %s INICIAIS: %s' %(gen, crip, crip[0:4]))
    print('ACHOO')

main()
