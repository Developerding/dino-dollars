-- phpMyAdmin SQL Dump


--setting sql mode. By default 0 will be set to null
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
set AUTOCOMMIT=0
START TRANSACTION;
SET time_zone="+08:00"




-- Database name: voucher
CREATE DATABASE IF NOT EXISTS `voucher` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `voucher`;



--No list type in MySQL, LinkedAccounts will just be varchar that records platform name
DROP TABLE IF EXISTS 'user';
CREATE TABLE IF NOT EXISTS 'user'(
    'UID' int(4) NOT NULL AUTO_INCREMENT,
    'Name' varchar(64) NOT NULL,
    'Email' varchar(64) NOT NULL,
    'Points' int(10) NOT NULL DEFAULT 0,
    'LinkedAccounts' varchar(64) ,
    PRIMARY KEY ('UID')

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS 'Error';
CREATE TABLE IF NOT EXISTS 'Error'(
    'ErrID' int(4) NOT NULL AUTO_INCREMENT,
    'StatusCode' int(4) NOT NULL,
    'ErrDesc' varchar(300) NOT NULL,
    PRIMARY KEY ('UID')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS 'AvailableVouchers';
CREATE TABLE IF NOT EXISTS 'AvailableVouchers'(
    'PlatformName' varchar(50) NOT NULL ,
    'DiscountAmt' varchar(20) NOT NULL,
    'Cost' int(10) NOT NULL,
    CONSTRAINT PK_AvailableVouchers PRIMARY KEY ('PlatformName', 'DiscountAmt')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS 'PurchasedVouchers';
CREATE TABLE IF NOT EXISTS 'PurchasedVouchers'(
    'VID' int(4) NOT NULL AUTO_INCREMENT,
    'UID' int(4) NOT NULL,
    'PlatformName' varchar(50) NOT NULL,
    'PointsRequired' int(4) NOT NULL,
    'DiscountAmt' varchar(20) NOT NULL,
    'PurchasedDate' timestamp DEFAULT NULL,
    'RedeemedDate' timestamp DEFAULT NULL,
    'ExpiryDate' timestamp DEFAULT NULL,
    CONSTRAINT PK_PurchasedVouchers PRIMARY KEY ('VID', 'UID')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
