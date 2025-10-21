# Example multithreading

support de cours 5A SRI 2025-2026

## Stream

https://asciinema.org/s/o0TMSfke5sgf4aEY

## Lancement d’une tâche "longue"

Affiche le temps nécessaire à la résolution d’un problème linéaire de taille 6000: `Ax=b`

```bash
$ ./task.py
2.9041853889998492
```

## Lancement de plusieurs process en parallèle

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
