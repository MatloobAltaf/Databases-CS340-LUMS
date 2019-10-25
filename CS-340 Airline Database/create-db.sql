DROP DATABASE IF EXISTS `airline`;
CREATE DATABASE `airline`;
USE `airline`;

CREATE TABLE `Airports` (
	`a_iata` varchar(3) NOT NULL,
	`a_name` varchar(20) NOT NULL,
	PRIMARY KEY (`a_iata`)
);

CREATE TABLE `Flights` (
    `f_id` int NOT NULL,
	`f_date` varchar(10) NOT NULL,
	`f_departure_time` TIME NOT NULL,
	`f_arrival_time` TIME NOT NULL,
	`f_departure_airport` varchar(3) NOT NULL,
	`f_arrival_airport` varchar(3) NOT NULL,
	`f_fare` int NOT NULL,
	PRIMARY KEY (`f_id`)
);

CREATE TABLE `Passengers` (
	`p_id` int NOT NULL ,
	`p_name` varchar(20) NOT NULL,
	`p_address` varchar(50) NOT NULL,
	`p_contact` varchar(15) NOT NULL,
	`p_nationality` varchar(20) NOT NULL,
	PRIMARY KEY (`p_id`)
);

CREATE TABLE `Tickets` (
	`t_id` int NOT NULL ,
	`t_passenger_id` int NOT NULL,
	`t_flight_id` int NOT NULL,
	PRIMARY KEY (`t_id`)
);

ALTER TABLE `Flights` ADD CONSTRAINT `Flights_fk0` FOREIGN KEY (`f_departure_airport`) REFERENCES `Airports`(`a_iata`) ON DELETE CASCADE;

ALTER TABLE `Flights` ADD CONSTRAINT `Flights_fk1` FOREIGN KEY (`f_arrival_airport`) REFERENCES `Airports`(`a_iata`) ON DELETE CASCADE;

ALTER TABLE `Tickets` ADD CONSTRAINT `Tickets_fk0` FOREIGN KEY (`t_passenger_id`) REFERENCES `Passengers`(`p_id`) ON DELETE CASCADE;

ALTER TABLE `Tickets` ADD CONSTRAINT `Tickets_fk1` FOREIGN KEY (`t_flight_id`) REFERENCES `Flights`(`f_id`) ON DELETE CASCADE;

