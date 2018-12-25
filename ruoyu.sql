/*
/*
Navicat MySQL Data Transfer

Source Server         : name
Source Server Version : 80012
Source Host           : localhost:3306
Source Database       : ruoyu

Target Server Type    : MYSQL
Target Server Version : 80012
File Encoding         : 65001

Date: 2018-12-24 13:43:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for collect
-- ----------------------------
DROP TABLE IF EXISTS `collect`;
CREATE TABLE `collect` (
  `id` int(9) NOT NULL,
  `content` varchar(1000) DEFAULT NULL,
  `other_id` int(9) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `other_id` (`other_id`),
  CONSTRAINT `collect_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`),
  CONSTRAINT `collect_ibfk_2` FOREIGN KEY (`other_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of collect
-- ----------------------------
INSERT INTO `collect` VALUES ('2', '\n\n第一次正式写影评：虽然一直是MCU的影迷，但这次真的是被DC惊艳到了，它摒弃了以往DC的暗黑风格，成功的关键是我一直以来喜爱的导演：温子仁，终于明白为什么那么喜欢他的作品了，才华使他作任何类型片都可以好好的讲故事，抓住观众的心，无论剧情，特效都是美轮美奂。期初是抱着最近市场没什么大片正好赶上中国全球首映，所以尝鲜，结果真的很出乎意料，凭我越影无数 电影发烧友来说这部作品是我近几年看到最好的超级英雄电影。不分DC和MCU只轮电影本身。我也不随意站队，只想表达我的客观感受，好就是好，至少这个电影我不觉得时间长而且全程无尿点无瞌睡，无论剧情 打斗 特效 场景 都很吸引我。为电影迷来说我看的是IMAX版本，我也推荐大家看IMAX或中国巨幕，不然很浪费这部作品。不是水军，影票截图为证！希望可以帮到大家，虽然我说的很肤浅，很表面，但是我只想说好看！', '3');

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `User_id` int(9) NOT NULL,
  `Commented_id` int(9) NOT NULL,
  `Content` varchar(1000) NOT NULL,
  `Creatime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`User_id`),
  KEY `Commented_id` (`Commented_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`User_id`) REFERENCES `users` (`id`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`Commented_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES ('1', '3', '剧情也美轮美奂？想看特效的可以去电影院，剧情和黑豹一模一样的套路，你懂得。', '2018-12-22 12:04:23');

-- ----------------------------
-- Table structure for focus
-- ----------------------------
DROP TABLE IF EXISTS `focus`;
CREATE TABLE `focus` (
  `id` int(9) NOT NULL,
  `focusid1` int(9) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `focusid1` (`focusid1`),
  CONSTRAINT `focus_ibfk_1` FOREIGN KEY (`id`) REFERENCES `users` (`id`),
  CONSTRAINT `focus_ibfk_2` FOREIGN KEY (`focusid1`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of focus
-- ----------------------------
INSERT INTO `focus` VALUES ('1', '2');

-- ----------------------------
-- Table structure for forum
-- ----------------------------
DROP TABLE IF EXISTS `forum`;
CREATE TABLE `forum` (
  `Post_id` int(9) NOT NULL AUTO_INCREMENT,
  `Title` varchar(55) NOT NULL,
  `Content` varchar(1000) NOT NULL,
  `Createtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `UserId` int(9) NOT NULL,
  `LastAnswerTime` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `Hitcount` int(5) NOT NULL DEFAULT '0',
  `AnswerID` int(4) NOT NULL DEFAULT '0',
  `AnswerCount` int(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`Post_id`),
  KEY `forum_ibfk_1` (`UserId`),
  CONSTRAINT `forum_ibfk_1` FOREIGN KEY (`UserId`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of forum
-- ----------------------------
INSERT INTO `forum` VALUES ('1', '海王观后真实推荐', '\n第一次正式写影评：虽然一直是MCU的影迷，但这次真的是被DC惊艳到了，它摒弃了以往DC的暗黑风格，成功的关键是我一直以来喜爱的导演：温子仁，终于明白为什么那么喜欢他的作品了，才华使他作任何类型片都可以好好的讲故事，抓住观众的心，无论剧情，特效都是美轮美奂。期初是抱着最近市场没什么大片正好赶上中国全球首映，所以尝鲜，结果真的很出乎意料，凭我越影无数 电影发烧友来说这部作品是我近几年看到最好的超级英雄电影。不分DC和MCU只轮电影本身。我也不随意站队，只想表达我的客观感受，好就是好，至少这个电影我不觉得时间长而且全程无尿点无瞌睡，无论剧情 打斗 特效 场景 都很吸引我。为电影迷来说我看的是IMAX版本，我也推荐大家看IMAX或中国巨幕，不然很浪费这部作品。不是水军，影票截图为证！希望可以帮到大家，虽然我说的很肤浅，很表面，但是我只想说好看！', '2018-12-22 11:59:45', '2', '2018-12-22 12:07:20', '0', '0', '0');

-- ----------------------------
-- Table structure for movie
-- ----------------------------
DROP TABLE IF EXISTS `movie`;
CREATE TABLE `movie` (
  `movie_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `actor` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `movie_id` int(9) NOT NULL AUTO_INCREMENT,
  `grade` int(3) NOT NULL DEFAULT '0',
  `releasetime` timestamp NOT NULL,
  `language` varchar(20) NOT NULL,
  `director` varchar(20) NOT NULL,
  `Plot` varchar(1000) NOT NULL,
  `Picture` longblob NOT NULL,
  PRIMARY KEY (`movie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of movie
-- ----------------------------
INSERT INTO `movie` VALUES ('海王', '杰森·莫玛、艾梅柏·希尔德、帕特里克·威尔森、叶海亚·阿卜杜勒-迈丁、妮可·基德曼', '1', '0', '2018-12-07 11:38:30', 'English', '温子华', '亚瑟（杰森·莫玛饰）是亚特兰蒂斯女王亚特兰娜（妮可·基德曼饰）的儿子。亚特兰娜当年因反抗政治婚姻，逃到陆上与一个灯塔守护人相爱，生下半人半神的亚瑟。几年之后，亚特兰娜被迫回到海底国家缔结政治婚姻，生下儿子奥姆（帕特里克·威尔森饰）。奥姆长大后对陆地人类充满憎恨，开始用使用计谋打算吞并海底中发展中的国家的兵力，一举消灭陆地人。海底王国泽贝尔的公主湄拉（艾梅柏·希尔德饰）打算阻止这场战争，她到陆地找回亚瑟，让他以亚特兰娜女王长子身份回亚特兰蒂斯把王位争回来，而且湄拉要协助亚瑟找回能统治大海的失落的三叉戟 [3]  。', 0xD1C7C9AAA3A8BDDCC9ADA1A4C4AAC2EACACEA3A9CAC7D1C7CCD8C0BCB5D9CBB9C5AECDF5D1C7CCD8C0BCC4C8A3A8C4DDBFC9A1A4BBF9B5C2C2FCCACEA3A9B5C4B6F9D7D3A1A3D1C7CCD8C0BCC4C8B5B1C4EAD2F2B7B4BFB9D5FED6CEBBE9D2F6A3ACCCD3B5BDC2BDC9CFD3EBD2BBB8F6B5C6CBFECAD8BBA4C8CBCFE0B0AEA3ACC9FACFC2B0EBC8CBB0EBC9F1B5C4D1C7C9AAA1A3BCB8C4EAD6AEBAF3A3ACD1C7CCD8C0BCC4C8B1BBC6C8BBD8B5BDBAA3B5D7B9FABCD2B5DEBDE1D5FED6CEBBE9D2F6A3ACC9FACFC2B6F9D7D3B0C2C4B7A3A8C5C1CCD8C0EFBFCBA1A4CDFEB6FBC9ADCACEA3A9A1A3B0C2C4B7B3A4B4F3BAF3B6D4C2BDB5D8C8CBC0E0B3E4C2FAD4F7BADEA3ACBFAACABCD3C3CAB9D3C3BCC6C4B1B4F2CBE3CDCCB2A2BAA3B5D7D6D0B7A2D5B9D6D0B5C4B9FABCD2B5C4B1F8C1A6A3ACD2BBBED9CFFBC3F0C2BDB5D8C8CBA1A3BAA3B5D7CDF5B9FAD4F3B1B4B6FBB5C4B9ABD6F7E4D8C0ADA3A8B0ACC3B7B0D8A1A4CFA3B6FBB5C2CACEA3A9B4F2CBE3D7E8D6B9D5E2B3A1D5BDD5F9A3ACCBFDB5BDC2BDB5D8D5D2BBD8D1C7C9AAA3ACC8C3CBFBD2D4D1C7CCD8C0BCC4C8C5AECDF5B3A4D7D3C9EDB7DDBBD8D1C7CCD8C0BCB5D9CBB9B0D1CDF5CEBBD5F9BBD8C0B4A3ACB6F8C7D2E4D8C0ADD2AAD0ADD6FAD1C7C9AAD5D2BBD8C4DCCDB3D6CEB4F3BAA3B5C4CAA7C2E4B5C4C8FDB2E6EAAA205B335D2020A1A3);
INSERT INTO `movie` VALUES ('蜘蛛侠：平行宇宙', ' 沙梅克·摩尔 /杰克·约翰逊 /尼古拉斯·凯奇 /列维·施瑞博尔 /莉莉·汤姆林', '3', '0', '2018-12-20 11:41:29', 'English', ' 鲍勃·佩尔西凯蒂 /彼得·拉姆齐', '蜘蛛侠不止一个！漫威超英动画巨制《蜘蛛侠：平行宇宙》将经典漫画与CGI技术完美呈现，讲述了普通高中生迈尔斯·莫拉斯如何师从蜘蛛侠彼得·帕克，成长为新一代超级英雄的故事。影片中迈尔斯和从其它平行宇宙中穿越而来的彼得、女蜘蛛侠格温、暗影蜘蛛侠、潘妮·帕克和蜘猪侠集结成团，六位蜘蛛侠首次同框大银幕，对抗蜘蛛侠宇宙最强反派。', '');
INSERT INTO `movie` VALUES ('龙猫', '配音：日高法子、坂本千夏、糸井重里', '4', '0', '2018-12-14 11:53:54', '日语', '宫崎骏', '小月（日高法子 配音）的母亲（岛本须美 配音）生病住院了，父亲（糸井重里 配音）带着她与四岁的妹妹小梅（坂本千夏 配音）到乡间居住。她们对那里的环境都感到十分新奇，也发现了很多有趣的事情。她们遇到了很多小精灵，她们来到属于她们的环境中，看到了她们世界中很多的奇怪事物，更与一只大大胖胖的龙猫（高木均 配音）成为了朋友。龙猫与小精灵们利用他们的神奇力量，为小月与妹妹带来了很多神奇的景观，令她们大开眼界。妹妹小梅常常挂念生病中的母亲，嚷着要姐姐带着她去看母亲，但小月拒绝了。小梅竟然自己前往，不料途中迷路了，小月只好寻找她的龙猫及小精灵朋友们的帮助。', '');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(9) NOT NULL AUTO_INCREMENT,
  `email` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `nick_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `pw` varchar(20) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `avatar_url` varchar(10) DEFAULT NULL,
  `signture` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `nick_name` (`nick_name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', '17zxgao@stu.edu.cn', '不知名', 'password', '2018-12-19 17:06:42', '', null);
INSERT INTO `users` VALUES ('2', '17qrgaga@stu.edu.cn', '个气温很高', 'qphgqa', '2018-12-19 17:20:15', null, null);
INSERT INTO `users` VALUES ('3', '18wgeaa@stu.edu.cn', '认为如果', '髂骨', '2018-12-19 17:28:36', null, null);
INSERT INTO `users` VALUES ('4', '17wjli6@stu.edu.cn', '李大爷', '17wjli6@stu.edu.cn', '2018-12-22 10:56:41', null, null);
INSERT INTO `users` VALUES ('5', '17xjhe@stu.edu.cn', '便便', '17xjhe@stu.edu.cn', '2018-12-22 10:58:00', null, null);
INSERT INTO `users` VALUES ('6', '17qychen1@stu.edu.cn', 'joy', '17qychen1@stu.edu.cn', '2018-12-22 10:59:32', null, null);

-- ----------------------------
-- Table structure for verification_code
-- ----------------------------
DROP TABLE IF EXISTS `verification_code`;
CREATE TABLE `verification_code` (
  `Code_num` int(5) NOT NULL,
  `email` varchar(30) NOT NULL,
  `verification_code` int(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`Code_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of verification_code
-- ----------------------------
