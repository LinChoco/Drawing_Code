WITH re AS (
    SELECT day_mode, rent_time, -COUNT(rent_station) AS num_rent FROM rent_index re
    JOIN day_mode dc ON re.rent_date = dc.date
    GROUP BY day_mode, rent_time
),
ru AS (
    SELECT day_mode, rent_time, COUNT(rent_station) AS num_return FROM return_index ru
    JOIN day_mode dc ON ru.rent_date = dc.date
    GROUP BY day_mode, rent_time
)

SELECT re.day_mode, re.rent_time, re.num_rent, ru.num_return
FROM re
LEFT JOIN ru ON re.day_mode = ru.day_mode AND re.rent_time = ru.rent_time
order by re.day_mode, re.rent_time;
