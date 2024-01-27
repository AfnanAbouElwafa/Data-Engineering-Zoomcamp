
--Q3: How many taxi trips were totally made on September 18th 2019?
SELECT 
	count(1)
FROM 
	green_taxi_trips
WHERE 
	lpep_pickup_datetime::date = date '2019-09-18' AND
	lpep_dropoff_datetime::date = date '2019-09-18';


--Q4: Which was the pick up day with the largest trip distance?
SELECT 
	CAST(lpep_pickup_datetime as DATE) AS "pickup_day"
FROM 
	green_taxi_trips	
ORDER BY
	trip_distance DESC
LIMIT 1


--Q5: Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown
-- Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?
SELECT 
	"Borough"
FROM 
	green_taxi_trips JOIN zones ON 
	"PULocationID" = "LocationID" 
WHERE
	lpep_pickup_datetime::date = date '2019-09-18' AND
	"Borough" != 'Unknown'
Group BY 
	"Borough"
HAVING
	SUM(total_amount)>50000
	

--Q6: For the passengers picked up in September 2019 in the zone name Astoria
-- which was the drop off zone that had the largest tip?
SELECT 
	zdo."Zone"
FROM 
	green_taxi_trips JOIN zones zpu ON 
	"PULocationID" = zpu."LocationID" 
	Join zones zdo ON
	"DOLocationID" = zdo."LocationID" 
WHERE
	to_char(lpep_pickup_datetime, 'YYYY-MM') = '2019-09'
	AND zpu."Zone" = 'Astoria'
ORDER BY
	tip_amount DESC
LIMIT 1

