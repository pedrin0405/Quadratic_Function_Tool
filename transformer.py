def conversor(a, b, c):
    if a:
        if '.' in a:
            a = float(a)
        elif ',' in a:
            a = float(a.replace(',','.'))
        else:
            a = int(a)
    if b:
        if '.' in b:
            b = float(b)
        elif ',' in b:
            b = float(b.replace(',','.'))
        else:
            b = int(b) 
    if c:
        if '.' in c:
            c = float(c)
        elif ',' in c:
            c = float(c.replace(',','.'))
        else:
            c = int(c)
    return a, b, c

def function(a, b, c): # Resolução da Equação
                # Valor de Delta:
                delta = (b ** 2) - (4 * a * c)
                
                Xv = -b/(2*a)
                Yv = - delta/ (4*a)
                
                if delta < 0:
                    return False
                else:
                    x1 = (- b + (delta ** (1/2))) / (2 * a)
                    x2 = (- b - (delta ** (1/2))) / (2 * a)
                    
                    valor_X = []
                    valor_Y = []
            
                    for x in range(-10,10,1):
                        valor_X.append (x)
                        valor_Y.append ((a * (x ** 2)) + (b * x) + c)
                    
                return valor_X, valor_Y, x1, x2, delta, Xv, Yv, a, b, c