USE `airline`;
INSERT INTO `Airports`(
    `a_iata`,
    `a_name`
)
VALUES(
    "ISB",
    "Islamabad"
);
INSERT INTO `Airports`(
    `a_iata`,
    `a_name`
)
VALUES(
    "KHI",
    "Karachi"
);
INSERT INTO `Airports`(
    `a_iata`,
    `a_name`
)
VALUES(
    "LHE",
    "Lahore"
);
INSERT INTO `Airports`(
    `a_iata`,
    `a_name`
)
VALUES(
    "DEA",
    "Dera Ghazi Khan"
);
INSERT INTO `Airports`(
    `a_iata`,
    `a_name`
)
VALUES(
    "LYP",
    "Faislabad"
);
INSERT INTO `Airports`(
    `a_iata`,
    `a_name`
)
VALUES(
    "GWD",
    "Gwadar"
);
INSERT INTO `Airports`(
    `a_iata`,
    `a_name`
)
VALUES(
    "MUX",
    "Multan"
);
INSERT INTO `Airports`(
    `a_iata`,
    `a_name`
)
VALUES(
    "PEW",
    "Peshawar"
);
INSERT INTO `Airports`(
    `a_iata`,
    `a_name`
)
VALUES(
    "UET",
    "Quetta"
);
INSERT INTO `Airports`(
    `a_iata`,
    `a_name`
)
VALUES(
    "SKT",
    "Sialkot"
);
INSERT INTO `Airports`(
    `a_iata`,
    `a_name`
)
VALUES(
    "TUK",
    "Turban"
);
INSERT INTO `Airports`(
    `a_iata`,
    `a_name`
)
VALUES(
    "BHV",
    "Bahawalpur"
);
INSERT INTO `Airports`(
    `a_iata`,
    `a_name`
)
VALUES(
    "CHB",
    "Chillas"
);
INSERT INTO `Airports`(
    `a_iata`,
    `a_name`
)
VALUES(
    "GIL",
    "Gilgit"
);
INSERT INTO `Flights`(
	`f_id`,
    `f_date`,
	`f_departure_time`,
	`f_arrival_time`,
	`f_departure_airport`,
	`f_arrival_airport`,
	`f_fare`
)
VALUES(
    1,
	"19/10/2019",
	"10:00",
	"12:00",
	"LYP",
	"MUX",
	"10000"
);
INSERT INTO `Flights`(
	`f_id`,
    `f_date`,
	`f_departure_time`,
	`f_arrival_time`,
	`f_departure_airport`,
	`f_arrival_airport`,
	`f_fare`
)
VALUES(
    2,
	"20/11/2019",
	"12:00",
	"11:00",
	"CHB",
	"GIL",
	"13000"
);
INSERT INTO `Flights`(
	`f_id`,
    `f_date`,
	`f_departure_time`,
	`f_arrival_time`,
	`f_departure_airport`,
	`f_arrival_airport`,
	`f_fare`
)
VALUES(
    3,
	"21/12/2019",
	"12:00",
	"14:00",
	"CHB",
	"BHV",
	"12000"
);
INSERT INTO `Flights`(
	`f_id`,
    `f_date`,
	`f_departure_time`,
	`f_arrival_time`,
	`f_departure_airport`,
	`f_arrival_airport`,
	`f_fare`
)
VALUES(
    4,
	"20/11/2019",
	"09:00",
	"10:00",
	"SKT",
	"TUK",
	"14000"
);
INSERT INTO `Flights`(
	`f_id`,
    `f_date`,
	`f_departure_time`,
	`f_arrival_time`,
	`f_departure_airport`,
	`f_arrival_airport`,
	`f_fare`
)
VALUES(
    5,
	"19/11/2019",
	"14:00",
	"15:00",
	"SKT",
	"UET",
	"16000"
);
INSERT INTO `Flights`(
	`f_id`,
    `f_date`,
	`f_departure_time`,
	`f_arrival_time`,
	`f_departure_airport`,
	`f_arrival_airport`,
	`f_fare`
)
VALUES(
    6,
	"19/11/2019",
	"16:00",
	"17:00",
	"PEW",
	"MUX",
	"26000"
);
INSERT INTO `Flights`(
	`f_id`,
    `f_date`,
	`f_departure_time`,
	`f_arrival_time`,
	`f_departure_airport`,
	`f_arrival_airport`,
	`f_fare`
)
VALUES(
    7,
	"19/11/2019",
	"19:00",
	"20:00",
	"PEW",
	"SKT",
	"16000"
);
INSERT INTO `Flights`(
	`f_id`,
    `f_date`,
	`f_departure_time`,
	`f_arrival_time`,
	`f_departure_airport`,
	`f_arrival_airport`,
	`f_fare`
)
VALUES(
    8,
	"23/11/2019",
	"01:00",
	"02:00",
	"PEW",
	"TUK",
	"36000"
);
INSERT INTO `Flights`(
	`f_id`,
    `f_date`,
	`f_departure_time`,
	`f_arrival_time`,
	`f_departure_airport`,
	`f_arrival_airport`,
	`f_fare`
)
VALUES(
    9,
	"19/11/2019",
	"12:00",
	"11:00",
	"SKT",
	"UET",
	"16000"
);
INSERT INTO `Flights`(
	`f_id`,
    `f_date`,
	`f_departure_time`,
	`f_arrival_time`,
	`f_departure_airport`,
	`f_arrival_airport`,
	`f_fare`
)
VALUES(
    10,
	"01/11/2019",
	"15:00",
	"18:00",
	"SKT",
	"UET",
	"16000"
);
INSERT INTO `Passengers`(
	`p_id`,
	`p_name`,
	`p_address`,
	`p_contact`,
	`p_nationality`
)
VALUES(
	1,
	"Matloob",
	"LUMS",
	"(340) 460 9424",
	"Pakistani"
);
INSERT INTO `Passengers`(
	`p_id`,
	`p_name`,
	`p_address`,
	`p_contact`,
	`p_nationality`
)
VALUES(
	2,
	"Maaz",
	"UET",
	"(123) 432 1234",
	"Pakistani"
);
INSERT INTO `Passengers`(
	`p_id`,
	`p_name`,
	`p_address`,
	`p_contact`,
	`p_nationality`
)
VALUES(
	3,
	"Usman",
	"BNU",
	"(111) 222 3333",
	"Pakistani"
);
INSERT INTO `Passengers`(
	`p_id`,
	`p_name`,
	`p_address`,
	`p_contact`,
	`p_nationality`
)
VALUES(
	4,
	"Usama",
	"MIT",
	"(123) 780 9424",
	"Pakistani"
);
INSERT INTO `Passengers`(
	`p_id`,
	`p_name`,
	`p_address`,
	`p_contact`,
	`p_nationality`
)
VALUES(
	5,
	"Ammar",
	"TU Delft",
	"(111) 781 9424",
	"Pakistani"
);
INSERT INTO `Passengers`(
	`p_id`,
	`p_name`,
	`p_address`,
	`p_contact`,
	`p_nationality`
)
VALUES(
	6,
	"Sher Muhammad",
	"TU Berlin",
	"(100) 219 9424",
	"Pakistani"
);
INSERT INTO `Passengers`(
	`p_id`,
	`p_name`,
	`p_address`,
	`p_contact`,
	`p_nationality`
)
VALUES(
	7,
	"Sadaf",
	"Stanford",
	"(001) 460 9424",
	"Pakistani"
);
INSERT INTO `Passengers`(
	`p_id`,
	`p_name`,
	`p_address`,
	`p_contact`,
	`p_nationality`
)
VALUES(
	8,
	"Ruhan",
	"NUST",
	"(190) 460 9424",
	"Pakistani"
);
INSERT INTO `Passengers`(
	`p_id`,
	`p_name`,
	`p_address`,
	`p_contact`,
	`p_nationality`
)
VALUES(
	9,
	"Larasib",
	"Pen State",
	"(001) 460 9414",
	"Pakistani"
);
INSERT INTO `Passengers`(
	`p_id`,
	`p_name`,
	`p_address`,
	`p_contact`,
	`p_nationality`
)
VALUES(
	10,
	"Bushra",
	"TU Munich",
	"(350) 460 9424",
	"Pakistani"
);
INSERT INTO `Tickets`(
	`t_id`,
	`t_passenger_id`,
	`t_flight_id`
)
VALUES(
	1,
	1,
	1
);
INSERT INTO `Tickets`(
	`t_id`,
	`t_passenger_id`,
	`t_flight_id`
)
VALUES(
	2,
	2,
	2
);
INSERT INTO `Tickets`(
	`t_id`,
	`t_passenger_id`,
	`t_flight_id`
)
VALUES(
	3,
	3,
	3
);
INSERT INTO `Tickets`(
	`t_id`,
	`t_passenger_id`,
	`t_flight_id`
)
VALUES(
	4,
	4,
	4
);
INSERT INTO `Tickets`(
	`t_id`,
	`t_passenger_id`,
	`t_flight_id`
)
VALUES(
	5,
	5,
	5
);
INSERT INTO `Tickets`(
	`t_id`,
	`t_passenger_id`,
	`t_flight_id`
)
VALUES(
	6,
	6,
	6
);
INSERT INTO `Tickets`(
	`t_id`,
	`t_passenger_id`,
	`t_flight_id`
)
VALUES(
	7,
	7,
	7
);
INSERT INTO `Tickets`(
	`t_id`,
	`t_passenger_id`,
	`t_flight_id`
)
VALUES(
	8,
	8,
	8
);
INSERT INTO `Tickets`(
	`t_id`,
	`t_passenger_id`,
	`t_flight_id`
)
VALUES(
	9,
	9,
	9
);
INSERT INTO `Tickets`(
	`t_id`,
	`t_passenger_id`,
	`t_flight_id`
)
VALUES(
	10,
	10,
	10
);