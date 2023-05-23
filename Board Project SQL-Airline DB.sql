create database airlinedb;
create table airline_info( Sno int auto_increment primary key,
Airline varchar(40),
FlightNo int,
Origin varchar(30),
Destination varchar(30),
DepartureTime varchar(4),
ArrivalTime varchar(4),
Aircraft varchar(8),
Duration int,
MaxPax int,
CostInAED int,
Rating float,
IFE char(1)
);

desc airline_info;
insert into airline_info(Sno, Airline, FlightNo, Origin, Destination, DepartureTime, ArrivalTime, Aircraft, Duration, MaxPax, CostInAED, Rating, IFE)
values(1, 'Emirates', 001, 'Dubai DXB', 'London Heathrow LHR', 0745, 1225, 'A380', 0700, 489, 3000, 4.3, 'Y'),
(2, 'Emirates', 201, 'Dubai DXB', 'New York JFK', 0845, 1530, 'A380', 1450, 489, 5500, 3.8, 'Y'),
(3, 'Air Canada', 057, 'Dubai DXB', 'Toronto-Pearson YYZ', 2300, 0600, 'B789', 1450, 321, 4000, 4.0, 'Y'),
(4, 'KLM', 448, 'Dubai DXB', 'Amsterdam Schiphol', 0040, 0535, 'B78X', 0640, 367, 3300, 5.0, 'Y'),
(5, 'IndiGo', 066, 'Dubai DXB', 'Chennai', 2140, 0250, 'A321', 0330, 189, 900, 4.1, 'N'),
(6, 'Cebu Pacific', 019, 'Dubai DXB', 'Manila', 0355, 1715, 'A333', 0830, 258, 1300, 2.6, 'N'),
(7, 'Emirates', 248, 'Dubai DXB', 'Rio De Janeiro', 0745, 1630, 'B773', 1500, 300, 4960, 4.1, 'Y'),
(8, 'Emirates', 414, 'Dubai DXB', 'Sydney', 0340, 2250, 'A380', 1530, 489, 5000, 03.7, 'Y'),
(9, 'Cathay Pacific', 062, 'Dubai DXB', 'Hong Kong', 0615, 1715, 'B773', 0900, 283, 3300, 4.4, 'Y'),
(10, 'Korean Air', 738, 'Dubai DXB', 'Seoul-Incheon ICN', 0345, 1705, 'A333', 1100, 241, 3600, 4.4, 'Y'),
(11, 'Air China', 415, 'Dubai DXB', 'Wuhan', 0600, 1615, 'B773', 0910, 287, 2200, 4.4, 'Y'),
(12, 'Gulf Air', 121, 'Dubai DXB', 'Bahrain', 1600, 1615, 'A321', 0115, 184, 800, 3.1, 'N'),
(13, 'Swiss', 235, 'Dubai DXB', 'Muscat', 2115, 2220, 'A333', 0110, 300, 1100, 4.0, 'Y'),
(14, 'Swiss', 236, 'Dubai DXB', 'Zurich', 0100, 0610, 'A333', 0610, 300, 3267, 3.6, 'Y'),
(15, 'Emirates', 701, 'Dubai DXB', 'Mauritius', 0300, 1015, 'A388', 0715, 444, 2250, 5, 'Y'),
(16, 'Air France', 637, 'Dubai DXB', 'Paris CDG', 0040, 0555, 'B788', 0650, 289, 3100, 2.6, 'Y'),
(17, 'British Airways', 596, 'Dubai DXB', 'Birmingham', 1355, 2015, 'B744', 0750, 386, 3200, 2.6, 'N'),
(18, 'Aeroflot', 111, 'Dubai DXB', 'Moscow SVO', 0400, 0655, 'B738', 0355, 156, 1200, 4.7, 'N'),
(19, 'Turkish Airlines', 52, 'Dubai DXB', 'Istanbul', 0745, 1110, 'A333', 0340, 242, 2600, 5, 'Y'),
(20, 'Air India', 40, 'Dubai DXB', 'Mumbai', 2100, 0100, 'A321', 0230, 193, 400, 1.6, 'N');
select * from airline_info;
drop table airline_info;


