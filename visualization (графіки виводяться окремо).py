import psycopg2
import matplotlib.pyplot as plt

username = 'ryzhkova_daria'
password = '1111'
database = 'lab2_DB'
host = 'localhost'
port = '5432'

query_1 = '''
select sum(viewers_quantity) as quantity, genre_name from Podcasts inner join Genres using(genre_id) group by genre_name order by quantity
'''
query_2 = '''
select pod_name, viewers_quantity from Podcasts where genre_id = '2000000001'
'''

query_3 = '''
select viewers_quantity,rating from Podcasts  where country_id = '003' order by viewers_quantity
'''

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(con))

with con:

    cur = con.cursor()

    cur.execute(query_1)
    genre = []
    total = []
    for row in cur:
        genre.append(row[0])
        total.append(row[1])
    x_range = range(len(genre))

    #plt.subplot(2, 2, 3)
    plt.bar(total, genre)
    plt.title('Популярність подкастів \nпо жанрам')
    plt.xlabel("Genre")
    plt.ylabel("Viewers")
    plt.show()



    cur.execute(query_2)
    pod_name = []
    total = []
    for row in cur:
        pod_name.append(row[0])
        total.append(row[1])
    x_range = range(len(pod_name))

    #plt.subplot(2, 2, 1)
    plt.pie(total, labels=pod_name, autopct='%1.1f%%')
    plt.title('Кількість слухачів уподкастів в жанрі Technology')
    plt.show()

    cur.execute(query_3)
    quantity = []
    rating = []
    for row in cur:
        quantity.append(row[0])
        rating.append(row[1])
    x_range = range(len(quantity))

    #plt.subplot(1, 2, 2)
    plt.plot(quantity, rating, marker='o')
    plt.xlabel('Viewers')
    plt.ylabel('Rating')
    plt.title('Графік залежності оцінки від\n кількості слухачів подкастів в USA')
    for qnt, price in zip(quantity, rating):
        plt.annotate(price, xy=(qnt, price), xytext=(7, 2), textcoords='offset points')
    plt.show()



#plt.show()
