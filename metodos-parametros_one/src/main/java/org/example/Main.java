package org.example;

import java.util.Random;
import java.util.Scanner;

public class Main {
    //metodo con multiples parametros

    public static void calculate(int a, int b) {
        int sum = a + b;
        int product = a * b;
        System.out.println("La suma es: " + sum);
        System.out.println("el producto: " + product);

    }

    // metodo recursivo para calcular el factorial de un numero
    public static int factorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    // generacion de numeros aleatorios
    public static int generateRandomNumber(int min, int max) {
        Random rand = new Random();
        return rand.nextInt((max - min) + 1) + min;
    }

    // juego de probabilidad
    public static void playGame() {
        Scanner scanner = new Scanner(System.in);
        int randomNumber = generateRandomNumber(1, 100);
        System.out.println("Adivinia el numero entre 1 y 100");
        int guess = scanner.nextInt();

        if (guess == randomNumber) {
        System.out.println("Correcto. Adivinaste el numero");
    } else {
        System.out.println("Incorrecto, el numero era: " + randomNumber);
    }
}

public static void main(String[] args) {
    // uso de metodos con multiples parametros
    calculate(4, 9);
    // uso de metodo recursivo
    int num = 4;
    System.out.println("El factorial de " + num + " es: " + factorial(num));

    // juego de probabilidad
    playGame();

}



}
