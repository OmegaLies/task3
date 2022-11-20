from io import StringIO
import csv

def task(csvString):
  # Переводим csv в более удобное представление, в моем случае
  # в словарь, где ключ - номер вершины, которая имеет ребра,
  # а значение - массив нормеров вершин, в которые эти ребра приходят
  f = StringIO(csvString)
  reader = csv.reader(f, delimiter=',')
  graph = {}
  for row in reader:
    edge = list(map(int, row[0].split(';')))
    edge.sort()
    if edge[0] in graph:
      if not edge[1] in graph[edge[0]]:
        graph[edge[0]].append(edge[1])
    else:
      graph[edge[0]] = [edge[1]]

  # Создаем результирующий массив
  out = [[] for i in range(5)]

  # Заполняем r1 - прямое управление
  out[0] = sorted(list(graph.keys()))

  # Заполняем r2 - прямое подчинение, и r5 - соподчинение
  for i in graph:
    for j in graph[i]:
      if not j in out[1]:
        out[1].append(j)
      if len(graph[i]) != 1 and not j in out[4]:
        out[4].append(j)
  out[1].sort()
  out[4].sort()

  # Заполняем r3 - опосредованное управление 
  # и r4 - опосредованное подчинение
  for i in out[1]:
    if i in graph.keys():
      for j in graph[i]:
        if not j in out[3]:
          out[3].append(j)
      for j in graph:
        if i in graph[j]:
          if not j in out[2]:
            out[2].append(j)
  out[2].sort()
  out[3].sort()
  return out

