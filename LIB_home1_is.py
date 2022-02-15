#!/usr/bin/env python
# coding: utf-8

# ##Задание 1
# Импортируйте библиотеку Numpy и дайте ей псевдоним np.
# Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов. Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7. Будем считать, что каждый столбец - это признак, а строка - наблюдение. Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy. Результат запишите в массив mean_a, в нем должно быть 2 элемента.
# 

# In[1]:


import numpy as np


# In[76]:


a = np.array([[1,6],[2,8],[3,11],[3,10],[1,7]], dtype = np.int32)
a


# In[77]:


# размерность
a.ndim


# In[78]:


a.shape


# In[79]:


# количество элементов
a.size


# In[81]:


mean_a = a.mean(axis = 0)
mean_a


# #Задание 2
# Вычислите массив a_centered, отняв от значений массива “а” средние значения соответствующих признаков, содержащиеся в массиве mean_a. Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.

# In[82]:


a_centered = np.subtract(a, mean_a)
a_centered


# #Задание 3
# Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp. Затем поделите a_centered_sp на N-1, где N - число наблюдений.

# In[83]:


a_centered_sp = a_centered[0,0]*a_centered[0,1] + a_centered[1,0]*a_centered[1,1] + a_centered[2,0]*a_centered[2,1] + a_centered[3,0]*a_centered[3,1] + a_centered[4,0]*a_centered[4,1]
a_centered_sp


# In[84]:


a_centered[:, 0] @ a_centered[:, 1]


# In[85]:


N = a.size
cov_value1 = a_centered_sp/(N - 1)
cov_value1


# #Задание 4**
# Число, которое мы получили в конце задания 3, является ковариацией двух признаков, содержащихся в массиве “а”. В задании 4 мы делили сумму произведений центрированных признаков на N-1, а не на N, поэтому полученная нами величина является несмещенной оценкой ковариации.В этом задании проверьте получившееся число, вычислив ковариацию еще одним способом - с помощью функции np.cov. В качестве аргумента m функция np.cov должна принимать транспонированный массив “a”. В получившейся ковариационной матрице (массив Numpy размером 2x2) искомое значение ковариации будет равно элементу в строке с индексом 0 и столбце с индексом 1.

# In[86]:


a = np.array([[1,6],[2,8],[3,11],[3,10],[1,7]], dtype = np.int32)
a_t = a.T
a_t


# In[97]:


cov_value2 = np.cov(a_t, ddof = 1)
cov_value2


# In[91]:


cov_value2[0,1] ==  cov_value1


# Увы, не совпало ((
