-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 18, 2023 at 07:42 AM
-- Server version: 8.0.27
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `voucher`
--

CREATE DATABASE IF NOT EXISTS `voucher` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `voucher`;

-- --------------------------------------------------------

--
-- Table structure for table `availablevouchers`
--

DROP TABLE IF EXISTS `availablevouchers`;
CREATE TABLE IF NOT EXISTS `availablevouchers` (
  `PlatformName` varchar(50) NOT NULL,
  `DiscountAmt` varchar(20) NOT NULL,
  `Cost` int NOT NULL,
  PRIMARY KEY (`PlatformName`,`DiscountAmt`,`Cost`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `availablevouchers`
--

INSERT INTO `availablevouchers` (`PlatformName`, `DiscountAmt`, `Cost`) VALUES
('ASOS', '10% discount', 40),
('ASOS', '5% discount', 20);

-- --------------------------------------------------------

--
-- Table structure for table `purchasedvouchers`
--

DROP TABLE IF EXISTS `purchasedvouchers`;
CREATE TABLE IF NOT EXISTS `purchasedvouchers` (
  `VID` int NOT NULL AUTO_INCREMENT,
  `UID` int NOT NULL,
  `PlatformName` varchar(50) NOT NULL,
  `PointsRequired` int NOT NULL,
  `DiscountAmt` varchar(20) NOT NULL,
  `PurchasedDate` timestamp NULL DEFAULT NULL,
  `RedeemedDate` timestamp NULL DEFAULT NULL,
  `ExpiryDate` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`VID`,`UID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `purchasedvouchers`
--

INSERT INTO `purchasedvouchers` (`VID`, `UID`, `PlatformName`, `PointsRequired`, `DiscountAmt`, `PurchasedDate`, `RedeemedDate`, `ExpiryDate`) VALUES
(1, 11, 'ASOS', 20, '5% discount', '2023-03-18 07:22:12', '2023-03-17 23:37:41', '2023-03-17 23:22:12'),
(2, 11, 'ASOS', 20, '5% discount', '2023-03-18 07:23:06', NULL, '2023-03-17 23:23:06'),
(3, 11, 'ASOS', 20, '5% discount', '2023-03-18 07:25:28', NULL, '2023-03-17 23:25:28');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
