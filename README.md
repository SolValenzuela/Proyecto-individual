

PARA EL PROYECTO DE HORNOS SE UTILIZARON LOS SIGUIENTES RECURSOS.

Pipenv install flask pymysql flask-bcrypt
TITLE: 
Greatness - 100% Fully Responsive Free HTML5 Bootstrap Template

AUTHOR:
DESIGNED & DEVELOPED by FreeHTML5.co

Website: http://freehtml5.co/
Twitter: http://twitter.com/fh5co
Facebook: http://facebook.com/fh5co


CREDITS:

Bootstrap
http://getbootstrap.com/

jQuery
http://jquery.com/

jQuery Easing
http://gsgd.co.uk/sandbox/jquery/easing/

Modernizr
http://modernizr.com/

Google Fonts
https://www.google.com/fonts/

Icomoon
https://icomoon.io/app/

Respond JS
https://github.com/scottjehl/Respond/blob/master/LICENSE-MIT

animate.css
http://daneden.me/animate

jQuery Waypoint
https://github.com/imakewebthings/waypoints/blog/master/licenses.txt

Owl Carousel
http://www.owlcarousel.owlgraphic.com/

jQuery countTo
http://www.owlcarousel.owlgraphic.com/

Magnific Popup
http://dimsemenov.com/plugins/magnific-popup/

Demo Images:
http://unsplash.com

PLANIFICADO:
El proyecto proponía ser una plataforma para disponibilizar hornos para ceramistas en un sólo lugar, basado en la necesidad
de un grupo importante de ceramistas de la Región Metropolitana que requieren del servicio ,pero el agendamiento se ve
entorpecido por lo disperso de la información.

El proyecto se plantéo con funcionalidad mínima,donde al principio se mostrarán los hornos disponibles en la Rm que se inscriban en la pagina.
El proyecto es escalable y podría llegar a tener otras funcionalidades como Blog,Shop y lo que requiera el círculo de ceramistas.
La idea principal es que se convierta en una vitrina para la comunidad ceramista.


Durante el desarrollo se realizaron algunas modificaciones del proyecto original a petición del cliente,como la solicitud de buscar hornos sin loguearse.

El oferente de Hornos debe loguearse para poder ofrecer sus servicios.

Una vez realizada la reserva de horas se envía confirmación a traves de mail tanto a quien reserva como al taller.




Dump base de datos: 

Tabla Agenda
``` SQL
CREATE DATABASE  IF NOT EXISTS `nueva_prueba_proyecto` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `nueva_prueba_proyecto`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: nueva_prueba_proyecto
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `agendas`
--

DROP TABLE IF EXISTS `agendas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agendas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fecha_inicio` date NOT NULL,
  `hora_inicio` time DEFAULT NULL,
  `hora_termino` time DEFAULT NULL,
  `usuario_horno` varchar(255) DEFAULT NULL,
  `horno_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `agendada` int DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_agenda_hornos1_idx` (`horno_id`),
  CONSTRAINT `fk_agenda_hornos1` FOREIGN KEY (`horno_id`) REFERENCES `hornos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agendas`
--

LOCK TABLES `agendas` WRITE;
/*!40000 ALTER TABLE `agendas` DISABLE KEYS */;
INSERT INTO `agendas` VALUES (12,'2023-01-15','12:00:00','15:00:00','10',19,'2023-01-07 20:04:09','2023-01-07 20:04:09',0,NULL,NULL),(13,'2023-01-10','15:00:00','18:00:00','10',20,'2023-01-07 20:06:53','2023-01-07 20:06:53',1,'pina@mail.com','56977777777'),(14,'2023-01-13','18:30:00','21:30:00','10',21,'2023-01-07 20:08:47','2023-01-07 20:08:47',1,'luke@starwars.com','56977777777'),(15,'2023-01-12','14:30:00','16:30:00','10',20,'2023-01-07 20:18:45','2023-01-07 20:18:45',0,NULL,NULL),(17,'2023-01-19','10:00:00','15:00:00','10',21,'2023-01-07 20:28:52','2023-01-07 20:28:52',0,NULL,NULL),(18,'2023-01-20','08:00:00','13:00:00','10',19,'2023-01-07 20:29:24','2023-01-07 20:29:24',0,NULL,NULL),(19,'2023-01-09','15:30:00','17:30:00','13',22,'2023-01-08 02:23:35','2023-01-08 02:23:35',1,'rodrigo.acd@gmail.com','987654321'),(22,'2023-01-16','09:30:00','11:30:00','24',24,'2023-01-08 06:06:38','2023-01-08 06:06:38',0,NULL,NULL),(23,'2023-01-31','11:00:00','12:00:00','13',22,'2023-01-08 12:16:52','2023-01-08 12:16:52',0,NULL,NULL),(24,'2023-01-26','08:00:00','10:00:00','13',22,'2023-01-08 12:24:15','2023-01-08 12:24:15',0,NULL,NULL),(25,'2023-01-23','10:00:00','12:00:00','13',22,'2023-01-08 12:27:50','2023-01-08 12:27:50',0,NULL,NULL),(26,'2023-01-03','12:00:00','15:00:00','13',22,'2023-01-08 12:37:26','2023-01-08 12:37:26',0,NULL,NULL),(27,'2023-01-29','21:00:00','22:00:00','10',20,'2023-01-08 18:24:05','2023-01-08 18:24:05',0,NULL,NULL);
/*!40000 ALTER TABLE `agendas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-08 18:53:14
```


Tabla Hornos:
```SQL
CREATE DATABASE  IF NOT EXISTS `nueva_prueba_proyecto` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `nueva_prueba_proyecto`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: nueva_prueba_proyecto
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `hornos`
--

