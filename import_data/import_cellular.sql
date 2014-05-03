DROP TABLE IF EXISTS cellular_performance;
CREATE SEQUENCE cellular_performance_gid_seq;
CREATE TABLE cellular_performance (
  gid INT not null default nextval('cellular_performance_gid_seq'::regclass),
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