# Module 1 Homework

## Docker & SQL

### Q1: Which tag has the following text: "Automatically remove the container when it exits"
- --delete
- --rc
- --rmc
- **--rm**
  
  The answer is `--rm`

### Q2: What is the version of the package wheel?
- **0.42.0** 
- 1.0.0
- 23.0.1
- 58.1.0

  The answer is `0.42.0`

```shell
docker run -it python:3.9 bash
root@532b222df6a5:/# pip list
Package    Version
---------- -------
pip        23.0.1
setuptools 58.1.0
wheel      0.42.0
```

## Prepare Postgres

I ingested the green taxi trips from September 2019 data using [ingest_green_data.py](https://github.com/AfnanAbouElwafa/Data-Engineering-Zoomcamp/blob/main/1-docker-terraform/ingest_green_data.py).


Also, ingested the zones data using [ingest_zone_data.ipynb](https://github.com/AfnanAbouElwafa/Data-Engineering-Zoomcamp/blob/main/1-docker-terraform/ingest_zone_data.ipynb).


### Q3: How many taxi trips were totally made on September 18th, 2019?
- 15767
- **15612** 
- 15859
- 89009

  The answer is `15612`

```sql
SELECT 
    COUNT(1)
FROM 
    green_taxi_trips
WHERE 
    lpep_pickup_datetime::date = date '2019-09-18' AND
    lpep_dropoff_datetime::date = date '2019-09-18';
```


### Q4: Which was the pickup day with the largest trip distance?
- 2019-09-18
- 2019-09-16
- **2019-09-26** 
- 2019-09-21

  The answer is `2019-09-26`

```sql
SELECT 
    CAST(lpep_pickup_datetime AS DATE) AS "pickup_day"
FROM 
    green_taxi_trips    
ORDER BY
    trip_distance DESC
LIMIT 1;
```


### Q5: Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown. Which were the 3 pick-up boroughs that had a sum of total_amount superior to 50000?
- **"Brooklyn" "Manhattan" "Queens"** 
- "Bronx" "Brooklyn" "Manhattan"
- "Bronx" "Manhattan" "Queens"
- "Brooklyn" "Queens" "Staten Island"

  The answer is `"Brooklyn" "Manhattan" "Queens"`

```sql
SELECT 
    "Borough"
FROM 
    green_taxi_trips
JOIN 
    zones ON "PULocationID" = "LocationID"
WHERE
    lpep_pickup_datetime::date = date '2019-09-18' AND
    "Borough" != 'Unknown'
GROUP BY 
    "Borough"
HAVING
    SUM(total_amount) > 50000;
```

### Q6: For the passengers picked up in September 2019 in the zone named Astoria, which was the drop-off zone that had the largest tip?
- Central Park
- Jamaica
- **JFK Airport** 
- Long Island City/Queens Plaza

  The answer is `JFK Airport`

```sql
SELECT 
    zdo."Zone"
FROM 
    green_taxi_trips
JOIN 
    zones zpu ON "PULocationID" = zpu."LocationID"
JOIN 
    zones zdo ON "DOLocationID" = zdo."LocationID"
WHERE
    to_char(lpep_pickup_datetime, 'YYYY-MM') = '2019-09' AND
    zpu."Zone" = 'Astoria'
ORDER BY
    tip_amount DESC
LIMIT 1;
```



