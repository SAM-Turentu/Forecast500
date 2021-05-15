/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80021
 Source Host           : localhost:3306
 Source Schema         : forecast500

 Target Server Type    : MySQL
 Target Server Version : 80021
 File Encoding         : 65001

 Date: 11/05/2021 22:54:06
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for forecast_user
-- ----------------------------
DROP TABLE IF EXISTS `forecast_user`;
CREATE TABLE `forecast_user`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `userId` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `userPhone` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `userPassword` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `userName` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `userBirthday` datetime(0) NULL DEFAULT NULL,
  `userEmail` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `userSex` smallint NULL DEFAULT 0 COMMENT '0:男，1：女',
  `userLoginTime` datetime(0) NULL DEFAULT NULL,
  `userCreateTime` datetime(0) NULL DEFAULT NULL,
  `userUpdateTime` datetime(0) NULL DEFAULT NULL,
  `userDelete` smallint NULL DEFAULT 0,
  `userStatus` smallint NULL DEFAULT 0,
  `userDisable` smallint NULL DEFAULT 0,
  `userVIP` smallint NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `userId`(`userId`) USING BTREE,
  INDEX `userPhone`(`userPhone`) USING BTREE,
  INDEX `userName`(`userName`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
