#include <iostream>
#include <cmath>
#include <chrono>

using namespace std;


bool isPrime1(int n) {
    if (n < 2) {
        return false;
    }
    int d = 2;
    while (n % d != 0) {
        d++;
    }
    return d == n;
}

bool isPrime2(int n) {
    if (n < 2) {
        return false;
    }
    int d = 2;
    while (n % d != 0 && d <= n / 2) {
        d++;
    }
    return d == floor(n / 2) + 1;
}

bool isPrime3(int n) {
    if (n < 2) {
        return false;
    }
    int d = 2;
    while (n % d != 0 && d <= sqrt(n)) {
        d++;
    }
    return d == floor(sqrt(n)) + 1;
}

// There is a better way to implement this...

double meanValue(int arr[], int n) {
    double mv = 0;
    for (int i = 0; i < n; i++) {
        mv += arr[i];
    }
    return mv / n;
}

double sigma(int arr[], int n) {
    double s = 0;
    double mv = meanValue(arr, n);
    for (int i = 0; i < n; i++) {
        s += pow(arr[i] - mv, 2);
    }
    return sqrt(s / n);
}

void stressTest(int n = 10000) {
    int times1[n];
    int times2[n];
    int times3[n];
    for (int i = 0; i < n; i++) {
        chrono::steady_clock::time_point start = chrono::steady_clock::now();
        bool isPrime = isPrime1(i);
        chrono::steady_clock::time_point end = chrono::steady_clock::now();
        times1[i] = chrono::duration_cast<chrono::nanoseconds>(end - start).count();
        start = chrono::steady_clock::now();
        isPrime = isPrime2(i);
        end = chrono::steady_clock::now();
        times2[i] = chrono::duration_cast<chrono::nanoseconds>(end - start).count();
        start = chrono::steady_clock::now();
        isPrime = isPrime3(i);
        end = chrono::steady_clock::now();
        times3[i] = chrono::duration_cast<chrono::nanoseconds>(end - start).count();
    }
    cout << "isPrime1: mean exec time: " << meanValue(times1, n) << " (ns), std: " << sigma(times1, n) << " (ns)." << endl;
    cout << "isPrime2: mean exec time: " << meanValue(times2, n) << " (ns), std: " << sigma(times2, n) << " (ns)." << endl;
    cout << "isPrime3: mean exec time: " << meanValue(times3, n) << " (ns), std: " << sigma(times3, n) << " (ns)." << endl;
}

int main() {
    stressTest();
    return 0;
}