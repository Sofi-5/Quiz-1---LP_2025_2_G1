#Una cola es ideal para este escenario,
#Defina los métodos que necesitará, como 'addCustomer(customer)' y 'serveCustomer()'.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 5

typedef struct {
    char nombre[50];
} Cliente;

typedef struct {
    Cliente cola[MAX];
    int front;
    int rear;
    int size;
} Queue;

void inicializar(Queue *q) {
    q->front = 0;
    q->rear = 0;
    q->size = 0;
}

void addCustomer(Queue *q, char *nombre) {
    if (q->size == MAX) {
        printf(" La cola está llena. No se puede agregar a %s\n", nombre);
        return;
    }
    strcpy(q->cola[q->rear].nombre, nombre);
    q->rear = (q->rear + 1) % MAX;
    q->size++;
    printf("Cliente agregado: %s\n", nombre);
}

void serveCustomer(Queue *q) {
    if (q->size == 0) {
        printf(" No hay clientes para atender\n");
        return;
    }
    printf(" Atendiendo a: %s\n", q->cola[q->front].nombre);
    q->front = (q->front + 1) % MAX;
    q->size--;
}

void printQueue(Queue *q) {
    printf("Cola actual:\n");
    if (q->size == 0) {
        printf("   (vacía)\n");
        return;
    }
    for (int i = 0; i < q->size; i++) {
        int index = (q->front + i) % MAX;
        printf("   - %s\n", q->cola[index].nombre);
    }
}

int main() {
    Queue q;
    inicializar(&q);

    addCustomer(&q, "Ana");
    addCustomer(&q, "Luis");
    addCustomer(&q, "Pedro");

    printQueue(&q);

    serveCustomer(&q);
    printQueue(&q);

    addCustomer(&q, "Marta");
    addCustomer(&q, "Carlos");
    addCustomer(&q, "Laura");  //  capacidad

    serveCustomer(&q);
    serveCustomer(&q);

    printQueue(&q);

    return 0;
}

