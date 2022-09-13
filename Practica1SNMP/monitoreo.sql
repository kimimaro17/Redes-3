-- MySQL dump 10.13  Distrib 8.0.30, for Linux (x86_64)
--
-- Host: localhost    Database: monitoreo
-- ------------------------------------------------------
-- Server version	8.0.30-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Dispositivos`
--

DROP TABLE IF EXISTS `Dispositivos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Dispositivos` (
  `IDispo` int NOT NULL AUTO_INCREMENT,
  `host` varchar(300) NOT NULL,
  `comunidad` varchar(300) NOT NULL,
  `puerto` int NOT NULL,
  `so` varchar(100) NOT NULL,
  `version` varchar(500) NOT NULL,
  `nombre` varchar(300) NOT NULL,
  `contacto` varchar(300) NOT NULL,
  `ubicacion` varchar(300) NOT NULL,
  `ninter` varchar(10) NOT NULL,
  PRIMARY KEY (`IDispo`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dispositivos`
--

LOCK TABLES `Dispositivos` WRITE;
/*!40000 ALTER TABLE `Dispositivos` DISABLE KEYS */;
INSERT INTO `Dispositivos` VALUES (18,'localhost','Bowser',161,'Linux','5.4.0-74-generic#83-Ubuntu','kimi','kimimaro1789@gmail.com','\"Mi compu\"','5'),(20,'192.168.31.193','Bowser',161,'Linux','3.19.0-32-generic#37~14.04.1-Ubuntu','kimimaroV','ahernandezo1606@alumno.ipn.mx','LinuxDos','2'),(21,'192.168.31.184','Bowser',161,'Windows','Version6.3','kimi','kimimaro1789@gmail.com','Ventanas','7');
/*!40000 ALTER TABLE `Dispositivos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Interfaces`
--

DROP TABLE IF EXISTS `Interfaces`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Interfaces` (
  `IDispo` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(300) NOT NULL,
  `estado` varchar(300) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `IDispo` (`IDispo`),
  CONSTRAINT `Interfaces_ibfk_1` FOREIGN KEY (`IDispo`) REFERENCES `Dispositivos` (`IDispo`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Interfaces`
--

LOCK TABLES `Interfaces` WRITE;
/*!40000 ALTER TABLE `Interfaces` DISABLE KEYS */;
INSERT INTO `Interfaces` VALUES (18,55,'lo','up'),(18,56,'Realtek Semiconductor Co., Ltd. RTL810xE PCI Express Fast Ethernet controller','down'),(18,57,'Ralink corp. RT3290 Wireless 802.11n 1T/1R PCIe','up'),(18,58,'virbr0','down'),(18,59,'virbr0-nic','down'),(20,61,'lo','up'),(20,62,'eth0','up'),(21,63,'Software Loopback Interface 1\0','up'),(21,64,'Adaptador de red de depuraci¢n de kernel de Microsoft\0','notPresent'),(21,65,'Adaptador de escritorio Intel(R) PRO/1000 MT\0','up'),(21,66,'Adaptador ISATAP de Microsoft\0','down'),(21,67,'Adaptador de escritorio Intel(R) PRO/1000 MT-WFP Native MAC Layer LightWeight Filter-0000\0','up'),(21,68,'Adaptador de escritorio Intel(R) PRO/1000 MT-QoS Packet Scheduler-0000\0','up'),(21,69,'Adaptador de escritorio Intel(R) PRO/1000 MT-WFP 802.3 MAC Layer LightWeight Filter-0000\0','up');
/*!40000 ALTER TABLE `Interfaces` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-13 15:23:55
