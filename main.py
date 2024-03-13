from transformer import conversor, function
from screen import limpar_tela, grafic, prints

limpar_tela()

# Entradas dos Coeficientes
while True:
    print("""\nEntradas dos Coeficientes - Equação de 2º Grau 
    [ Y = (A)xˆ2 - (B)x + (C) ]\n""")
    
    print('[OBS: Digite o Coeficiente ou press "0" p/ sair.]')
    a = input('A = ')
    
    if a == "0": 
        break
    else:
        b = input('B = ')
        c = input('C = ')
        a, b, c = conversor(a, b, c)

        enter = int(input(f"""\nSua equação é: A = {a} | B = {b} | C = {c}
                        
        [ Y = {a}xˆ2 - {b}x + {c} ]

        >> Escolha: [1] p/Continuar; 
                    [2] p/Corrigir; 
                    [3] p/Sair
                    
        >> Resposta: """))

        while True:
            if enter == 3: break # Sair
            elif enter == 2: # Corrigir
                
                a = input('A = ')
                b = input('B = ')
                c = input('C = ')
                
                a, b, c = conversor(a, b, c)
                
                enter = 1
                print(f"""Sua equação é: A = {a} | B = {b} | C = {c}                  
        [ Y = {a}xˆ2 - {b}x + {c} ]""")
                    
            if enter == 1: # Processar -> Gráfico
                if a != 0:
                    if function(a, b, c): # Validar Gráfico
                        X, Y, x1, x2, delta, Xv, Yv, a, b, c = function(a, b, c)
                        prints(a, b, c, X, Y, x1, x2, delta, Xv, Yv)
                        grafic(X, Y, x1, x2, Xv, Yv)
                        break  
                    else: 
                        print('Raiz não Existe!')
                    break      
                else: 
                    print( 'Não é uma equação de 2° Grau.')
                break
            break

            

