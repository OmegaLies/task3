# task3
Task3 for "System analysis and decision making" course

Example of using the function:
```
import task3

reference = [[1,3],[2,3,4,5],[1],[4,5],[2,3,4,5]]

with open('data.csv') as file:
  csvString = file.read()
  result = task3.task(csvString)
  print(result == reference)
```
