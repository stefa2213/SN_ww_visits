import sqlite3
from pprint import pprint


def connect_db():
    conn = sqlite3.connect('poc.db')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS cities '
        '(city_id int primary key, '
        'city_name varchar(25), '
        'country_name varchar(25), '
        'lati int, '
        'longi int, '
        'last_visit varchar(25),'
        'type_visit varchar(25), '
        'clr varchar(25),'
        'ph_city varchar(200),'
        'ph_flag varchar(200))')
    conn.commit()
    conn.close()


def insert_db():
    conn = sqlite3.connect('poc.db')
    cur = conn.cursor()

    # Port of call / visits ----------------------------------------------------------------------------------------

    cur.execute(
        'insert into cities values (1, "Dar es-Salaam", "Tanzania",-6.776, 39.178, "Feb - 2015", "ship", "red", '
        '"https://snos.ro/media/cities/daressalaam.jpg", "https://snos.ro/media/flags/TANZANIA.GIF")')
    cur.execute(
        'insert into cities values (2, "Laem Chabang", "Thailand",13.069,100.911, "Mar - 2015", "ship", "red", '
        '"https://snos.ro/media/cities/laemchabang.JPG", "https://snos.ro/media/flags/THAILAND.GIF")')
    cur.execute(
        'insert into cities values (3, "Tanjung Pelepas", "Malaysia",1.383,103.572, "Oct - 2023", "ship", "red", '
        '"https://snos.ro/media/cities/tpp.jpg", "https://snos.ro/media/flags/MALAYSIA.GIF")')
    cur.execute('insert into cities values (4, "Singapore", "Singapore", 1.270,103.836, "Dec - 2021", "ship", "green", '
                '"https://snos.ro/media/cities/singapore.jpg", "https://snos.ro/media/flags/SINGAPORE.GIF")')
    cur.execute('insert into cities values (5, "Dutch Harbour", "USA", 53.877,-166.545, "Apr - 2015", "ship", "green", '
                '"https://snos.ro/media/cities/dutchharbour.jpg", "https://snos.ro/media/flags/UNITEDSTATES.GIF")')
    cur.execute('insert into cities values (6, "Pusan", "South Korea", 35.074,128.809, "Dec - 2021", "ship", "red", '
                '"https://snos.ro/media/cities/busan.jpg", "https://snos.ro/media/flags/SOUTH-KOREA.GIF")')
    cur.execute('insert into cities values (7, "Qingdao", "China", 36.068,120.376, "Feb - 2019", "ship", "red", '
                '"https://snos.ro/media/cities/qingdao.jpg", "https://snos.ro/media/flags/CHINA.GIF")')
    cur.execute(
        'insert into cities values (8, "Kwangyang", "South Korea", 34.975,127.589, "May - 2015", "ship", "red", '
        '"https://snos.ro/media/cities/kwangyang.jpg", "https://snos.ro/media/flags/SOUTH-KOREA.GIF")')
    cur.execute('insert into cities values (9, "Shanghai", "China", 31.221,121.482, "Oct - 2023", "ship", "green", '
                '"https://snos.ro/media/cities/shanghai.jpg", "https://snos.ro/media/flags/CHINA.GIF")')
    cur.execute('insert into cities values (10, "Shekou", "China", 22.473,113.907, "May - 2015", "ship", "red", '
                '"https://snos.ro/media/cities/shekou.jpg", "https://snos.ro/media/flags/CHINA.GIF")')
    cur.execute('insert into cities values (11, "Port Klang", "Malaysia", 3.000,101.400, "Apr - 2020", "ship", "red", '
                '"https://snos.ro/media/cities/portklang.jpg", "https://snos.ro/media/flags/MALAYSIA.GIF")')
    cur.execute('insert into cities values (12, "Penang", "Malaysia", 5.285,100.456, "Feb - 2019", "ship", "green", '
                '"https://snos.ro/media/cities/penang.jpg", "https://snos.ro/media/flags/MALAYSIA.GIF")')
    cur.execute(
        'insert into cities values (13, "Pasir Gudang", "Malaysia", 1.502,103.947, "May - 2015", "ship", "red", '
        '"https://snos.ro/media/cities/pasirgudang.jpg", "https://snos.ro/media/flags/MALAYSIA.GIF")')
    cur.execute('insert into cities values (14, "Hong Kong", "Hong Kong", 22.303,114.177, "Nov - 2022", "ship", "red", '
                '"https://snos.ro/media/cities/hongkong.jpg", "https://snos.ro/media/flags/HONGKONG.png")')
    cur.execute('insert into cities values (15, "Xiamen", "China", 24.480,118.089, "Nov - 2022", "ship", "red", '
                '"https://snos.ro/media/cities/xiamen.jpg", "https://snos.ro/media/flags/CHINA.GIF")')
    cur.execute('insert into cities values (16, "Yantian", "China", 22.556,114.237, "Oct - 2023", "ship", "green", '
                '"https://snos.ro/media/cities/yantian.jpg", "https://snos.ro/media/flags/CHINA.GIF")')
    cur.execute('insert into cities values (17, "Kaohsiung", "Taiwan", 22.633,120.267, "Iun - 2015", "ship", "red", '
                '"https://snos.ro/media/cities/kaohsiung.jpg", "https://snos.ro/media/flags/TAIWAN.GIF")')
    cur.execute('insert into cities values (18, "Manila", "Philippines", 14.593,120.989, "Iun - 2015", "ship", "red", '
                '"https://snos.ro/media/cities/manila.jpg", "https://snos.ro/media/flags/PHILIPPINES.GIF")')
    cur.execute(
        'insert into cities values (19, "Batangas", "Philippines", 13.942,121.164, "Jul - 2015", "ship", "red", '
        '"https://snos.ro/media/cities/batangas.jpg", "https://snos.ro/media/flags/PHILIPPINES.GIF")')
    cur.execute(
        'insert into cities values (20, "Cagayan de Oro", "Philippines", 8.477,124.946, "Jul - 2015", "ship", "green", '
        '"https://snos.ro/media/cities/cagayandeoro.jpg", "https://snos.ro/media/flags/PHILIPPINES.GIF")')
    cur.execute(
        'insert into cities values (21, "General Santos", "Philippines", 6.116,125.172, "Jul - 2015", "ship", "green", '
        '"https://snos.ro/media/cities/generalsantos.jpg", "https://snos.ro/media/flags/PHILIPPINES.GIF")')
    cur.execute(
        'insert into cities values (22, "Davao City", "Philippines", 7.067,125.600, "Jul - 2015", "ship", "green", '
        '"https://snos.ro/media/cities/davaocity.jpg", "https://snos.ro/media/flags/PHILIPPINES.GIF")')
    cur.execute('insert into cities values (23, "Ningbo", "China", 29.868,121.544, "Sep - 2023", "ship", "red", '
                '"https://snos.ro/media/cities/ningbo.JPG", "https://snos.ro/media/flags/CHINA.GIF")')
    cur.execute(
        'insert into cities values (24, "Vladivostok", "Russia", 43.133,131.900, "Jul - 2015", "ship", "green", '
        '"https://snos.ro/media/cities/vladivostok.JPG", "https://snos.ro/media/flags/RUSSIA.GIF")')
    cur.execute('insert into cities values (25, "Valencia", "Spain", 39.467,-0.375, "Apr - 2019", "ship", "green", '
                '"https://snos.ro/media/cities/valencia.JPG", "https://snos.ro/media/flags/SPAIN.GIF")')
    cur.execute('insert into cities values (26, "Tarragona", "Spain", 41.116,1.249, "Jan - 2016", "ship", "red", '
                '"https://snos.ro/media/cities/tarragona.JPG", "https://snos.ro/media/flags/SPAIN.GIF")')
    cur.execute('insert into cities values (27, "Algeciras", "Spain", 36.123,-5.452, "Jan - 2016", "ship", "green", '
                '"https://snos.ro/media/cities/algeciras.jpg", "https://snos.ro/media/flags/SPAIN.GIF")')
    cur.execute('insert into cities values (28, "Tanger Med", "Morocco", 35.875,-5.521, "Feb - 2016", "ship", "red", '
                '"https://snos.ro/media/cities/tangermed.jpg", "https://snos.ro/media/flags/MOROCCO.GIF")')
    cur.execute('insert into cities values (29, "Dakar", "Senegal", 14.717,-17.468, "Feb - 2016", "ship", "red", '
                '"https://snos.ro/media/cities/dakar.jpg", "https://snos.ro/media/flags/SENEGAL.GIF")')
    cur.execute('insert into cities values (30, "Lagos", "Nigeria", 6.465,3.406, "Feb - 2016", "ship", "red", '
                '"https://snos.ro/media/cities/lagos.jpg", "https://snos.ro/media/flags/NIGERIA.GIF")')
    cur.execute('insert into cities values (31, "Bata", "Equatorial Guinea", 1.853,9.779, "Feb - 2016", "ship", "red", '
                '"https://snos.ro/media/cities/bata.JPG", "https://snos.ro/media/flags/EGUINEA.jpg")')
    cur.execute(
        'insert into cities values (32, "Malabo", "Equatorial Guinea", 3.750,8.737, "Feb - 2016", "ship", "red", '
        '"https://snos.ro/media/cities/malabo.jpg", "https://snos.ro/media/flags/EGUINEA.jpg")')
    cur.execute('insert into cities values (33, "Tema", "Ghana", 5.666,0.000, "Feb - 2016", "ship", "red", '
                '"https://snos.ro/media/cities/tema.jpg", "https://snos.ro/media/flags/GHANA.JPG")')
    cur.execute('insert into cities values (34, "Takoradi", "Ghana", 4.902,-1.783, "Jan - 2016", "ship", "red", '
                '"https://snos.ro/media/cities/takoradi.jpg", "https://snos.ro/media/flags/GHANA.JPG")')
    cur.execute('insert into cities values (35, "Abidjan", "Ivory Coast", 5.345,-4.024, "Mar - 2016", "ship", "red", '
                '"https://snos.ro/media/cities/abidjan.JPG", "https://snos.ro/media/flags/COTEDIVOIRE.GIF")')
    cur.execute('insert into cities values (36, "Casablanca", "Morocoo", 33.590,-7.604, "Apr - 2016", "ship", "green", '
                '"https://snos.ro/media/cities/casablanca.jpg", "https://snos.ro/media/flags/MOROCCO.GIF")')
    cur.execute('insert into cities values (37, "Lisbon", "Portugal", 38.737,-9.143, "Apr - 2016", "ship", "green", '
                '"https://snos.ro/media/cities/lisbon.jpg", "https://snos.ro/media/flags/PORTUGAL.GIF")')
    cur.execute('insert into cities values (38, "Marin", "Spain", 42.393,-8.700, "May - 2016", "ship", "red", '
                '"https://snos.ro/media/cities/marin.jpg", "https://snos.ro/media/flags/SPAIN.GIF")')
    cur.execute('insert into cities values (39, "Vigo", "Spain", 42.216,-8.617, "May - 2016", "ship", "green", '
                '"https://snos.ro/media/cities/vigo.jpg", "https://snos.ro/media/flags/SPAIN.GIF")')
    cur.execute('insert into cities values (40, "Bilbao", "Spain", 43.263,-2.935, "May - 2016", "ship", "green", '
                '"https://snos.ro/media/cities/bilbao.jpg", "https://snos.ro/media/flags/SPAIN.GIF")')
    cur.execute('insert into cities values (41, "Varna", "Bulgaria", 43.214,27.915, "Jul - 2017", "ship", "green", '
                '"https://snos.ro/media/cities/varna.jpg", "https://snos.ro/media/flags/BULGARIA.GIF")')
    cur.execute('insert into cities values (42, "Nemrut", "Turkey", 36.857,36.134, "Apr - 2017", "ship", "red", '
                '"https://snos.ro/media/cities/nemrut.jpg", "https://snos.ro/media/flags/TURKEY.GIF")')
    cur.execute('insert into cities values (43, "Nemrut", "Turkey", 36.857,36.134, "Apr - 2017", "ship", "red", '
                '"https://snos.ro/media/cities/nemrut.jpg", "https://snos.ro/media/flags/TURKEY.GIF")')
    cur.execute('insert into cities values (44, "Hereke", "Turkey", 40.785,29.609, "May - 2017", "ship", "green", '
                '"https://snos.ro/media/cities/hereke.JPG", "https://snos.ro/media/flags/TURKEY.GIF")')
    cur.execute('insert into cities values (45, "Icdas", "Turkey", 40.441,27.138, "May - 2017", "ship", "red", '
                '"https://snos.ro/media/cities/icdas.jpg", "https://snos.ro/media/flags/TURKEY.GIF")')
    cur.execute('insert into cities values (46, "Diliskelesi", "Turkey", 40.767,29.533, "Jun - 2017", "ship", "red", '
                '"https://snos.ro/media/cities/diliskelesi.JPG", "https://snos.ro/media/flags/TURKEY.GIF")')
    cur.execute('insert into cities values (47, "Temryuk", "Russia", 45.271,37.382, "Jun - 2017", "ship", "green", '
                '"https://snos.ro/media/cities/temryuk.JPG", "https://snos.ro/media/flags/RUSSIA.GIF")')
    cur.execute('insert into cities values (48, "Eregli", "Turkey", 41.280,31.420, "Jul - 2017", "ship", "green", '
                '"https://snos.ro/media/cities/eregli.jpg", "https://snos.ro/media/flags/TURKEY.GIF")')
    cur.execute('insert into cities values (49, "Valletta", "Malta", 35.8992, 14.5141, "Apr - 2019", "ship", "green", '
                '"https://snos.ro/media/cities/valleta.JPG", "https://snos.ro/media/flags/MALTA.GIF")')
    cur.execute('insert into cities values (50, "Jeddah", "Saudi Arabia", 21.543,39.173, "Sep - 2023", "ship", "red", '
                '"https://snos.ro/media/cities/jeddah.jpeg", "https://snos.ro/media/flags/SAUDI.GIF")')
    cur.execute('insert into cities values (51, "Jebel Ali", "UAE", 25.036,55.122, "Sep - 2023", "ship", "red", '
                '"https://snos.ro/media/cities/jebelali.jpeg", "https://snos.ro/media/flags/UAE.jpg")')
    cur.execute('insert into cities values (52, "Nansha", "China", 22.802,113.525, "Oct - 2023", "ship", "red", '
                '"https://snos.ro/media/cities/nansha.jpg", "https://snos.ro/media/flags/CHINA.GIF")')
    cur.execute('insert into cities values (53, "Barcelona", "Spain", 41.390,2.154, "Apr - 2019", "ship", "green", '
                '"https://snos.ro/media/cities/barcelona.JPG", "https://snos.ro/media/flags/SPAIN.GIF")')
    cur.execute('insert into cities values (54, "Marseille", "France", 43.202,5.205, "Aug - 2021", "ship", "red", '
                '"https://snos.ro/media/cities/marseille.jpg", "https://snos.ro/media/flags/FRANCE.GIF")')
    cur.execute('insert into cities values (55, "Voltri-Genoa", "Italy", 44.433,8.767, "Apr - 2019", "ship", "green", '
                '"https://snos.ro/media/cities/voltri.jpg", "https://snos.ro/media/flags/ITALY.GIF")')
    cur.execute('insert into cities values (56, "Shenzen", "China", 22.543,114.063, "Dec - 2019", "ship", "green", '
                '"https://snos.ro/media/cities/shenzen.jpg", "https://snos.ro/media/flags/CHINA.GIF")')
    cur.execute(
        'insert into cities values (57, "Southampton", "England", 50.910,-1.404, "Apr - 2020", "ship", "green", '
        '"https://snos.ro/media/cities/southampton.jpg", "https://snos.ro/media/flags/ENGLAND.jpg")')
    cur.execute('insert into cities values (58, "Hamburg", "Germany", 53.551,9.994, "Aug - 2023", "ship", "green", '
                '"https://snos.ro/media/cities/hamburg.jpg", "https://snos.ro/media/flags/GERMANY.GIF")')
    cur.execute(
        'insert into cities values (59, "Rotterdam", "Netherlands", 51.905,4.467, "Apr - 2020", "ship", "red", '
        '"https://snos.ro/media/cities/rotterdam.jpg", "https://snos.ro/media/flags/NED.GIF")')
    cur.execute('insert into cities values (60, "Tianjin", "China", 39.343,117.362, "Mar - 2020", "ship", "red", '
                '"https://snos.ro/media/cities/tianjin.jpg", "https://snos.ro/media/flags/CHINA.GIF")')
    cur.execute('insert into cities values (61, "Cristobal", "Panama", 8.373,-81.534, "Oct - 2021", "ship", "red", '
                '"https://snos.ro/media/cities/cristobal.JPG", "https://snos.ro/media/flags/PANAMA.GIF")')
    cur.execute('insert into cities values (62, "Panama", "Panama", 8.9824, -79.5199, "May - 2021", "ship", "green", '
                '"https://snos.ro/media/cities/panama.JPG", "https://snos.ro/media/flags/PANAMA.GIF")')
    cur.execute('insert into cities values (63, "New York", "USA", 40.736,-74.172, "Feb - 2022", "ship", "green", '
                '"https://snos.ro/media/cities/newyork.JPG", "https://snos.ro/media/flags/UNITEDSTATES.GIF")')
    cur.execute('insert into cities values (64, "Norfolk", "USA", 36.850,-76.286, "Oct - 2021", "ship", "red", '
                '"https://snos.ro/media/cities/norfolk.JPG", "https://snos.ro/media/flags/UNITEDSTATES.GIF")')
    cur.execute('insert into cities values (65, "Baltimore", "USA", 39.299,-76.609, "Feb - 2021", "ship", "red", '
                '"https://snos.ro/media/cities/baltimore.jpg", "https://snos.ro/media/flags/UNITEDSTATES.GIF")')
    cur.execute('insert into cities values (66, "Salalah", "Oman", 17.051,54.107, "Mar - 2021", "ship", "red", '
                '"https://snos.ro/media/cities/salalah.jpg", "https://snos.ro/media/flags/OMAN.GIF")')
    cur.execute('insert into cities values (67, "Colombo", "Sri Lanka", 6.927,79.861, "Mar - 2021", "ship", "red", '
                '"https://snos.ro/media/cities/colombo.JPG", "https://snos.ro/media/flags/SRILANKA.JPG")')
    cur.execute('insert into cities values (68, "Savannah", "USA", 32.076,-81.088, "Oct - 2021", "ship", "red", '
                '"https://snos.ro/media/cities/savannah.jpg", "https://snos.ro/media/flags/UNITEDSTATES.GIF")')
    cur.execute('insert into cities values (69, "Los Angeles", "USA", 34.0549, -118.2426, "Dec - 2022", "ship", "red", '
                '"https://snos.ro/media/cities/losangeles.JPG", "https://snos.ro/media/flags/UNITEDSTATES.GIF")')
    cur.execute('insert into cities values (70, "Yokohama", "Japan", 35.4437, 139.6380, "Nov - 2022", "ship", "red", '
                '"https://snos.ro/media/cities/yokohama.JPG", "https://snos.ro/media/flags/JAPAN.GIF")')
    cur.execute(
        'insert into cities values (71, "Vung Tau", "Vietnam", 10.4114, 107.1362, "Nov - 2022", "ship", "green", '
        '"https://snos.ro/media/cities/vungtau.JPG", "https://snos.ro/media/flags/VIETNAM.GIF")')
    cur.execute('insert into cities values (72, "Antwerp", "Belgium", 51.2213, 4.4051, "Aug - 2023", "ship", "red", '
                '"https://snos.ro/media/cities/antwerp.jpg", "https://snos.ro/media/flags/BELGIUM.GIF")')
    cur.execute(
        'insert into cities values (73, "London Gateway", "England", 51.5101, 0.4596, "Aug - 2023", "ship", "green", '
        '"https://snos.ro/media/cities/londongateway.JPG", "https://snos.ro/media/flags/ENGLAND.jpg")')
    cur.execute('insert into cities values (74, "Le Havre", "France", 49.4944, 0.1079, "Aug - 2023", "ship", "red", '
                '"https://snos.ro/media/cities/lehavre.jpg", "https://snos.ro/media/flags/FRANCE.GIF")')
    cur.execute('insert into cities values (75, "Abu Dhabi", "UAE", 24.4539, 54.3773, "Sep - 2023", "ship", "red", '
                '"https://snos.ro/media/cities/abudhabi.jpg", "https://snos.ro/media/flags/UAE.jpg")')
    cur.execute('insert into cities values (76, "Felixstowe", "England", 51.9617, 1.3513, "Nov - 2023", "ship", "red", '
                '"https://snos.ro/media/cities/felixstowe.jpg", "https://snos.ro/media/flags/ENGLAND.jpg")')

    # Transits ----------------------------------------------------------------------------------------------------
    cur.execute('insert into cities values (77, "Suez", "Egypt", 31.265,32.302, "Sep - 2023", "ship", "red", '
                '"https://snos.ro/media/cities/suez.JPG", "https://snos.ro/media/flags/EGYPT.GIF")')
    cur.execute('insert into cities values (78, "Billund", "Denmark", 55.7284, 9.1124, "Jul - 2021", "plane", "red", '
                '"https://snos.ro/media/cities/billund.jpg", "https://snos.ro/media/flags/DENMARK.GIF")')
    cur.execute('insert into cities values (79, "Doha", "Qatar", 25.2854, 51.5310, "Feb - 2015", "plane", "red", '
                '"https://snos.ro/media/cities/doha.JPG", "https://snos.ro/media/flags/QATAR.GIF")')
    cur.execute('insert into cities values (80, "Paris", "France", 48.8566, 2.3522, "Dec - 2022", "plane", "red", '
                '"https://snos.ro/media/cities/paris.JPG", "https://snos.ro/media/flags/FRANCE.GIF")')
    cur.execute('insert into cities values (81, "Frankfurt", "Germany", 50.1109, 8.6821, "Jul - 2021", "plane", "red", '
                '"https://snos.ro/media/cities/frankfurt.jpg", "https://snos.ro/media/flags/GERMANY.GIF")')
    cur.execute('insert into cities values (82, "Vienna", "Austria", 48.2082, 16.3738, "Aug - 2023", "plane", "red", '
                '"https://snos.ro/media/cities/vienna.JPG", "https://snos.ro/media/flags/AUSTRIA.GIF")')
    cur.execute('insert into cities values (83, "Istanbul", "Turkey", 41.0082, 28.9784, "May - 2021", "car", "red", '
                '"https://snos.ro/media/cities/istanbul.jpg", "https://snos.ro/media/flags/TURKEY.GIF")')
    cur.execute('insert into cities values (84, "Warsaw", "Poland", 52.2297, 21.0122, "Feb - 2022", "plane", "red", '
                '"https://snos.ro/media/cities/warsaw.jpeg", "https://snos.ro/media/flags/POLAND.GIF")')
    cur.execute('insert into cities values (85, "Patras", "Greece", 38.2466, 21.7346, "Jul - 2010", "ship", "red", '
                '"https://snos.ro/media/cities/patras.jpg", "https://snos.ro/media/flags/GREECE.GIF")')
    cur.execute(
        'insert into cities values (86, "Igoumenitsa", "Greece", 39.5061, 20.2655, "Jul - 2010", "ship", "red", '
        '"https://snos.ro/media/cities/igoumenitsa.JPG", "https://snos.ro/media/flags/GREECE.GIF")')
    cur.execute('insert into cities values (87, "Bologna", "Italy", 44.4949, 11.3426, "Jul - 2010", "car", "red", '
                '"https://snos.ro/media/cities/bologna.jpeg", "https://snos.ro/media/flags/ITALY.GIF")')
    cur.execute('insert into cities values (88, "Sofia", "Bulgaria", 42.6977, 23.3219, "Jul - 2020", "car", "red", '
                '"https://snos.ro/media/cities/sofia.jpg", "https://snos.ro/media/flags/BULGARIA.GIF")')
    cur.execute('insert into cities values (118, "Malaga", "Spain", 36.7213, -4.4213, "Jul - 2020", "car", "red", '
                '"https://snos.ro/media/cities/malaga.JPG", "https://snos.ro/media/flags/SPAIN.GIF")')

    # Visits ------------------------------------------------------------------------------------------------------
    cur.execute('insert into cities values (89, "Rome", "Italy", 41.9028, 12.4964, "Aug - 2018", "car", "green", '
                '"https://snos.ro/media/cities/rome.JPG", "https://snos.ro/media/flags/ITALY.GIF")')
    cur.execute(
        'insert into cities values (90, "Svenborg", "Denmark", 55.0674, 10.6073, "Jul - 2021", "university", "green", '
        '"https://snos.ro/media/cities/svenborg.JPG", "https://snos.ro/media/flags/DENMARK.GIF")')
    cur.execute('insert into cities values (91, "London", "England", 51.5000, -0.1250, "Aug - 2023", "car", "green", '
                '"https://snos.ro/media/cities/london.JPG", "https://snos.ro/media/flags/ENGLAND.jpg")')
    cur.execute('insert into cities values (92, "Ancona", "Italy", 43.6158, 13.5189, "Jul - 2010", "car", "green", '
                '"https://snos.ro/media/cities/ancona.jpg", "https://snos.ro/media/flags/ITALY.GIF")')
    cur.execute(
        'insert into cities values (93, "Liverpool", "England", 53.4084, -2.9916, "Jun - 2023", "car", "green", '
        '"https://snos.ro/media/cities/liverpool.JPG", "https://snos.ro/media/flags/ENGLAND.jpg")')
    cur.execute(
        'insert into cities values (94, "Amsterdam", "Netherlands", 52.3676, 4.9041, "Jul - 2010", "plane", "green", '
        '"https://snos.ro/media/cities/amsterdam.JPG", "https://snos.ro/media/flags/NED.GIF")')

    # Romanian visits --------------------------------------------------------------------------------------

    cur.execute(
        'insert into cities values (95, "Hunedoara", "România", 45.7678, 22.9072, "Jul - 2023", "car", "green", '
        '"https://snos.ro/media/cities/romania/hunedoara.JPG", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (96, "Târgu Jiu", "România", 45.0314, 23.2689, "Aug - 2019", "car", "green", '
        '"https://snos.ro/media/cities/romania/targujiu.jpg", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (97, "Deva", "România", 45.8663, 22.9144, "Aug - 2019", "car", "green", '
        '"https://snos.ro/media/cities/romania/deva.jpeg", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (98, "Sibiu", "România", 45.8035, 24.1450, "Iul - 2023", "car", "green", '
        '"https://snos.ro/media/cities/romania/sibiu.jpg", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (99, "Brașov", "România", 45.6427, 25.5887, "Ian - 2023", "car", "green", '
        '"https://snos.ro/media/cities/romania/brasov.JPG", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (100, "Brăila", "România", 45.2652, 27.9595, "Iul - 2023", "car", "green", '
        '"https://snos.ro/media/cities/romania/braila.jpg", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (101, "Alba Iulia", "România", 46.0733, 23.5805, "Iul - 2022", "car", "green", '
        '"https://snos.ro/media/cities/romania/albaiulia.JPG", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (102, "Oradea", "România", 47.0465, 21.9189, "May - 2021", "car", "green", '
        '"https://snos.ro/media/cities/romania/oradea.JPG", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (103, "Arad", "România", 46.1866, 21.3123, "Iul - 2011", "car", "green", '
        '"https://snos.ro/media/cities/romania/arad.jpg", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (104, "Galați", "România", 45.4353, 28.0080, "Iul - 2023", "car", "green", '
        '"https://snos.ro/media/cities/romania/galati.jpg", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (105, "București", "România", 44.4268, 26.1025, "Iul - 2023", "car", "green", '
        '"https://snos.ro/media/cities/romania/bucuresti.jpg", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (106, "Constanța", "România", 44.1917, 028.6233, "Aug - 2023", "car", "green", '
        '"https://snos.ro/media/cities/romania/constanta.JPG", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (107, "Vaslui", "România", 46.6407, 27.7276, "Iul - 2023", "car", "green", '
        '"https://snos.ro/media/cities/romania/vaslui.jpg", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (108, "Iași", "România", 47.1585, 27.6014, "Iul - 2023", "car", "green", '
        '"https://snos.ro/media/cities/romania/iasi.jpeg", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (109, "Suceava", "România", 47.6635, 26.2732, "Sep - 2022", "car", "green", '
        '"https://snos.ro/media/cities/romania/suceava.JPG", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (111, "Maramureș", "România", 47.6738, 23.7456, "Aug - 2018", "car", "green", '
        '"https://snos.ro/media/cities/romania/maramures.JPG", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (112, "Drobeta-Turnu Severin", "România", 44.6369, 22.6597, "Aug - 2019", "car", "green", '
        '"https://snos.ro/media/cities/romania/drobeta.jpeg", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (113, "Bacău", "România", 46.5670, 26.9146, "May - 2021", "car", "green", '
        '"https://snos.ro/media/cities/romania/bacau.jpeg", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (114, "Buzău", "România", 45.1371, 26.8171, "May - 2021", "car", "green", '
        '"https://snos.ro/media/cities/romania/buzau.jpg", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (115, "Piatra Neamț", "România", 46.9300, 26.3780, "Jul - 2022", "car", "green", '
        '"https://snos.ro/media/cities/romania/piatraneamt.JPG", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (116, "Pitești", "România", 44.8565, 24.8692, "Jul - 2023", "car", "green", '
        '"https://snos.ro/media/cities/romania/pitesti.jpg", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (117, "Tulcea", "România", 45.1716, 28.7914, "May - 2022", "car", "green", '
        '"https://snos.ro/media/cities/romania/tulcea.JPG", "https://snos.ro/media/flags/ROMANIA.GIF")')
    cur.execute(
        'insert into cities values (119, "Cluj-Napoca", "România", 46.7712, 23.6236, "Aug - 2018", "car", "red", '
        '"https://snos.ro/media/cities/romania/cluj.jpg", "https://snos.ro/media/flags/ROMANIA.GIF")')



    conn.commit()
    conn.close()


def show_table():
    conn = sqlite3.connect('poc.db')
    cur = conn.cursor()
    cur.execute('select * from cities')
    rows = cur.fetchall()
    conn.close()
    return rows


connect_db()
# insert_db()
# show_table()

# Use insert_db() only once, otherwise you need to delete .db file from current directory!!!
