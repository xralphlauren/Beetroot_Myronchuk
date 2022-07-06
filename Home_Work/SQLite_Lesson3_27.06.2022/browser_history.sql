# task 2.1
SELECT datetime((v.visit_time/1000000)-11644473600, 'unixepoch'), u.url
FROM visits v LEFT JOIN urls u
ON u.id = v.url
ORDER BY v.visit_time ASC
LIMIT 1;


# task 2.2
SELECT datetime((v.visit_time/1000000)-11644473600, 'unixepoch'), u.url
FROM visits v LEFT JOIN urls u
ON u.id = v.url
ORDER BY v.visit_time DESC
LIMIT 1;


# task 5

SELECT strftime('%H:%M:%S', datetime((sum(visit_duration)/1000000)-11644473600, 'unixepoch'))
FROM visits v
GROUP BY  strftime('%Y-%m-%d', datetime((v.visit_time/1000000)-11644473600, 'unixepoch'))
