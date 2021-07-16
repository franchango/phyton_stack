-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: walldb
-- ------------------------------------------------------
-- Server version	5.7.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `messages_id` int(11) NOT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_messages1_idx` (`messages_id`),
  KEY `fk_comments_users1_idx` (`users_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`messages_id`) REFERENCES `messages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,'Hi','2017-10-13 17:46:35',NULL,5,1),(2,'shut up already','2017-10-13 18:34:40',NULL,6,1),(3,'y u talk to self','2017-10-13 18:49:26',NULL,5,4),(4,'sndalfkjisdaf\r\n','2017-10-13 18:59:44',NULL,5,3),(5,'yeah I agree\r\n','2017-10-13 21:14:32',NULL,2,5);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`users_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'My money\'s in that office, right? If she start giving me some bullshit about it ain\'t there, and we got to go someplace else and get it, I\'m gonna shoot you in the head then and there. Then I\'m gonna shoot that bitch in the kneecaps, find out where my goddamn money is. She gonna tell me too. Hey, look at me when I\'m talking to you, motherfucker. You listen: we go in there, and that nigga Winston or anybody else is in there, you the first motherfucker to get shot. You understand?',NULL,NULL,1),(2,'Your bones don\'t break, mine do. That\'s clear. Your cells react to bacteria and viruses differently than mine. You don\'t get sick, I do. That\'s also clear. But for some reason, you and I react the exact same way to water. We swallow it too fast, we choke. We get some in our lungs, we drown. However unreal it may seem, we are connected, you and I. We\'re on the same curve, just on opposite ends.',NULL,NULL,1),(3,'ImmutableMultiDict([(\'action\', u\'message\'), (\'go\', u\'Post a message\'), (\'message\', u\'hullo\')])','2017-10-13 16:12:04',NULL,1),(4,'\"Hey, do you guys have szechuan sauce?\", I ask the low IQ minimum wage slave. \"N-no, sir. We just ran out\", he muttered. I was overcome with a primal rage. I jump on the counter, screaming \"I\'m Pickle Rick!”. The 200 IQ crowd chanted in unison, “WUBBALUBBA DUB DUB” whilst beating their chests towards the cowering worker. I put my shirt over my head and let out the purest REEE to show my devotion to Rick. Everyone else REEEs as well. Yes, my brothers, let it all out. The manger comes in and calls the police, he doesn’t understand the mature and intellectual nature of our cries. We Naruto run to the next McDonalds store as we search endlessly for that sauce.','2017-10-13 16:18:12',NULL,1),(5,'I\"M PICKLE RIIIIICK','2017-10-13 16:20:19',NULL,2),(6,'uh suuuuuuuuuuuh dude','2017-10-13 16:24:24',NULL,3),(7,'Well, the way they make shows is, they make one show. That show\'s called a pilot. Then they show that show to the people who make shows, and on the strength of that one show they decide if they\'re going to make more shows. Some pilots get picked and become television programs. Some don\'t, become nothing. She starred in one of the ones that became nothing.','2017-10-13 18:58:20',NULL,3),(8,'The path of the righteous man is beset on all sides by the iniquities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of darkness, for he is truly his brother\'s keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who would attempt to poison and destroy My brothers. And you will know My name is the Lord when I lay My vengeance upon thee.\r\n','2017-10-13 20:47:31',NULL,5);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Test','Testy','test@test.com',NULL,NULL,'05a671c66aefea124cc08b76ea6d30bb'),(2,'Pickle Rick','Sanchez','pr@pbr.com',NULL,NULL,'65d671ec9787b32cfb7e33188be32ff7'),(3,'Brat','Fratley','beer@suhdude.com',NULL,NULL,'612c2a27442c5c04649caf6f10a40251'),(4,'george','of jungle','watch@for.tree',NULL,NULL,'2bb940bf531217f7b59db15665af1012'),(5,'bitchass','pTags','big@kahunaburger.com',NULL,NULL,'7efd64defed78f97ee4ef1a9462305a7');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-13 21:20:18