DROP TABLE IF EXISTS `hornos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hornos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `temperatura_min` int NOT NULL,
  `temperatura_max` int NOT NULL,
  `alto` int DEFAULT NULL,
  `ancho` int DEFAULT NULL,
  `fondo` int DEFAULT NULL,
  `costo_bandeja` int DEFAULT NULL,
  `costo_medio_horno` int DEFAULT NULL,
  `costo_horno_completo` int DEFAULT NULL,
  `observaciones` varchar(255) DEFAULT NULL,
  `usuario_creador_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_hornos_users_idx` (`usuario_creador_id`),
  CONSTRAINT `fk_hornos_users` FOREIGN KEY (`usuario_creador_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hornos`
--

LOCK TABLES `hornos` WRITE;
/*!40000 ALTER TABLE `hornos` DISABLE KEYS */;
INSERT INTO `hornos` VALUES (19,'Blanco',200,300,50,50,60,2000,3000,4000,'No nos responsabilizamos por piezas rotas',10,'2023-01-07 20:03:47','2023-01-07 20:03:47'),(20,'Verde',150,200,60,80,100,3000,4000,6000,'No nos responsabilizamos por piezas rotas',10,'2023-01-07 20:06:32','2023-01-07 20:06:32'),(21,'Rojo',300,500,50,50,50,1000,2000,3000,'No nos responsabilizamos por piezas rotas',10,'2023-01-07 20:08:20','2023-01-07 20:08:20'),(22,'Azul',300,500,80,70,80,6000,7000,8000,'Cuidamos tus piezas como si fueran nuestras',13,'2023-01-08 01:56:03','2023-01-08 01:56:03'),(24,'Turquesa',350,500,90,90,90,3500,5000,7000,'Nos responsabilizamos por tus piezas',24,'2023-01-08 06:05:43','2023-01-08 06:05:43');
/*!40000 ALTER TABLE `hornos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-08 18:53:14
```

Tabla Usuarios 
```SQL
CREATE DATABASE  IF NOT EXISTS `nueva_prueba_proyecto` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `nueva_prueba_proyecto`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: nueva_prueba_proyecto
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `comuna` varchar(45) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (10,'Carlitos','Malaquias concha 0310','Providencia','carlitos@mail.com','$2b$12$eK5YmuArZqDqubrVrWAKoOB6OERTjtUD6UQajsPOMloWXKNChl9di','2023-01-07 20:03:07','2023-01-07 20:03:07'),(13,'Carlota','Avenida Italia 1258','Providencia','carlota@mail.com','$2b$12$Tys1UGjcQ8twRYYUs2fj/u4ehA3cjlVJbBlhNCQAWsT9k3EMg24FW','2023-01-08 01:40:57','2023-01-08 01:40:57'),(19,'Flor','Avenida Italia 1201','Providencia','flor@mail.com','$2b$12$SNuBrOCNv/gOi7iBDSITZOrn1AEHuaJOn8yMeisU23fgyauyBWYb2','2023-01-08 03:47:41','2023-01-08 03:47:41'),(24,'Cristal','Almirante Pastene 70','Providencia','cristal@mail.com','$2b$12$lW6bubvW2jNwwPhUQkseR.B6yVuuCd.hTx6PjrgQ5XlPpP7UiH5Su','2023-01-08 06:05:12','2023-01-08 06:05:12');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-08 18:53:14
``` 