from os import system, name  # Modulo pra Limpar o Terminal
import matplotlib.pyplot as plt  # Modulo de Gráfico


def limpar_tela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
        
def grafic(x, y, x1, x2, Xv, Yv):  # Gráfico
    
    # plt.style.use('fivethirtyeight') # Modelo 1
    plt.style.use('bmh')               # Modelo 2
    fig, ax = plt. subplots()
    ax.plot(x, y, linewidth=2, color='red') 
    plt. scatter(x, y, color='red', marker="o") 
    plt. title("Gráfico Equação 2° Grau\n", fontsize=15) 
    
    plt.plot((-100, 100), (0, 0), color='black', linewidth=1)
    plt.plot((0, 0), (-100, 100), color='black', linewidth=1)
        
    if x1 > x2: # X' > X" -> CRESCENTE
        plt.annotate(f"X':{x1} ",[x1+1,1], color='black')
        plt.annotate(f'X":{x2}',[x2-4.5,1], color='black')
        
        plt.annotate(f"↑",[Xv-(Xv*0.09),Yv-(Yv*-0.09)], color='black')
        plt.annotate(f'V({Xv}; {Yv})',[Xv+(Xv*0.1),Yv-(Yv*-0.09)], color='black')
        
        plt. scatter(x1, 0, color='blue', marker="o") 
        plt. scatter(x2, 0, color='blue', marker="o")
        
    elif x1 < x2: # X' < X" -> DECRESCENTE 
        plt. scatter(x1, 0, color='blue', marker="o") 
        plt. scatter(x2, 0, color='blue', marker="o")

        plt.annotate(f"↓",[Xv,Yv+(Yv*0.09)], color='black')
        plt.annotate(f'V({Xv}; {Yv})',[Xv+(Xv*0.99),Yv+(Yv*0.09)], color='black')
        
        plt.annotate(f"X':{x1} ",[x1-4.5,1], color='black')
        plt.annotate(f'X":{x2}',[x2+1,1], color='black')

    plt.legend([r'$F(x) = {a}xˆ2 - {b}x + {c}$'], loc = 'upper left')
    plt.xlabel("Valores de X", fontsize=12) 
    plt.ylabel("Valores de Y", fontsize=12) 
    
    plt.xticks(range(-100,101,1), fontsize=7)
    plt.yticks(range(-100,101,1), fontsize=7)
    
    plt.xlim (-10,10)
    plt.ylim (-10,10)

    return plt.show()        
        
def prints(a, b, c, X, Y, x1, x2, delta, Xv, Yv):
    print(f'>> Y = {a}xˆ2 - {b}x + {c}\n')
                
    print(f'Δ = {b}ˆ2 - 4 * {a} * {c}')
    print(f' Δ = {delta}\n')
    
    print(f"X' = -{b} + √{delta} / 2 * {a}")
    print(f" X' = {x2}\n")
    
    print(f'X" = -{b} - √{delta} / 2 * {a}')
    print(f' X" = {x1}\n')
    
    print(f"Xv = -{b}/2*{a}")
    print(f"Xv = {Xv}\n")
    
    print(f"Yv = - {delta}/ 4*{a}")
    print(f"Yv = {Yv}\n")
    

    print(f"""X = {X}
Y = {Y}""")