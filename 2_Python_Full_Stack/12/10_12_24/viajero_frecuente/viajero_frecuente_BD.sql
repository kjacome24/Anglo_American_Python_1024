CREATE DATABASE  IF NOT EXISTS `viajero_frecuente` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `viajero_frecuente`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: viajero_frecuente
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
-- Table structure for table `unirse`
--

DROP TABLE IF EXISTS `unirse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unirse` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `viaje_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_usuarios_has_viajes_viajes1_idx` (`viaje_id`),
  KEY `fk_usuarios_has_viajes_usuarios1_idx` (`usuario_id`),
  CONSTRAINT `fk_usuarios_has_viajes_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `fk_usuarios_has_viajes_viajes1` FOREIGN KEY (`viaje_id`) REFERENCES `viajes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unirse`
--

LOCK TABLES `unirse` WRITE;
/*!40000 ALTER TABLE `unirse` DISABLE KEYS */;
INSERT INTO `unirse` VALUES (6,21,22),(18,20,25);
/*!40000 ALTER TABLE `unirse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `apellido` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (20,'Kevin','Duque','kevin.arturo.jacome.duque@gmail.com','$2b$12$ql6iJpirrUuckxn.gObxj.wKdNJQUhNMAoR6Qo2sJsMUyBul0M3RO','2024-12-10 13:26:48','2024-12-10 13:26:48'),(21,'Arturo','Duque','support@acme.com','$2b$12$.3lRufp.Dl.dVASDAFXvsupHh/nAErrZnTqVOoyEFzZ0q6krMDk4K','2024-12-10 17:20:53','2024-12-10 17:20:53');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `viajes`
--

DROP TABLE IF EXISTS `viajes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `viajes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `destino` varchar(255) DEFAULT NULL,
  `fecha_inicio` datetime DEFAULT NULL,
  `fecha_fin` datetime DEFAULT NULL,
  `itinerario` varchar(255) DEFAULT NULL,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `organizador_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_resetas_usuarios_idx` (`organizador_id`),
  CONSTRAINT `fk_resetas_usuarios` FOREIGN KEY (`organizador_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `viajes`
--

LOCK TABLES `viajes` WRITE;
/*!40000 ALTER TABLE `viajes` DISABLE KEYS */;
INSERT INTO `viajes` VALUES (22,'Amazonas','2024-12-12 16:11:13','2024-12-13 16:11:13','xxxx','2024-12-10 16:28:41','2024-12-10 16:11:13',20),(24,'saaaa','2024-12-10 16:25:35','2024-12-10 16:25:35','qqqqq','2024-12-10 16:25:35','2024-12-10 16:25:35',20),(25,'Acapulco','2024-12-13 17:23:17','2024-12-14 17:23:17','wwwww','2024-12-10 17:23:43','2024-12-10 17:23:17',21);
/*!40000 ALTER TABLE `viajes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-10 22:12:56
