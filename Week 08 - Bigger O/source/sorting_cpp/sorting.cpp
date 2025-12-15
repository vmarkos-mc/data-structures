#include <iostream>
#include <cstdlib>
#include <chrono>
#include <fstream>

using namespace std;

void bubbleSort(double arr[], int n) {
    bool swapped = true;
    double temp;
    double current;
    int j = 1;
    while (swapped) {
        swapped = false;
        for (int i = 0; i < n - j; i++) {
            if (arr[i + 1] < arr[i]) {
                temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                swapped = true;
            }
            current++;
        }
        j++;
    }
    return;
}



void copyArray(double arr1[], double arr2[], int n) {
    for (int i = 0; i < n; i++) {
        arr2[i] = arr1[i];
    }
}

void inplaceMerge(double arr1[], int size1, double arr2[], int size2, int left, int right, int end) {
    int i = left, j = right;
    for (int k = left; k < end; k++) {
        if (i < right && (j >= end || arr1[i] <= arr1[j])) {
            arr2[k] = arr1[i];
            i++;
        } else {
            arr2[k] = arr1[j];
            j++;
        }
    }
}

void mergeSort(double arr1[], double arr2[], int n) {
    for (int width = 1; width < n; width *= 2) {
        for (int i = 0; i < n; i = i + 2 * width) {
            inplaceMerge(arr1, n, arr2, n, i, min(i + width, n), min(i + 2 * width, n));
        }
        copyArray(arr2, arr1, n);
    }
}

template <typename T>
void printArr(T arr[], int n) {
    for (int i = 0; i < n; i++) {
        if (i < n - 1) {
            cout << arr[i] << ", ";
        } else {
            cout << arr[i] << endl;
        }
    }
}

double* randomArray(int n) {
    double* arr = new double[n];
    for (int i = 0; i < n; i++) {
        arr[i] = rand();
    }
    return arr;
}

template <typename T>
double arrAvg(T arr[], int n) {
    double m = 0;
    for (int i = 0; i < n; i++) {
        m += arr[i];
    }
    return m / n;
}

void writeResults(int results[], int n, const string& filename) {
    ofstream ofile;
    ofile.open(filename, ios::app);
    for (int i = 0; i < n; i++) {
        if (i < n - 1) {
            ofile << results[i] << ",";
        } else {
            ofile << results[i] << endl;
        }
    }
    ofile.close();
}

void test(int n = 200, int rep = 10) {
    int bubbleTimes[n - 1];
    int mergeTimes[n - 1];
    int tempBubble[rep];
    int tempMerge[rep];
    double* currentArr;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < rep; j++) {
            currentArr = randomArray(i);
            chrono::steady_clock::time_point start = chrono::steady_clock::now();
            bubbleSort(currentArr, i);
            chrono::steady_clock::time_point end = chrono::steady_clock::now();
            tempBubble[j] = chrono::duration_cast<chrono::nanoseconds>(end - start).count();
            double currentWork[i];
            start = chrono::steady_clock::now();
            mergeSort(currentArr, currentWork, i);
            end = chrono::steady_clock::now();
            tempMerge[j] = chrono::duration_cast<chrono::nanoseconds>(end - start).count();
            delete[] currentArr;
        }
        bubbleTimes[i - 1] = arrAvg<int>(tempBubble, rep);
        mergeTimes[i - 1] = arrAvg<int>(tempMerge, rep);
    }
    writeResults(bubbleTimes, n - 1, "bubbleResults.txt");
    writeResults(mergeTimes, n - 1, "mergeResults.txt");
    // printArr<int>(bubbleTimes, n - 1);
    // printArr<int>(mergeTimes, n - 1);
}

int main() {
    test();
    return 0;
}