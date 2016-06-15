/*
Navicat MySQL Data Transfer

Source Server         : myBD
Source Server Version : 50537
Source Host           : localhost:3306
Source Database       : avdata

Target Server Type    : MYSQL
Target Server Version : 50537
File Encoding         : 65001

Date: 2016-06-15 17:54:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `codeinfo`
-- ----------------------------
DROP TABLE IF EXISTS `codeinfo`;
CREATE TABLE `codeinfo` (
  `codeid` int(11) NOT NULL,
  `代码` char(6) NOT NULL,
  `名称` tinytext,
  `沪深` tinytext,
  `次新` char(1) DEFAULT NULL,
  `中心` char(1) DEFAULT NULL,
  `创业` char(1) DEFAULT NULL,
  `st` char(1) DEFAULT NULL,
  `行业` tinytext,
  `市值` tinytext,
  PRIMARY KEY (`代码`)
) ENGINE=InnoDB DEFAULT CHARSET=gb2312;

-- ----------------------------
-- Records of codeinfo
-- ----------------------------
