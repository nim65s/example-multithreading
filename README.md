# Example multithreading

support de cours 5A SRI 2025-2026

## Stream

Séance 1: https://asciinema.org/s/o0TMSfke5sgf4aEY

Séance 2: https://asciinema.org/s/Rq07rFSCYThyvwjW

Séance 3:  https://asciinema.org/s/pkCAZ6oX3VrRMYjr


## Python

### Lancement d’une tâche "longue"

Affiche le temps nécessaire à la résolution d’un problème linéaire de taille 6000: `Ax=b`

```bash
$ ./task.py
2.9041853889998492
```

### Lancement de plusieurs process en parallèle

Utilise la librairie `subprocess` de python:

```bash
$ ./sub.py
3.7703498119999495
3.754473242000131
3.788909047000743
3.7627060060003714
total: 4.221463750999646
mean: 1.0553659377499116
```

### Idem, mais avec un ProcessPoolExecutor

```bash
$ ./pool.py
total: 4.037198985000032
mean: 1.009299746250008
```

### Idem, mais avec des threads

```bash
$ ./threads.py
total: 4.547516429000098
mean: 1.1368791072500244
```

NB: On s’attendrait à ce que des threads aillent plus vite, mais on a bien fait de mesurer: ici, dans notre cas, les threads sont ~13% plus lent que les process

### Des threads pour faire des requêtes HTTP

```bash
$ ./threads_http.py
total: 7.1779993729999205
mean: 0.0717799937299992
```

Chaque requête met strictement plus d’une seconde, mais en en lançant 100 en parallèle, on finit en 7s

### Programation asynchrone

```bash
$ ./async_http.py
total: 1.6072773939999934
mean: 0.016072773939999934
```

Si on indique à un executeur asynchrone quand nos opérations peuvent être mises en attente, il peut très efficacement jongler entre des centaines de tâches.

### Free Threaded Python interpreter

```bash
$ uv run --python 3.14 gil.py
total: 6.111903016000269
mean: 1.5279757540000674
```

```bash
uv run --python 3.14t gil.py
total: 1.8368778059998476
mean: 0.4592194514999619
```

## C++

<https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines>

### Threads, Mutex & Locks

```bash
c++ threads.cpp -o threads && ./threads
```

### Deadlocks

```bash
c++ banque.cpp -o banque && ./banque
```

### Atomics

```bash
c++ atomic.cpp -o atomic && ./atomic
```

### Asynchrone

```bash
c++ async.cpp -o async && ./async
```
