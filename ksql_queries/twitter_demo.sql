CREATE STREAM all_tweets
(
  text VARCHAR,
  id_str VARCHAR,
  user STRUCT<
name VARCHAR,
screen_name VARCHAR,
verified BOOLEAN>
) WITH (kafka_topic='tweet_real_three', value_format='JSON');





CREATE STREAM verified_tweets AS
SELECT
text AS tweet,
id_str AS status_id,
	user->name AS name,
	user->screen_name AS handle
FROM
	all_tweets
WHERE
	user->verified
AND user->screen_name <> 'therealreal';
