/*
Navicat MySQL Data Transfer

Source Server         : arfcrrr
Source Server Version : 100411
Source Host           : localhost:3306
Source Database       : karchiz

Target Server Type    : MYSQL
Target Server Version : 100411
File Encoding         : 65001

Date: 2021-01-02 09:58:40
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES ('1', 'Pop');
INSERT INTO `category` VALUES ('2', 'R&B');
INSERT INTO `category` VALUES ('3', 'Heavy Metal');
INSERT INTO `category` VALUES ('4', 'EDM');
INSERT INTO `category` VALUES ('5', 'Hip Hop');

-- ----------------------------
-- Table structure for event
-- ----------------------------
DROP TABLE IF EXISTS `event`;
CREATE TABLE `event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(30) NOT NULL,
  `schedule` datetime NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `event_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of event
-- ----------------------------
INSERT INTO `event` VALUES ('1', 'Stadiums in the Summer Tour', '2021-01-05 20:00:00', '1', null, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit');
INSERT INTO `event` VALUES ('2', 'On the Road Again Tour', '2021-01-07 15:30:00', '1', null, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.');
INSERT INTO `event` VALUES ('3', 'Airbeat-One Festival', '2021-02-11 21:00:00', '4', null, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.');
INSERT INTO `event` VALUES ('4', 'Weekend at Fattys', '2021-03-13 20:30:00', '3', null, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.');
INSERT INTO `event` VALUES ('5', 'OMG Tour', '2021-04-20 16:00:00', '2', null, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.');
INSERT INTO `event` VALUES ('6', '4:44 Tour', '2021-04-05 22:00:00', '5', null, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.');

-- ----------------------------
-- Table structure for order
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `ticket_id` int(11) DEFAULT NULL,
  `order_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `ticket_id` (`ticket_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES ('1', '1', '9', '2020-12-30 22:00:13');
INSERT INTO `orders` VALUES ('2', '2', '7', '2020-12-31 16:45:20');
INSERT INTO `orders` VALUES ('3', '3', '5', '2020-12-31 19:30:22');
INSERT INTO `orders` VALUES ('4', '4', '3', '2021-01-01 04:15:36');
INSERT INTO `orders` VALUES ('5', '5', '2', '2021-01-01 09:22:47');
INSERT INTO `orders` VALUES ('6', '6', '1', '2021-01-01 10:02:22');
INSERT INTO `orders` VALUES ('7', '7', '4', '2021-01-01 20:56:18');
INSERT INTO `orders` VALUES ('8', '8', '6', '2021-01-02 12:03:56');
INSERT INTO `orders` VALUES ('9', '9', '8', '2021-01-02 13:40:02');
INSERT INTO `orders` VALUES ('10', '10', '1', '2021-01-03 02:05:05');

-- ----------------------------
-- Table structure for ticket
-- ----------------------------
DROP TABLE IF EXISTS `ticket`;
CREATE TABLE `ticket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) DEFAULT NULL,
  `type` varchar(30) NOT NULL,
  `price` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `event_id` (`event_id`),
  CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of ticket
-- ----------------------------
INSERT INTO `ticket` VALUES ('1', '1', 'Bronze', '1200000');
INSERT INTO `ticket` VALUES ('2', '1', 'Silver', '1600000');
INSERT INTO `ticket` VALUES ('3', '1', 'Gold', '2000000');
INSERT INTO `ticket` VALUES ('4', '2', 'Bronze', '800000');
INSERT INTO `ticket` VALUES ('5', '2', 'Silver', '1300000');
INSERT INTO `ticket` VALUES ('6', '2', 'Gold', '1750000');
INSERT INTO `ticket` VALUES ('7', '3', 'Bronze', '1400000');
INSERT INTO `ticket` VALUES ('8', '3', 'Silver', '1800000');
INSERT INTO `ticket` VALUES ('9', '3', 'Gold', '2250000');
INSERT INTO `ticket` VALUES ('10', '4', 'Bronze', '500000');
INSERT INTO `ticket` VALUES ('11', '4', 'Silver', '900000');
INSERT INTO `ticket` VALUES ('12', '4', 'Gold', '1300000');
INSERT INTO `ticket` VALUES ('13', '5', 'Bronze', '1250000');
INSERT INTO `ticket` VALUES ('14', '5', 'Silver', '1600000');
INSERT INTO `ticket` VALUES ('15', '5', 'Gold', '1950000');
INSERT INTO `ticket` VALUES ('16', '6', 'Bronze', '2000000');
INSERT INTO `ticket` VALUES ('17', '6', 'Silver', '2600000');
INSERT INTO `ticket` VALUES ('18', '6', 'Gold', '3200000');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `age` int(11) NOT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'ajengarifacr', 'ajengacr048', 'wanita', '20', null);
INSERT INTO `user` VALUES ('2', 'albanikautsar', 'albani047', 'pria', '25', null);
INSERT INTO `user` VALUES ('3', 'alfianpratama', 'alfian050', 'pria', '23', null);
INSERT INTO `user` VALUES ('4', 'putrisarahft', 'putri037', 'wanita', '19', null);
INSERT INTO `user` VALUES ('5', 'wahyumiftahul', 'wahyu060', 'pria', '18', null);
INSERT INTO `user` VALUES ('6', 'dylanminn', '123minnete', 'pria', '29', null);
INSERT INTO `user` VALUES ('7', 'braedenlm', '456lemasters', 'pria', '23', null);
INSERT INTO `user` VALUES ('8', 'namdosan', '789dosan', 'pria', '25', null);
INSERT INTO `user` VALUES ('9', 'carlalala', 'carla025', 'wanita', '27', null);
INSERT INTO `user` VALUES ('10', 'seodalmi', 'dalmi100', 'wanita', '24', null);
SET FOREIGN_KEY_CHECKS=1;
