-- -------------------------------------------------------------
-- TablePlus 5.3.8(500)
--
-- https://tableplus.com/
--
-- Database: hadar
-- Generation Time: 2023-06-09 13:16:19.4660
-- -------------------------------------------------------------


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


CREATE TABLE `lessons` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  `date` datetime DEFAULT NULL,
  `TeacherId` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `type` text,
  `price` float DEFAULT NULL,
  `RoomColor` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `schedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `LessonId` varchar(100) DEFAULT NULL,
  `ScheduleDate` datetime DEFAULT NULL,
  `StudentId` text,
  `canceled` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `FirstName` text,
  `LastName` text,
  `IdentificationCard` text,
  `date` datetime DEFAULT NULL,
  `address` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `teachers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `FirstName` text,
  `LastName` text,
  `IdentificationCard` text,
  `SalaryPerHour` float DEFAULT NULL,
  `address` text,
  `password` text,
  `username` text,
  `token` text,
  `permission` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `lessons` (`id`, `name`, `date`, `TeacherId`, `type`, `price`, `RoomColor`) VALUES
(25, 'גיטרה', '2023-06-03 19:03:54', '1', NULL, 50, 'green'),
(26, 'גיטרה', '2023-06-03 19:07:01', '2', NULL, 50, 'green'),
(27, 'קלידים', '2023-06-04 02:13:56', '2', NULL, 50, 'blue'),
(28, 'קלידים', '2023-06-04 20:48:02', '2', NULL, 50, 'orange'),
(29, 'קלידים', '2023-06-04 23:56:18', '2', NULL, 50, 'orange'),
(30, 'rerer', '2023-06-04 23:59:17', '1 ', NULL, 34, 'blue'),
(31, 'njddd', '2023-06-05 00:00:01', '1 ', NULL, 4545, 'blue'),
(32, 'nrnr', '2023-06-05 00:00:49', '1 ', NULL, 34, 'blue'),
(33, 'nr', '2023-06-05 00:01:35', '1 ', NULL, 45, 'blue'),
(34, 'קלידים', '2023-06-05 22:33:17', '2', NULL, 50, 'orange'),
(35, 'כינור למתחילים', '2023-06-06 02:24:10', '1 ', NULL, 200, 'blue'),
(36, 'קלידים', '2023-06-06 22:43:58', '2', NULL, 50, 'orange'),
(37, 'קלידים', '2023-06-06 22:45:28', '2', NULL, 50, 'orange'),
(38, 'קלידים', '2023-06-06 22:51:49', '2', NULL, 50, 'orange'),
(39, 'קלידים', '2023-06-06 22:52:57', '2', NULL, 50, 'orange'),
(40, 'קלידים', '2023-06-06 22:53:40', '2', NULL, 50, 'orange');

INSERT INTO `schedule` (`id`, `date`, `LessonId`, `ScheduleDate`, `StudentId`, `canceled`) VALUES
(1, NULL, '25', '2023-06-21 17:50:00', '1', NULL),
(20, NULL, '1', '2023-06-26 17:00:00', '34', NULL),
(21, NULL, '25', '2023-06-19 12:00:00', '1', NULL),
(22, NULL, '25', '2023-06-05 11:00:00', '1', NULL),
(23, NULL, '28', '2023-06-06 17:00:00', '1', NULL),
(24, NULL, '25', '2023-06-17 16:00:00', '1', 1),
(25, NULL, '35', '2023-06-08 15:00:00', '1', 1),
(26, NULL, '25', '2023-06-03 11:00:00', '1', 0),
(27, NULL, '31', '2023-06-03 11:00:00', '1', 0),
(28, NULL, '25', '2023-06-10 15:00:00', '1', 0),
(29, NULL, '27', '2023-06-10 15:00:00', '1', 0),
(30, NULL, '26', '2023-06-19 12:00:00', '1', 0),
(31, NULL, '31', '2023-06-19 12:00:00', '1', 0),
(32, NULL, '25', '2023-06-06 12:00:00', '1', 0),
(33, NULL, '25', '2027-07-12 10:00:00', '1', 0),
(34, NULL, '25', '2023-06-01 16:00:00', '1', 0),
(35, NULL, '37', '2023-06-01 16:00:00', '1', 0),
(36, NULL, '25', '2023-06-02 10:00:00', '1', 0),
(37, NULL, '25', '2023-06-01 10:00:00', '1', 0),
(38, NULL, '27', '2023-06-01 10:00:00', '1', 0);

