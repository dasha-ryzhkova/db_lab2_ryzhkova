import psycopg2

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

    print("Database opened successfully")

    cur = con.cursor()

    print('1.  ')

    cur.execute(query_1)
    for row in cur:
        print(row)

    print('\n2.  ')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print('\n3.  ')
    cur.execute(query_3)
    for row in cur:
        print(row)