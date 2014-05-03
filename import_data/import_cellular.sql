DROP TABLE IF EXISTS cellular_performance;
CREATE TABLE cellular_performance (
  downloadSpeed NUMERIC,
  latencyAverage NUMERIC,
  deviceSignalStrength NUMERIC,
  uploadSpeed NUMERIC,
  Latitude NUMERIC,
  Longitude NUMERIC,
  location GEOGRAPHY(POINT,4326) );

COPY cellular_performance ( Latitude, Longitude, deviceSignalStrength, latencyAverage, downloadSpeed, uploadSpeed )
    FROM '/tmp/Cellular_Performance_Ag.csv'
    WITH DELIMITER ',' HEADER NULL AS '' CSV;