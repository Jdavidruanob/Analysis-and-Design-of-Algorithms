from sys import stdin
def main():
    t = int(stdin.readline().strip())
    for i in range(t):  
        a, b = map(int, stdin.readline().split())
        ans = 0
        print(f"Case: {i+1} {ans} ")
    
import sys

# Aumentamos un poco el límite de recursión por si acaso
sys.setrecursionlimit(2000)

MAX = 1000001  # El problema dice B <= 1,000,000
sieve = [True] * MAX
div = [None] * MAX
nod = [0] * MAX
seq = []

# --- 1. Lógica de Pre-cálculo (Ya la tenías) ---

def pcount(n, d):
    # Cuenta cuántas veces 'd' divide a 'n'
    return 0 if (n % d) != 0 else 1 + pcount(n // d, d)

def make_sieve():
    global sieve, div
    sieve[0] = sieve[1] = False
    # Optimización: Marcar pares primero
    for j in range(4, MAX, 2):
        sieve[j], div[j] = False, 2
    
    # Criba para impares
    for i in range(3, MAX, 2):
        if sieve[i]:
            div[i] = i # El divisor de un primo es él mismo
            for j in range(i * i, MAX, i):
                if sieve[j]: # Solo marcamos si no ha sido marcado
                    sieve[j] = False
                    div[j] = i

def make_nod():
    global nod
    nod[1] = 1
    for n in range(2, MAX):
        if sieve[n]:
            nod[n] = 2 # Si es primo, tiene 2 divisores (1 y él mismo)
        else:
            # Fórmula recursiva basada en factorización prima
            # NOD(n) = (potencia + 1) * NOD(n / p^potencia)
            p = div[n]
            if p is None: p = 2 # Fallback para pares básicos si div no se llenó
            power = pcount(n, p)
            nod[n] = (power + 1) * nod[n // (p ** power)]

def make_seq():
    global seq
    # Generamos la secuencia.
    # N_0 = 1
    # N_i = N_{i-1} + NOD(N_{i-1})
    seq = [1]
    curr = 1
    while curr <= MAX:
        next_val = curr + nod[curr]
        seq.append(next_val)
        curr = next_val

# --- 2. La parte que faltaba: Búsqueda Binaria y Solución ---

def solve():
    # Pre-calcular todo una sola vez al inicio
    make_sieve()
    make_nod()
    make_seq()
    
    # Leer entrada
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        num_cases = int(next(iterator))
    except StopIteration:
        return

    for case_num in range(1, num_cases + 1):
        try:
            A = int(next(iterator))
            B = int(next(iterator))
        except StopIteration:
            break

        # --- BÚSQUEDA BINARIA 1: Límite Inferior (Lower Bound) ---
        # Busamos el índice L tal que seq[L] >= A
        low = 0
        hi = len(seq) - 1
        ans_low = len(seq) # Valor por defecto si todos son menores que A
        
        while low <= hi:
            mid = (low + hi) // 2
            if seq[mid] >= A:
                ans_low = mid
                hi = mid - 1 # Intentamos buscar uno más a la izquierda
            else:
                low = mid + 1
        
        # --- BÚSQUEDA BINARIA 2: Límite Superior (Upper Bound) ---
        # Buscamos el índice R tal que seq[R] <= B
        low = 0
        hi = len(seq) - 1
        ans_high = -1 # Valor por defecto
        
        while low <= hi:
            mid = (low + hi) // 2
            if seq[mid] <= B:
                ans_high = mid
                low = mid + 1 # Intentamos buscar uno más a la derecha
            else:
                hi = mid - 1

        # Calcular cantidad
        # Si el rango es inválido (ej. A > B o números fuera de rango), el conteo es 0
        if ans_low > ans_high:
            result = 0
        else:
            result = ans_high - ans_low + 1

        print(f"Case {case_num}: {result}")

if __name__ == '__main__':
    solve()