INSERT INTO `students` (`id`, `FirstName`, `LastName`, `IdentificationCard`, `date`, `address`) VALUES
(1, 'מאי', 'כהן', '123123123', NULL, NULL),
(2, 'ihihiouhoiuh', 'fgfgfg', '23423554454', '2023-06-05 00:11:37', 'fgfgfggfg'),
(3, '', '', '', '2023-06-05 00:16:01', ''),
(4, 'כלגצדכףדצגכדכ', 'גדכעצדףכךעדגכע', 'דגכלעצףדגכע', '2023-06-05 00:16:13', 'דגכעלדףכע'),
(5, '', '', '', '2023-06-06 23:19:52', ''),
(6, 'rrt', 'rtrt', 'rtrtr', '2023-06-06 23:19:59', 'rtrt'),
(7, 'ihihiouhoiuh', 'fgfgfg', '23423554454', '2023-06-07 00:53:00', 'fgfgfggfg'),
(8, 'ihihiouhoiuh', 'fgfgfg', '23423554454', '2023-06-07 00:53:16', 'fgfgfggfg'),
(9, 'ihihiouhoiuh', 'fgfgfg', '23423554454', '2023-06-07 00:54:16', 'fgfgfggfg');

INSERT INTO `teachers` (`id`, `date`, `FirstName`, `LastName`, `IdentificationCard`, `SalaryPerHour`, `address`, `password`, `username`, `token`, `permission`) VALUES
(1, '2023-06-03 19:14:29', 'הדר', 'רובין', NULL, 4.9, NULL, NULL, NULL, NULL, NULL),
(2, '2023-06-03 20:01:26', 'הדר', 'רובין', NULL, 4.9, NULL, NULL, NULL, NULL, NULL),
(3, '2023-06-04 02:15:05', 'נריה', 'אלול', NULL, 89899000000000, NULL, NULL, NULL, NULL, NULL),
(4, '2023-06-05 01:20:02', 'נריה', 'אלול', NULL, 89899000000000, NULL, NULL, NULL, NULL, NULL),
(5, '2023-06-05 01:38:20', 'נריה', 'אלול', '', 89899000000000, '', NULL, NULL, NULL, NULL),
(6, '2023-06-05 01:38:50', 'df', 'fdf', 'df', 45, 'dfdf', NULL, NULL, NULL, NULL),
(7, '2023-06-06 21:36:10', 'f', 'dfd', '34354345', 45, '345354', '932f3c1b56257ce8539ac269d7aab42550dacf8818d075f0bdf1990562aae3ef', 'nerr', NULL, NULL),
(8, '2023-06-06 22:13:06', 'dfd', 'fdf', 'df', 34, 'dfd', 'f51dd528c1681918707cb4d73772f1798007c3d9fa519325c7298f89c21425a9', 'dfdf', NULL, 3),
(9, '2023-06-06 22:13:21', 'dfd', 'fdf', 'df', 34, 'dfd', 'f51dd528c1681918707cb4d73772f1798007c3d9fa519325c7298f89c21425a9', '456464645', NULL, 3),
(10, '2023-06-06 22:27:56', 'bbbbb', 'bbbb', 'bbbb', 45, 'bbbbb', '932f3c1b56257ce8539ac269d7aab42550dacf8818d075f0bdf1990562aae3ef', 'nerry', 'nerry-uIuoKjKzfmQalgezbYjjTysTCEkPAebQoxKBOZat', 3),
(11, '2023-06-07 00:47:44', 'נריה', 'אלול', '', 89899000000000, '', '4da91f5e2f598ed75622a326abc9b44af64e3211d04eb11761a09b28dcd49729', 'dddfdfdfdfdf', NULL, 3),
(12, '2023-06-07 00:49:13', 'dtdg§', 'eryrydy', 'rtertert', 343, 'erter', 'd8cbc065185bb5cf1e41e0c59b35f8a710cc34854e333f4c8cee4db8be194d64', 'thrtyryt', NULL, 1);



/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
