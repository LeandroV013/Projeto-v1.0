lista_de_compras = []

def menu():
    return input('Lista de compras \nSelecione uma opção [i]nserir [a]pagar [l]istar: ')

while True:
    select = menu().lower()
    if not select or select[0] not in 'ial':
        print('Selecione uma opção válida.')
        continue


    if select[0].lower() == 'i':
        inserir = input('Digite para inserir a lista (Usar vírgula para mais de 1 item): ')
        itens = (inserir.strip() for inserir in inserir.split(','))
        lista_de_compras.extend(itens)


    elif select[0].lower() == 'a':

        if len(lista_de_compras) == 0:
            print('Sua lista está vazia. Você precisa adicionar itens antes de apagar.')
        else:
            apagar = input('digite o item a ser apagado: ')
            if apagar in lista_de_compras:
                lista_de_compras.remove(apagar)
                print(f'O item {apagar} foi apagado da sua lista.')
            else:
                print(f'O item {apagar} não está na lista de compras.')

    elif select[0].lower() == 'l':
        if len(lista_de_compras) == 0:
            print('Sua lista de compras está vazia.')
        else:
            print(lista_de_compras)
    else:
        print(f'Entrada inesperada: {select}')
