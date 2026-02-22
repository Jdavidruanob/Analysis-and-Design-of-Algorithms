/*
Jose David Ruano Burbano
Tarea 1 - Need for Speed
ADA - Análisis y Diseño de Algoritmos 2026-1

Análisis de complejidad:
La complejidad temporal de este algoritmo es O(N * log(R/eps)), donde N es el número de segmentos, 
R es el rango de búsqueda inicial y eps es la precisión requerida.
En cada iteración de la bisección recorremos los N segmentos para calcular el tiempo total.
*/

#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

// Variables globales para facilitar el acceso dentro de la función de cálculo
// tal como se suele hacer en programación competitiva para mantener las firmas limpias.
int n;
double t;
vector<double> dists;
vector<double> speeds;

// Función que calcula el tiempo total del viaje dado un valor de constante c
// Fórmula: Tiempo = Distancia / (Velocidad_Lectura + c)
double calculate_time(double c) {
    double total_time = 0;
    for (int i = 0; i < n; ++i) {
        total_time += dists[i] / (speeds[i] + c);
    }
    return total_time;
}

int main() {
    // Lectura de casos de prueba. El problema dice que hay varios sets.
    // El input termina cuando no hay más datos (EOF).
    while (cin >> n >> t) {
        dists.resize(n);
        speeds.resize(n);
        
        double min_speed = 1001.0; // Valor inicial mayor al máximo posible (1000)

        for (int i = 0; i < n; ++i) {
            cin >> dists[i] >> speeds[i];
            // Buscamos la velocidad de lectura mínima para definir el límite inferior
            if (speeds[i] < min_speed) {
                min_speed = speeds[i];
            }
        }

        // Definición de límites para la bisección
        // low: debe ser mayor que -min_speed para evitar división por cero o tiempos negativos.
        // high: un valor suficientemente grande donde el tiempo sea muy pequeño.
        double low = -min_speed + 1e-9; 
        double high = 10000000.0; 
        double mid;
        
        // Precisión requerida por el problema
        const double eps = 1e-9; 
        
        // Para asegurar precisión robusta, a veces se usa un for fijo (ej: 100 iteraciones),
        // pero usaremos el while con eps para respetar el estilo de tu ejemplo "Ladders".
        while (high - low > eps) {
            mid = (low + high) / 2;
            
            // Si el tiempo calculado con 'mid' es mayor al tiempo objetivo 't',
            // significa que vamos muy lento. Necesitamos aumentar la velocidad (aumentar c).
            // Como la función tiempo es decreciente respecto a c:
            if (calculate_time(mid) > t) {
                low = mid;
            } else {
                high = mid;
            }
        }

        // El problema pide 4 decimales de precisión
        printf("%.9f\n", mid);
    }

    return 0;
}