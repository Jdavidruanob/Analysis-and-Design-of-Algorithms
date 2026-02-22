"""
Jose David Ruano Burbano 8982982
Tarea 1 - N + NOD(N)
ADA - Análisis y Diseño de Algoritmos 2026-1

Análisis de complejidad:
La complejidad temporal total es O(M * log(log M) + T * log K), donde M es el límite máximo (1,000,001), 
T es el número de casos de prueba y K es la longitud de la secuencia generada.

1. Pre-calculo: O(M * log(log M)). Dominado por la Criba y el llenado del arreglo NOD 
   para todos los números hasta M. Esto se ejecuta una única vez al inicio.
2. Consultas: O(T * 2log K). Por cada caso de prueba, realizamos dos busquedas binarias (bisecciones) 
   sobre la secuencia "seq" para encontrar los índices del rango, lo cual es logarítmico respecto 
   al tamaño de la secuencia.
"""

import sys
sys.setrecursionlimit(3000)

MAX = 1000001
sieve = [True] * MAX
div = [None] * MAX
nod = [0] * MAX
seq = []

# --- funciones de precalculo necesarias,  implementacion tomada de la explicacion hecha por el Profesor Camilo Rocha en clase ---

def pcount(n, d):
    # Cuenta cuantas veces 'd' divide a 'n'
    return 0 if (n % d) != 0 else 1 + pcount(n // d, d)

def make_sieve():
    global sieve, div
    sieve[0] = sieve[1] = False
    
    # Marcar pares primero
    for j in range(4, MAX, 2):
        sieve[j], div[j] = False, 2
    
    # Criba para impares
    for i in range(3, MAX, 2):
        if sieve[i]:
            div[i] = i 
            for j in range(i * i, MAX, i):
                if sieve[j]: 
                    sieve[j] = False
                    div[j] = i

def make_nod():
    global nod
    nod[1] = 1
    for n in range(2, MAX):
        if sieve[n]:
            nod[n] = 2 
        else:
            p = div[n]
            if p is None: p = 2 
            power = pcount(n, p)
            nod[n] = (power + 1) * nod[n // (p ** power)]

def make_seq():
    global seq
    seq = [1]
    curr = 1
    # Generamos la secuencia hasta superar el MAX
    while curr <= MAX:
        next_val = curr + nod[curr]
        seq.append(next_val)
        curr = next_val

# Ejecutamos las funciones para tener todo listo
make_sieve()
make_nod()
make_seq()


def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):  
        a, b = map(int, sys.stdin.readline().split())
        
        # --- busqueda 1: 
        # Buscamos el primer índice donde seq[mid] >= A
        low = 0
        hi = len(seq) - 1
        ans_low = len(seq) 
        
        while low <= hi:
            mid = (low + hi) // 2
            if seq[mid] >= a:
                ans_low = mid
                hi = mid - 1
            else:
                low = mid + 1
        
        # --- Busqueda  2: Limite Superior ---
        # Buscamos el último índice donde seq[mid] <= B
        low = 0
        hi = len(seq) - 1
        ans_high = -1 
        
        while low <= hi:
            mid = (low + hi) // 2
            if seq[mid] <= b:
                ans_high = mid
                low = mid + 1
            else:
                hi = mid - 1

        if ans_low > ans_high:
            ans = 0
        else:
            ans = ans_high - ans_low + 1

        print(f"Case {i+1}: {ans}")


main()