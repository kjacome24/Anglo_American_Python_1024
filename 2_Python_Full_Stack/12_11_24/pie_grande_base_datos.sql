CREATE DATABASE  IF NOT EXISTS `pie_grande` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `pie_grande`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: pie_grande
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
-- Table structure for table `avistamientos`
--

DROP TABLE IF EXISTS `avistamientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avistamientos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ubicacion` varchar(100) DEFAULT NULL,
  `descripcion` varchar(400) DEFAULT NULL,
  `numero_de_pie_grandes` int DEFAULT NULL,
  `fecha_avistamiento` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_avistamientos_usuarios_idx` (`usuario_id`),
  CONSTRAINT `fk_avistamientos_usuarios` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avistamientos`
--

LOCK TABLES `avistamientos` WRITE;
/*!40000 ALTER TABLE `avistamientos` DISABLE KEYS */;
INSERT INTO `avistamientos` VALUES (1,'El desierto de la tatacoa','El piegrande estaba escondido',1,'2024-11-12 19:44:14','2024-11-12 19:43:29','2024-11-12 19:44:14',1),(2,'El amazonas','El piegrande se estaba bananado',1,'2024-11-12 00:00:00','2024-11-12 19:45:25','2024-11-12 19:45:25',1),(3,'xxx','xxxx',2,'2024-11-12 00:00:00','2024-11-12 19:45:51','2024-11-12 19:45:51',2),(4,'zzz','xxxx',1,NULL,'2024-11-12 19:50:38','2024-11-12 19:50:38',3);
/*!40000 ALTER TABLE `avistamientos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `no_creo`
--

DROP TABLE IF EXISTS `no_creo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `no_creo` (
  `usuario_id` int NOT NULL,
  `avistamiento_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`usuario_id`,`avistamiento_id`),
  KEY `fk_usuarios_has_avistamientos_avistamientos1_idx` (`avistamiento_id`),
  KEY `fk_usuarios_has_avistamientos_usuarios1_idx` (`usuario_id`),
  CONSTRAINT `fk_usuarios_has_avistamientos_avistamientos1` FOREIGN KEY (`avistamiento_id`) REFERENCES `avistamientos` (`id`),
  CONSTRAINT `fk_usuarios_has_avistamientos_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `no_creo`
--

LOCK TABLES `no_creo` WRITE;
/*!40000 ALTER TABLE `no_creo` DISABLE KEYS */;
/*!40000 ALTER TABLE `no_creo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombres` varchar(45) DEFAULT NULL,
  `apellidos` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Kevin A','Jacome D','kduque@codingdojo.la','123456','2024-11-12 19:22:58','2024-11-12 19:23:45'),(2,'Renata','Fernandez','rfrenandez@codingdojo.la','123456','2024-11-12 19:26:02','2024-11-12 19:26:02'),(3,'Jose Mateo','Castillo','jcastillo@codingdojo.la','1234567','2024-11-12 19:29:47','2024-11-12 19:29:47'),(4,'Arturo','Marino','amarino@codingdojo.la','1234567','2024-11-12 19:30:18','2024-11-12 19:30:18'),(5,'Fabian','Marino','fabian@codingdojo.la','1234567','2024-11-12 19:33:12','2024-11-12 19:33:12');
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

-- Dump completed on 2024-11-13 14:53:39
