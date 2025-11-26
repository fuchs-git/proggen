DROP DATABASE IF EXISTS ais;
CREATE DATABASE ais;

CREATE TABLE vessel
(
    mmsi INT PRIMARY KEY,
    name TEXT,
    typ  TEXT
);

CREATE TABLE aisdata
(
    mmsi         INT REFERENCES vessel (mmsi),
    basedatetime TIMESTAMP,
    lat          DECIMAL,
    lon          DECIMAL,
    PRIMARY KEY (mmsi, basedatetime)
);

-- INSERT INTO vessel (mmsi, name, typ) VALUES (%s,%s,%s); -- für Python
INSERT INTO vessel (mmsi, name, typ)
VALUES (?, ?, ?);
-- Zum Testen

-- INSERT INTO aisdata (mmsi, basedatetime, lat, lon) VALUES (%s,%s,%s,%s); -- für Python
INSERT INTO aisdata (mmsi, basedatetime, lat, lon)
VALUES (?, ?, ?, ?); -- Zum Testen

SELECT mmsi, name, typ
FROM vessel;

-- SELECT basedatetime, lat, lon
-- FROM vessel
--          INNER JOIN aisdata on vessel.mmsi = aisdata.mmsi
-- WHERE vessel.mmsi = %s
-- ORDER BY basedatetime;
SELECT basedatetime, lat, lon
FROM vessel
         INNER JOIN aisdata on vessel.mmsi = aisdata.mmsi
WHERE vessel.mmsi = ?
ORDER BY basedatetime;

-- braucht man nicht
SELECT *
FROM aisdata
         INNER JOIN vessel v on v.mmsi = aisdata.mmsi
WHERE v.mmsi = ?
ORDER BY basedatetime;