--select sum(viewers_quantity) as quantity, genre_name from Podcasts inner join Genres using(genre_id) group by genre_name order by quantity
--select pod_name, viewers_quantity from Podcasts where genre_id = '2000000001'
--select viewers_quantity,rating from Podcasts  where country_id = '003' order by viewers_quantity

select * from Podcasts