# Тестовое задание
Классификация предикатов и кратких прилагательных

# Запуск решения
1. Собрать Docker-образ следующей командой:\
```docker build -t task_pr -f Dockerfile .```
2. Запустить контейнер:\
```docker run -it -v ~/task_pr/result:/result task_pr python coelus_nlp.py```
3. Файл с результатом будет лежать по следующему пути: `~/task_pr/result`
