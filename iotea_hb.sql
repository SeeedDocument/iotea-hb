CREATE DATABASE `iotea`;

USE `iotea`;

CREATE TABLE `iotea_hb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(45) DEFAULT NULL,
  `hour` varchar(45) DEFAULT NULL,
  `minute` varchar(45) DEFAULT NULL,
  `second` varchar(45) DEFAULT NULL,
  `air_temp` varchar(45) DEFAULT NULL,
  `air_hum` varchar(45) DEFAULT NULL,
  `pressure` varchar(45) DEFAULT NULL,
  `co2` varchar(45) DEFAULT NULL,
  `dust` varchar(45) DEFAULT NULL,
  `illumination` varchar(45) DEFAULT NULL,
  `o2` varchar(45) DEFAULT NULL,
  `soil_temp` varchar(45) DEFAULT NULL,
  `soil_hum` varchar(45) DEFAULT NULL,
  `voltage` varchar(45) DEFAULT NULL,
  `error` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;