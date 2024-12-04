CREATE DATABASE  IF NOT EXISTS `starwars_db` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `starwars_db`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: starwars_db
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `alianzas`
--

DROP TABLE IF EXISTS `alianzas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alianzas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `lider_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_alianzas_personajes1_idx` (`lider_id`),
  CONSTRAINT `fk_alianzas_personajes1` FOREIGN KEY (`lider_id`) REFERENCES `personajes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alianzas`
--

LOCK TABLES `alianzas` WRITE;
/*!40000 ALTER TABLE `alianzas` DISABLE KEYS */;
INSERT INTO `alianzas` VALUES (1,'Alianza Rebelde',1,'2024-11-13 16:48:03','2024-11-13 16:48:03'),(2,'Imperio Galáctico',3,'2024-11-13 16:48:03','2024-11-13 16:48:03'),(3,'Guild de Cazarrecompensas',7,'2024-11-13 16:48:03','2024-11-13 16:48:03'),(4,'Primera Orden',8,'2024-11-13 16:48:03','2024-11-13 16:48:03');
/*!40000 ALTER TABLE `alianzas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `especies`
--

DROP TABLE IF EXISTS `especies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `especies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `especies`
--

LOCK TABLES `especies` WRITE;
/*!40000 ALTER TABLE `especies` DISABLE KEYS */;
INSERT INTO `especies` VALUES (1,'Humano','2024-11-13 16:46:23','2024-11-13 16:46:23'),(2,'Wookie','2024-11-13 16:46:23','2024-11-13 16:46:23'),(3,'Droide','2024-11-13 16:46:23','2024-11-13 16:46:23'),(4,'Twilek','2024-11-13 16:46:23','2024-11-13 16:46:23');
/*!40000 ALTER TABLE `especies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `naves`
--

DROP TABLE IF EXISTS `naves`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `naves` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `modelo` varchar(45) DEFAULT NULL,
  `capacidad` varchar(45) DEFAULT NULL,
  `piloto_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_naves_personajes1_idx` (`piloto_id`),
  CONSTRAINT `fk_naves_personajes1` FOREIGN KEY (`piloto_id`) REFERENCES `personajes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `naves`
--

LOCK TABLES `naves` WRITE;
/*!40000 ALTER TABLE `naves` DISABLE KEYS */;
INSERT INTO `naves` VALUES (1,'X-wing','T-65B','1',1,'2024-11-13 17:27:00','2024-11-13 17:27:00'),(2,'Millennium Falcon','YT-1300','6',5,'2024-11-13 17:27:00','2024-11-13 17:27:00'),(3,'TIE Fighter','TIE/LN','1',3,'2024-11-13 17:27:00','2024-11-13 17:27:00'),(4,'Slave I','Firespray-31','1',7,'2024-11-13 17:27:00','2024-11-13 17:27:00'),(5,'A-wing','RZ-1','1',11,'2024-11-13 17:27:00','2024-11-13 17:27:00'),(6,'Star Destroyer','Imperial I','47000',3,'2024-11-13 17:27:00','2024-11-13 17:27:00'),(7,'TIE Interceptor','TIE/IN','1',8,'2024-11-13 17:27:00','2024-11-13 17:27:00'),(8,'U-wing','UT-60D','2',9,'2024-11-13 17:27:00','2024-11-13 17:27:00');
/*!40000 ALTER TABLE `naves` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personajes`
--

DROP TABLE IF EXISTS `personajes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personajes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `año_nacimiento` int DEFAULT NULL,
  `planeta_id` int NOT NULL,
  `especie_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_personajes_planetas1_idx` (`planeta_id`),
  KEY `fk_personajes_especies1_idx` (`especie_id`),
  CONSTRAINT `fk_personajes_especies1` FOREIGN KEY (`especie_id`) REFERENCES `especies` (`id`),
  CONSTRAINT `fk_personajes_planetas1` FOREIGN KEY (`planeta_id`) REFERENCES `planetas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personajes`
--

LOCK TABLES `personajes` WRITE;
/*!40000 ALTER TABLE `personajes` DISABLE KEYS */;
INSERT INTO `personajes` VALUES (1,'Luke Skywalker',19,1,1,'2024-11-13 16:47:40','2024-11-13 16:47:40'),(2,'Leia Organa',19,2,1,'2024-11-13 16:47:40','2024-11-13 16:47:40'),(3,'Darth Vader',41,4,1,'2024-11-13 16:47:40','2024-11-13 16:47:40'),(4,'Yoda',896,3,4,'2024-11-13 16:47:40','2024-11-13 16:47:40'),(5,'Han Solo',29,1,1,'2024-11-13 16:47:40','2024-11-13 16:47:40'),(6,'Chewbacca',200,6,2,'2024-11-13 16:47:40','2024-11-13 16:47:40'),(7,'Boba Fett',32,5,1,'2024-11-13 16:47:40','2024-11-13 16:47:40'),(8,'Kylo Ren',-5,5,1,'2024-11-13 16:47:40','2024-11-13 16:47:40'),(9,'R2-D2',33,5,3,'2024-11-13 16:47:40','2024-11-13 16:47:40'),(10,'Rey',15,1,1,'2024-11-13 16:47:40','2024-11-13 16:47:40'),(11,'Finn',7,5,1,'2024-11-13 16:47:40','2024-11-13 16:47:40');
/*!40000 ALTER TABLE `personajes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `planetas`
--

DROP TABLE IF EXISTS `planetas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `planetas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `region` varchar(45) DEFAULT NULL,
  `poblacion` bigint DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `planetas`
--

LOCK TABLES `planetas` WRITE;
/*!40000 ALTER TABLE `planetas` DISABLE KEYS */;
INSERT INTO `planetas` VALUES (1,'Tatooine','Borde Exterior',200000,'2024-11-13 16:46:48','2024-11-13 16:46:48'),(2,'Alderaan','Mundos del Núcleo',0,'2024-11-13 16:46:48','2024-11-13 16:46:48'),(3,'Dagobah','Borde Exterior',NULL,'2024-11-13 16:46:48','2024-11-13 16:46:48'),(4,'Coruscant','Mundos del Núcleo',1000000000000,'2024-11-13 16:46:48','2024-11-13 16:46:48'),(5,'Naboo','Mundos del Núcleo',4500000000,'2024-11-13 16:46:48','2024-11-13 16:46:48'),(6,'Kashyyyk','Borde Medio',7000000,'2024-11-13 16:46:48','2024-11-13 16:46:48'),(7,'Hoth','Borde Exterior',1000,'2024-11-13 16:46:48','2024-11-13 16:46:48'),(8,'Endor','Región Desconocida',30000,'2024-11-13 16:46:48','2024-11-13 16:46:48'),(9,'Mustafar','Borde Exterior',NULL,'2024-11-13 16:46:48','2024-11-13 16:46:48'),(10,'Yavin IV','Borde Exterior',1000,'2024-11-13 16:46:48','2024-11-13 16:46:48'),(11,'Geonosis','Borde Exterior',100000000,'2024-11-13 16:46:48','2024-11-13 16:46:48'),(12,'Kamino','Borde Medio',500000,'2024-11-13 16:46:48','2024-11-13 16:46:48'),(13,'Bespin','Región del Núcleo',NULL,'2024-11-13 16:46:48','2024-11-13 16:46:48'),(14,'Mandalore','Borde Exterior',500000,'2024-11-13 16:46:48','2024-11-13 16:46:48'),(15,'Jakku','Borde Exterior',50000,'2024-11-13 16:46:48','2024-11-13 16:46:48');
/*!40000 ALTER TABLE `planetas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-13 18:36:56
