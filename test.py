import numpy as np
import matplotlib.pyplot as plt





def dist(x, y):
    return np.sqrt(np.sum((x - y)**2)) # np.sqrt и np.sum являются numpy-функциями, предназначенные для работы с numpy-массивами





# Настройте matplotlib для встраивания отображения в выходные ячейки данного notebook'а



X_train = np.array([[1,1], [2,2.5], [3,1.2], [5.5,6.3], [6,9], [7,6]]) # Определите numpy-массив двумерных точек
Y_train = ['red', 'red', 'red', 'blue', 'blue', 'blue'] # Определите список (т.е. массив) строк

print(X_train[5,0]) # Получить 0 координату 5ой точки в массиве
print(X_train[5,1]) # Получить 1 координату 5ой точки в массиве



plt.figure() # Определите новый образ
plt.scatter(X_train[:,0], X_train[:,1], s = 170, color = Y_train[:]) # Отобразите точки, используя синтаксис нарезки Python


X_test = np.array([3,4])

print(X_test)



num = len(X_train) # Вычислите количество точек в X_train
distance = np.zeros(num) # Инициализируйте numpy-массив нулей
for i in range(num):
    distance[i] = dist(X_train[i], X_test) # Вычислите расстояние от X_train[i] до X_test


print(distance)


plt.scatter(X_train[:,0], X_train[:,1], s = 170, color = Y_train[:])
plt.scatter(X_test[0], X_test[1], s = 170, color = 'green')
plt.show() # Покажите рисунок

min_index = np.argmin(distance) # Получите индекс с наименьшим расстоянием (distance)
print(Y_train[min_index])
