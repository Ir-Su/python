#!/usr/bin/env python
# coding: utf-8

# Тема “Работа с данными в Pandas”

# Задание 1
# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. 
# Создайте датафрейм authors со столбцами author_id и author_name, 
# в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


authors = pd.DataFrame({
    'author_id': [1, 2, 3],
    'author_name': ['Тургенев','Чехов','Островский']})
authors

Затем создайте датафрейм books cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
[1, 1, 1, 2, 2, 3, 3],
['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
[450, 300, 350, 500, 450, 370, 290]
# In[4]:


books = pd.DataFrame({
    'author_id': [1, 1, 1, 2, 2, 3, 3],
    'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
    'book_price': [450, 300, 350, 500, 450, 370, 290]
})

books

Задание 2
Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.
# In[5]:


authors_price = pd.merge(authors, books, on='author_id', how='outer')

authors_price.set_index('author_id', inplace=True)

authors_price

Задание 3
Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.
# In[6]:


top5 = authors_price.nlargest(5, 'book_price')

top5

Задание 4
Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
author_name, min_price, max_price и mean_price,
в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.
# In[9]:


authors_stat = authors_price.groupby('author_name').agg({'book_price':['min', 'max', 'mean']})

authors_stat = authors_stat.rename(columns={'min':'min_price', 'max':'max_price', 'mean':'mean_price'})

authors_stat

Задание 5**
Создайте новый столбец в датафрейме authors_price под названием cover, в нем будут располагаться данные о том, какая обложка у данной книги - твердая или мягкая. В этот столбец поместите данные из следующего списка:
['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая'].
Просмотрите документацию по функции pd.pivot_table с помощью вопросительного знака.Для каждого автора посчитайте суммарную стоимость книг в твердой и мягкой обложке. Используйте для этого функцию pd.pivot_table. При этом столбцы должны называться "твердая" и "мягкая", а индексами должны быть фамилии авторов. Пропущенные значения стоимостей заполните нулями, при необходимости загрузите библиотеку Numpy.
Назовите полученный датасет book_info и сохраните его в формат pickle под названием "book_info.pkl". Затем загрузите из этого файла датафрейм и назовите его book_info2. Удостоверьтесь, что датафреймы book_info и book_info2 идентичны.
# In[22]:


authors_price ['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
authors_price


# In[ ]:


get_ipython().run_line_magic('pinfo', 'pd.pivot_table')


# In[27]:


import numpy as np

book_info = pd.pivot_table(authors_price, values = ['book_price'], index = ['author_name'], columns = ['cover'], aggfunc = np.sum, fill_value = 0)

book_info


# In[28]:


book_info.to_pickle('book_info.pkl')


# In[30]:


book_info_read = pd.read_pickle('book_info.pkl')


# In[31]:


book_info.equals(book_info_read)

