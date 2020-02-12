# -*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * ammount

def run():
    print('CALCULADORA')
    print('Convierte de pesos meicanos a pesos colombianos.')
    print('')

    ammount = float(raw_input('Ingresa la cantidad de pesos mexicanos que quieres convertir'))

    result = foreign_exchange_calculator(ammount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount,result))
    print('')

if __name__ == '__main__':
    run()