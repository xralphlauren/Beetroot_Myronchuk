SELECT (sum(salary)/count(salary)) FROM sotr;
SELECT name, salary FROM sotr ORDER BY salary DESC, name LIMIT 10;
SELECT count() FROM sotr WHERE status = 'Detailee';
SELECT count() FROM sotr WHERE position_title = 'STAFF ASSISTANT';
SELECT (sum(salary)/count()) FROM sotr WHERE position_title = 'STAFF ASSISTANT';
SELECT position_title FROM sotr GROUP BY position_title;
SELECT count(position_title), position_title FROM sotr GROUP BY position_title;