SET 'auto.offset.reset'='earliest';

CREATE TABLE MOVIES_TABLE
(
 movieId VARCHAR,
 name VARCHAR,
 year INTEGER,
 isChristmasMovie BOOLEAN
) WITH (kafka_topic='movie', key='movieId', value_format='json');


select * from MOVIES_TABLE;


select * from MOVIES_TABLE where year > 2000;


select * from MOVIES_TABLE where isChristmasMovie;


CREATE STREAM RATINGS
(
  movieId varchar,
  rating INTEGER
) WITH (kafka_topic='ratings', value_format='JSON');


SELECT * FROM RATINGS;


SELECT MOVIES_TABLE.movieId AS movieId,
       MOVIES_TABLE.name,
	 MOVIES_TABLE.year,
       MOVIES_TABLE.isChristmasMovie,
       RATINGS.rating
FROM RATINGS
JOIN MOVIES_TABLE ON MOVIES_TABLE.movieId = RATINGS.movieId;


CREATE STREAM MOVIES_RATING AS
SELECT MOVIES_TABLE.movieId AS movieId,
       UCASE(MOVIES_TABLE.name) AS name,
	 MOVIES_TABLE.year,
       MOVIES_TABLE.isChristmasMovie,
       RATINGS.rating
FROM RATINGS
JOIN MOVIES_TABLE ON MOVIES_TABLE.movieId = RATINGS.movieId;


DESCRIBE MOVIES_RATING;


CREATE TABLE MOVIE_RATING_AVG AS SELECT name, SUM(RATING)/COUNT(*) AS avg_rating FROM MOVIES_RATING GROUP BY name;


CREATE TABLE MOVIE_WINDOW_TUMB1 AS
SELECT
name,
      COUNT(*) AS cnt,
      WindowStart() AS WindowStart,
      WindowEnd() AS WindowEnd
FROM
	MOVIES_RATING
WINDOW TUMBLING (size 1 minute)
GROUP BY name;


SELECT
    TIMESTAMPTOSTRING(WindowStart, 'yyyy-MM-dd HH:mm:ss.SSS') as ts_s,
    TIMESTAMPTOSTRING(WindowEnd, 'yyyy-MM-dd HH:mm:ss.SSS') as ts_e,
    name,
    cnt
from MOVIE_WINDOW_TUMB1;


-- udf/udaf

SELECT
    movieId,
    name,
    movieAbbr(name),
    year
FROM
    Movies_table;
