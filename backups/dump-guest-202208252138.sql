-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: guest
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add event',7,'add_event'),(26,'Can change event',7,'change_event'),(27,'Can delete event',7,'delete_event'),(28,'Can view event',7,'view_event'),(29,'Can add guest',8,'add_guest'),(30,'Can change guest',8,'change_guest'),(31,'Can delete guest',8,'delete_guest'),(32,'Can view guest',8,'view_guest');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$320000$JI9Z5LQYoDeM5yYnqWONeP$EhEzILZFHd+j+h63wEO7jpjeil3BUtN7hVtDvpGLne8=','2022-08-21 20:43:53.589335',1,'admin','','','admin@mail.com',1,1,'2022-08-06 11:01:25.074709');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-08-06 11:09:21.443642','1','中国中心发布会',1,'[{\"added\": {}}]',7,1),(2,'2022-08-06 11:09:55.518418','2','世界中线发布会',1,'[{\"added\": {}}]',7,1),(3,'2022-08-06 11:11:00.836300','3','太阳系发布会',1,'[{\"added\": {}}]',7,1),(4,'2022-08-06 11:11:58.073277','4','宇宙发布会',1,'[{\"added\": {}}]',7,1),(5,'2022-08-06 11:12:35.658637','4','宇宙发布会',2,'[]',7,1),(6,'2022-08-06 11:13:30.197372','5','银河系发布会',1,'[{\"added\": {}}]',7,1),(7,'2022-08-06 11:16:18.850608','1','地球人',1,'[{\"added\": {}}]',8,1),(8,'2022-08-06 11:16:52.077820','2','地球人',1,'[{\"added\": {}}]',8,1),(9,'2022-08-06 11:17:16.164776','3','太阳系人',1,'[{\"added\": {}}]',8,1),(10,'2022-08-06 11:17:44.393432','4','银河系人',1,'[{\"added\": {}}]',8,1),(11,'2022-08-06 11:18:07.854239','5','宇宙人',1,'[{\"added\": {}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'sign','event'),(8,'sign','guest');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-08-06 11:00:20.046672'),(2,'auth','0001_initial','2022-08-06 11:00:21.321314'),(3,'admin','0001_initial','2022-08-06 11:00:21.569820'),(4,'admin','0002_logentry_remove_auto_add','2022-08-06 11:00:21.582312'),(5,'admin','0003_logentry_add_action_flag_choices','2022-08-06 11:00:21.594985'),(6,'contenttypes','0002_remove_content_type_name','2022-08-06 11:00:21.706788'),(7,'auth','0002_alter_permission_name_max_length','2022-08-06 11:00:21.801057'),(8,'auth','0003_alter_user_email_max_length','2022-08-06 11:00:21.931872'),(9,'auth','0004_alter_user_username_opts','2022-08-06 11:00:21.949412'),(10,'auth','0005_alter_user_last_login_null','2022-08-06 11:00:22.042434'),(11,'auth','0006_require_contenttypes_0002','2022-08-06 11:00:22.047997'),(12,'auth','0007_alter_validators_add_error_messages','2022-08-06 11:00:22.061086'),(13,'auth','0008_alter_user_username_max_length','2022-08-06 11:00:22.159548'),(14,'auth','0009_alter_user_last_name_max_length','2022-08-06 11:00:22.275789'),(15,'auth','0010_alter_group_name_max_length','2022-08-06 11:00:22.375765'),(16,'auth','0011_update_proxy_permissions','2022-08-06 11:00:22.390031'),(17,'auth','0012_alter_user_first_name_max_length','2022-08-06 11:00:22.490553'),(18,'sessions','0001_initial','2022-08-06 11:00:22.551690'),(19,'sign','0001_initial','2022-08-06 11:00:22.704340');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('8n1tesdns66louf9n0jktc4lkv6btyyn','.eJxVjEEOwiAQRe_C2pBSQAaX7nsGMjCDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwk7gIJU6_W8T04LoDumO9NZlaXZc5yl2RB-1yasTP6-H-HRTs5Vsb4OjS2YOxJg3ZZ40aMI0Q2YDzaAm9zoPVYBTS6CIikwfrjGLtKYn3B-YhOB0:1oKA9v:mFyyTFon8BVcgWXVlysiGkdAQWDknGtIu9YA1y5V_98','2022-08-20 11:07:27.715662'),('uyu535olrz3rpev00ya9a3kfozlbq1z1','.eJxVjDsOwyAQBe9CHSFjICwp0_sM1sIuwfmA5E8V5e7BkoukfTNv3mLEbc3jtvA8TiQuQonT7xYwPrjsgO5YblXGWtZ5CnJX5EEXOVTi5_Vw_wIZl9zeBji4ePZgrIld8kmjBow9BDbgPFpCr1NnNRiF1LuAyOTBOqNYe4otuudaCek1FfH5AlIaPNM:1oPkIz:ooPTYKmsXdxr_yUq2h0Ggv8NsGXEMoo2eYdWiiD-ARw','2022-09-04 20:43:53.605640'),('xby92b1pjmtejvh10aqlwlfphxi9l067','.eJxVjDsOwyAQBe9CHSFjICwp0_sM1sIuwfmA5E8V5e7BkoukfTNv3mLEbc3jtvA8TiQuQonT7xYwPrjsgO5YblXGWtZ5CnJX5EEXOVTi5_Vw_wIZl9zeBji4ePZgrIld8kmjBow9BDbgPFpCr1NnNRiF1LuAyOTBOqNYe4otuudaCek1FfH5AlIaPNM:1oKtBr:2Fi85IKi6GvMHZYm51dFfNN0IXFnO27OEnMJG3W94B8','2022-08-22 11:12:27.070753');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sign_event`
--

DROP TABLE IF EXISTS `sign_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sign_event` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `limit` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `address` varchar(200) NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sign_event`
--

LOCK TABLES `sign_event` WRITE;
/*!40000 ALTER TABLE `sign_event` DISABLE KEYS */;
INSERT INTO `sign_event` VALUES (1,'中国中心发布会',10000,1,'中国中心','2022-07-26 02:42:48.000000','2022-08-06 11:09:21.442642'),(2,'世界中线发布会',50000,1,'世界中心','2022-08-27 00:00:00.000000','2022-08-06 11:09:55.517420'),(3,'太阳系发布会',100000,1,'地球','2050-08-06 00:00:00.000000','2022-08-06 11:11:00.836300'),(4,'银河系发布会',70000,1,'火星','2100-01-01 12:00:00.000000','2022-08-06 11:13:30.196372'),(5,'宇宙发布会',50000,1,'地球','2200-08-06 00:00:00.000000','2022-08-06 11:12:35.657639'),(11,'RedMI4',3000,1,'BeiJing','2023-11-08 14:00:00.000000','2022-08-24 17:55:43.178648');
/*!40000 ALTER TABLE `sign_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sign_guest`
--

DROP TABLE IF EXISTS `sign_guest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sign_guest` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `realname` varchar(64) NOT NULL,
  `phone` varchar(16) NOT NULL,
  `email` varchar(254) NOT NULL,
  `sign` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `event_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sign_guest_event_id_fa7638b3_fk_sign_event_id` (`event_id`),
  CONSTRAINT `sign_guest_event_id_fa7638b3_fk_sign_event_id` FOREIGN KEY (`event_id`) REFERENCES `sign_event` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sign_guest`
--

LOCK TABLES `sign_guest` WRITE;
/*!40000 ALTER TABLE `sign_guest` DISABLE KEYS */;
INSERT INTO `sign_guest` VALUES (1,'地球人','1234658901','1234658901@mail.com',1,'2022-08-06 11:16:18.849609',1),(2,'地球人','12345678902','12345678902@mail.com',0,'2022-08-06 11:16:52.076819',2),(3,'太阳系人','1234578903','1234578903@mail.com',1,'2022-08-06 11:17:16.163838',3),(4,'银河系人','12345678904','12345678904@mail.com',1,'2022-08-06 11:17:44.392431',4),(5,'宇宙人','12345678905','1345679805@mail.com',1,'2022-08-06 11:18:07.853236',5);
/*!40000 ALTER TABLE `sign_guest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'guest'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-25 21:38:40
