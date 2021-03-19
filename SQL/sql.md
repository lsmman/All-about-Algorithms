# SQL 정리
```MYSQL 기준```

#### Table score
| ID | NUM | called | meaning | Date |
|---|---|:---:|---:|---|---|
|2|100|Ant|Null|2013-12-22 11:30:00|
|3|120|Banana|hey|2013-12-23 12:30:00|
|4|90|carpet|who|2013-12-24 13:30:00|
|5|90|DISK|HO|2013-12-25 14:30:00|

#### SELECT, FROM
```SQL
SELECT *
FROM score
```

#### Where
```SQL
SELECT ID, called
FROM score
WHERE meaning = "Null"
```

#### ID 역순으로 정렬 (2순위 NUM)
```SQL
SELECT *
FROM score
ORDER BY ID DESC, NUM
```

#### SUM, MIN, MAX, COUNT
```SQL
SELECT MAX(called) AS max_called
FROM score
```

#### GROUP BY
```SQL
SELECT *
FROM score
GROUP BY NUM
```

#### DATETIME 추출
```SQL
SELECT called, HOUR(DATE)
FROM score
```
```SQL
SELECT HOUR, COUNT(HOUR)
FROM (
    SELECT HOUR(DATETIME) AS HOUR
    FROM ANIMAL_OUTS
    ) AS B
WHERE HOUR >= 9 AND HOUR <= 19
GROUP BY HOUR
ORDER BY HOUR 
```
YEAR : 연도 추출
MONTH : 월 추출
DAY : 일 추출 (DAYOFMONTH와 같은 함수)
HOUR : 시 추출
MINUTE : 분 추출
SECOND : 초 추출



