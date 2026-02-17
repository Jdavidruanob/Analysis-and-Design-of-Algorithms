import sys

def solve():
    # Leemos todo el input de una vez para manejar los casos múltiples fácilmente
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        while True:
            # Intentamos leer n y t para el siguiente caso
            try:
                n_str = next(iterator)
                t_str = next(iterator)
            except StopIteration:
                break
            
            n = int(n_str)
            t = float(t_str)
            
            dists = []
            speeds = []
            min_speed = float('inf')
            
            # Leemos los n segmentos
            for _ in range(n):
                d = float(next(iterator))
                s = float(next(iterator))
                dists.append(d)
                speeds.append(s)
                if s < min_speed:
                    min_speed = s
            
            # Configuración de la Bisección
            # low: Debe ser mayor que -min_speed para evitar división por cero.
            # Se añade un epsilon pequeño para asegurar que el denominador sea positivo.
            low = -min_speed + 1e-9
            high = 10000000.0  # Un valor suficientemente grande
            
            # Usamos 100 iteraciones fijas.
            # Esto es estándar en Python para problemas de geometría/búsqueda binaria
            # para evitar problemas con epsilons y bucles infinitos.
            for _ in range(100):
                mid = (low + high) / 2
                
                # Calculamos el tiempo total con la constante 'mid'
                curr_t = 0.0
                for i in range(n):
                    curr_t += dists[i] / (speeds[i] + mid)
                
                # Lógica de decisión:
                # Si el tiempo calculado es mayor que el objetivo (t), vamos muy lento.
                # Necesitamos aumentar la velocidad, por lo tanto aumentamos c (mid).
                # Movemos el límite inferior hacia arriba.
                if curr_t > t:
                    low = mid
                else:
                    high = mid
            
            # Imprimimos el resultado con 4 decimales como pide el problema
            print(f"{mid:.9f}")
            
    except StopIteration:
        pass

if __name__ == '__main__':
    solve()