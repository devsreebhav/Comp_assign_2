#include <stdio.h>
#include <math.h>

double f(double t, double y) {
    return y - pow(t, 2) + 1;
}

double exact_solution(double t) {
    return pow(t + 1, 2) - 0.5 * exp(t);
}

int main() {
    double t0 = 0, y0 = 0.5;
    double t_end = 2;
    double h = 0.2;
    double t = t0, y = y0;

    printf("t\t\tEuler's Method\t\tExact Solution\t\tError\t\tError Bound\n");
    printf("----------------------------------------------------------------------------\n");
    
    while (t <= t_end) {
        double euler_y = y + h * f(t, y);
        double exact_y = exact_solution(t);
        double error = fabs(euler_y - exact_y);
        double error_bound = 0.2 * fabs(f(t, y)); // Euler's method error bound
        
        printf("%.2f\t\t%.6f\t\t\t%.6f\t\t%.6f\t%.6f\n", t, euler_y, exact_y, error, error_bound);

        t += h;
        y = euler_y;
    }

    return 0;
}
