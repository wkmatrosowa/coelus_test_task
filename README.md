# Тестовое задание
Классификация предикатов и кратких прилагательных

# Запуск решения
1. Docker-образ будет собираться командой:\
```docker build -t task_pr -f Dockerfile .```
2. Далее контейнер будет запускаться:\
```docker run -it -v ~/task_pr/result:/result task_pr python coelus_nlp.py```
3. Файл с результатом будет лежать по следующему пути: `~/task_pr/result`
