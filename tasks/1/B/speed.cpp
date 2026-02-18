/*
Jose David Ruano Burbano  8982982
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

int n;
double t;
vector<double> dists;
vector<double> speeds;

// Funcion que calcula el tiempo total del viaje dado un valor de constante c
double calculate_time(double c) {
    double total_time = 0;
    for (int i = 0; i < n; ++i) {
        total_time += dists[i] / (speeds[i] + c);
    }
    return total_time;
}

int main() {
    while (cin >> n >> t) {
        dists.resize(n);
        speeds.resize(n);
        double min_speed = 1001.0; // Valor inicial mayor al maximo posible (1000)

        for (int i = 0; i < n; ++i) {
            cin >> dists[i] >> speeds[i];
            // Buscamos la velocidad de lectura mínima para definir el límite inferior
            if (speeds[i] < min_speed) {
                min_speed = speeds[i];
            }
        }

        // Definición de límites para la biseccion
        // low: debe ser mayor que -min_speed para evitar division por cero o tiempos negativos.
        // high: un valor suficientemente grande donde el tiempo sea muy pequeño.
        double low = -min_speed + 1e-9; 
        double high = 10000000.0; 
        double mid;
        const double eps = 1e-9; 
        
        while (high - low > eps) {
            mid = (low + high) / 2;
            // Si el tiempo con mid es mayor al tiempo objetivo 't',
            // significa que vamos lento. Necesitamos aumentar la velocidad (es decir aumentar c).
            // esto ya que la función tiempo es decreciente respecto a c:
            if (calculate_time(mid) > t) {
                low = mid;
            } else {
                high = mid;
            }
        }

        printf("%.9f\n", mid);
    }

    return 0;
}