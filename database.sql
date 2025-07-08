-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 07, 2025 at 07:48 PM
-- Server version: 8.0.42-cll-lve
-- PHP Version: 8.3.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gdcplati_drink_software`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_site_activitylogmodel`
--

CREATE TABLE `admin_site_activitylogmodel` (
  `id` bigint NOT NULL,
  `log` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `customer_id` bigint DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `category` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `supplier_id` bigint DEFAULT NULL,
  `keywords` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `driver_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `admin_site_activitylogmodel`
--

INSERT INTO `admin_site_activitylogmodel` (`id`, `log`, `created_at`, `customer_id`, `user_id`, `category`, `supplier_id`, `keywords`, `driver_id`) VALUES
(1, '\n    <div style=\'border-radius:5px\' class=\'text-white bg-dark p-2\'>\n        <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> executed cash transfer: <b>Bank Balance Adjustment - Add</b> of ₦1,833,055.00.<br>\n        \n        \n        Note: Reconciled the bank and the vendor accounts to capture the right closing balances.\n        <br><span style=\'float:right\'>2025-06-28 06:44:23</span></p>\n    </div>\n    ', '2025-06-28 06:44:23.270245', NULL, 2, 'finance', NULL, 'finance__cash_transfer__adjustment_add', NULL),
(2, '\n    <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n        <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> created a new supplier: <b>Nigerian Breweries</b> under category \n        <b>NBL</b> with an opening balance of \n        <b>₦0.0</b>.<br>\n        <span style=\'float:right\'>2025-06-28 06:54:17</span></p>\n    </div>\n    ', '2025-06-28 06:54:17.282614', NULL, 2, 'inventory', 1, NULL, NULL),
(3, '\n    <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n        <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> created a new supplier: <b>International Breweries</b> under category \n        <b>IBL</b> with an opening balance of \n        <b>₦0.0</b>.<br>\n        <span style=\'float:right\'>2025-06-28 07:10:05</span></p>\n    </div>\n    ', '2025-06-28 07:10:05.077147', NULL, 2, 'inventory', 2, NULL, NULL),
(4, '\n    <div style=\'border-radius:5px\' class=\'text-white bg-dark p-2\'>\n        <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> executed cash transfer: <b>Bank to Supplier</b> of ₦323,990.00.<br>\n        From <b>Bank</b> to <b>Supplier</b><br>\n        Supplier: <b>International Breweries</b><br>\n        Note: No comment\n        <br><span style=\'float:right\'>2025-06-28 07:10:53</span></p>\n    </div>\n    ', '2025-06-28 07:10:53.534091', NULL, 2, 'finance', NULL, 'finance__cash_transfer__bank_to_supplier', NULL),
(5, '\n    <div style=\'border-radius:5px\' class=\'text-white bg-dark p-2\'>\n        <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> executed cash transfer: <b>Bank to Supplier</b> of ₦323,990.00.<br>\n        From <b>Bank</b> to <b>Supplier</b><br>\n        Supplier: <b>Nigerian Breweries</b><br>\n        Note: No comment\n        <br><span style=\'float:right\'>2025-06-28 07:14:15</span></p>\n    </div>\n    ', '2025-06-28 07:14:15.065640', NULL, 2, 'finance', NULL, 'finance__cash_transfer__bank_to_supplier', NULL),
(6, '\n    <div style=\'border-radius:5px\' class=\'text-white bg-dark p-2\'>\n        <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> executed cash transfer: <b>Bank to Supplier</b> of ₦362,277.00.<br>\n        From <b>Bank</b> to <b>Supplier</b><br>\n        Supplier: <b>International Breweries</b><br>\n        Note: No comment\n        <br><span style=\'float:right\'>2025-06-28 07:15:08</span></p>\n    </div>\n    ', '2025-06-28 07:15:08.601476', NULL, 2, 'finance', NULL, 'finance__cash_transfer__bank_to_supplier', NULL),
(7, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: GOLDBERG <br>\n                    Qty: 234, Cost Price: ₦8,720.00, Selling Price: ₦9,055.00.\n                    <br>\n                    <a href=\"/inventory/product/1/detail\"><b>Goldberg</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:09:34</span></p>\n                </div>\n            ', '2025-06-29 10:09:34.924200', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(8, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: LIFE <br>\n                    Qty: 721, Cost Price: ₦8,720.00, Selling Price: ₦9,055.00.\n                    <br>\n                    <a href=\"/inventory/product/2/detail\"><b>Life</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:10:14</span></p>\n                </div>\n            ', '2025-06-29 10:10:14.887414', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(9, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: LEGEND 60CL <br>\n                    Qty: 20, Cost Price: ₦10,475.00, Selling Price: ₦11,020.00.\n                    <br>\n                    <a href=\"/inventory/product/3/detail\"><b>Legend 60cl</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:11:18</span></p>\n                </div>\n            ', '2025-06-29 10:11:18.791815', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(10, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: LEGEND 45CL <br>\n                    Qty: 35, Cost Price: ₦10,475.00, Selling Price: ₦15,230.00.\n                    <br>\n                    <a href=\"/inventory/product/4/detail\"><b>Legend 45cl</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:12:38</span></p>\n                </div>\n            ', '2025-06-29 10:12:38.022871', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(11, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: HEINEKEN 60CL <br>\n                    Qty: 350, Cost Price: ₦11,350.00, Selling Price: ₦11,915.00.\n                    <br>\n                    <a href=\"/inventory/product/5/detail\"><b>Heineken 60cl</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:14:00</span></p>\n                </div>\n            ', '2025-06-29 10:14:00.431541', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(12, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: DESPERADO <br>\n                    Qty: 73, Cost Price: ₦16,030.00, Selling Price: ₦16,880.00.\n                    <br>\n                    <a href=\"/inventory/product/6/detail\"><b>Desperado</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:14:48</span></p>\n                </div>\n            ', '2025-06-29 10:14:48.325269', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(13, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: TIGER <br>\n                    Qty: 325, Cost Price: ₦14,450.00, Selling Price: ₦15,055.00.\n                    <br>\n                    <a href=\"/inventory/product/7/detail\"><b>Tiger</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:15:46</span></p>\n                </div>\n            ', '2025-06-29 10:15:46.701579', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(14, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: AMSTEL <br>\n                    Qty: 247, Cost Price: ₦12,065.00, Selling Price: ₦12,655.00.\n                    <br>\n                    <a href=\"/inventory/product/8/detail\"><b>Amstel</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:18:27</span></p>\n                </div>\n            ', '2025-06-29 10:18:27.354342', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(15, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: MALTINA <br>\n                    Qty: 57, Cost Price: ₦12,065.00, Selling Price: ₦12,655.00.\n                    <br>\n                    <a href=\"/inventory/product/9/detail\"><b>Maltina</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:19:15</span></p>\n                </div>\n            ', '2025-06-29 10:19:15.626227', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(16, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: GULDER <br>\n                    Qty: 347, Cost Price: ₦10,285.00, Selling Price: ₦10,825.00.\n                    <br>\n                    <a href=\"/inventory/product/10/detail\"><b>Gulder</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:23:25</span></p>\n                </div>\n            ', '2025-06-29 10:23:25.643896', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(17, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: STAR <br>\n                    Qty: 153, Cost Price: ₦9,800.00, Selling Price: ₦10,210.00.\n                    <br>\n                    <a href=\"/inventory/product/11/detail\"><b>Star</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:25:39</span></p>\n                </div>\n            ', '2025-06-29 10:25:39.693532', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(18, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: RADLER <br>\n                    Qty: 167, Cost Price: ₦11,795.00, Selling Price: ₦12,315.00.\n                    <br>\n                    <a href=\"/inventory/product/12/detail\"><b>Radler</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:28:33</span></p>\n                </div>\n            ', '2025-06-29 10:28:33.113833', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(19, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: GOLDBERG BLACK 45CL <br>\n                    Qty: 53, Cost Price: ₦12,035.00, Selling Price: ₦12,610.00.\n                    <br>\n                    <a href=\"/inventory/product/13/detail\"><b>Goldberg Black 45cl</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:30:24</span></p>\n                </div>\n            ', '2025-06-29 10:30:24.031380', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(20, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: FAYROUZ <br>\n                    Qty: 27, Cost Price: ₦8,490.00, Selling Price: ₦8,825.00.\n                    <br>\n                    <a href=\"/inventory/product/14/detail\"><b>Fayrouz</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:31:21</span></p>\n                </div>\n            ', '2025-06-29 10:31:21.167369', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(21, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: TROPHY <br>\n                    Qty: 2756, Cost Price: ₦8,550.00, Selling Price: ₦8,870.00.\n                    <br>\n                    <a href=\"/inventory/product/16/detail\"><b>Trophy</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:34:11</span></p>\n                </div>\n            ', '2025-06-29 10:34:11.363680', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(22, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: HERO <br>\n                    Qty: 362, Cost Price: ₦8,550.00, Selling Price: ₦8,870.00.\n                    <br>\n                    <a href=\"/inventory/product/17/detail\"><b>Hero</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:34:40</span></p>\n                </div>\n            ', '2025-06-29 10:34:40.052165', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(23, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: TROPHY STOUT <br>\n                    Qty: 222, Cost Price: ₦8,800.00, Selling Price: ₦9,300.00.\n                    <br>\n                    <a href=\"/inventory/product/18/detail\"><b>Trophy Stout</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:35:41</span></p>\n                </div>\n            ', '2025-06-29 10:35:41.048763', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(24, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: CASTLE LITE <br>\n                    Qty: 934, Cost Price: ₦8,830.00, Selling Price: ₦9,250.00.\n                    <br>\n                    <a href=\"/inventory/product/19/detail\"><b>Castle Lite</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:36:49</span></p>\n                </div>\n            ', '2025-06-29 10:36:49.640754', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(25, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: BUDWEISER <br>\n                    Qty: 882, Cost Price: ₦9,050.00, Selling Price: ₦9,450.00.\n                    <br>\n                    <a href=\"/inventory/product/20/detail\"><b>Budweiser</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:37:32</span></p>\n                </div>\n            ', '2025-06-29 10:37:32.101427', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(26, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: RED BULL <br>\n                    Qty: 10, Cost Price: ₦28,000.00, Selling Price: ₦28,500.00.\n                    <br>\n                    <a href=\"/inventory/product/21/detail\"><b>Red Bull</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:40:01</span></p>\n                </div>\n            ', '2025-06-29 10:40:01.528463', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(27, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: LEGEND TWIST <br>\n                    Qty: 2, Cost Price: ₦13,810.00, Selling Price: ₦14,720.00.\n                    <br>\n                    <a href=\"/inventory/product/22/detail\"><b>Legend Twist</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:41:10</span></p>\n                </div>\n            ', '2025-06-29 10:41:10.916321', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(28, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: STAR LITE <br>\n                    Qty: 40, Cost Price: ₦9,255.00, Selling Price: ₦9,855.00.\n                    <br>\n                    <a href=\"/inventory/product/23/detail\"><b>Star Lite</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:42:30</span></p>\n                </div>\n            ', '2025-06-29 10:42:30.527567', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(29, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: AMSTEL CAN <br>\n                    Qty: 142, Cost Price: ₦12,815.00, Selling Price: ₦13,355.00.\n                    <br>\n                    <a href=\"/inventory/product/24/detail\"><b>Amstel Can</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:43:35</span></p>\n                </div>\n            ', '2025-06-29 10:43:35.732811', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(30, '\n                <div style=\'border-radius:5px\' class=\'text-white bg-primary p-2\'>\n                    <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> added a new Product: BETA MALT CAN <br>\n                    Qty: 399, Cost Price: ₦10,550.00, Selling Price: ₦10,990.00.\n                    <br>\n                    <a href=\"/inventory/product/25/detail\"><b>Beta Malt Can</b></a>\n                    <br><span style=\'float:right\'>2025-06-29 10:44:28</span></p>\n                </div>\n            ', '2025-06-29 10:44:28.378643', NULL, 2, 'inventory', NULL, 'inventory__initial_stock', NULL),
(31, '\n    <div style=\'border-radius:5px\' class=\'text-white bg-dark p-2\'>\n        <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> executed cash transfer: <b>Bank to Petty Cash</b> of ₦70,000.00.<br>\n        From <b>Bank</b> to <b>Petty Cash</b><br>\n        \n        Note: No comment\n        <br><span style=\'float:right\'>2025-06-29 10:45:27</span></p>\n    </div>\n    ', '2025-06-29 10:45:27.852217', NULL, 2, 'finance', NULL, 'finance__cash_transfer__bank_to_petty', NULL),
(32, '\n        <div class=\'bg-danger text-white p-2\' style=\'border-radius:5px;\'>\n            <p>\n                <b><a href=\"/human_resource/staff/1/detail\" class=\"text-white text-decoration-underline\">\n                    Mrs Nnenna\n                </a></b> recorded an expense of \n                <b>₦50,000.00</b> under <b>Kuja Salary</b>.<br>\n                Remark: Kuja Salary for the month of May\n                <span class=\'float-end\'>2025-06-29 11:54:59</span>\n            </p>\n        </div>\n        ', '2025-06-29 10:54:59.497991', NULL, 2, 'finance', NULL, 'finance__expense_created', NULL),
(33, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/1/detail\" class=\"text-white text-decoration-underline\">Mrs Nnenna</a></b>\n                            confirmed sale <b>#SALE-20250629120257592</b>.<br>\n                            <b>Total:</b> ₦1022000.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦1022000.00<br>\n                            <a href=\"/sale/1/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-06-29 12:02:57</span>\n                          </p>\n                        </div>\n                        ', '2025-06-29 12:02:57.675316', 3, 2, 'sales', NULL, 'sale__confirmed', 5),
(34, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/1/detail\" class=\"text-white text-decoration-underline\">\n                    Mrs Nnenna\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦400000.00</b> to <b>bank</b> for\n                <a href=\"/sale/customer/5/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Success Ojonugwa</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦0.00<br>\n                <a href=\"/sale/customer/5/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-06-29 18:21:24</span>\n              </p>\n            </div>\n            ', '2025-06-29 17:21:24.309251', 5, 2, 'sales', NULL, 'customer__repayment', NULL),
(35, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>70</b> empty crates for\n                <a href=\"/sale/customer/3/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Chika Ugwu</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/3/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-06-30 12:23:54</span>\n              </p>\n            </div>\n            ', '2025-06-30 11:23:54.111647', 3, 3, 'sales', NULL, 'customer__crate_return', NULL),
(36, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>30</b> empty crates for\n                <a href=\"/sale/customer/3/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Chika Ugwu</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/3/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-06-30 12:24:32</span>\n              </p>\n            </div>\n            ', '2025-06-30 11:24:32.513441', 3, 3, 'sales', NULL, 'customer__crate_return', NULL),
(37, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250630123703382</b>.<br>\n                            <b>Total:</b> ₦850000.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦850000.00<br>\n                            <a href=\"/sale/2/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-06-30 12:37:03</span>\n                          </p>\n                        </div>\n                        ', '2025-06-30 12:37:03.404256', 17, 3, 'sales', NULL, 'sale__confirmed', 5),
(38, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250630124630004</b>.<br>\n                            <b>Total:</b> ₦84110.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦84110.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦0.00<br>\n                            <a href=\"/sale/3/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-06-30 12:46:30</span>\n                          </p>\n                        </div>\n                        ', '2025-06-30 12:46:30.030367', 4, 3, 'sales', NULL, 'sale__confirmed', NULL),
(39, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250630125854474</b>.<br>\n                            <b>Total:</b> ₦1010600.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦1010600.00<br>\n                            <a href=\"/sale/4/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-06-30 12:58:54</span>\n                          </p>\n                        </div>\n                        ', '2025-06-30 12:58:54.498727', 7, 3, 'sales', NULL, 'sale__confirmed', 5),
(40, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>79</b> empty crates for\n                <a href=\"/sale/customer/7/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Simple</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/7/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-06-30 14:01:26</span>\n              </p>\n            </div>\n            ', '2025-06-30 13:01:26.893986', 7, 3, 'sales', NULL, 'customer__crate_return', NULL),
(41, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>79</b> empty crates for\n                <a href=\"/sale/customer/7/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Simple</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/7/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-06-30 14:01:47</span>\n              </p>\n            </div>\n            ', '2025-06-30 13:01:47.955031', 7, 3, 'sales', NULL, 'customer__crate_return', NULL),
(42, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250702100704965</b>.<br>\n                            <b>Total:</b> ₦185000.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦185000.00<br>\n                            <a href=\"/sale/5/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-02 10:07:05</span>\n                          </p>\n                        </div>\n                        ', '2025-07-02 10:07:05.009691', 18, 3, 'sales', NULL, 'sale__confirmed', 5),
(43, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦46250.00</b> in <b>cash</b> for\n                <a href=\"/sale/customer/18/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Abel (bernard)</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦138750.00<br>\n                <a href=\"/sale/customer/18/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-02 11:08:41</span>\n              </p>\n            </div>\n            ', '2025-07-02 10:08:41.647877', 18, 3, 'sales', NULL, 'customer__repayment', NULL),
(44, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦841500.00</b> to <b>bank</b> for\n                <a href=\"/sale/customer/17/detail\" class=\"text-white text-decoration-underline\">\n                  <b>orlando</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦8500.00<br>\n                <a href=\"/sale/customer/17/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-02 11:11:53</span>\n              </p>\n            </div>\n            ', '2025-07-02 10:11:53.012870', 17, 3, 'sales', NULL, 'customer__repayment', NULL),
(45, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦997750.00</b> to <b>bank</b> for\n                <a href=\"/sale/customer/7/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Simple</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦14550.00<br>\n                <a href=\"/sale/customer/7/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-02 11:21:06</span>\n              </p>\n            </div>\n            ', '2025-07-02 10:21:06.428948', 7, 3, 'sales', NULL, 'customer__repayment', NULL),
(46, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250702103243828</b>.<br>\n                            <b>Total:</b> ₦944900.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦944900.00<br>\n                            <a href=\"/sale/6/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-02 10:32:43</span>\n                          </p>\n                        </div>\n                        ', '2025-07-02 10:32:43.879726', 5, 3, 'sales', NULL, 'sale__confirmed', 5),
(47, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250702103722240</b>.<br>\n                            <b>Total:</b> ₦309500.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦309500.00<br>\n                            <a href=\"/sale/7/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-02 10:37:22</span>\n                          </p>\n                        </div>\n                        ', '2025-07-02 10:37:22.300476', 19, 3, 'sales', NULL, 'sale__confirmed', NULL),
(48, '\n    <div style=\'border-radius:5px\' class=\'text-white bg-dark p-2\'>\n        <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> executed cash transfer: <b>Bank Balance Adjustment - Add</b> of ₦21,820,590.00.<br>\n        \n        \n        Note: was already in nbl before system migration\n        <br><span style=\'float:right\'>2025-07-02 10:48:55</span></p>\n    </div>\n    ', '2025-07-02 10:48:55.195019', NULL, 2, 'finance', NULL, 'finance__cash_transfer__adjustment_add', NULL),
(49, '\n    <div style=\'border-radius:5px\' class=\'text-white bg-dark p-2\'>\n        <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> executed cash transfer: <b>Bank Balance Adjustment - Add</b> of ₦474,155.00.<br>\n        \n        \n        Note: was already in nbl before system migration\n        <br><span style=\'float:right\'>2025-07-02 10:49:27</span></p>\n    </div>\n    ', '2025-07-02 10:49:27.955283', NULL, 2, 'finance', NULL, 'finance__cash_transfer__adjustment_add', NULL),
(50, '\n    <div style=\'border-radius:5px\' class=\'text-white bg-dark p-2\'>\n        <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> executed cash transfer: <b>Bank to Supplier</b> of ₦21,820,590.00.<br>\n        From <b>Bank</b> to <b>Supplier</b><br>\n        Supplier: <b>Nigerian Breweries</b><br>\n        Note: No comment\n        <br><span style=\'float:right\'>2025-07-02 10:50:16</span></p>\n    </div>\n    ', '2025-07-02 10:50:16.252975', NULL, 2, 'finance', NULL, 'finance__cash_transfer__bank_to_supplier', NULL),
(51, '\n    <div style=\'border-radius:5px\' class=\'text-white bg-dark p-2\'>\n        <p><a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> executed cash transfer: <b>Bank to Supplier</b> of ₦474,155.00.<br>\n        From <b>Bank</b> to <b>Supplier</b><br>\n        Supplier: <b>Nigerian Breweries</b><br>\n        Note: No comment\n        <br><span style=\'float:right\'>2025-07-02 10:50:43</span></p>\n    </div>\n    ', '2025-07-02 10:50:43.586707', NULL, 2, 'finance', NULL, 'finance__cash_transfer__bank_to_supplier', NULL),
(52, '\n                    <div class=\'bg-primary text-white p-2\' style=\'border-radius: 5px;\'>\n                        <p>\n                            <a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> recorded a <b>CONFIRMED</b> stock-in summary.<br>\n                            <b>Products:</b> 1 &nbsp; | &nbsp;\n                            <b>Total Cost:</b> ₦20,146,590.00\n                            <br>\n                            <a href=\'/inventory/stock-in/1/detail/\'\n                               class=\'btn btn-sm btn-light mt-2\'>\n                               View Receipt\n                            </a>\n                            <span class=\'float-end\'>2025-07-02 11:02:50</span>\n                        </p>\n                    </div>\n                    ', '2025-07-02 11:02:50.566788', NULL, 2, 'inventory', 1, 'inventory__stockin', NULL),
(53, '\n                        <div class=\'bg-dark text-white p-2\' style=\'border-radius: 5px;\'>\n                            <p>1: ₦20,146,590.00 was removed from supplier <b>Nigerian Breweries</b>\'s wallet due to purchase.<br>\n                            2: 1456 empty containers was removed for category <b>NBL</b>.<br>\n                            3: A further ₦218,000.00 was removed due to shortfall of 218 empty containers.<br>\n                            4: Current supplier balance is: <b>₦2,254,145.00</b>.\n                            <span class=\'float-end\'>2025-07-02 11:02:50</span></p>\n                        </div>\n                        ', '2025-07-02 11:02:50.573438', NULL, 2, 'finance', 1, 'finance__supplier_deduction', NULL),
(54, '\n                    <div class=\'bg-primary text-white p-2\' style=\'border-radius: 5px;\'>\n                        <p>\n                            <a href=\'/human_resource/staff/1/detail\'><b>Mrs Nnenna</b></a> recorded a <b>CONFIRMED</b> stock-in summary.<br>\n                            <b>Products:</b> 1 &nbsp; | &nbsp;\n                            <b>Total Cost:</b> ₦474,155.00\n                            <br>\n                            <a href=\'/inventory/stock-in/2/detail/\'\n                               class=\'btn btn-sm btn-light mt-2\'>\n                               View Receipt\n                            </a>\n                            <span class=\'float-end\'>2025-07-02 11:08:54</span>\n                        </p>\n                    </div>\n                    ', '2025-07-02 11:08:54.990922', NULL, 2, 'inventory', 1, 'inventory__stockin', NULL),
(55, '\n                        <div class=\'bg-dark text-white p-2\' style=\'border-radius: 5px;\'>\n                            <p>1: ₦474,155.00 was removed from supplier <b>Nigerian Breweries</b>\'s wallet due to purchase.<br>\n                            2: 0 empty containers was removed for category <b>NBL</b>.<br>\n                            3: No additional charge or refund for empty containers.<br>\n                            4: Current supplier balance is: <b>₦1,779,990.00</b>.\n                            <span class=\'float-end\'>2025-07-02 11:08:54</span></p>\n                        </div>\n                        ', '2025-07-02 11:08:54.995475', NULL, 2, 'finance', 1, 'finance__supplier_deduction', NULL),
(56, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250702111636243</b>.<br>\n                            <b>Total:</b> ₦1160000.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦1100000.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦60000.00<br>\n                            <a href=\"/sale/8/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-02 11:16:36</span>\n                          </p>\n                        </div>\n                        ', '2025-07-02 11:16:36.285047', 20, 3, 'sales', NULL, 'sale__confirmed', 4),
(57, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250702113607263</b>.<br>\n                            <b>Total:</b> ₦2473250.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦2473250.00<br>\n                            <a href=\"/sale/9/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-02 11:36:07</span>\n                          </p>\n                        </div>\n                        ', '2025-07-02 11:36:07.286040', 12, 3, 'sales', NULL, 'sale__confirmed', 4),
(58, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦2473250.00</b> to <b>bank</b> for\n                <a href=\"/sale/customer/12/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Chinedu Ugwuoke</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦0.00<br>\n                <a href=\"/sale/customer/12/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-02 13:23:25</span>\n              </p>\n            </div>\n            ', '2025-07-02 12:23:25.740770', 12, 3, 'sales', NULL, 'customer__repayment', NULL),
(59, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦309200.00</b> to <b>bank</b> for\n                <a href=\"/sale/customer/19/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Sylvester Gomes</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦300.00<br>\n                <a href=\"/sale/customer/19/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-02 13:35:14</span>\n              </p>\n            </div>\n            ', '2025-07-02 12:35:14.116936', 19, 3, 'sales', NULL, 'customer__repayment', NULL),
(60, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦138750.00</b> to <b>bank</b> for\n                <a href=\"/sale/customer/18/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Abel (bernard)</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦0.00<br>\n                <a href=\"/sale/customer/18/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-02 13:39:26</span>\n              </p>\n            </div>\n            ', '2025-07-02 12:39:26.832670', 18, 3, 'sales', NULL, 'customer__repayment', NULL),
(61, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦1022000.00</b> to <b>bank</b> for\n                <a href=\"/sale/customer/3/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Chika Ugwu</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦83625.00<br>\n                <a href=\"/sale/customer/3/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-02 13:40:55</span>\n              </p>\n            </div>\n            ', '2025-07-02 12:40:55.952840', 3, 3, 'sales', NULL, 'customer__repayment', NULL),
(62, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>100</b> empty crates for\n                <a href=\"/sale/customer/12/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Chinedu Ugwuoke</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/12/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-02 13:45:31</span>\n              </p>\n            </div>\n            ', '2025-07-02 12:45:31.903273', 12, 3, 'sales', NULL, 'customer__crate_return', NULL),
(63, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>149</b> empty crates for\n                <a href=\"/sale/customer/5/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Success Ojonugwa</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/5/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-02 14:35:30</span>\n              </p>\n            </div>\n            ', '2025-07-02 13:35:30.104292', 5, 3, 'sales', NULL, 'customer__crate_return', NULL),
(64, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250702135813716</b>.<br>\n                            <b>Total:</b> ₦192660.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦192660.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦0.00<br>\n                            <a href=\"/sale/10/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-02 13:58:13</span>\n                          </p>\n                        </div>\n                        ', '2025-07-02 13:58:13.761364', 21, 3, 'sales', NULL, 'sale__confirmed', NULL),
(65, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>1</b> empty crates for\n                <a href=\"/sale/customer/21/detail\" class=\"text-white text-decoration-underline\">\n                  <b>oscar lavida</b>\n                </a>\n                as <b>Cash Return</b> and paid <b>₦1000.00</b>.<br>\n                <a href=\"/sale/customer/21/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-02 15:00:55</span>\n              </p>\n            </div>\n            ', '2025-07-02 14:00:55.432572', 21, 3, 'sales', NULL, 'customer__crate_return', NULL),
(66, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250702140744380</b>.<br>\n                            <b>Total:</b> ₦240725.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦240725.00<br>\n                            <a href=\"/sale/11/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-02 14:07:44</span>\n                          </p>\n                        </div>\n                        ', '2025-07-02 14:07:44.416446', 13, 3, 'sales', NULL, 'sale__confirmed', 5),
(67, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>113</b> empty crates for\n                <a href=\"/sale/customer/13/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Over The Bar</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/13/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-02 15:10:46</span>\n              </p>\n            </div>\n            ', '2025-07-02 14:10:46.607675', 13, 3, 'sales', NULL, 'customer__crate_return', NULL);
INSERT INTO `admin_site_activitylogmodel` (`id`, `log`, `created_at`, `customer_id`, `user_id`, `category`, `supplier_id`, `keywords`, `driver_id`) VALUES
(68, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>79</b> empty crates for\n                <a href=\"/sale/customer/13/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Over The Bar</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/13/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-02 15:11:42</span>\n              </p>\n            </div>\n            ', '2025-07-02 14:11:42.677391', 13, 3, 'sales', NULL, 'customer__crate_return', NULL),
(69, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250702152200822</b>.<br>\n                            <b>Total:</b> ₦831550.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦831550.00<br>\n                            <a href=\"/sale/12/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-02 15:22:00</span>\n                          </p>\n                        </div>\n                        ', '2025-07-02 15:22:00.892514', 3, 3, 'sales', NULL, 'sale__confirmed', 4),
(70, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250702152531997</b>.<br>\n                            <b>Total:</b> ₦253100.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦253100.00<br>\n                            <a href=\"/sale/13/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-02 15:25:32</span>\n                          </p>\n                        </div>\n                        ', '2025-07-02 15:25:32.016068', 4, 3, 'sales', NULL, 'sale__confirmed', NULL),
(71, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250702152630055</b>.<br>\n                            <b>Total:</b> ₦362200.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦362200.00<br>\n                            <a href=\"/sale/14/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-02 15:26:30</span>\n                          </p>\n                        </div>\n                        ', '2025-07-02 15:26:30.072001', 7, 3, 'sales', NULL, 'sale__confirmed', 4),
(72, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250702152723909</b>.<br>\n                            <b>Total:</b> ₦277500.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦277500.00<br>\n                            <a href=\"/sale/15/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-02 15:27:23</span>\n                          </p>\n                        </div>\n                        ', '2025-07-02 15:27:23.929856', 18, 3, 'sales', NULL, 'sale__confirmed', 5),
(73, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250703134913518</b>.<br>\n                            <b>Total:</b> ₦337600.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦337600.00<br>\n                            <a href=\"/sale/16/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-03 13:49:13</span>\n                          </p>\n                        </div>\n                        ', '2025-07-03 13:49:13.535416', 16, 3, 'sales', NULL, 'sale__confirmed', 4),
(74, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250703140110008</b>.<br>\n                            <b>Total:</b> ₦63275.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦28585.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦34690.00<br>\n                            <a href=\"/sale/17/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-03 14:01:10</span>\n                          </p>\n                        </div>\n                        ', '2025-07-03 14:01:10.034604', 22, 3, 'sales', NULL, 'sale__confirmed', 5),
(75, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦34690.00</b> in <b>cash</b> for\n                <a href=\"/sale/customer/22/detail\" class=\"text-white text-decoration-underline\">\n                  <b>madam chioma</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦0.00<br>\n                <a href=\"/sale/customer/22/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 15:02:29</span>\n              </p>\n            </div>\n            ', '2025-07-03 14:02:29.149081', 22, 3, 'sales', NULL, 'customer__repayment', NULL),
(76, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>5</b> empty crates for\n                <a href=\"/sale/customer/22/detail\" class=\"text-white text-decoration-underline\">\n                  <b>madam chioma</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/22/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 15:02:53</span>\n              </p>\n            </div>\n            ', '2025-07-03 14:02:53.040121', 22, 3, 'sales', NULL, 'customer__crate_return', NULL),
(77, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>5</b> empty crates for\n                <a href=\"/sale/customer/22/detail\" class=\"text-white text-decoration-underline\">\n                  <b>madam chioma</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/22/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 15:02:53</span>\n              </p>\n            </div>\n            ', '2025-07-03 14:02:53.761063', 22, 3, 'sales', NULL, 'customer__crate_return', NULL),
(78, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250703140352090</b>.<br>\n                            <b>Total:</b> ₦25310.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦25310.00<br>\n                            <a href=\"/sale/18/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-03 14:03:52</span>\n                          </p>\n                        </div>\n                        ', '2025-07-03 14:03:52.107094', 23, 3, 'sales', NULL, 'sale__confirmed', 5),
(79, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>2</b> empty crates for\n                <a href=\"/sale/customer/23/detail\" class=\"text-white text-decoration-underline\">\n                  <b>bernard eliagwu</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/23/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 15:04:18</span>\n              </p>\n            </div>\n            ', '2025-07-03 14:04:18.636710', 23, 3, 'sales', NULL, 'customer__crate_return', NULL),
(80, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250703143449282</b>.<br>\n                            <b>Total:</b> ₦20275.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦20275.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦0.00<br>\n                            <a href=\"/sale/19/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-03 14:34:49</span>\n                          </p>\n                        </div>\n                        ', '2025-07-03 14:34:49.425812', 24, 3, 'sales', NULL, 'sale__confirmed', NULL),
(81, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250703143645723</b>.<br>\n                            <b>Total:</b> ₦105000.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦105000.00<br>\n                            <a href=\"/sale/20/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-03 14:36:45</span>\n                          </p>\n                        </div>\n                        ', '2025-07-03 14:36:45.741157', 25, 3, 'sales', NULL, 'sale__confirmed', NULL),
(82, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦277500.00</b> to <b>bank</b> for\n                <a href=\"/sale/customer/18/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Abel (bernard)</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦0.00<br>\n                <a href=\"/sale/customer/18/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 15:40:48</span>\n              </p>\n            </div>\n            ', '2025-07-03 14:40:48.566207', 18, 3, 'sales', NULL, 'customer__repayment', NULL),
(83, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>30</b> empty crates for\n                <a href=\"/sale/customer/18/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Abel (bernard)</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/18/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 15:41:45</span>\n              </p>\n            </div>\n            ', '2025-07-03 14:41:45.369199', 18, 3, 'sales', NULL, 'customer__crate_return', NULL),
(84, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>75</b> empty crates for\n                <a href=\"/sale/customer/3/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Chika Ugwu</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/3/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 15:44:39</span>\n              </p>\n            </div>\n            ', '2025-07-03 14:44:39.514581', 3, 3, 'sales', NULL, 'customer__crate_return', NULL),
(85, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>29</b> empty crates for\n                <a href=\"/sale/customer/3/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Chika Ugwu</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/3/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 15:46:01</span>\n              </p>\n            </div>\n            ', '2025-07-03 14:46:01.848498', 3, 3, 'sales', NULL, 'customer__crate_return', NULL),
(86, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>30</b> empty crates for\n                <a href=\"/sale/customer/9/detail\" class=\"text-white text-decoration-underline\">\n                  <b>KC Gwandara</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/9/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 15:47:14</span>\n              </p>\n            </div>\n            ', '2025-07-03 14:47:14.619020', 9, 3, 'sales', NULL, 'customer__crate_return', NULL),
(87, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>70</b> empty crates for\n                <a href=\"/sale/customer/9/detail\" class=\"text-white text-decoration-underline\">\n                  <b>KC Gwandara</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/9/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 15:52:34</span>\n              </p>\n            </div>\n            ', '2025-07-03 14:52:34.276929', 9, 3, 'sales', NULL, 'customer__crate_return', NULL),
(88, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦300000.00</b> to driver <b>kenneth Erita</b> for\n                <a href=\"/sale/customer/10/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Ken Kabayi</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦302525.00<br>\n                <a href=\"/sale/customer/10/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 16:01:18</span>\n              </p>\n            </div>\n            ', '2025-07-03 15:01:18.713305', 10, 3, 'sales', NULL, 'customer__repayment', 4),
(89, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦60000.00</b> to driver <b>kenneth Erita</b> for\n                <a href=\"/sale/customer/20/detail\" class=\"text-white text-decoration-underline\">\n                  <b>mama chimanda</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦0.00<br>\n                <a href=\"/sale/customer/20/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 16:05:08</span>\n              </p>\n            </div>\n            ', '2025-07-03 15:05:08.630786', 20, 3, 'sales', NULL, 'customer__repayment', 4),
(90, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦700000.00</b> to <b>bank</b> for\n                <a href=\"/sale/customer/11/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Me &amp; U</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦130200.00<br>\n                <a href=\"/sale/customer/11/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 16:06:12</span>\n              </p>\n            </div>\n            ', '2025-07-03 15:06:12.513822', 11, 3, 'sales', NULL, 'customer__repayment', NULL),
(91, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦800000.00</b> to <b>bank</b> for\n                <a href=\"/sale/customer/8/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Mike Aso</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦791910.00<br>\n                <a href=\"/sale/customer/8/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 16:19:02</span>\n              </p>\n            </div>\n            ', '2025-07-03 15:19:02.064310', 8, 3, 'sales', NULL, 'customer__repayment', NULL),
(92, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>255</b> empty crates for\n                <a href=\"/sale/customer/16/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Pascal Ojobor</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/16/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 16:24:28</span>\n              </p>\n            </div>\n            ', '2025-07-03 15:24:28.661149', 16, 3, 'sales', NULL, 'customer__crate_return', NULL),
(93, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a crate return of <b>39</b> empty crates for\n                <a href=\"/sale/customer/7/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Simple</b>\n                </a>\n                as <b>Empty Return</b>.<br>\n                <a href=\"/sale/customer/7/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 16:28:02</span>\n              </p>\n            </div>\n            ', '2025-07-03 15:28:02.969933', 7, 3, 'sales', NULL, 'customer__crate_return', NULL),
(94, '\n            <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n              <p>\n                <b>\n                  <a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                  </a>\n                </b>\n                recorded a customer repayment of <b>₦253100.00</b> to <b>bank</b> for\n                <a href=\"/sale/customer/4/detail\" class=\"text-white text-decoration-underline\">\n                  <b>Sule David</b>\n                </a>.<br>\n                <b>Current Debt:</b> ₦18600.00<br>\n                <a href=\"/sale/customer/4/detail\" class=\"btn btn-sm btn-light mt-2\">View Customer</a>\n                <span class=\'float-end\'>2025-07-03 16:30:00</span>\n              </p>\n            </div>\n            ', '2025-07-03 15:30:00.093643', 4, 3, 'sales', NULL, 'customer__repayment', NULL),
(95, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250703153201283</b>.<br>\n                            <b>Total:</b> ₦8870.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦8870.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦0.00<br>\n                            <a href=\"/sale/21/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-03 15:32:01</span>\n                          </p>\n                        </div>\n                        ', '2025-07-03 15:32:01.354996', 24, 3, 'sales', NULL, 'sale__confirmed', NULL),
(96, '\n        <div class=\'bg-danger text-white p-2\' style=\'border-radius:5px;\'>\n            <p>\n                <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                </a></b> recorded an expense of \n                <b>₦3,900.00</b> under <b>Loading &amp; Offloading</b>.<br>\n                Remark: on 27/6/25\n                <span class=\'float-end\'>2025-07-03 16:42:22</span>\n            </p>\n        </div>\n        ', '2025-07-03 15:42:22.974400', NULL, 3, 'finance', NULL, 'finance__expense_created', NULL),
(97, '\n        <div class=\'bg-danger text-white p-2\' style=\'border-radius:5px;\'>\n            <p>\n                <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                </a></b> recorded an expense of \n                <b>₦2,400.00</b> under <b>Transport Fare</b>.<br>\n                Remark: Tp to madam&#x27;s house\n                <span class=\'float-end\'>2025-07-03 16:44:28</span>\n            </p>\n        </div>\n        ', '2025-07-03 15:44:28.920716', NULL, 3, 'finance', NULL, 'finance__expense_created', NULL),
(98, '\n        <div class=\'bg-danger text-white p-2\' style=\'border-radius:5px;\'>\n            <p>\n                <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">\n                    Adekanbi Yetunde\n                </a></b> recorded an expense of \n                <b>₦8,000.00</b> under <b>Loading &amp; Offloading</b>.<br>\n                Remark: part payment on 28/6/25\n                <span class=\'float-end\'>2025-07-03 16:46:19</span>\n            </p>\n        </div>\n        ', '2025-07-03 15:46:19.607844', NULL, 3, 'finance', NULL, 'finance__expense_created', NULL),
(99, '\n                        <div class=\'bg-success text-white p-2\' style=\'border-radius:5px;\'>\n                          <p>\n                            <b><a href=\"/human_resource/staff/2/detail\" class=\"text-white text-decoration-underline\">Adekanbi Yetunde</a></b>\n                            confirmed sale <b>#SALE-20250704090511110</b>.<br>\n                            <b>Total:</b> ₦493850.00 &nbsp;|&nbsp;\n                            <b>Paid:</b> ₦0.00 &nbsp;|&nbsp;\n                            <b>Owed:</b> ₦493850.00<br>\n                            <a href=\"/sale/22/\" class=\"btn btn-sm btn-light mt-2\">View Receipt</a>\n                            <span class=\'float-end\'>2025-07-04 09:05:11</span>\n                          </p>\n                        </div>\n                        ', '2025-07-04 09:05:11.161569', 26, 3, 'sales', NULL, 'sale__confirmed', 5);

-- --------------------------------------------------------

--
-- Table structure for table `admin_site_dashboardmodel`
--

CREATE TABLE `admin_site_dashboardmodel` (
  `id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `admin_site_siteinfomodel`
--

CREATE TABLE `admin_site_siteinfomodel` (
  `id` bigint NOT NULL,
  `name` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `short_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `logo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mobile` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `admin_site_siteinfomodel`
--

INSERT INTO `admin_site_siteinfomodel` (`id`, `name`, `short_name`, `logo`, `mobile`, `email`, `address`) VALUES
(1, 'GDC Platinum Royal Limited', 'GDC Platinum', 'images/logo/IMG_2568.png', '+2348138319994', 'gdcplatinum@gmail.com', 'Suite 8, Shappy Apo plaza, abacha Road, Maraba');

-- --------------------------------------------------------

--
-- Table structure for table `admin_site_sitesettingmodel`
--

CREATE TABLE `admin_site_sitesettingmodel` (
  `id` bigint NOT NULL,
  `opening_balance` double NOT NULL,
  `allow_sale_discount` tinyint(1) NOT NULL,
  `default_reorder_level` int NOT NULL,
  `crate_target_for_bonus` int DEFAULT NULL,
  `bonus_amount_per_crate` double DEFAULT NULL,
  `minimum_unit_profit` double NOT NULL,
  `recommended_unit_profit` double NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `max_category_crate_debt` int NOT NULL,
  `max_crate_debt` int NOT NULL,
  `max_customer_debt` int NOT NULL,
  `opening_cash_balance` double NOT NULL,
  `balance` double NOT NULL,
  `cash_balance` double NOT NULL,
  `opening_petty_cash_balance` double NOT NULL,
  `petty_cash_balance` double NOT NULL,
  `price_for_empty` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `admin_site_sitesettingmodel`
--

INSERT INTO `admin_site_sitesettingmodel` (`id`, `opening_balance`, `allow_sale_discount`, `default_reorder_level`, `crate_target_for_bonus`, `bonus_amount_per_crate`, `minimum_unit_profit`, `recommended_unit_profit`, `created_at`, `max_category_crate_debt`, `max_crate_debt`, `max_customer_debt`, `opening_cash_balance`, `balance`, `cash_balance`, `opening_petty_cash_balance`, `petty_cash_balance`, `price_for_empty`) VALUES
(1, 1000000, 1, 100, 4000, 25, 0, 400, '2025-06-26 13:49:23.742057', 200, 500, 20000000, 1000, 11178543, 304745, 1420, 7120, 1000);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(3, 'cashier'),
(1, 'director'),
(4, 'driver'),
(2, 'manager'),
(5, 'offloaders');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(20, 1, 9),
(16, 1, 30),
(15, 1, 34),
(22, 1, 37),
(23, 1, 40),
(24, 1, 57),
(25, 1, 65),
(26, 1, 69),
(27, 1, 73),
(28, 1, 77),
(29, 1, 78),
(30, 1, 79),
(31, 1, 80),
(32, 1, 93),
(33, 1, 96),
(34, 1, 101),
(35, 1, 102),
(36, 1, 104),
(37, 1, 113),
(38, 1, 116),
(58, 1, 125),
(39, 1, 127),
(17, 1, 128),
(18, 1, 129),
(19, 1, 132),
(21, 1, 153),
(53, 2, 37),
(1, 2, 65),
(57, 2, 78),
(11, 2, 80),
(56, 2, 93),
(49, 2, 96),
(51, 2, 101),
(54, 2, 104),
(55, 2, 125),
(50, 2, 128),
(2, 2, 129),
(4, 2, 132),
(12, 2, 153),
(45, 3, 37),
(42, 3, 65),
(48, 3, 125),
(40, 3, 128),
(41, 3, 129),
(43, 3, 132),
(47, 3, 153);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add activity log model', 7, 'add_activitylogmodel'),
(26, 'Can change activity log model', 7, 'change_activitylogmodel'),
(27, 'Can delete activity log model', 7, 'delete_activitylogmodel'),
(28, 'Can view activity log model', 7, 'view_activitylogmodel'),
(29, 'Can add site info model', 8, 'add_siteinfomodel'),
(30, 'Can change site info model', 8, 'change_siteinfomodel'),
(31, 'Can delete site info model', 8, 'delete_siteinfomodel'),
(32, 'Can view site info model', 8, 'view_siteinfomodel'),
(33, 'Can add site setting model', 9, 'add_sitesettingmodel'),
(34, 'Can change site setting model', 9, 'change_sitesettingmodel'),
(35, 'Can delete site setting model', 9, 'delete_sitesettingmodel'),
(36, 'Can view site setting model', 9, 'view_sitesettingmodel'),
(37, 'Can add dashboard model', 10, 'add_dashboardmodel'),
(38, 'Can change dashboard model', 10, 'change_dashboardmodel'),
(39, 'Can delete dashboard model', 10, 'delete_dashboardmodel'),
(40, 'Can view dashboard model', 10, 'view_dashboardmodel'),
(41, 'Can add expense type model', 11, 'add_expensetypemodel'),
(42, 'Can change expense type model', 11, 'change_expensetypemodel'),
(43, 'Can delete expense type model', 11, 'delete_expensetypemodel'),
(44, 'Can view expense type model', 11, 'view_expensetypemodel'),
(45, 'Can add staff deduction model', 12, 'add_staffdeductionmodel'),
(46, 'Can change staff deduction model', 12, 'change_staffdeductionmodel'),
(47, 'Can delete staff deduction model', 12, 'delete_staffdeductionmodel'),
(48, 'Can view staff deduction model', 12, 'view_staffdeductionmodel'),
(49, 'Can add staff salary history model', 13, 'add_staffsalaryhistorymodel'),
(50, 'Can change staff salary history model', 13, 'change_staffsalaryhistorymodel'),
(51, 'Can delete staff salary history model', 13, 'delete_staffsalaryhistorymodel'),
(52, 'Can view staff salary history model', 13, 'view_staffsalaryhistorymodel'),
(53, 'Can add staff salary model', 14, 'add_staffsalarymodel'),
(54, 'Can change staff salary model', 14, 'change_staffsalarymodel'),
(55, 'Can delete staff salary model', 14, 'delete_staffsalarymodel'),
(56, 'Can view staff salary model', 14, 'view_staffsalarymodel'),
(57, 'Can add staff salary payment model', 15, 'add_staffsalarypaymentmodel'),
(58, 'Can change staff salary payment model', 15, 'change_staffsalarypaymentmodel'),
(59, 'Can delete staff salary payment model', 15, 'delete_staffsalarypaymentmodel'),
(60, 'Can view staff salary payment model', 15, 'view_staffsalarypaymentmodel'),
(61, 'Can add staff salary summary model', 16, 'add_staffsalarysummarymodel'),
(62, 'Can change staff salary summary model', 16, 'change_staffsalarysummarymodel'),
(63, 'Can delete staff salary summary model', 16, 'delete_staffsalarysummarymodel'),
(64, 'Can view staff salary summary model', 16, 'view_staffsalarysummarymodel'),
(65, 'Can add expense model', 17, 'add_expensemodel'),
(66, 'Can change expense model', 17, 'change_expensemodel'),
(67, 'Can delete expense model', 17, 'delete_expensemodel'),
(68, 'Can view expense model', 17, 'view_expensemodel'),
(69, 'Can add staff bonus model', 18, 'add_staffbonusmodel'),
(70, 'Can change staff bonus model', 18, 'change_staffbonusmodel'),
(71, 'Can delete staff bonus model', 18, 'delete_staffbonusmodel'),
(72, 'Can view staff bonus model', 18, 'view_staffbonusmodel'),
(73, 'Can add cash transfer model', 19, 'add_cashtransfermodel'),
(74, 'Can change cash transfer model', 19, 'change_cashtransfermodel'),
(75, 'Can delete cash transfer model', 19, 'delete_cashtransfermodel'),
(76, 'Can view cash transfer model', 19, 'view_cashtransfermodel'),
(77, 'Can add staff model', 20, 'add_staffmodel'),
(78, 'Can change staff model', 20, 'change_staffmodel'),
(79, 'Can delete staff model', 20, 'delete_staffmodel'),
(80, 'Can view staff model', 20, 'view_staffmodel'),
(81, 'Can add staff profile model', 21, 'add_staffprofilemodel'),
(82, 'Can change staff profile model', 21, 'change_staffprofilemodel'),
(83, 'Can delete staff profile model', 21, 'delete_staffprofilemodel'),
(84, 'Can view staff profile model', 21, 'view_staffprofilemodel'),
(85, 'Can add staff wallet model', 22, 'add_staffwalletmodel'),
(86, 'Can change staff wallet model', 22, 'change_staffwalletmodel'),
(87, 'Can delete staff wallet model', 22, 'delete_staffwalletmodel'),
(88, 'Can view staff wallet model', 22, 'view_staffwalletmodel'),
(89, 'Can add category model', 23, 'add_categorymodel'),
(90, 'Can change category model', 23, 'change_categorymodel'),
(91, 'Can delete category model', 23, 'delete_categorymodel'),
(92, 'Can view category model', 23, 'view_categorymodel'),
(93, 'Can add product model', 24, 'add_productmodel'),
(94, 'Can change product model', 24, 'change_productmodel'),
(95, 'Can delete product model', 24, 'delete_productmodel'),
(96, 'Can view product model', 24, 'view_productmodel'),
(97, 'Can add price history model', 25, 'add_pricehistorymodel'),
(98, 'Can change price history model', 25, 'change_pricehistorymodel'),
(99, 'Can delete price history model', 25, 'delete_pricehistorymodel'),
(100, 'Can view price history model', 25, 'view_pricehistorymodel'),
(101, 'Can add Stock In Record', 26, 'add_stockinmodel'),
(102, 'Can change Stock In Record', 26, 'change_stockinmodel'),
(103, 'Can delete Stock In Record', 26, 'delete_stockinmodel'),
(104, 'Can view Stock In Record', 26, 'view_stockinmodel'),
(105, 'Can add Stock In Summary', 27, 'add_stockinsummarymodel'),
(106, 'Can change Stock In Summary', 27, 'change_stockinsummarymodel'),
(107, 'Can delete Stock In Summary', 27, 'delete_stockinsummarymodel'),
(108, 'Can view Stock In Summary', 27, 'view_stockinsummarymodel'),
(109, 'Can add Stock Out Record', 28, 'add_stockoutmodel'),
(110, 'Can change Stock Out Record', 28, 'change_stockoutmodel'),
(111, 'Can delete Stock Out Record', 28, 'delete_stockoutmodel'),
(112, 'Can view Stock Out Record', 28, 'view_stockoutmodel'),
(113, 'Can add supplier model', 29, 'add_suppliermodel'),
(114, 'Can change supplier model', 29, 'change_suppliermodel'),
(115, 'Can delete supplier model', 29, 'delete_suppliermodel'),
(116, 'Can view supplier model', 29, 'view_suppliermodel'),
(117, 'Can add empty adjustment model', 30, 'add_emptyadjustmentmodel'),
(118, 'Can change empty adjustment model', 30, 'change_emptyadjustmentmodel'),
(119, 'Can delete empty adjustment model', 30, 'delete_emptyadjustmentmodel'),
(120, 'Can view empty adjustment model', 30, 'view_emptyadjustmentmodel'),
(121, 'Can add supplier cash flow history model', 31, 'add_suppliercashflowhistorymodel'),
(122, 'Can change supplier cash flow history model', 31, 'change_suppliercashflowhistorymodel'),
(123, 'Can delete supplier cash flow history model', 31, 'delete_suppliercashflowhistorymodel'),
(124, 'Can view supplier cash flow history model', 31, 'view_suppliercashflowhistorymodel'),
(125, 'Can add customer model', 32, 'add_customermodel'),
(126, 'Can change customer model', 32, 'change_customermodel'),
(127, 'Can delete customer model', 32, 'delete_customermodel'),
(128, 'Can view customer model', 32, 'view_customermodel'),
(129, 'Can add sale model', 33, 'add_salemodel'),
(130, 'Can change sale model', 33, 'change_salemodel'),
(131, 'Can delete sale model', 33, 'delete_salemodel'),
(132, 'Can view sale model', 33, 'view_salemodel'),
(133, 'Can add return model', 34, 'add_returnmodel'),
(134, 'Can change return model', 34, 'change_returnmodel'),
(135, 'Can delete return model', 34, 'delete_returnmodel'),
(136, 'Can view return model', 34, 'view_returnmodel'),
(137, 'Can add Sale Item', 35, 'add_saleitemmodel'),
(138, 'Can change Sale Item', 35, 'change_saleitemmodel'),
(139, 'Can delete Sale Item', 35, 'delete_saleitemmodel'),
(140, 'Can view Sale Item', 35, 'view_saleitemmodel'),
(141, 'Can add customer wallet model', 36, 'add_customerwalletmodel'),
(142, 'Can change customer wallet model', 36, 'change_customerwalletmodel'),
(143, 'Can delete customer wallet model', 36, 'delete_customerwalletmodel'),
(144, 'Can view customer wallet model', 36, 'view_customerwalletmodel'),
(145, 'Can add Customer Crate Debt', 37, 'add_customercratedebtmodel'),
(146, 'Can change Customer Crate Debt', 37, 'change_customercratedebtmodel'),
(147, 'Can delete Customer Crate Debt', 37, 'delete_customercratedebtmodel'),
(148, 'Can view Customer Crate Debt', 37, 'view_customercratedebtmodel'),
(149, 'Can add Sale Category Crate Record', 38, 'add_salecategoryempty'),
(150, 'Can change Sale Category Crate Record', 38, 'change_salecategoryempty'),
(151, 'Can delete Sale Category Crate Record', 38, 'delete_salecategoryempty'),
(152, 'Can view Sale Category Crate Record', 38, 'view_salecategoryempty'),
(153, 'Can add Debt Repayment', 39, 'add_customerdebtrepaymentmodel'),
(154, 'Can change Debt Repayment', 39, 'change_customerdebtrepaymentmodel'),
(155, 'Can delete Debt Repayment', 39, 'delete_customerdebtrepaymentmodel'),
(156, 'Can view Debt Repayment', 39, 'view_customerdebtrepaymentmodel'),
(157, 'Can add Crate Return', 40, 'add_customercratereturnmodel'),
(158, 'Can change Crate Return', 40, 'change_customercratereturnmodel'),
(159, 'Can delete Crate Return', 40, 'delete_customercratereturnmodel'),
(160, 'Can view Crate Return', 40, 'view_customercratereturnmodel');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$NG1o3fQQ47BrZ4MFyuEmbx$LAeknlTCTS+EmwKO4hdXl0NIeM8IH0aro7/erR2syyc=', '2025-07-03 14:09:45.637807', 1, 'admin', '', '', '', 1, 1, '2025-06-26 13:07:10.254150'),
(2, 'pbkdf2_sha256$260000$lpA3sc6R94nw8246Wh4Cmo$OG0u7hrYhXxrJWF3brOFTIVK3PRje7OH1iFKkRLUjNQ=', '2025-07-03 13:44:19.218127', 0, 'nnenna.odo', '', '', '', 0, 1, '2025-06-26 13:16:31.475398'),
(3, 'pbkdf2_sha256$260000$8yaHW6plsk0U4elnCM2Mss$8dwuUtLxoMemuJjtJss+0MMHf4Jo507Iv7F01JxdcXo=', '2025-07-04 12:21:34.603365', 0, 'suzan', '', '', '', 0, 1, '2025-06-26 13:53:14.000000'),
(4, 'pbkdf2_sha256$260000$qpviv9nvHYhkc6H00NOtrK$GsCGZctqMlTaz7O4w5rxFnLeuNmmsi2/vQ363iTCTBE=', NULL, 0, 'nebechi', '', '', '', 0, 1, '2025-06-26 13:58:19.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 2, 1),
(2, 2, 2),
(3, 3, 2),
(4, 4, 3);

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-06-26 13:16:31.555093', '2', 'nnenna.odo', 1, '[{\"added\": {}}]', 4, 1),
(2, '2025-06-26 13:20:46.295134', '1', 'nnenna.odo', 1, '[{\"added\": {}}]', 21, 1),
(3, '2025-06-26 13:22:32.471743', '1', 'Mrs Nnenna', 2, '[{\"changed\": {\"fields\": [\"Group\"]}}]', 20, 1),
(4, '2025-06-26 13:52:26.474047', '1', 'SiteSettingModel object (1)', 2, '[{\"changed\": {\"fields\": [\"Opening petty cash balance\", \"Petty cash balance\"]}}]', 9, 1),
(5, '2025-06-26 13:54:18.148969', '3', 'stf-3234', 2, '[]', 4, 1),
(6, '2025-06-26 13:54:37.848137', '3', 'suzan', 2, '[{\"changed\": {\"fields\": [\"Username\"]}}]', 4, 1),
(7, '2025-06-26 13:58:54.435055', '4', 'nebechi', 2, '[{\"changed\": {\"fields\": [\"Username\"]}}]', 4, 1),
(8, '2025-06-26 13:59:30.539397', '4', 'nebechi', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'admin_site', 'activitylogmodel'),
(10, 'admin_site', 'dashboardmodel'),
(8, 'admin_site', 'siteinfomodel'),
(9, 'admin_site', 'sitesettingmodel'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(19, 'finance', 'cashtransfermodel'),
(17, 'finance', 'expensemodel'),
(11, 'finance', 'expensetypemodel'),
(18, 'finance', 'staffbonusmodel'),
(12, 'finance', 'staffdeductionmodel'),
(13, 'finance', 'staffsalaryhistorymodel'),
(14, 'finance', 'staffsalarymodel'),
(15, 'finance', 'staffsalarypaymentmodel'),
(16, 'finance', 'staffsalarysummarymodel'),
(20, 'human_resource', 'staffmodel'),
(21, 'human_resource', 'staffprofilemodel'),
(22, 'human_resource', 'staffwalletmodel'),
(23, 'inventory', 'categorymodel'),
(30, 'inventory', 'emptyadjustmentmodel'),
(25, 'inventory', 'pricehistorymodel'),
(24, 'inventory', 'productmodel'),
(26, 'inventory', 'stockinmodel'),
(27, 'inventory', 'stockinsummarymodel'),
(28, 'inventory', 'stockoutmodel'),
(31, 'inventory', 'suppliercashflowhistorymodel'),
(29, 'inventory', 'suppliermodel'),
(37, 'sale', 'customercratedebtmodel'),
(40, 'sale', 'customercratereturnmodel'),
(39, 'sale', 'customerdebtrepaymentmodel'),
(32, 'sale', 'customermodel'),
(36, 'sale', 'customerwalletmodel'),
(34, 'sale', 'returnmodel'),
(38, 'sale', 'salecategoryempty'),
(35, 'sale', 'saleitemmodel'),
(33, 'sale', 'salemodel'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-06-26 13:05:42.824048'),
(2, 'auth', '0001_initial', '2025-06-26 13:05:44.319978'),
(3, 'admin', '0001_initial', '2025-06-26 13:05:44.611659'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-06-26 13:05:44.622597'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-06-26 13:05:44.630665'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-06-26 13:05:44.733389'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-06-26 13:05:44.826914'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-06-26 13:05:44.913786'),
(9, 'auth', '0004_alter_user_username_opts', '2025-06-26 13:05:44.923404'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-06-26 13:05:45.036084'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-06-26 13:05:45.041070'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-06-26 13:05:45.051026'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-06-26 13:05:45.180889'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-06-26 13:05:45.232625'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-06-26 13:05:45.266520'),
(16, 'auth', '0011_update_proxy_permissions', '2025-06-26 13:05:45.274560'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-06-26 13:05:45.328376'),
(18, 'human_resource', '0001_initial', '2025-06-26 13:05:46.154833'),
(19, 'human_resource', '0002_alter_staffmodel_email', '2025-06-26 13:05:46.261704'),
(20, 'human_resource', '0003_alter_staffprofilemodel_staff', '2025-06-26 13:05:46.271471'),
(21, 'human_resource', '0004_staffmodel_crate_target_for_bonus', '2025-06-26 13:05:46.347530'),
(22, 'inventory', '0001_initial', '2025-06-26 13:05:48.067914'),
(23, 'inventory', '0002_stockinsummarymodel_is_tampered_and_more', '2025-06-26 13:05:48.206267'),
(24, 'inventory', '0003_alter_stockinmodel_quantity_added', '2025-06-26 13:05:48.220736'),
(25, 'inventory', '0004_stockinmodel_unit_selling_price', '2025-06-26 13:05:48.315896'),
(26, 'inventory', '0005_alter_stockinsummarymodel_status', '2025-06-26 13:05:48.327184'),
(27, 'inventory', '0006_stockoutmodel_stock_out_empty', '2025-06-26 13:05:48.410683'),
(28, 'inventory', '0007_productmodel_last_cost_price', '2025-06-26 13:05:48.509045'),
(29, 'inventory', '0008_emptyadjustmentmodel', '2025-06-26 13:05:48.902224'),
(30, 'inventory', '0009_productmodel_updated_by', '2025-06-26 13:05:49.026975'),
(31, 'inventory', '0010_stockinsummarymodel_payment_source', '2025-06-26 13:05:49.110531'),
(32, 'inventory', '0011_remove_suppliermodel_products_suppliermodel_category_and_more', '2025-06-26 13:05:49.345369'),
(33, 'sale', '0001_initial', '2025-06-26 13:05:50.403509'),
(34, 'sale', '0002_remove_returnmodel_product_remove_returnmodel_sale_and_more', '2025-06-26 13:05:51.953428'),
(35, 'sale', '0003_alter_salemodel_delivery_status', '2025-06-26 13:05:51.970056'),
(36, 'sale', '0004_alter_salemodel_status', '2025-06-26 13:05:51.985035'),
(37, 'sale', '0005_alter_salemodel_status', '2025-06-26 13:05:52.000930'),
(38, 'sale', '0006_alter_salemodel_delivery_status', '2025-06-26 13:05:52.015769'),
(39, 'admin_site', '0001_initial', '2025-06-26 13:05:52.344300'),
(40, 'admin_site', '0002_sitesettingmodel_created_at', '2025-06-26 13:05:52.398189'),
(41, 'admin_site', '0003_alter_siteinfomodel_logo', '2025-06-26 13:05:52.421381'),
(42, 'admin_site', '0004_sitesettingmodel_max_category_crate_debt_and_more', '2025-06-26 13:05:52.515085'),
(43, 'admin_site', '0005_sitesettingmodel_max_customer_debt', '2025-06-26 13:05:52.577837'),
(44, 'admin_site', '0006_sitesettingmodel_opening_cash_balance', '2025-06-26 13:05:52.625872'),
(45, 'admin_site', '0007_activitylogmodel_customer_activitylogmodel_user', '2025-06-26 13:05:52.765228'),
(46, 'admin_site', '0008_sitesettingmodel_balance_and_more', '2025-06-26 13:05:52.866787'),
(47, 'admin_site', '0009_activitylogmodel_category', '2025-06-26 13:05:52.930348'),
(48, 'admin_site', '0010_sitesettingmodel_opening_petty_balance_and_more', '2025-06-26 13:05:53.029178'),
(49, 'admin_site', '0011_sitesettingmodel_price_for_empty', '2025-06-26 13:05:53.304485'),
(50, 'admin_site', '0012_activitylogmodel_supplier', '2025-06-26 13:05:53.402062'),
(51, 'admin_site', '0013_activitylogmodel_keywords', '2025-06-26 13:05:53.459315'),
(52, 'admin_site', '0014_rename_opening_petty_balance_sitesettingmodel_opening_petty_cash_balance_and_more', '2025-06-26 13:05:53.495468'),
(53, 'admin_site', '0015_activitylogmodel_driver', '2025-06-26 13:05:53.593653'),
(54, 'admin_site', '0016_dashboardmodel', '2025-06-26 13:05:53.629662'),
(55, 'inventory', '0012_suppliermodel_balance_suppliermodel_initial_balance_and_more', '2025-06-26 13:05:53.840252'),
(56, 'inventory', '0013_alter_suppliermodel_initial_balance', '2025-06-26 13:05:53.848615'),
(57, 'inventory', '0014_suppliermodel_updated_by', '2025-06-26 13:05:53.957074'),
(58, 'inventory', '0015_alter_stockinmodel_date_added', '2025-06-26 13:05:53.976570'),
(59, 'finance', '0001_initial', '2025-06-26 13:05:55.096010'),
(60, 'finance', '0002_initial', '2025-06-26 13:05:56.152618'),
(61, 'finance', '0003_alter_staffsalarypaymentmodel_options_and_more', '2025-06-26 13:05:57.082820'),
(62, 'finance', '0004_cashtransfermodel', '2025-06-26 13:05:57.769977'),
(63, 'finance', '0005_alter_cashtransfermodel_transfer_type', '2025-06-26 13:05:57.806234'),
(64, 'finance', '0006_alter_staffsalarymodel_salary', '2025-06-26 13:05:57.832655'),
(65, 'finance', '0007_cashtransfermodel_supplier_and_more', '2025-06-26 13:05:57.971195'),
(66, 'finance', '0008_staffsalarypaymentmodel_payment_source', '2025-06-26 13:05:58.061511'),
(67, 'finance', '0009_remove_staffsalarypaymentmodel_payment_source_and_more', '2025-06-26 13:05:58.205634'),
(68, 'inventory', '0016_remove_stockinsummarymodel_payment_source_and_more', '2025-06-26 13:05:58.917277'),
(69, 'inventory', '0017_stockinsummarymodel_total_quantity', '2025-06-26 13:05:59.005986'),
(70, 'inventory', '0018_productmodel_initial_quantity_and_more', '2025-06-26 13:05:59.321018'),
(71, 'sale', '0007_salemodel_payment_destination', '2025-06-26 13:05:59.620111'),
(72, 'sale', '0008_remove_saleitemmodel_crate_brought_and_more', '2025-06-26 13:06:00.196097'),
(73, 'sale', '0009_saleitemmodel_stock_saleitemmodel_total_discount_and_more', '2025-06-26 13:06:00.940998'),
(74, 'sale', '0010_alter_customercratedebtmodel_category_and_more', '2025-06-26 13:06:01.851588'),
(75, 'sale', '0011_customercratedebtmodel_driver', '2025-06-26 13:06:01.969795'),
(76, 'sale', '0012_remove_customercratedebtmodel_driver_and_more', '2025-06-26 13:06:02.204739'),
(77, 'sale', '0013_alter_salecategoryempty_sale', '2025-06-26 13:06:02.273445'),
(78, 'sale', '0014_alter_salecategoryempty_sale', '2025-06-26 13:06:02.300205'),
(79, 'sale', '0015_customercratereturnmodel_amount_paid_and_more', '2025-06-26 13:06:02.622641'),
(80, 'sessions', '0001_initial', '2025-06-26 13:06:02.800153'),
(81, 'inventory', '0019_auto_20250630_1829', '2025-06-30 18:29:44.189311');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0t3gy4qzygibn1q2ejib72rnaqnedza7', '.eJxVjMsOwiAQRf-FtSG8ikyX7v0GAszUogaa0iYa479rky50e8-558V8WJfRr41mn5H1TLLD7xZDulHZAF5DuVSealnmHPmm8J02fq5I99Pu_gXG0MbvWyUrpe1EtGCUNgYH4QDSUafgkiMjjEStQQHaOEDs1KADgJZOiIgGaYs2ai3X4ukx5fnJevH-AE6_Plc:1uUnAr:Tq6yT8ScUlOFFfODOy8kap_WCWEfk5AUdiCf3lUQ6YA', '2025-07-10 14:01:57.889748'),
('2efiwzwurl4b3zrnw6yayn4brm70omn8', '.eJxVjMEOwiAQBf-FsyGUtkB79O43kGVZBDVgSptojP-uJD3o9c28eTEL2xrtVmmxybOZSXb43RzglXID_gL5XDiWvC7J8abwnVZ-Kp5ux939C0Sosb2noZMjGvCTUAQqaAc9BArUDw6ARkItlETRI4Zg_LesyYxSTuh8R9CilWpNJVt63NPyZLN4fwDsEkEV:1uUmtz:O2p74Ijzjb5bqHvpYPDjO-3rfAyLfa4pium2kH9l9D8', '2025-07-10 13:44:31.546376'),
('66wjd5fc46fu8nbs2c3o7njraznz0603', '.eJxVjEEOwiAQAP_C2RAoLbQevfsGsssuFjVgSptojH83JD3odWYyb-FhW2e_VV58InEURhx-GUK4cW6CrpAvRYaS1yWhbIncbZXnQnw_7e3fYIY6ty1YM3JnTYCOMHSTHpwalR16F12gMMXJMCsN6FwkRBWVZeDeaaNHUtimlWtNJXt-PtLyEkf1-QKQzT9n:1uWuK4:K_OXuIC7L3VNjQ8QIcbz7KDRQbF5ElTFLdArIGul6JI', '2025-07-16 10:04:12.971730'),
('6wlatq6bc5cpftqh7ayrwpzq5z27i3gs', '.eJxVjEEOwiAQAP_C2RAoLbQevfsGsssuFjVgSptojH83JD3odWYyb-FhW2e_VV58InEURhx-GUK4cW6CrpAvRYaS1yWhbIncbZXnQnw_7e3fYIY6ty1YM3JnTYCOMHSTHpwalR16F12gMMXJMCsN6FwkRBWVZeDeaaNHUtimlWtNJXt-PtLyEkf1-QKQzT9n:1uXLdi:y0JSdXbdi2jQM9674TV6slP4daaQSpS7AlAWWrtmyeU', '2025-07-17 15:14:18.407095'),
('763h65y2jok4evcs7idc3ok42j1yb45n', '.eJxVjEEOwiAQAP_C2RAoLbQevfsGsssuFjVgSptojH83JD3odWYyb-FhW2e_VV58InEURhx-GUK4cW6CrpAvRYaS1yWhbIncbZXnQnw_7e3fYIY6ty1YM3JnTYCOMHSTHpwalR16F12gMMXJMCsN6FwkRBWVZeDeaaNHUtimlWtNJXt-PtLyEkf1-QKQzT9n:1uWe2O:IR4jq3fasIPwYlNoE35dqPw7PX-gMHd129Y_0fb-rck', '2025-07-15 16:40:52.078137'),
('800a19l17502m9zptp7szd32nab8px42', '.eJxVjMEOwiAQBf-FsyGUtkB79O43kGVZBDVgSptojP-uJD3o9c28eTEL2xrtVmmxybOZSXb43RzglXID_gL5XDiWvC7J8abwnVZ-Kp5ux939C0Sosb2noZMjGvCTUAQqaAc9BArUDw6ARkItlETRI4Zg_LesyYxSTuh8R9CilWpNJVt63NPyZLN4fwDsEkEV:1uWzhr:tnxGAXVzN8uCuXCG07orTMP0DpgDGxC1BvntdvFQPbY', '2025-07-16 15:49:07.207691'),
('9carxv3qv5gelhp75jbypwc58culcz7v', '.eJxVjMsOwiAQRf-FtSG8ikyX7v0GAszUogaa0iYa479rky50e8-558V8WJfRr41mn5H1TLLD7xZDulHZAF5DuVSealnmHPmm8J02fq5I99Pu_gXG0MbvWyUrpe1EtGCUNgYH4QDSUafgkiMjjEStQQHaOEDs1KADgJZOiIgGaYs2ai3X4ukx5fnJevH-AE6_Plc:1uUmb2:Ajx_nm4NhM5YYBidnzvqbv6xSdY17ikmh215DNqeFBA', '2025-07-10 13:24:56.351895'),
('alrhskcwo7z3jqxghr145uryd9ee9tqa', '.eJxVjMEOwiAQBf-FsyGUtkB79O43kGVZBDVgSptojP-uJD3o9c28eTEL2xrtVmmxybOZSXb43RzglXID_gL5XDiWvC7J8abwnVZ-Kp5ux939C0Sosb2noZMjGvCTUAQqaAc9BArUDw6ARkItlETRI4Zg_LesyYxSTuh8R9CilWpNJVt63NPyZLN4fwDsEkEV:1uXKEd:JF-rb1uV9i2eqUEeJg89PNH2Or3PXDDHVjeSXl9sRJg', '2025-07-17 13:44:19.212946'),
('csizfjoutvvbjgq97afi9raaao50dibb', '.eJxVjEEOwiAQAP_C2RAoLbQevfsGsssuFjVgSptojH83JD3odWYyb-FhW2e_VV58InEURhx-GUK4cW6CrpAvRYaS1yWhbIncbZXnQnw_7e3fYIY6ty1YM3JnTYCOMHSTHpwalR16F12gMMXJMCsN6FwkRBWVZeDeaaNHUtimlWtNJXt-PtLyEkf1-QKQzT9n:1uVRMp:Fl4RHxkE5W9u8SEUtTNf3qtpRFvG_DspYjPSsuC_IgM', '2025-07-12 08:56:59.000209'),
('f2q5lm9qqck0y5li513hjj4510ly239k', '.eJxVjEEOwiAQAP_C2RAoLbQevfsGsssuFjVgSptojH83JD3odWYyb-FhW2e_VV58InEURhx-GUK4cW6CrpAvRYaS1yWhbIncbZXnQnw_7e3fYIY6ty1YM3JnTYCOMHSTHpwalR16F12gMMXJMCsN6FwkRBWVZeDeaaNHUtimlWtNJXt-PtLyEkf1-QKQzT9n:1uWwPn:ozoKNsxIj52C1ilqPpGI2rXeweYibYimzuWGCQkE3XI', '2025-07-16 12:18:15.861580'),
('fvoi30vt6gngg21ge26njvd76ofm8gr1', '.eJxVjEEOwiAQAP_C2RAoLbQevfsGsssuFjVgSptojH83JD3odWYyb-FhW2e_VV58InEURhx-GUK4cW6CrpAvRYaS1yWhbIncbZXnQnw_7e3fYIY6ty1YM3JnTYCOMHSTHpwalR16F12gMMXJMCsN6FwkRBWVZeDeaaNHUtimlWtNJXt-PtLyEkf1-QKQzT9n:1uXLhJ:2eITEgW6jxxYeM2nNP0Y-HUpYJ4qXLJ4EI-KqdGY3Hw', '2025-07-17 15:18:01.192345'),
('gauac7tiu2jdowhgh7slu4hlre4a12u6', '.eJxVjEEOwiAQAP_C2RAoLbQevfsGsssuFjVgSptojH83JD3odWYyb-FhW2e_VV58InEURhx-GUK4cW6CrpAvRYaS1yWhbIncbZXnQnw_7e3fYIY6ty1YM3JnTYCOMHSTHpwalR16F12gMMXJMCsN6FwkRBWVZeDeaaNHUtimlWtNJXt-PtLyEkf1-QKQzT9n:1uXfQ6:8gIgfxLc-hQEKpoQN7iCloEUY0sQSDCIF9zi6J4NQec', '2025-07-18 12:21:34.644842'),
('gbfi8pn6kqe9eoojn5qyc9o0rt9deue2', '.eJxVjMEOwiAQBf-FsyGUtkB79O43kGVZBDVgSptojP-uJD3o9c28eTEL2xrtVmmxybOZSXb43RzglXID_gL5XDiWvC7J8abwnVZ-Kp5ux939C0Sosb2noZMjGvCTUAQqaAc9BArUDw6ARkItlETRI4Zg_LesyYxSTuh8R9CilWpNJVt63NPyZLN4fwDsEkEV:1uWckS:n-cobHF-aRNAwCHa-kVm4AEXzaENJ7Piyh6uIEVauyU', '2025-07-15 15:18:16.308652'),
('gvny541wzeyosslu680nwl60ztuv9l3a', '.eJxVjMsOwiAQRf-FtSG8ikyX7v0GAszUogaa0iYa479rky50e8-558V8WJfRr41mn5H1TLLD7xZDulHZAF5DuVSealnmHPmm8J02fq5I99Pu_gXG0MbvWyUrpe1EtGCUNgYH4QDSUafgkiMjjEStQQHaOEDs1KADgJZOiIgGaYs2ai3X4ukx5fnJevH-AE6_Plc:1uUpfN:VR0IaiyoWNZ7ILmV7Ay6Fj71wK_tRChkHax5ycgkkrU', '2025-07-10 16:41:37.057960'),
('hcu57hm684atpogidzontp4tmwjdic7v', '.eJxVjMEOwiAQBf-FsyGUtkB79O43kGVZBDVgSptojP-uJD3o9c28eTEL2xrtVmmxybOZSXb43RzglXID_gL5XDiWvC7J8abwnVZ-Kp5ux939C0Sosb2noZMjGvCTUAQqaAc9BArUDw6ARkItlETRI4Zg_LesyYxSTuh8R9CilWpNJVt63NPyZLN4fwDsEkEV:1uXEE1:TgNll-BaQduhPYPCJMlTBOBCQ8jsZlVRYVKyDp-CBuU', '2025-07-17 07:19:17.943584'),
('heny6fpvmubqxw8w288yj2caz8yodxg0', '.eJxVjMsOwiAQRf-FtSG8ikyX7v0GAszUogaa0iYa479rky50e8-558V8WJfRr41mn5H1TLLD7xZDulHZAF5DuVSealnmHPmm8J02fq5I99Pu_gXG0MbvWyUrpe1EtGCUNgYH4QDSUafgkiMjjEStQQHaOEDs1KADgJZOiIgGaYs2ai3X4ukx5fnJevH-AE6_Plc:1uWtWc:X3E5AvuxJ1H_WJ6Tshw13bqWfmnu9fctSks_XEm4lPI', '2025-07-16 09:13:06.742641'),
('il6ziaoh1rf6t9gmvu2x0olwm1re7bvg', '.eJxVjMEOwiAQBf-FsyGUtkB79O43kGVZBDVgSptojP-uJD3o9c28eTEL2xrtVmmxybOZSXb43RzglXID_gL5XDiWvC7J8abwnVZ-Kp5ux939C0Sosb2noZMjGvCTUAQqaAc9BArUDw6ARkItlETRI4Zg_LesyYxSTuh8R9CilWpNJVt63NPyZLN4fwDsEkEV:1uVvgx:fahQry3twUWeL9aRH9U-5FQu7q5u5kEBZV1teeRz808', '2025-07-13 17:19:47.319940'),
('kbprtz6yr0hxrsmgvi5i91f5fak8qqk6', '.eJxVjMEOwiAQBf-FsyGUtkB79O43kGVZBDVgSptojP-uJD3o9c28eTEL2xrtVmmxybOZSXb43RzglXID_gL5XDiWvC7J8abwnVZ-Kp5ux939C0Sosb2noZMjGvCTUAQqaAc9BArUDw6ARkItlETRI4Zg_LesyYxSTuh8R9CilWpNJVt63NPyZLN4fwDsEkEV:1uWLrw:2pqnMC9Yx9c-Fxe4T6_Wq0t6fYdM-Lr13DG8dCb29ZU', '2025-07-14 21:16:52.758770'),
('lx6l6mliv2n8to3ocmg05qwxehkmo6cp', '.eJxVjMEOwiAQBf-FsyGUtkB79O43kGVZBDVgSptojP-uJD3o9c28eTEL2xrtVmmxybOZSXb43RzglXID_gL5XDiWvC7J8abwnVZ-Kp5ux939C0Sosb2noZMjGvCTUAQqaAc9BArUDw6ARkItlETRI4Zg_LesyYxSTuh8R9CilWpNJVt63NPyZLN4fwDsEkEV:1uWdez:cg35ceejlzn3CfgXJSfxLPgDa1PMHkkGp7hkQ5PnqD4', '2025-07-15 16:16:41.294689'),
('myoyw6hwmbo7n6damxtxb83goxd21kzy', '.eJxVjMEOwiAQBf-FsyGUtkB79O43kGVZBDVgSptojP-uJD3o9c28eTEL2xrtVmmxybOZSXb43RzglXID_gL5XDiWvC7J8abwnVZ-Kp5ux939C0Sosb2noZMjGvCTUAQqaAc9BArUDw6ARkItlETRI4Zg_LesyYxSTuh8R9CilWpNJVt63NPyZLN4fwDsEkEV:1uWvup:LyZbv3KkepSlK63-79WkmM_FEeERGaH2SHG9AFsqqZo', '2025-07-16 11:46:15.114896'),
('nfril8zg8y5iwnl2ctz94g6pvsnqppya', '.eJxVjEEOwiAQAP_C2RAoLbQevfsGsssuFjVgSptojH83JD3odWYyb-FhW2e_VV58InEURhx-GUK4cW6CrpAvRYaS1yWhbIncbZXnQnw_7e3fYIY6ty1YM3JnTYCOMHSTHpwalR16F12gMMXJMCsN6FwkRBWVZeDeaaNHUtimlWtNJXt-PtLyEkf1-QKQzT9n:1uVRhf:llm06UY6k0dAwQyj1pYKgbdDVHKxNYS3zlkLuN5Gg5Q', '2025-07-12 09:18:31.249693'),
('o5c1xdt8wk19235yedqcwfoh737k6fjh', '.eJxVjEEOwiAQAP_C2RAoLbQevfsGsssuFjVgSptojH83JD3odWYyb-FhW2e_VV58InEURhx-GUK4cW6CrpAvRYaS1yWhbIncbZXnQnw_7e3fYIY6ty1YM3JnTYCOMHSTHpwalR16F12gMMXJMCsN6FwkRBWVZeDeaaNHUtimlWtNJXt-PtLyEkf1-QKQzT9n:1uUn9e:iPgo0A95R3s5V4m-capv2hvCxe-1QlQTIlqE-yCTkmk', '2025-07-10 14:00:42.024023'),
('o5i8074icbkedsek88azrlm3rlf239e3', '.eJxVjEEOwiAQAP_C2RAoLbQevfsGsssuFjVgSptojH83JD3odWYyb-FhW2e_VV58InEURhx-GUK4cW6CrpAvRYaS1yWhbIncbZXnQnw_7e3fYIY6ty1YM3JnTYCOMHSTHpwalR16F12gMMXJMCsN6FwkRBWVZeDeaaNHUtimlWtNJXt-PtLyEkf1-QKQzT9n:1uXLL2:2jtcNXaHWYcmrtMzKHgNP8xUU9nBN0Cv-c9Hgcd2LnU', '2025-07-17 14:55:00.278010'),
('qh2ieu4c1uh9hhc5yi4y8qapkv8lm49p', '.eJxVjMEOwiAQBf-FsyGUtkB79O43kGVZBDVgSptojP-uJD3o9c28eTEL2xrtVmmxybOZSXb43RzglXID_gL5XDiWvC7J8abwnVZ-Kp5ux939C0Sosb2noZMjGvCTUAQqaAc9BArUDw6ARkItlETRI4Zg_LesyYxSTuh8R9CilWpNJVt63NPyZLN4fwDsEkEV:1uWIpr:PCCfLEqbxKpcREWmAsqRtkxJcczU1iuKQ8gUKhRzQFY', '2025-07-14 18:02:31.269458'),
('sw65garhht59lj5lo8henxdqsu3t5twq', '.eJxVjMsOwiAQRf-FtSG8ikyX7v0GAszUogaa0iYa479rky50e8-558V8WJfRr41mn5H1TLLD7xZDulHZAF5DuVSealnmHPmm8J02fq5I99Pu_gXG0MbvWyUrpe1EtGCUNgYH4QDSUafgkiMjjEStQQHaOEDs1KADgJZOiIgGaYs2ai3X4ukx5fnJevH-AE6_Plc:1uUmrD:qHJ2JLCf8szrqBYAvJPsv-MsE0Rb2s1Xa4yffO509ao', '2025-07-10 13:41:39.951831'),
('u0ygxd3pj7ek3fb61viv5xs0xfpxey4k', '.eJxVjMEOwiAQBf-FsyGUtkB79O43kGVZBDVgSptojP-uJD3o9c28eTEL2xrtVmmxybOZSXb43RzglXID_gL5XDiWvC7J8abwnVZ-Kp5ux939C0Sosb2noZMjGvCTUAQqaAc9BArUDw6ARkItlETRI4Zg_LesyYxSTuh8R9CilWpNJVt63NPyZLN4fwDsEkEV:1uUmZd:PTE6wfFUVMTZ4AQjPBHxAKS89GcY6VMtBiUNsKiUqro', '2025-07-10 13:23:29.891900'),
('wh20heoxsz0v2375v8b82b13ns9lq4h5', '.eJxVjMEOwiAQBf-FsyGUtkB79O43kGVZBDVgSptojP-uJD3o9c28eTEL2xrtVmmxybOZSXb43RzglXID_gL5XDiWvC7J8abwnVZ-Kp5ux939C0Sosb2noZMjGvCTUAQqaAc9BArUDw6ARkItlETRI4Zg_LesyYxSTuh8R9CilWpNJVt63NPyZLN4fwDsEkEV:1uXKEd:JF-rb1uV9i2eqUEeJg89PNH2Or3PXDDHVjeSXl9sRJg', '2025-07-17 13:44:19.224151'),
('xrsffx4syziwui5aiea2byyo42ad8yly', '.eJxVjEEOwiAQAP_C2RAoLbQevfsGsssuFjVgSptojH83JD3odWYyb-FhW2e_VV58InEURhx-GUK4cW6CrpAvRYaS1yWhbIncbZXnQnw_7e3fYIY6ty1YM3JnTYCOMHSTHpwalR16F12gMMXJMCsN6FwkRBWVZeDeaaNHUtimlWtNJXt-PtLyEkf1-QKQzT9n:1uXc9X:g4qHlTZGQ6yLe-5KhUZa8mQzFJjJt96WzexSkbvd1KQ', '2025-07-18 08:52:15.060113'),
('xsgi7rmbfzw4ohk6hyyo8k1qi5xzz64w', '.eJxVjMEOwiAQBf-FsyGUtkB79O43kGVZBDVgSptojP-uJD3o9c28eTEL2xrtVmmxybOZSXb43RzglXID_gL5XDiWvC7J8abwnVZ-Kp5ux939C0Sosb2noZMjGvCTUAQqaAc9BArUDw6ARkItlETRI4Zg_LesyYxSTuh8R9CilWpNJVt63NPyZLN4fwDsEkEV:1uVsnt:SnwOtBaIU-QkWrsYm0xpcYWcfFTgbaLu-CCjPawgJi4', '2025-07-13 14:14:45.854870'),
('xy424khepkbnwqla523t4iyql2a2eta5', '.eJxVjMsOwiAQRf-FtSG8ikyX7v0GAszUogaa0iYa479rky50e8-558V8WJfRr41mn5H1TLLD7xZDulHZAF5DuVSealnmHPmm8J02fq5I99Pu_gXG0MbvWyUrpe1EtGCUNgYH4QDSUafgkiMjjEStQQHaOEDs1KADgJZOiIgGaYs2ai3X4ukx5fnJevH-AE6_Plc:1uXKdF:vvSdlAEX8-lq8czdVcKieJe-DJq9QPYz8Gu66wU8iz8', '2025-07-17 14:09:45.639906'),
('xzf7ckpssxfjduuj9sozyklpss3a0vs0', '.eJxVjMsOwiAQRf-FtSG8ikyX7v0GAszUogaa0iYa479rky50e8-558V8WJfRr41mn5H1TLLD7xZDulHZAF5DuVSealnmHPmm8J02fq5I99Pu_gXG0MbvWyUrpe1EtGCUNgYH4QDSUafgkiMjjEStQQHaOEDs1KADgJZOiIgGaYs2ai3X4ukx5fnJevH-AE6_Plc:1uWJHa:8zQS-o0dy8wihNFjtQA_qT8lj8O0QlmC580Z2nOwYo0', '2025-07-14 18:31:10.496458'),
('zkwhun7la67gzk12arltn0fgf3aqw2pk', '.eJxVjEEOwiAQAP_C2RAoLbQevfsGsssuFjVgSptojH83JD3odWYyb-FhW2e_VV58InEURhx-GUK4cW6CrpAvRYaS1yWhbIncbZXnQnw_7e3fYIY6ty1YM3JnTYCOMHSTHpwalR16F12gMMXJMCsN6FwkRBWVZeDeaaNHUtimlWtNJXt-PtLyEkf1-QKQzT9n:1uWCYA:2nZHZ3n2nPa9_z1REjurAe3om_ja-zWDOxSCi70w-uA', '2025-07-14 11:19:50.396321');

-- --------------------------------------------------------

--
-- Table structure for table `finance_cashtransfermodel`
--

CREATE TABLE `finance_cashtransfermodel` (
  `id` bigint NOT NULL,
  `transfer_type` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `source` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `destination` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `amount` double NOT NULL,
  `comment` longtext COLLATE utf8mb4_unicode_ci,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `staff_id` bigint DEFAULT NULL,
  `supplier_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `finance_cashtransfermodel`
--

INSERT INTO `finance_cashtransfermodel` (`id`, `transfer_type`, `source`, `destination`, `amount`, `comment`, `created_at`, `created_by_id`, `staff_id`, `supplier_id`) VALUES
(1, 'adjustment_add', 'bank', 'bank', 1833055, 'Reconciled the bank and the vendor accounts to capture the right closing balances.', '2025-06-28 06:44:23.264303', 2, NULL, NULL),
(2, 'bank_to_supplier', 'bank', 'supplier', 323990, '', '2025-06-28 07:10:53.506011', 2, NULL, 2),
(3, 'bank_to_supplier', 'bank', 'supplier', 323990, '', '2025-06-28 07:14:15.060023', 2, NULL, 1),
(4, 'bank_to_supplier', 'bank', 'supplier', 362277, '', '2025-06-28 07:15:08.597945', 2, NULL, 2),
(5, 'bank_to_petty', 'bank', 'petty', 70000, '', '2025-06-29 10:45:27.847432', 2, NULL, NULL),
(6, 'adjustment_add', 'bank', 'bank', 21820590, 'was already in nbl before system migration', '2025-07-02 10:48:55.168730', 2, NULL, NULL),
(7, 'adjustment_add', 'bank', 'bank', 474155, 'was already in nbl before system migration', '2025-07-02 10:49:27.951748', 2, NULL, NULL),
(8, 'bank_to_supplier', 'bank', 'supplier', 21820590, '', '2025-07-02 10:50:16.250706', 2, NULL, 1),
(9, 'bank_to_supplier', 'bank', 'supplier', 474155, '', '2025-07-02 10:50:43.582951', 2, NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `finance_expensemodel`
--

CREATE TABLE `finance_expensemodel` (
  `id` bigint NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `remark` longtext COLLATE utf8mb4_unicode_ci,
  `date` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `type_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `finance_expensemodel`
--

INSERT INTO `finance_expensemodel` (`id`, `amount`, `remark`, `date`, `created_at`, `created_by_id`, `type_id`) VALUES
(1, 50000.00, 'Kuja Salary for the month of May', '2025-06-29', '2025-06-29 10:54:59.477393', 2, 2),
(2, 3900.00, 'on 27/6/25', '2025-07-03', '2025-07-03 15:42:22.958166', 3, 3),
(3, 2400.00, 'Tp to madam\'s house', '2025-07-03', '2025-07-03 15:44:28.915135', 3, 8),
(4, 8000.00, 'part payment on 28/6/25', '2025-07-03', '2025-07-03 15:46:19.601784', 3, 3);

-- --------------------------------------------------------

--
-- Table structure for table `finance_expensetypemodel`
--

CREATE TABLE `finance_expensetypemodel` (
  `id` bigint NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `finance_expensetypemodel`
--

INSERT INTO `finance_expensetypemodel` (`id`, `name`, `description`, `created_at`) VALUES
(1, 'Salary', 'Monthly Salary paid to workers', '2025-06-29 10:46:41.858822'),
(2, 'Kuja Salary', 'Monthly Payment to Kuja Clerk', '2025-06-29 10:47:26.670514'),
(3, 'Loading & Offloading', 'Commission paid to offloaders, set at 4 naira per case, and 8 naira per case for long trucks', '2025-06-29 10:48:38.100645'),
(4, 'Diesel', 'Diesel for the big Truck', '2025-06-29 10:49:24.681393'),
(5, 'Fuel', 'Fuel money for the small Truck', '2025-06-29 10:49:56.540881'),
(6, 'Vehicle Repair and Maintenance', 'Servicing and mechanical works', '2025-06-29 10:50:59.312567'),
(7, 'Office Supplies', 'Staionaries and Books', '2025-06-29 10:51:28.512410'),
(8, 'Transport Fare', 'Weekly Transport allowance to workers', '2025-06-29 10:52:06.996743'),
(9, 'Yearly Bonus/Housing Allowance', 'Yearly one-off payment to staff based on the overall performance of the Business.', '2025-06-29 10:53:17.438307'),
(10, 'Withdrawal', 'Directors\' withdrawal from the business to meet up with contingencies.', '2025-06-29 10:54:15.197102');

-- --------------------------------------------------------

--
-- Table structure for table `finance_staffbonusmodel`
--

CREATE TABLE `finance_staffbonusmodel` (
  `id` bigint NOT NULL,
  `bonus` decimal(10,2) NOT NULL,
  `note` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `date` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `staff_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `finance_staffdeductionmodel`
--

CREATE TABLE `finance_staffdeductionmodel` (
  `id` bigint NOT NULL,
  `deduction` decimal(10,2) NOT NULL,
  `note` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `date` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `staff_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `finance_staffsalaryhistorymodel`
--

CREATE TABLE `finance_staffsalaryhistorymodel` (
  `id` bigint NOT NULL,
  `old_salary` decimal(10,2) NOT NULL,
  `new_salary` decimal(10,2) NOT NULL,
  `change_date` datetime(6) NOT NULL,
  `staff_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `finance_staffsalarymodel`
--

CREATE TABLE `finance_staffsalarymodel` (
  `id` bigint NOT NULL,
  `salary` decimal(10,2) NOT NULL,
  `account_name` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `account_number` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `bank` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_by_id` int DEFAULT NULL,
  `staff_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `finance_staffsalarymodel`
--

INSERT INTO `finance_staffsalarymodel` (`id`, `salary`, `account_name`, `account_number`, `bank`, `created_by_id`, `staff_id`) VALUES
(1, 0.00, NULL, NULL, NULL, NULL, 1),
(2, 0.00, NULL, NULL, NULL, NULL, 2),
(3, 0.00, NULL, NULL, NULL, NULL, 3),
(4, 0.00, NULL, NULL, NULL, NULL, 4),
(5, 0.00, NULL, NULL, NULL, NULL, 5),
(6, 0.00, NULL, NULL, NULL, NULL, 6);

-- --------------------------------------------------------

--
-- Table structure for table `finance_staffsalarypaymentmodel`
--

CREATE TABLE `finance_staffsalarypaymentmodel` (
  `id` bigint NOT NULL,
  `salary` decimal(10,2) NOT NULL,
  `bonus` decimal(10,2) NOT NULL,
  `deduction` decimal(10,2) NOT NULL,
  `total_payment` decimal(10,2) NOT NULL,
  `payment_date` datetime(6) NOT NULL,
  `month` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `staff_id` bigint NOT NULL,
  `target_bonus` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `finance_staffsalarysummarymodel`
--

CREATE TABLE `finance_staffsalarysummarymodel` (
  `id` bigint NOT NULL,
  `total_staff` int UNSIGNED NOT NULL,
  `total_bonus` decimal(10,2) NOT NULL,
  `total_deduction` decimal(10,2) NOT NULL,
  `total_payment` decimal(10,2) NOT NULL,
  `month` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `payment_source` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `human_resource_staffmodel`
--

CREATE TABLE `human_resource_staffmodel` (
  `id` bigint NOT NULL,
  `full_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mobile` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `create_account` tinyint(1) NOT NULL,
  `is_driver` tinyint(1) NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `group_id` int DEFAULT NULL,
  `crate_target_for_bonus` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `human_resource_staffmodel`
--

INSERT INTO `human_resource_staffmodel` (`id`, `full_name`, `image`, `mobile`, `address`, `email`, `status`, `created_at`, `updated_at`, `create_account`, `is_driver`, `created_by_id`, `group_id`, `crate_target_for_bonus`) VALUES
(1, 'Mrs Nnenna', '', '+2348138319994', NULL, NULL, 'active', '2025-06-26 13:20:04.244411', '2025-06-26 13:22:32.470654', 0, 0, NULL, 1, NULL),
(2, 'adekanbi yetunde', '', '+2348063530321', NULL, NULL, 'active', '2025-06-26 13:50:06.297570', '2025-06-26 13:50:06.297599', 0, 0, NULL, 2, NULL),
(3, 'onoja esther', '', '+2348144156654', NULL, NULL, 'active', '2025-06-26 13:58:14.302069', '2025-06-26 13:58:14.302106', 0, 0, NULL, 3, NULL),
(4, 'kenneth Erita', '', '+2348034360072', NULL, NULL, 'active', '2025-06-26 14:06:36.641441', '2025-06-26 14:06:36.641471', 0, 1, NULL, 4, 4000),
(5, 'eliagwu bernard', '', '+2348023216289', NULL, NULL, 'active', '2025-06-26 14:08:29.227405', '2025-06-26 14:08:29.227430', 0, 1, NULL, 4, 2500),
(6, 'etim paul enefiok', '', '+2349033392876', NULL, NULL, 'active', '2025-06-26 14:09:48.020161', '2025-06-26 14:09:48.020194', 0, 0, NULL, 5, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `human_resource_staffprofilemodel`
--

CREATE TABLE `human_resource_staffprofilemodel` (
  `id` bigint NOT NULL,
  `default_password` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `staff_id` bigint DEFAULT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `human_resource_staffprofilemodel`
--

INSERT INTO `human_resource_staffprofilemodel` (`id`, `default_password`, `staff_id`, `user_id`) VALUES
(1, 'cherylchisom', 1, 2),
(2, 'THL3xGjr', 2, 3),
(3, 'iFGYlSEE', 3, 4);

-- --------------------------------------------------------

--
-- Table structure for table `human_resource_staffwalletmodel`
--

CREATE TABLE `human_resource_staffwalletmodel` (
  `id` bigint NOT NULL,
  `balance` double NOT NULL,
  `staff_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `human_resource_staffwalletmodel`
--

INSERT INTO `human_resource_staffwalletmodel` (`id`, `balance`, `staff_id`) VALUES
(1, 0, 1),
(2, 0, 2),
(3, 0, 3),
(4, 360000, 4),
(5, 0, 5),
(6, 0, 6);

-- --------------------------------------------------------

--
-- Table structure for table `inventory_categorymodel`
--

CREATE TABLE `inventory_categorymodel` (
  `id` bigint NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `number_of_empty` double NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `inventory_categorymodel`
--

INSERT INTO `inventory_categorymodel` (`id`, `name`, `number_of_empty`, `created_at`, `updated_at`) VALUES
(1, 'NBL', 2003, '2025-06-28 06:46:58.370140', '2025-07-02 11:08:54.993962'),
(2, 'IBL', 1108, '2025-06-28 06:48:09.157928', '2025-06-28 06:48:09.157958');

-- --------------------------------------------------------

--
-- Table structure for table `inventory_emptyadjustmentmodel`
--

CREATE TABLE `inventory_emptyadjustmentmodel` (
  `id` bigint NOT NULL,
  `adjustment_type` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `reason` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `amount` int NOT NULL,
  `comment` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `category_id` bigint NOT NULL,
  `created_by_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inventory_pricehistorymodel`
--

CREATE TABLE `inventory_pricehistorymodel` (
  `id` bigint NOT NULL,
  `old_price` decimal(10,2) NOT NULL,
  `new_price` decimal(10,2) NOT NULL,
  `change_date` datetime(6) NOT NULL,
  `product_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inventory_productmodel`
--

CREATE TABLE `inventory_productmodel` (
  `id` bigint NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `selling_price` decimal(10,2) NOT NULL,
  `quantity` int NOT NULL,
  `reorder_level` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `category_id` bigint NOT NULL,
  `last_cost_price` decimal(10,2) DEFAULT NULL,
  `updated_by_id` int DEFAULT NULL,
  `initial_quantity` int NOT NULL,
  `initial_quantity_left` int NOT NULL,
  `type` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `inventory_productmodel`
--

INSERT INTO `inventory_productmodel` (`id`, `name`, `selling_price`, `quantity`, `reorder_level`, `created_at`, `updated_at`, `category_id`, `last_cost_price`, `updated_by_id`, `initial_quantity`, `initial_quantity_left`, `type`) VALUES
(1, 'Goldberg', 9055.00, 174, 100, '2025-06-29 10:09:34.916948', '2025-06-29 10:09:34.927268', 1, 8720.00, 2, 234, 174, 'bottle'),
(2, 'Life', 9055.00, 666, 100, '2025-06-29 10:10:14.882260', '2025-06-29 10:10:14.889523', 1, 8720.00, 2, 721, 666, 'bottle'),
(3, 'Legend 60cl', 11020.00, 1, 100, '2025-06-29 10:11:18.764938', '2025-06-29 10:11:18.794109', 1, 10475.00, 2, 20, 1, 'bottle'),
(4, 'Legend 45cl', 15230.00, 35, 100, '2025-06-29 10:12:38.016886', '2025-06-29 10:12:38.025565', 1, 10475.00, 2, 35, 35, 'bottle'),
(5, 'Heineken 60cl', 11915.00, 270, 100, '2025-06-29 10:14:00.398879', '2025-06-29 10:14:00.434538', 1, 11350.00, 2, 350, 270, 'bottle'),
(6, 'Desperado', 16880.00, 42, 100, '2025-06-29 10:14:48.320812', '2025-06-29 10:14:48.330414', 1, 16030.00, 2, 73, 42, 'bottle'),
(7, 'Tiger', 15055.00, 322, 100, '2025-06-29 10:15:46.697239', '2025-06-29 10:15:46.703328', 1, 14450.00, 2, 325, 322, 'bottle'),
(8, 'Amstel', 12655.00, 153, 100, '2025-06-29 10:18:27.349087', '2025-06-29 10:18:27.356421', 1, 12065.00, 2, 247, 153, 'bottle'),
(9, 'Maltina', 12655.00, 47, 100, '2025-06-29 10:19:15.621569', '2025-06-29 10:19:15.629813', 1, 12065.00, 2, 57, 47, 'bottle'),
(10, 'Gulder', 10825.00, 329, 100, '2025-06-29 10:23:25.638484', '2025-06-29 10:23:25.646036', 1, 10285.00, 2, 347, 329, 'bottle'),
(11, 'Star', 10210.00, 148, 100, '2025-06-29 10:25:39.664764', '2025-06-29 10:25:39.696237', 1, 9800.00, 2, 153, 148, 'bottle'),
(12, 'Radler', 12315.00, 162, 100, '2025-06-29 10:28:33.109341', '2025-06-29 10:28:33.115819', 1, 11795.00, 2, 167, 162, 'bottle'),
(13, 'Goldberg Black 45cl', 12610.00, 1527, 100, '2025-06-29 10:30:24.025895', '2025-06-29 10:30:24.033551', 1, 12035.00, 2, 53, 0, 'bottle'),
(14, 'Fayrouz', 8825.00, 22, 100, '2025-06-29 10:31:21.162997', '2025-06-29 10:31:21.169034', 1, 8490.00, 2, 27, 22, 'bottle'),
(15, '\"33\"', 9055.00, 0, 100, '2025-06-29 10:32:12.644458', '2025-06-29 10:32:12.645927', 1, 8720.00, 2, 0, 0, 'bottle'),
(16, 'Trophy', 8870.00, 2663, 100, '2025-06-29 10:34:11.357747', '2025-06-29 10:34:11.365821', 2, 8550.00, 2, 2756, 2663, 'bottle'),
(17, 'Hero', 8870.00, 247, 100, '2025-06-29 10:34:40.047573', '2025-06-29 10:34:40.053920', 2, 8550.00, 2, 362, 247, 'bottle'),
(18, 'Trophy Stout', 9300.00, 216, 100, '2025-06-29 10:35:41.043337', '2025-06-29 10:35:41.050895', 2, 8800.00, 2, 222, 216, 'bottle'),
(19, 'Castle Lite', 9250.00, 829, 100, '2025-06-29 10:36:49.634533', '2025-06-29 10:36:49.644834', 2, 8830.00, 2, 934, 829, 'bottle'),
(20, 'Budweiser', 9450.00, 867, 100, '2025-06-29 10:37:32.095515', '2025-06-29 10:37:32.103800', 2, 9050.00, 2, 882, 867, 'bottle'),
(21, 'Red Bull', 28500.00, 10, 100, '2025-06-29 10:40:01.522944', '2025-06-29 10:40:01.530444', 2, 28000.00, 2, 10, 10, 'bottle'),
(22, 'Legend Twist', 14720.00, 1, 100, '2025-06-29 10:41:10.911470', '2025-06-29 10:41:10.918176', 1, 13810.00, 2, 2, 1, 'bottle'),
(23, 'Star Lite', 9855.00, 35, 100, '2025-06-29 10:42:30.522998', '2025-06-29 10:42:30.530773', 1, 9255.00, 2, 40, 35, 'bottle'),
(24, 'Amstel Can', 13355.00, 79, 100, '2025-06-29 10:43:35.728342', '2025-07-01 16:17:13.241906', 1, 12815.00, 2, 142, 42, 'can'),
(25, 'Beta Malt Can', 10990.00, 389, 100, '2025-06-29 10:44:28.373636', '2025-07-01 16:17:29.762650', 2, 10550.00, 2, 399, 389, 'can');

-- --------------------------------------------------------

--
-- Table structure for table `inventory_stockinmodel`
--

CREATE TABLE `inventory_stockinmodel` (
  `id` bigint NOT NULL,
  `quantity_added` decimal(10,2) NOT NULL,
  `quantity_left` decimal(10,2) DEFAULT NULL,
  `quantity_sold` decimal(10,2) DEFAULT NULL,
  `quantity_stocked_out` decimal(10,2) DEFAULT NULL,
  `unit_cost_price` decimal(10,2) NOT NULL,
  `date_added` date NOT NULL,
  `status` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `product_id` bigint NOT NULL,
  `unit_selling_price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `inventory_stockinmodel`
--

INSERT INTO `inventory_stockinmodel` (`id`, `quantity_added`, `quantity_left`, `quantity_sold`, `quantity_stocked_out`, `unit_cost_price`, `date_added`, `status`, `created_at`, `created_by_id`, `product_id`, `unit_selling_price`) VALUES
(1, 234.00, 214.00, 20.00, 0.00, 8720.00, '2025-06-29', 'active', '2025-06-29 10:09:34.921282', 1, 1, 9055.00),
(2, 721.00, 721.00, 0.00, 0.00, 8720.00, '2025-06-29', 'active', '2025-06-29 10:10:14.885953', 1, 2, 9055.00),
(3, 20.00, 6.00, 14.00, 0.00, 10475.00, '2025-06-29', 'active', '2025-06-29 10:11:18.768557', 1, 3, 11020.00),
(4, 35.00, 35.00, 0.00, 0.00, 10475.00, '2025-06-29', 'active', '2025-06-29 10:12:38.021353', 1, 4, 15230.00),
(5, 350.00, 340.00, 10.00, 0.00, 11350.00, '2025-06-29', 'active', '2025-06-29 10:14:00.403380', 1, 5, 11915.00),
(6, 73.00, 73.00, 0.00, 0.00, 16030.00, '2025-06-29', 'active', '2025-06-29 10:14:48.324187', 1, 6, 16880.00),
(7, 325.00, 325.00, 0.00, 0.00, 14450.00, '2025-06-29', 'active', '2025-06-29 10:15:46.700491', 1, 7, 15055.00),
(8, 247.00, 195.00, 52.00, 0.00, 12065.00, '2025-06-29', 'active', '2025-06-29 10:18:27.352829', 1, 8, 12655.00),
(9, 57.00, 57.00, 0.00, 0.00, 12065.00, '2025-06-29', 'active', '2025-06-29 10:19:15.624932', 1, 9, 12655.00),
(10, 347.00, 337.00, 10.00, 0.00, 10285.00, '2025-06-29', 'active', '2025-06-29 10:23:25.642250', 1, 10, 10825.00),
(11, 153.00, 153.00, 0.00, 0.00, 9800.00, '2025-06-29', 'active', '2025-06-29 10:25:39.669308', 1, 11, 10210.00),
(12, 167.00, 167.00, 0.00, 0.00, 11795.00, '2025-06-29', 'active', '2025-06-29 10:28:33.112428', 1, 12, 12315.00),
(13, 53.00, 0.00, 53.00, 0.00, 12035.00, '2025-06-29', 'active', '2025-06-29 10:30:24.029829', 1, 13, 12610.00),
(14, 27.00, 22.00, 5.00, 0.00, 8490.00, '2025-06-29', 'active', '2025-06-29 10:31:21.166182', 1, 14, 8825.00),
(15, 2756.00, 2756.00, 0.00, 0.00, 8550.00, '2025-06-29', 'active', '2025-06-29 10:34:11.361919', 1, 16, 8870.00),
(16, 362.00, 262.00, 100.00, 0.00, 8550.00, '2025-06-29', 'active', '2025-06-29 10:34:40.051005', 1, 17, 8870.00),
(17, 222.00, 222.00, 0.00, 0.00, 8800.00, '2025-06-29', 'active', '2025-06-29 10:35:41.047339', 1, 18, 9300.00),
(18, 934.00, 909.00, 25.00, 0.00, 8830.00, '2025-06-29', 'active', '2025-06-29 10:36:49.639413', 1, 19, 9250.00),
(19, 882.00, 877.00, 5.00, 0.00, 9050.00, '2025-06-29', 'active', '2025-06-29 10:37:32.099941', 1, 20, 9450.00),
(20, 10.00, 10.00, 0.00, 0.00, 28000.00, '2025-06-29', 'active', '2025-06-29 10:40:01.526903', 1, 21, 28500.00),
(21, 2.00, 1.00, 1.00, 0.00, 13810.00, '2025-06-29', 'active', '2025-06-29 10:41:10.914969', 1, 22, 14720.00),
(22, 40.00, 35.00, 5.00, 0.00, 9255.00, '2025-06-29', 'active', '2025-06-29 10:42:30.526410', 1, 23, 9855.00),
(23, 142.00, 142.00, 0.00, 0.00, 12815.00, '2025-06-29', 'active', '2025-06-29 10:43:35.731732', 1, 24, 13355.00),
(24, 399.00, 399.00, 0.00, 0.00, 10550.00, '2025-06-29', 'active', '2025-06-29 10:44:28.377364', 1, 25, 10990.00),
(25, 1674.00, 1540.00, 134.00, 0.00, 12035.00, '2025-07-02', 'active', '2025-07-02 11:02:50.536909', 1, 13, 12610.00),
(26, 37.00, 37.00, 0.00, 0.00, 12815.00, '2025-07-02', 'active', '2025-07-02 11:08:54.963543', 1, 24, 13355.00);

-- --------------------------------------------------------

--
-- Table structure for table `inventory_stockinsummarymodel`
--

CREATE TABLE `inventory_stockinsummarymodel` (
  `id` bigint NOT NULL,
  `status` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `is_tampered` tinyint(1) NOT NULL,
  `empty` int NOT NULL,
  `supplier_id` bigint DEFAULT NULL,
  `total_quantity` int NOT NULL,
  `total_empty` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `inventory_stockinsummarymodel`
--

INSERT INTO `inventory_stockinsummarymodel` (`id`, `status`, `date`, `created_at`, `created_by_id`, `is_tampered`, `empty`, `supplier_id`, `total_quantity`, `total_empty`) VALUES
(1, 'confirmed', '2025-06-29', '2025-07-02 11:02:50.534573', 1, 0, 1456, 1, 1674, 1674),
(2, 'confirmed', '2025-07-01', '2025-07-02 11:08:54.961478', 1, 0, 0, 1, 37, 0);

-- --------------------------------------------------------

--
-- Table structure for table `inventory_stockinsummarymodel_products`
--

CREATE TABLE `inventory_stockinsummarymodel_products` (
  `id` bigint NOT NULL,
  `stockinsummarymodel_id` bigint NOT NULL,
  `stockinmodel_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `inventory_stockinsummarymodel_products`
--

INSERT INTO `inventory_stockinsummarymodel_products` (`id`, `stockinsummarymodel_id`, `stockinmodel_id`) VALUES
(1, 1, 25),
(2, 2, 26);

-- --------------------------------------------------------

--
-- Table structure for table `inventory_stockoutmodel`
--

CREATE TABLE `inventory_stockoutmodel` (
  `id` bigint NOT NULL,
  `quantity_removed` decimal(10,2) NOT NULL,
  `cost_of_removed_stock` decimal(10,2) DEFAULT NULL,
  `reason` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_removed` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `stock_id` bigint NOT NULL,
  `stock_out_empty` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inventory_suppliercashflowhistorymodel`
--

CREATE TABLE `inventory_suppliercashflowhistorymodel` (
  `id` bigint NOT NULL,
  `subject` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `initial_amount` double NOT NULL,
  `amount` double NOT NULL,
  `final_amount` double NOT NULL,
  `date` datetime(6) NOT NULL,
  `supplier_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inventory_suppliermodel`
--

CREATE TABLE `inventory_suppliermodel` (
  `id` bigint NOT NULL,
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `contact_person` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone_number` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `category_id` bigint NOT NULL,
  `balance` double NOT NULL,
  `initial_balance` double NOT NULL,
  `updated_by_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `inventory_suppliermodel`
--

INSERT INTO `inventory_suppliermodel` (`id`, `name`, `contact_person`, `phone_number`, `email`, `address`, `created_at`, `updated_at`, `category_id`, `balance`, `initial_balance`, `updated_by_id`) VALUES
(1, 'Nigerian Breweries', 'Anayo Anyaso', '08056198471', 'anayo.anyaso@heineken.com', NULL, '2025-06-28 06:54:17.278099', '2025-07-02 11:08:54.994657', 1, 1779990, 0, 2),
(2, 'International Breweries', 'Onyeka', '08068244019', 'creditupdate@ng.ab-inbev.com', NULL, '2025-06-28 07:10:05.052014', '2025-06-28 07:15:08.595404', 2, 686267, 0, 2);

-- --------------------------------------------------------

--
-- Table structure for table `sale_customercratedebtmodel`
--

CREATE TABLE `sale_customercratedebtmodel` (
  `id` bigint NOT NULL,
  `crate` decimal(10,2) NOT NULL,
  `category_id` bigint NOT NULL,
  `customer_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `sale_customercratedebtmodel`
--

INSERT INTO `sale_customercratedebtmodel` (`id`, `crate`, `category_id`, `customer_id`) VALUES
(1, 1.00, 1, 3),
(2, 3.00, 2, 5),
(3, 0.00, 2, 9),
(4, 0.00, 1, 9),
(5, 7.00, 2, 10),
(6, 79.00, 1, 10),
(7, 40.00, 1, 11),
(8, 1.00, 2, 12),
(9, 316.00, 1, 12),
(10, 67.00, 2, 13),
(11, 81.00, 1, 13),
(12, 7.00, 1, 14),
(13, 6.00, 2, 15),
(14, 2.00, 1, 15),
(15, 0.00, 1, 16),
(16, 1.00, 2, 3),
(17, 1.00, 2, 17),
(18, 1.00, 1, 7),
(19, 0.00, 1, 21),
(20, 5.00, 2, 21),
(21, 0.00, 2, 18),
(22, 0.00, 1, 22),
(23, 0.00, 1, 23),
(24, 31.00, 1, 26),
(25, 17.00, 2, 26);

-- --------------------------------------------------------

--
-- Table structure for table `sale_customercratereturnmodel`
--

CREATE TABLE `sale_customercratereturnmodel` (
  `id` bigint NOT NULL,
  `crates_returned` decimal(10,2) NOT NULL,
  `note` longtext COLLATE utf8mb4_unicode_ci,
  `created_at` datetime(6) NOT NULL,
  `category_id` bigint NOT NULL,
  `customer_id` bigint NOT NULL,
  `recorded_by_id` int DEFAULT NULL,
  `amount_paid` decimal(12,2) DEFAULT NULL,
  `driver_id` bigint DEFAULT NULL,
  `payment_method` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `return_method` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `sale_customercratereturnmodel`
--

INSERT INTO `sale_customercratereturnmodel` (`id`, `crates_returned`, `note`, `created_at`, `category_id`, `customer_id`, `recorded_by_id`, `amount_paid`, `driver_id`, `payment_method`, `return_method`) VALUES
(1, 70.00, 'returned on 28/6/25', '2025-06-30 11:23:54.090355', 1, 3, 3, NULL, NULL, NULL, 'empty'),
(2, 30.00, 'returned on 28/6/25', '2025-06-30 11:24:32.507368', 2, 3, 3, NULL, NULL, NULL, 'empty'),
(3, 79.00, '1 crate of amstel rejected on 28/6/25 (police cap)', '2025-06-30 13:01:26.870448', 1, 7, 3, NULL, NULL, NULL, 'empty'),
(4, 79.00, '1 crate of amstel rejected on 28/6/25 (police cap)', '2025-06-30 13:01:47.911318', 1, 7, 3, NULL, NULL, NULL, 'empty'),
(5, 100.00, '', '2025-07-02 12:45:31.880679', 1, 12, 3, NULL, NULL, NULL, 'empty'),
(6, 149.00, '', '2025-07-02 13:35:30.082006', 2, 5, 3, NULL, NULL, NULL, 'empty'),
(7, 1.00, 'he deposited 5 Nbl empties for d Ibl drinks he bought', '2025-07-02 14:00:55.400320', 1, 21, 3, 1000.00, NULL, 'cash', 'cash'),
(8, 113.00, '', '2025-07-02 14:10:46.550026', 1, 13, 3, NULL, NULL, NULL, 'empty'),
(9, 79.00, '', '2025-07-02 14:11:42.671275', 2, 13, 3, NULL, NULL, NULL, 'empty'),
(10, 5.00, '', '2025-07-03 14:02:53.033947', 1, 22, 3, NULL, NULL, NULL, 'empty'),
(11, 5.00, '', '2025-07-03 14:02:53.756300', 1, 22, 3, NULL, NULL, NULL, 'empty'),
(12, 2.00, '', '2025-07-03 14:04:18.632224', 1, 23, 3, NULL, NULL, NULL, 'empty'),
(13, 30.00, '', '2025-07-03 14:41:45.333146', 2, 18, 3, NULL, NULL, NULL, 'empty'),
(14, 75.00, '', '2025-07-03 14:44:39.475758', 1, 3, 3, NULL, NULL, NULL, 'empty'),
(15, 29.00, '', '2025-07-03 14:46:01.799044', 2, 3, 3, NULL, NULL, NULL, 'empty'),
(16, 30.00, '', '2025-07-03 14:47:14.613574', 2, 9, 3, NULL, NULL, NULL, 'empty'),
(17, 70.00, '', '2025-07-03 14:52:34.238426', 1, 9, 3, NULL, NULL, NULL, 'empty'),
(18, 255.00, '', '2025-07-03 15:24:28.624620', 1, 16, 3, NULL, NULL, NULL, 'empty'),
(19, 39.00, '', '2025-07-03 15:28:02.955533', 1, 7, 3, NULL, NULL, NULL, 'empty');

-- --------------------------------------------------------

--
-- Table structure for table `sale_customerdebtrepaymentmodel`
--

CREATE TABLE `sale_customerdebtrepaymentmodel` (
  `id` bigint NOT NULL,
  `amount_paid` decimal(10,2) NOT NULL,
  `payment_method` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `note` longtext COLLATE utf8mb4_unicode_ci,
  `created_at` datetime(6) NOT NULL,
  `customer_id` bigint NOT NULL,
  `recorded_by_id` int DEFAULT NULL,
  `driver_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `sale_customerdebtrepaymentmodel`
--

INSERT INTO `sale_customerdebtrepaymentmodel` (`id`, `amount_paid`, `payment_method`, `note`, `created_at`, `customer_id`, `recorded_by_id`, `driver_id`) VALUES
(1, 400000.00, 'bank', 'Complete payment for last order made', '2025-06-29 17:21:24.289282', 5, 2, NULL),
(2, 46250.00, 'cash', '', '2025-07-02 10:08:41.627706', 18, 3, NULL),
(3, 841500.00, 'bank', 'pd to T1 on 29/6/25', '2025-07-02 10:11:53.008286', 17, 3, NULL),
(4, 997750.00, 'bank', 'pd to T1 on 01/7/25', '2025-07-02 10:21:06.414894', 7, 3, NULL),
(5, 2473250.00, 'bank', '', '2025-07-02 12:23:25.719127', 12, 3, NULL),
(6, 309200.00, 'bank', '', '2025-07-02 12:35:14.103368', 19, 3, NULL),
(7, 138750.00, 'bank', 'pd on 30/6/25', '2025-07-02 12:39:26.819840', 18, 3, NULL),
(8, 1022000.00, 'bank', '', '2025-07-02 12:40:55.948879', 3, 3, NULL),
(9, 34690.00, 'cash', '', '2025-07-03 14:02:29.127743', 22, 3, NULL),
(10, 277500.00, 'bank', '', '2025-07-03 14:40:48.544719', 18, 3, NULL),
(11, 300000.00, 'driver', '', '2025-07-03 15:01:18.670952', 10, 3, 4),
(12, 60000.00, 'driver', '', '2025-07-03 15:05:08.615935', 20, 3, 4),
(13, 700000.00, 'bank', '', '2025-07-03 15:06:12.499906', 11, 3, NULL),
(14, 800000.00, 'bank', '', '2025-07-03 15:19:02.050113', 8, 3, NULL),
(15, 253100.00, 'bank', '', '2025-07-03 15:30:00.075695', 4, 3, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `sale_customermodel`
--

CREATE TABLE `sale_customermodel` (
  `id` bigint NOT NULL,
  `full_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `mobile` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `created_by_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `sale_customermodel`
--

INSERT INTO `sale_customermodel` (`id`, `full_name`, `mobile`, `address`, `email`, `status`, `created_at`, `updated_at`, `created_by_id`) VALUES
(1, 'adinya william', '08067811699', NULL, NULL, 'active', '2025-06-26 14:43:47.238597', '2025-06-26 14:43:47.238626', 3),
(2, 'nebo collins', '08030868086', NULL, NULL, 'active', '2025-06-26 14:45:21.273144', '2025-06-26 14:45:21.273177', 3),
(3, 'Chika Ugwu', '07068535551', 'One Man Village', NULL, 'active', '2025-06-29 11:07:58.665264', '2025-06-29 11:07:58.665291', 2),
(4, 'Sule David', '08107694886', 'Abacha Road', NULL, 'active', '2025-06-29 11:10:29.652861', '2025-06-29 11:10:29.652894', 2),
(5, 'Success Ojonugwa', '08068882346', 'Abacha Road', NULL, 'active', '2025-06-29 11:12:43.462528', '2025-06-29 11:12:43.462559', 2),
(6, 'Shop Staff', '09033392876', 'Abacha Road', NULL, 'active', '2025-06-29 11:15:13.092917', '2025-06-29 11:15:13.092946', 2),
(7, 'Simple', '08032934368', 'Abacha Road', NULL, 'active', '2025-06-29 11:16:49.385549', '2025-06-29 11:16:49.385577', 2),
(8, 'Mike Aso', '09049916400', 'Aso Maraba', NULL, 'active', '2025-06-29 11:18:35.420976', '2025-06-29 11:18:35.421004', 2),
(9, 'KC Gwandara', '07034827634', 'Gwandara, Masaka', NULL, 'active', '2025-06-29 11:20:01.461103', '2025-06-29 11:20:01.461131', 2),
(10, 'Ken Kabayi', '00000', 'Kabayi. Maraba', NULL, 'active', '2025-06-29 11:23:20.614389', '2025-06-29 11:23:20.614419', 2),
(11, 'Me & U', '08084001049', 'Aso, Maraba', NULL, 'active', '2025-06-29 11:40:46.181665', '2025-06-29 11:40:46.181692', 2),
(12, 'Chinedu Ugwuoke', '07037388812', 'Aso Maraba', NULL, 'active', '2025-06-29 11:45:12.268040', '2025-06-29 11:45:12.268071', 2),
(13, 'Over The Bar', '08136687630', 'Aso Maraba', NULL, 'active', '2025-06-29 11:47:03.733228', '2025-06-29 11:47:03.733263', 2),
(14, 'Chimaco', '08166936134', 'Maraba', NULL, 'active', '2025-06-29 11:48:35.799174', '2025-06-29 11:48:35.799203', 2),
(15, 'Kenneth Erita', '08034360072', 'One Man Village', NULL, 'active', '2025-06-29 11:52:43.070001', '2025-06-29 11:52:43.070027', 2),
(16, 'Pascal Ojobor', '08039116644', 'Masaka', NULL, 'active', '2025-06-29 11:54:24.418891', '2025-06-29 11:54:24.418917', 2),
(17, 'orlando', '08124542009', 'gwandara,', NULL, 'active', '2025-06-30 12:34:53.585721', '2025-06-30 12:34:53.585749', 3),
(18, 'Abel (bernard)', '09063736466', NULL, NULL, 'active', '2025-07-01 16:45:42.133662', '2025-07-01 16:45:42.133694', 3),
(19, 'Sylvester Gomes', '08131952338', NULL, NULL, 'active', '2025-07-02 10:34:55.332043', '2025-07-02 10:34:55.332070', 3),
(20, 'mama chimanda', '08000000000', 'aso', NULL, 'active', '2025-07-02 11:12:43.337425', '2025-07-02 11:12:43.337453', 3),
(21, 'oscar lavida', '08100000000', NULL, NULL, 'active', '2025-07-02 13:53:43.433093', '2025-07-02 13:53:43.433123', 3),
(22, 'madam chioma', '07060905299', NULL, NULL, 'active', '2025-07-03 13:53:26.302009', '2025-07-03 13:53:26.302042', 3),
(23, 'bernard eliagwu', '08023216289', NULL, NULL, 'active', '2025-07-03 13:59:18.601605', '2025-07-03 13:59:18.601648', 3),
(24, 'walk in customer', '09000000000', NULL, NULL, 'active', '2025-07-03 14:27:19.976230', '2025-07-03 14:27:19.976269', 3),
(25, 'madam uju', '08069257007', NULL, NULL, 'active', '2025-07-03 14:35:42.821034', '2025-07-03 14:35:42.821061', 3),
(26, 'kenneth obinna', '08104130527', 'aso', NULL, 'active', '2025-07-04 09:02:38.925083', '2025-07-04 09:02:38.925108', 3),
(27, 'barrister godwin', '08142610393', NULL, NULL, 'active', '2025-07-04 12:40:52.091066', '2025-07-04 12:40:52.091100', 3);

-- --------------------------------------------------------

--
-- Table structure for table `sale_customerwalletmodel`
--

CREATE TABLE `sale_customerwalletmodel` (
  `id` bigint NOT NULL,
  `initial_debt` decimal(10,2) NOT NULL,
  `initial_debt_payment` decimal(10,2) NOT NULL,
  `balance` decimal(10,2) NOT NULL,
  `customer_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `sale_customerwalletmodel`
--

INSERT INTO `sale_customerwalletmodel` (`id`, `initial_debt`, `initial_debt_payment`, `balance`, `customer_id`) VALUES
(1, 114000.00, 0.00, 114000.00, 1),
(2, 36500.00, 0.00, 36500.00, 2),
(3, 83625.00, 0.00, 915175.00, 3),
(4, 18600.00, 0.00, 18600.00, 4),
(5, 400000.00, 0.00, 944900.00, 5),
(6, 77624.00, 0.00, 77624.00, 6),
(7, 1700.00, 0.00, 376750.00, 7),
(8, 1591910.00, 0.00, 791910.00, 8),
(9, 1400.00, 0.00, 1400.00, 9),
(10, 602525.00, 0.00, 302525.00, 10),
(11, 830200.00, 0.00, 130200.00, 11),
(12, 0.00, 0.00, 0.00, 12),
(13, 0.00, 0.00, 240725.00, 13),
(14, 0.00, 0.00, 0.00, 14),
(15, 157380.00, 0.00, 157380.00, 15),
(16, 0.00, 0.00, 337600.00, 16),
(17, 0.00, 0.00, 8500.00, 17),
(18, 0.00, 0.00, 0.00, 18),
(19, 0.00, 0.00, 300.00, 19),
(20, 0.00, 0.00, 0.00, 20),
(21, 0.00, 0.00, 0.00, 21),
(22, 0.00, 0.00, 0.00, 22),
(23, 0.00, 0.00, 25310.00, 23),
(24, 0.00, 0.00, 0.00, 24),
(25, 0.00, 0.00, 105000.00, 25),
(26, 0.00, 0.00, 493850.00, 26),
(27, 0.00, 0.00, 0.00, 27);

-- --------------------------------------------------------

--
-- Table structure for table `sale_returnmodel`
--

CREATE TABLE `sale_returnmodel` (
  `id` bigint NOT NULL,
  `quantity_returned` decimal(10,2) NOT NULL,
  `return_date` datetime(6) NOT NULL,
  `reason` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `refund_amount` decimal(10,2) NOT NULL,
  `notes` longtext COLLATE utf8mb4_unicode_ci,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `sale_item_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `sale_salecategoryempty`
--

CREATE TABLE `sale_salecategoryempty` (
  `id` bigint NOT NULL,
  `empty_expected` decimal(10,2) NOT NULL,
  `empty_brought` decimal(10,2) NOT NULL,
  `empty_owed` decimal(10,2) NOT NULL,
  `category_id` bigint NOT NULL,
  `sale_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `sale_salecategoryempty`
--

INSERT INTO `sale_salecategoryempty` (`id`, `empty_expected`, `empty_brought`, `empty_owed`, `category_id`, `sale_id`) VALUES
(1, 70.00, 0.00, 70.00, 1, 1),
(2, 30.00, 0.00, 30.00, 2, 1),
(3, 100.00, 99.00, 1.00, 2, 2),
(4, 7.00, 7.00, 0.00, 1, 3),
(5, 80.00, 0.00, 80.00, 1, 4),
(6, 20.00, 20.00, 0.00, 2, 5),
(7, 105.00, 0.00, 105.00, 2, 6),
(8, 10.00, 10.00, 0.00, 1, 7),
(9, 20.00, 20.00, 0.00, 2, 7),
(10, 200.00, 200.00, 0.00, 1, 9),
(11, 13.00, 12.00, 1.00, 1, 10),
(12, 5.00, 0.00, 5.00, 2, 10),
(13, 17.00, 17.00, 0.00, 1, 11),
(14, 5.00, 5.00, 0.00, 2, 11),
(15, 75.00, 0.00, 75.00, 1, 12),
(16, 30.00, 0.00, 30.00, 2, 12),
(17, 20.00, 20.00, 0.00, 1, 13),
(18, 40.00, 0.00, 40.00, 1, 14),
(19, 30.00, 0.00, 30.00, 2, 15),
(20, 20.00, 20.00, 0.00, 1, 16),
(21, 5.00, 0.00, 5.00, 1, 17),
(22, 2.00, 0.00, 2.00, 1, 18),
(23, 1.00, 1.00, 0.00, 1, 19),
(24, 1.00, 1.00, 0.00, 2, 19),
(25, 1.00, 1.00, 0.00, 2, 21),
(26, 31.00, 0.00, 31.00, 1, 22),
(27, 17.00, 0.00, 17.00, 2, 22);

-- --------------------------------------------------------

--
-- Table structure for table `sale_saleitemmodel`
--

CREATE TABLE `sale_saleitemmodel` (
  `id` bigint NOT NULL,
  `quantity` decimal(10,2) NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `cost_price` decimal(10,2) NOT NULL,
  `profit` decimal(10,2) NOT NULL,
  `product_id` bigint NOT NULL,
  `sale_id` bigint NOT NULL,
  `stock_id` bigint DEFAULT NULL,
  `total_discount` decimal(10,2) NOT NULL,
  `unit_discount` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `sale_saleitemmodel`
--

INSERT INTO `sale_saleitemmodel` (`id`, `quantity`, `unit_price`, `subtotal`, `cost_price`, `profit`, `product_id`, `sale_id`, `stock_id`, `total_discount`, `unit_discount`) VALUES
(1, 20.00, 9055.00, 181100.00, 8720.00, 6700.00, 1, 1, NULL, 0.00, 0.00),
(2, 10.00, 12655.00, 126550.00, 12065.00, 5900.00, 8, 1, NULL, 0.00, 0.00),
(3, 10.00, 11020.00, 110200.00, 10475.00, 5450.00, 3, 1, NULL, 0.00, 0.00),
(4, 10.00, 11915.00, 119150.00, 11350.00, 5650.00, 5, 1, NULL, 0.00, 0.00),
(5, 10.00, 10825.00, 108250.00, 10285.00, 5400.00, 10, 1, NULL, 0.00, 0.00),
(6, 5.00, 8825.00, 44125.00, 8490.00, 1675.00, 14, 1, NULL, 0.00, 0.00),
(7, 5.00, 10825.00, 54125.00, 9255.00, 7850.00, 23, 1, NULL, 0.00, 0.00),
(8, 25.00, 9250.00, 231250.00, 8830.00, 10500.00, 19, 1, NULL, 0.00, 0.00),
(9, 5.00, 9450.00, 47250.00, 9050.00, 2000.00, 20, 1, NULL, 0.00, 0.00),
(10, 100.00, 8500.00, 850000.00, 8550.00, -5000.00, 17, 2, NULL, 37000.00, 370.00),
(11, 4.00, 11020.00, 44080.00, 10475.00, 2180.00, 3, 3, NULL, 0.00, 0.00),
(12, 2.00, 12655.00, 25310.00, 12065.00, 1180.00, 8, 3, NULL, 0.00, 0.00),
(13, 1.00, 14720.00, 14720.00, 13810.00, 910.00, 22, 3, NULL, 0.00, 0.00),
(14, 40.00, 12610.00, 504400.00, 12035.00, 23000.00, 13, 4, NULL, 0.00, 0.00),
(15, 40.00, 12655.00, 506200.00, 12065.00, 23600.00, 8, 4, NULL, 0.00, 0.00),
(16, 20.00, 9250.00, 185000.00, 8830.00, 8400.00, 19, 5, NULL, 0.00, 0.00),
(17, 70.00, 8870.00, 620900.00, 8550.00, 22400.00, 16, 6, NULL, 0.00, 0.00),
(18, 30.00, 9250.00, 277500.00, 8830.00, 12600.00, 19, 6, NULL, 0.00, 0.00),
(19, 5.00, 9300.00, 46500.00, 8800.00, 2500.00, 18, 6, NULL, 0.00, 0.00),
(20, 10.00, 8500.00, 85000.00, 8550.00, -500.00, 16, 7, NULL, 3700.00, 370.00),
(21, 10.00, 8500.00, 85000.00, 8550.00, -500.00, 17, 7, NULL, 3700.00, 370.00),
(22, 5.00, 11020.00, 55100.00, 10475.00, 2725.00, 3, 7, NULL, 0.00, 0.00),
(23, 5.00, 16880.00, 84400.00, 16030.00, 4250.00, 6, 7, NULL, 0.00, 0.00),
(24, 100.00, 11600.00, 1160000.00, 12815.00, -121500.00, 24, 8, NULL, 175500.00, 1755.00),
(25, 150.00, 12540.00, 1881000.00, 12035.00, 75750.00, 13, 9, NULL, 10500.00, 70.00),
(26, 50.00, 11845.00, 592250.00, 11350.00, 24750.00, 5, 9, NULL, 3500.00, 70.00),
(27, 7.00, 11915.00, 83405.00, 11350.00, 3955.00, 5, 10, NULL, 0.00, 0.00),
(28, 5.00, 9055.00, 45275.00, 8720.00, 1675.00, 2, 10, NULL, 0.00, 0.00),
(29, 4.00, 9450.00, 37800.00, 9050.00, 1600.00, 20, 10, NULL, 0.00, 0.00),
(30, 1.00, 16880.00, 16880.00, 16030.00, 850.00, 6, 10, NULL, 0.00, 0.00),
(31, 1.00, 9300.00, 9300.00, 8800.00, 500.00, 18, 10, NULL, 0.00, 0.00),
(32, 10.00, 12655.00, 126550.00, 12065.00, 5900.00, 9, 11, NULL, 0.00, 0.00),
(33, 5.00, 9450.00, 47250.00, 9050.00, 2000.00, 20, 11, NULL, 0.00, 0.00),
(34, 2.00, 10825.00, 21650.00, 10285.00, 1080.00, 10, 11, NULL, 0.00, 0.00),
(35, 5.00, 9055.00, 45275.00, 8720.00, 1675.00, 2, 11, NULL, 0.00, 0.00),
(36, 30.00, 9055.00, 271650.00, 8720.00, 10050.00, 1, 12, NULL, 0.00, 0.00),
(37, 10.00, 11915.00, 119150.00, 11350.00, 5650.00, 5, 12, NULL, 0.00, 0.00),
(38, 10.00, 12655.00, 126550.00, 12065.00, 5900.00, 8, 12, NULL, 0.00, 0.00),
(39, 5.00, 16880.00, 84400.00, 16030.00, 4250.00, 6, 12, NULL, 0.00, 0.00),
(40, 5.00, 12315.00, 61575.00, 11795.00, 2600.00, 12, 12, NULL, 0.00, 0.00),
(41, 5.00, 10210.00, 51050.00, 9800.00, 2050.00, 11, 12, NULL, 0.00, 0.00),
(42, 5.00, 12610.00, 63050.00, 12035.00, 2875.00, 13, 12, NULL, 0.00, 0.00),
(43, 5.00, 10825.00, 54125.00, 10285.00, 2700.00, 10, 12, NULL, 0.00, 0.00),
(44, 20.00, 12655.00, 253100.00, 12065.00, 11800.00, 8, 13, NULL, 0.00, 0.00),
(45, 40.00, 9055.00, 362200.00, 8720.00, 13400.00, 2, 14, NULL, 0.00, 0.00),
(46, 30.00, 9250.00, 277500.00, 8830.00, 12600.00, 19, 15, NULL, 0.00, 0.00),
(47, 20.00, 16880.00, 337600.00, 16030.00, 17000.00, 6, 16, NULL, 0.00, 0.00),
(48, 5.00, 12655.00, 63275.00, 12065.00, 2950.00, 8, 17, NULL, 0.00, 0.00),
(49, 2.00, 12655.00, 25310.00, 12065.00, 1180.00, 8, 18, NULL, 0.00, 0.00),
(50, 1.00, 9450.00, 9450.00, 9050.00, 400.00, 20, 19, NULL, 0.00, 0.00),
(51, 1.00, 10825.00, 10825.00, 10285.00, 540.00, 10, 19, NULL, 0.00, 0.00),
(52, 10.00, 10500.00, 105000.00, 10550.00, -500.00, 25, 20, NULL, 4900.00, 490.00),
(53, 1.00, 8870.00, 8870.00, 8550.00, 320.00, 16, 21, NULL, 0.00, 0.00),
(54, 12.00, 8870.00, 106440.00, 8550.00, 3840.00, 16, 22, NULL, 0.00, 0.00),
(55, 10.00, 9055.00, 90550.00, 8720.00, 3350.00, 1, 22, NULL, 0.00, 0.00),
(56, 5.00, 12610.00, 63050.00, 12035.00, 2875.00, 13, 22, NULL, 0.00, 0.00),
(57, 5.00, 12655.00, 63275.00, 12065.00, 2950.00, 8, 22, NULL, 0.00, 0.00),
(58, 5.00, 9055.00, 45275.00, 8720.00, 1675.00, 2, 22, NULL, 0.00, 0.00),
(59, 5.00, 8870.00, 44350.00, 8550.00, 1600.00, 17, 22, NULL, 0.00, 0.00),
(60, 3.00, 11915.00, 35745.00, 11350.00, 1695.00, 5, 22, NULL, 0.00, 0.00),
(61, 3.00, 15055.00, 45165.00, 14450.00, 1815.00, 7, 22, NULL, 0.00, 0.00);

-- --------------------------------------------------------

--
-- Table structure for table `sale_salemodel`
--

CREATE TABLE `sale_salemodel` (
  `id` bigint NOT NULL,
  `transaction_id` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `sale_date` datetime(6) NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `customer_id` bigint DEFAULT NULL,
  `delivery_status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `driver_id` bigint DEFAULT NULL,
  `payment_status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `total_amount_left` decimal(10,2) NOT NULL,
  `total_amount_paid` decimal(10,2) NOT NULL,
  `payment_destination` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `total_discount` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `sale_salemodel`
--

INSERT INTO `sale_salemodel` (`id`, `transaction_id`, `sale_date`, `total_amount`, `status`, `created_at`, `updated_at`, `created_by_id`, `customer_id`, `delivery_status`, `driver_id`, `payment_status`, `total_amount_left`, `total_amount_paid`, `payment_destination`, `total_discount`) VALUES
(1, 'SALE-20250629120257592', '2025-06-27 00:00:00.000000', 1022000.00, 'confirmed', '2025-06-29 12:02:57.592811', '2025-06-29 12:02:57.642085', 2, 3, 'driver', 5, 'none', 1022000.00, 0.00, 'bank', 0.00),
(2, 'SALE-20250630123703382', '2025-06-28 00:00:00.000000', 850000.00, 'confirmed', '2025-06-30 12:37:03.382544', '2025-06-30 12:37:03.394891', 3, 17, 'driver', 5, 'none', 850000.00, 0.00, 'bank', 37000.00),
(3, 'SALE-20250630124630004', '2025-06-28 00:00:00.000000', 84110.00, 'confirmed', '2025-06-30 12:46:30.004878', '2025-06-30 12:46:30.024423', 3, 4, 'self', NULL, 'complete', 0.00, 84110.00, 'bank', 0.00),
(4, 'SALE-20250630125854474', '2025-06-28 00:00:00.000000', 1010600.00, 'confirmed', '2025-06-30 12:58:54.474877', '2025-06-30 12:58:54.488964', 3, 7, 'driver', 5, 'none', 1010600.00, 0.00, 'bank', 0.00),
(5, 'SALE-20250702100704965', '2025-06-28 00:00:00.000000', 185000.00, 'confirmed', '2025-07-02 10:07:04.966177', '2025-07-02 10:07:04.978514', 3, 18, 'driver', 5, 'none', 185000.00, 0.00, 'driver', 0.00),
(6, 'SALE-20250702103243828', '2025-06-30 00:00:00.000000', 944900.00, 'confirmed', '2025-07-02 10:32:43.829045', '2025-07-02 10:32:43.848817', 3, 5, 'driver', 5, 'none', 944900.00, 0.00, 'bank', 0.00),
(7, 'SALE-20250702103722240', '2025-06-30 00:00:00.000000', 309500.00, 'confirmed', '2025-07-02 10:37:22.240697', '2025-07-02 10:37:22.271373', 3, 19, 'self', NULL, 'none', 309500.00, 0.00, 'bank', 7400.00),
(8, 'SALE-20250702111636243', '2025-06-30 00:00:00.000000', 1160000.00, 'confirmed', '2025-07-02 11:16:36.244157', '2025-07-02 11:16:36.256711', 3, 20, 'driver', 4, 'partial', 60000.00, 1100000.00, 'bank', 175500.00),
(9, 'SALE-20250702113607263', '2025-06-30 00:00:00.000000', 2473250.00, 'confirmed', '2025-07-02 11:36:07.264228', '2025-07-02 11:36:07.279577', 3, 12, 'driver', 4, 'none', 2473250.00, 0.00, 'bank', 14000.00),
(10, 'SALE-20250702135813716', '2025-07-01 00:00:00.000000', 192660.00, 'confirmed', '2025-07-02 13:58:13.717177', '2025-07-02 13:58:13.747396', 3, 21, 'self', NULL, 'complete', 0.00, 192660.00, 'cash', 0.00),
(11, 'SALE-20250702140744380', '2025-07-01 00:00:00.000000', 240725.00, 'confirmed', '2025-07-02 14:07:44.380781', '2025-07-02 14:07:44.409228', 3, 13, 'driver', 5, 'none', 240725.00, 0.00, 'bank', 0.00),
(12, 'SALE-20250702152200822', '2025-07-02 00:00:00.000000', 831550.00, 'confirmed', '2025-07-02 15:22:00.823023', '2025-07-02 15:22:00.862315', 3, 3, 'driver', 4, 'none', 831550.00, 0.00, 'bank', 0.00),
(13, 'SALE-20250702152531997', '2025-07-02 00:00:00.000000', 253100.00, 'confirmed', '2025-07-02 15:25:31.997963', '2025-07-02 15:25:32.009076', 3, 4, 'self', NULL, 'none', 253100.00, 0.00, 'bank', 0.00),
(14, 'SALE-20250702152630055', '2025-07-02 00:00:00.000000', 362200.00, 'confirmed', '2025-07-02 15:26:30.055292', '2025-07-02 15:26:30.062893', 3, 7, 'driver', 4, 'none', 362200.00, 0.00, 'bank', 0.00),
(15, 'SALE-20250702152723909', '2025-07-02 00:00:00.000000', 277500.00, 'confirmed', '2025-07-02 15:27:23.909477', '2025-07-02 15:27:23.918717', 3, 18, 'driver', 5, 'none', 277500.00, 0.00, 'driver', 0.00),
(16, 'SALE-20250703134913518', '2025-07-02 00:00:00.000000', 337600.00, 'confirmed', '2025-07-03 13:49:13.518672', '2025-07-03 13:49:13.529068', 3, 16, 'driver', 4, 'none', 337600.00, 0.00, 'bank', 0.00),
(17, 'SALE-20250703140110008', '2025-07-02 00:00:00.000000', 63275.00, 'confirmed', '2025-07-03 14:01:10.008491', '2025-07-03 14:01:10.021900', 3, 22, 'driver', 5, 'partial', 34690.00, 28585.00, 'bank', 0.00),
(18, 'SALE-20250703140352090', '2025-07-02 00:00:00.000000', 25310.00, 'confirmed', '2025-07-03 14:03:52.091162', '2025-07-03 14:03:52.099804', 3, 23, 'driver', 5, 'none', 25310.00, 0.00, 'driver', 0.00),
(19, 'SALE-20250703143449282', '2025-07-03 00:00:00.000000', 20275.00, 'confirmed', '2025-07-03 14:34:49.283095', '2025-07-03 14:34:49.390202', 3, 24, 'self', NULL, 'complete', 0.00, 20275.00, 'cash', 0.00),
(20, 'SALE-20250703143645723', '2025-07-03 00:00:00.000000', 105000.00, 'confirmed', '2025-07-03 14:36:45.724099', '2025-07-03 14:36:45.735170', 3, 25, 'self', NULL, 'none', 105000.00, 0.00, 'bank', 4900.00),
(21, 'SALE-20250703153201283', '2025-07-03 00:00:00.000000', 8870.00, 'confirmed', '2025-07-03 15:32:01.284413', '2025-07-03 15:32:01.305802', 3, 24, 'self', NULL, 'complete', 0.00, 8870.00, 'cash', 0.00),
(22, 'SALE-20250704090511110', '2025-07-04 00:00:00.000000', 493850.00, 'confirmed', '2025-07-04 09:05:11.110629', '2025-07-04 09:05:11.149683', 3, 26, 'driver', 5, 'none', 493850.00, 0.00, 'bank', 0.00);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_site_activitylogmodel`
--
ALTER TABLE `admin_site_activitylogmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `admin_site_activityl_customer_id_d29d4b75_fk_sale_cust` (`customer_id`),
  ADD KEY `admin_site_activitylogmodel_user_id_ae789fff_fk_auth_user_id` (`user_id`),
  ADD KEY `admin_site_activityl_supplier_id_5d8907fb_fk_inventory` (`supplier_id`),
  ADD KEY `admin_site_activityl_driver_id_a433de14_fk_human_res` (`driver_id`);

--
-- Indexes for table `admin_site_dashboardmodel`
--
ALTER TABLE `admin_site_dashboardmodel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `admin_site_siteinfomodel`
--
ALTER TABLE `admin_site_siteinfomodel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `admin_site_sitesettingmodel`
--
ALTER TABLE `admin_site_sitesettingmodel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `finance_cashtransfermodel`
--
ALTER TABLE `finance_cashtransfermodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `finance_cashtransfermodel_created_by_id_ef1f885c_fk_auth_user_id` (`created_by_id`),
  ADD KEY `finance_cashtransfer_staff_id_efa4c434_fk_human_res` (`staff_id`),
  ADD KEY `finance_cashtransfer_supplier_id_ebba4966_fk_inventory` (`supplier_id`);

--
-- Indexes for table `finance_expensemodel`
--
ALTER TABLE `finance_expensemodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `finance_expensemodel_created_by_id_95dc215c_fk_auth_user_id` (`created_by_id`),
  ADD KEY `finance_expensemodel_type_id_6675db61_fk_finance_e` (`type_id`);

--
-- Indexes for table `finance_expensetypemodel`
--
ALTER TABLE `finance_expensetypemodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `finance_staffbonusmodel`
--
ALTER TABLE `finance_staffbonusmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `finance_staffbonusmodel_created_by_id_dedd4575_fk_auth_user_id` (`created_by_id`),
  ADD KEY `finance_staffbonusmo_staff_id_8bb947c2_fk_human_res` (`staff_id`);

--
-- Indexes for table `finance_staffdeductionmodel`
--
ALTER TABLE `finance_staffdeductionmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `finance_staffdeducti_created_by_id_0bbfe94d_fk_auth_user` (`created_by_id`),
  ADD KEY `finance_staffdeducti_staff_id_634e6787_fk_human_res` (`staff_id`);

--
-- Indexes for table `finance_staffsalaryhistorymodel`
--
ALTER TABLE `finance_staffsalaryhistorymodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `finance_staffsalaryh_staff_id_351a4942_fk_human_res` (`staff_id`);

--
-- Indexes for table `finance_staffsalarymodel`
--
ALTER TABLE `finance_staffsalarymodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `staff_id` (`staff_id`),
  ADD KEY `finance_staffsalarymodel_created_by_id_0e183d4d_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `finance_staffsalarypaymentmodel`
--
ALTER TABLE `finance_staffsalarypaymentmodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finance_staffsalarypaymentmodel_staff_id_month_a2d79131_uniq` (`staff_id`,`month`),
  ADD KEY `finance_staffsalaryp_created_by_id_b57eed7d_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `finance_staffsalarysummarymodel`
--
ALTER TABLE `finance_staffsalarysummarymodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `finance_staffsalarysummarymodel_month_d1f856c9_uniq` (`month`),
  ADD KEY `finance_staffsalarys_created_by_id_a1e18b89_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `human_resource_staffmodel`
--
ALTER TABLE `human_resource_staffmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `human_resource_staffmodel_created_by_id_f8fe0dbd_fk_auth_user_id` (`created_by_id`),
  ADD KEY `human_resource_staffmodel_group_id_c424357d_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `human_resource_staffprofilemodel`
--
ALTER TABLE `human_resource_staffprofilemodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD UNIQUE KEY `staff_id` (`staff_id`);

--
-- Indexes for table `human_resource_staffwalletmodel`
--
ALTER TABLE `human_resource_staffwalletmodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `staff_id` (`staff_id`);

--
-- Indexes for table `inventory_categorymodel`
--
ALTER TABLE `inventory_categorymodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `inventory_emptyadjustmentmodel`
--
ALTER TABLE `inventory_emptyadjustmentmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventory_emptyadjus_category_id_e1380a0c_fk_inventory` (`category_id`),
  ADD KEY `inventory_emptyadjus_created_by_id_2480a572_fk_auth_user` (`created_by_id`);

--
-- Indexes for table `inventory_pricehistorymodel`
--
ALTER TABLE `inventory_pricehistorymodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventory_pricehisto_product_id_d5ac115a_fk_inventory` (`product_id`);

--
-- Indexes for table `inventory_productmodel`
--
ALTER TABLE `inventory_productmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventory_productmod_category_id_47d8e9d4_fk_inventory` (`category_id`),
  ADD KEY `inventory_productmodel_updated_by_id_03d21fbe_fk_auth_user_id` (`updated_by_id`);

--
-- Indexes for table `inventory_stockinmodel`
--
ALTER TABLE `inventory_stockinmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventory_stockinmod_created_by_id_5976a58e_fk_human_res` (`created_by_id`),
  ADD KEY `inventory_stockinmod_product_id_7cd7a469_fk_inventory` (`product_id`);

--
-- Indexes for table `inventory_stockinsummarymodel`
--
ALTER TABLE `inventory_stockinsummarymodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventory_stockinsum_created_by_id_9aa5ff4f_fk_human_res` (`created_by_id`),
  ADD KEY `inventory_stockinsum_supplier_id_80f7a2e9_fk_inventory` (`supplier_id`);

--
-- Indexes for table `inventory_stockinsummarymodel_products`
--
ALTER TABLE `inventory_stockinsummarymodel_products`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `inventory_stockinsummary_stockinsummarymodel_id_s_95d80855_uniq` (`stockinsummarymodel_id`,`stockinmodel_id`),
  ADD KEY `inventory_stockinsum_stockinmodel_id_4397fc4c_fk_inventory` (`stockinmodel_id`);

--
-- Indexes for table `inventory_stockoutmodel`
--
ALTER TABLE `inventory_stockoutmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventory_stockoutmo_created_by_id_7c58001f_fk_human_res` (`created_by_id`),
  ADD KEY `inventory_stockoutmo_stock_id_fc709bec_fk_inventory` (`stock_id`);

--
-- Indexes for table `inventory_suppliercashflowhistorymodel`
--
ALTER TABLE `inventory_suppliercashflowhistorymodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventory_supplierca_supplier_id_a4138f6d_fk_inventory` (`supplier_id`);

--
-- Indexes for table `inventory_suppliermodel`
--
ALTER TABLE `inventory_suppliermodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `inventory_suppliermo_category_id_cacfaf36_fk_inventory` (`category_id`),
  ADD KEY `inventory_suppliermodel_updated_by_id_3a1308d2_fk_auth_user_id` (`updated_by_id`);

--
-- Indexes for table `sale_customercratedebtmodel`
--
ALTER TABLE `sale_customercratedebtmodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `sale_customercratedebtmo_customer_id_category_id_1409353b_uniq` (`customer_id`,`category_id`),
  ADD KEY `sale_customercratede_category_id_4c56d161_fk_inventory` (`category_id`);

--
-- Indexes for table `sale_customercratereturnmodel`
--
ALTER TABLE `sale_customercratereturnmodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `sale_customercratereturn_customer_id_category_id__2814cb05_uniq` (`customer_id`,`category_id`,`created_at`),
  ADD KEY `sale_customercratere_category_id_0c342605_fk_inventory` (`category_id`),
  ADD KEY `sale_customercratere_recorded_by_id_ecd0a6b4_fk_auth_user` (`recorded_by_id`),
  ADD KEY `sale_customercratere_driver_id_787d928f_fk_human_res` (`driver_id`);

--
-- Indexes for table `sale_customerdebtrepaymentmodel`
--
ALTER TABLE `sale_customerdebtrepaymentmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sale_customerdebtrep_customer_id_57c0053c_fk_sale_cust` (`customer_id`),
  ADD KEY `sale_customerdebtrep_recorded_by_id_5a931187_fk_auth_user` (`recorded_by_id`),
  ADD KEY `sale_customerdebtrep_driver_id_00a4021b_fk_human_res` (`driver_id`);

--
-- Indexes for table `sale_customermodel`
--
ALTER TABLE `sale_customermodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `sale_customermodel_created_by_id_1014930c_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `sale_customerwalletmodel`
--
ALTER TABLE `sale_customerwalletmodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `customer_id` (`customer_id`);

--
-- Indexes for table `sale_returnmodel`
--
ALTER TABLE `sale_returnmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sale_returnmodel_sale_item_id_b802aa3a_fk_sale_saleitemmodel_id` (`sale_item_id`);

--
-- Indexes for table `sale_salecategoryempty`
--
ALTER TABLE `sale_salecategoryempty`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `sale_salecategoryempty_sale_id_category_id_00253094_uniq` (`sale_id`,`category_id`),
  ADD KEY `sale_salecategoryemp_category_id_1102382a_fk_inventory` (`category_id`);

--
-- Indexes for table `sale_saleitemmodel`
--
ALTER TABLE `sale_saleitemmodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `sale_saleitemmodel_sale_id_product_id_65980108_uniq` (`sale_id`,`product_id`),
  ADD KEY `sale_saleitemmodel_product_id_43e32e35_fk_inventory` (`product_id`),
  ADD KEY `sale_saleitemmodel_stock_id_c8e7caab_fk_inventory` (`stock_id`);

--
-- Indexes for table `sale_salemodel`
--
ALTER TABLE `sale_salemodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `transaction_id` (`transaction_id`),
  ADD KEY `sale_salemodel_created_by_id_ea06a112_fk_auth_user_id` (`created_by_id`),
  ADD KEY `sale_salemodel_customer_id_80303570_fk_sale_customermodel_id` (`customer_id`),
  ADD KEY `sale_salemodel_driver_id_44681132_fk_human_res` (`driver_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_site_activitylogmodel`
--
ALTER TABLE `admin_site_activitylogmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT for table `admin_site_dashboardmodel`
--
ALTER TABLE `admin_site_dashboardmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `admin_site_siteinfomodel`
--
ALTER TABLE `admin_site_siteinfomodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `admin_site_sitesettingmodel`
--
ALTER TABLE `admin_site_sitesettingmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=161;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=82;

--
-- AUTO_INCREMENT for table `finance_cashtransfermodel`
--
ALTER TABLE `finance_cashtransfermodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `finance_expensemodel`
--
ALTER TABLE `finance_expensemodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `finance_expensetypemodel`
--
ALTER TABLE `finance_expensetypemodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `finance_staffbonusmodel`
--
ALTER TABLE `finance_staffbonusmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `finance_staffdeductionmodel`
--
ALTER TABLE `finance_staffdeductionmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `finance_staffsalaryhistorymodel`
--
ALTER TABLE `finance_staffsalaryhistorymodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `finance_staffsalarymodel`
--
ALTER TABLE `finance_staffsalarymodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `finance_staffsalarypaymentmodel`
--
ALTER TABLE `finance_staffsalarypaymentmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `finance_staffsalarysummarymodel`
--
ALTER TABLE `finance_staffsalarysummarymodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `human_resource_staffmodel`
--
ALTER TABLE `human_resource_staffmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `human_resource_staffprofilemodel`
--
ALTER TABLE `human_resource_staffprofilemodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `human_resource_staffwalletmodel`
--
ALTER TABLE `human_resource_staffwalletmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `inventory_categorymodel`
--
ALTER TABLE `inventory_categorymodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `inventory_emptyadjustmentmodel`
--
ALTER TABLE `inventory_emptyadjustmentmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inventory_pricehistorymodel`
--
ALTER TABLE `inventory_pricehistorymodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inventory_productmodel`
--
ALTER TABLE `inventory_productmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `inventory_stockinmodel`
--
ALTER TABLE `inventory_stockinmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `inventory_stockinsummarymodel`
--
ALTER TABLE `inventory_stockinsummarymodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `inventory_stockinsummarymodel_products`
--
ALTER TABLE `inventory_stockinsummarymodel_products`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `inventory_stockoutmodel`
--
ALTER TABLE `inventory_stockoutmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inventory_suppliercashflowhistorymodel`
--
ALTER TABLE `inventory_suppliercashflowhistorymodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inventory_suppliermodel`
--
ALTER TABLE `inventory_suppliermodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `sale_customercratedebtmodel`
--
ALTER TABLE `sale_customercratedebtmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `sale_customercratereturnmodel`
--
ALTER TABLE `sale_customercratereturnmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `sale_customerdebtrepaymentmodel`
--
ALTER TABLE `sale_customerdebtrepaymentmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `sale_customermodel`
--
ALTER TABLE `sale_customermodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `sale_customerwalletmodel`
--
ALTER TABLE `sale_customerwalletmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `sale_returnmodel`
--
ALTER TABLE `sale_returnmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sale_salecategoryempty`
--
ALTER TABLE `sale_salecategoryempty`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `sale_saleitemmodel`
--
ALTER TABLE `sale_saleitemmodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT for table `sale_salemodel`
--
ALTER TABLE `sale_salemodel`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin_site_activitylogmodel`
--
ALTER TABLE `admin_site_activitylogmodel`
  ADD CONSTRAINT `admin_site_activityl_customer_id_d29d4b75_fk_sale_cust` FOREIGN KEY (`customer_id`) REFERENCES `sale_customermodel` (`id`),
  ADD CONSTRAINT `admin_site_activityl_driver_id_a433de14_fk_human_res` FOREIGN KEY (`driver_id`) REFERENCES `human_resource_staffmodel` (`id`),
  ADD CONSTRAINT `admin_site_activityl_supplier_id_5d8907fb_fk_inventory` FOREIGN KEY (`supplier_id`) REFERENCES `inventory_suppliermodel` (`id`),
  ADD CONSTRAINT `admin_site_activitylogmodel_user_id_ae789fff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `finance_cashtransfermodel`
--
ALTER TABLE `finance_cashtransfermodel`
  ADD CONSTRAINT `finance_cashtransfer_staff_id_efa4c434_fk_human_res` FOREIGN KEY (`staff_id`) REFERENCES `human_resource_staffmodel` (`id`),
  ADD CONSTRAINT `finance_cashtransfer_supplier_id_ebba4966_fk_inventory` FOREIGN KEY (`supplier_id`) REFERENCES `inventory_suppliermodel` (`id`),
  ADD CONSTRAINT `finance_cashtransfermodel_created_by_id_ef1f885c_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `finance_expensemodel`
--
ALTER TABLE `finance_expensemodel`
  ADD CONSTRAINT `finance_expensemodel_created_by_id_95dc215c_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `finance_expensemodel_type_id_6675db61_fk_finance_e` FOREIGN KEY (`type_id`) REFERENCES `finance_expensetypemodel` (`id`);

--
-- Constraints for table `finance_staffbonusmodel`
--
ALTER TABLE `finance_staffbonusmodel`
  ADD CONSTRAINT `finance_staffbonusmo_staff_id_8bb947c2_fk_human_res` FOREIGN KEY (`staff_id`) REFERENCES `human_resource_staffmodel` (`id`),
  ADD CONSTRAINT `finance_staffbonusmodel_created_by_id_dedd4575_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `finance_staffdeductionmodel`
--
ALTER TABLE `finance_staffdeductionmodel`
  ADD CONSTRAINT `finance_staffdeducti_created_by_id_0bbfe94d_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `finance_staffdeducti_staff_id_634e6787_fk_human_res` FOREIGN KEY (`staff_id`) REFERENCES `human_resource_staffmodel` (`id`);

--
-- Constraints for table `finance_staffsalaryhistorymodel`
--
ALTER TABLE `finance_staffsalaryhistorymodel`
  ADD CONSTRAINT `finance_staffsalaryh_staff_id_351a4942_fk_human_res` FOREIGN KEY (`staff_id`) REFERENCES `human_resource_staffmodel` (`id`);

--
-- Constraints for table `finance_staffsalarymodel`
--
ALTER TABLE `finance_staffsalarymodel`
  ADD CONSTRAINT `finance_staffsalarym_staff_id_7ba58ad1_fk_human_res` FOREIGN KEY (`staff_id`) REFERENCES `human_resource_staffmodel` (`id`),
  ADD CONSTRAINT `finance_staffsalarymodel_created_by_id_0e183d4d_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `finance_staffsalarypaymentmodel`
--
ALTER TABLE `finance_staffsalarypaymentmodel`
  ADD CONSTRAINT `finance_staffsalaryp_created_by_id_b57eed7d_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `finance_staffsalaryp_staff_id_2bf39f02_fk_human_res` FOREIGN KEY (`staff_id`) REFERENCES `human_resource_staffmodel` (`id`);

--
-- Constraints for table `finance_staffsalarysummarymodel`
--
ALTER TABLE `finance_staffsalarysummarymodel`
  ADD CONSTRAINT `finance_staffsalarys_created_by_id_a1e18b89_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `human_resource_staffmodel`
--
ALTER TABLE `human_resource_staffmodel`
  ADD CONSTRAINT `human_resource_staffmodel_created_by_id_f8fe0dbd_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `human_resource_staffmodel_group_id_c424357d_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `human_resource_staffprofilemodel`
--
ALTER TABLE `human_resource_staffprofilemodel`
  ADD CONSTRAINT `human_resource_staff_staff_id_80032cc8_fk_human_res` FOREIGN KEY (`staff_id`) REFERENCES `human_resource_staffmodel` (`id`),
  ADD CONSTRAINT `human_resource_staff_user_id_98a3d39b_fk_auth_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `human_resource_staffwalletmodel`
--
ALTER TABLE `human_resource_staffwalletmodel`
  ADD CONSTRAINT `human_resource_staff_staff_id_ac1a9d00_fk_human_res` FOREIGN KEY (`staff_id`) REFERENCES `human_resource_staffmodel` (`id`);

--
-- Constraints for table `inventory_emptyadjustmentmodel`
--
ALTER TABLE `inventory_emptyadjustmentmodel`
  ADD CONSTRAINT `inventory_emptyadjus_category_id_e1380a0c_fk_inventory` FOREIGN KEY (`category_id`) REFERENCES `inventory_categorymodel` (`id`),
  ADD CONSTRAINT `inventory_emptyadjus_created_by_id_2480a572_fk_auth_user` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `inventory_pricehistorymodel`
--
ALTER TABLE `inventory_pricehistorymodel`
  ADD CONSTRAINT `inventory_pricehisto_product_id_d5ac115a_fk_inventory` FOREIGN KEY (`product_id`) REFERENCES `inventory_productmodel` (`id`);

--
-- Constraints for table `inventory_productmodel`
--
ALTER TABLE `inventory_productmodel`
  ADD CONSTRAINT `inventory_productmod_category_id_47d8e9d4_fk_inventory` FOREIGN KEY (`category_id`) REFERENCES `inventory_categorymodel` (`id`),
  ADD CONSTRAINT `inventory_productmodel_updated_by_id_03d21fbe_fk_auth_user_id` FOREIGN KEY (`updated_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `inventory_stockinmodel`
--
ALTER TABLE `inventory_stockinmodel`
  ADD CONSTRAINT `inventory_stockinmod_created_by_id_5976a58e_fk_human_res` FOREIGN KEY (`created_by_id`) REFERENCES `human_resource_staffmodel` (`id`),
  ADD CONSTRAINT `inventory_stockinmod_product_id_7cd7a469_fk_inventory` FOREIGN KEY (`product_id`) REFERENCES `inventory_productmodel` (`id`);

--
-- Constraints for table `inventory_stockinsummarymodel`
--
ALTER TABLE `inventory_stockinsummarymodel`
  ADD CONSTRAINT `inventory_stockinsum_created_by_id_9aa5ff4f_fk_human_res` FOREIGN KEY (`created_by_id`) REFERENCES `human_resource_staffmodel` (`id`),
  ADD CONSTRAINT `inventory_stockinsum_supplier_id_80f7a2e9_fk_inventory` FOREIGN KEY (`supplier_id`) REFERENCES `inventory_suppliermodel` (`id`);

--
-- Constraints for table `inventory_stockinsummarymodel_products`
--
ALTER TABLE `inventory_stockinsummarymodel_products`
  ADD CONSTRAINT `inventory_stockinsum_stockinmodel_id_4397fc4c_fk_inventory` FOREIGN KEY (`stockinmodel_id`) REFERENCES `inventory_stockinmodel` (`id`),
  ADD CONSTRAINT `inventory_stockinsum_stockinsummarymodel__d752c7a0_fk_inventory` FOREIGN KEY (`stockinsummarymodel_id`) REFERENCES `inventory_stockinsummarymodel` (`id`);

--
-- Constraints for table `inventory_stockoutmodel`
--
ALTER TABLE `inventory_stockoutmodel`
  ADD CONSTRAINT `inventory_stockoutmo_created_by_id_7c58001f_fk_human_res` FOREIGN KEY (`created_by_id`) REFERENCES `human_resource_staffmodel` (`id`),
  ADD CONSTRAINT `inventory_stockoutmo_stock_id_fc709bec_fk_inventory` FOREIGN KEY (`stock_id`) REFERENCES `inventory_stockinmodel` (`id`);

--
-- Constraints for table `inventory_suppliercashflowhistorymodel`
--
ALTER TABLE `inventory_suppliercashflowhistorymodel`
  ADD CONSTRAINT `inventory_supplierca_supplier_id_a4138f6d_fk_inventory` FOREIGN KEY (`supplier_id`) REFERENCES `inventory_suppliermodel` (`id`);

--
-- Constraints for table `inventory_suppliermodel`
--
ALTER TABLE `inventory_suppliermodel`
  ADD CONSTRAINT `inventory_suppliermo_category_id_cacfaf36_fk_inventory` FOREIGN KEY (`category_id`) REFERENCES `inventory_categorymodel` (`id`),
  ADD CONSTRAINT `inventory_suppliermodel_updated_by_id_3a1308d2_fk_auth_user_id` FOREIGN KEY (`updated_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `sale_customercratedebtmodel`
--
ALTER TABLE `sale_customercratedebtmodel`
  ADD CONSTRAINT `sale_customercratede_category_id_4c56d161_fk_inventory` FOREIGN KEY (`category_id`) REFERENCES `inventory_categorymodel` (`id`),
  ADD CONSTRAINT `sale_customercratede_customer_id_cf160a7c_fk_sale_cust` FOREIGN KEY (`customer_id`) REFERENCES `sale_customermodel` (`id`);

--
-- Constraints for table `sale_customercratereturnmodel`
--
ALTER TABLE `sale_customercratereturnmodel`
  ADD CONSTRAINT `sale_customercratere_category_id_0c342605_fk_inventory` FOREIGN KEY (`category_id`) REFERENCES `inventory_categorymodel` (`id`),
  ADD CONSTRAINT `sale_customercratere_customer_id_022353a4_fk_sale_cust` FOREIGN KEY (`customer_id`) REFERENCES `sale_customermodel` (`id`),
  ADD CONSTRAINT `sale_customercratere_driver_id_787d928f_fk_human_res` FOREIGN KEY (`driver_id`) REFERENCES `human_resource_staffmodel` (`id`),
  ADD CONSTRAINT `sale_customercratere_recorded_by_id_ecd0a6b4_fk_auth_user` FOREIGN KEY (`recorded_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `sale_customerdebtrepaymentmodel`
--
ALTER TABLE `sale_customerdebtrepaymentmodel`
  ADD CONSTRAINT `sale_customerdebtrep_customer_id_57c0053c_fk_sale_cust` FOREIGN KEY (`customer_id`) REFERENCES `sale_customermodel` (`id`),
  ADD CONSTRAINT `sale_customerdebtrep_driver_id_00a4021b_fk_human_res` FOREIGN KEY (`driver_id`) REFERENCES `human_resource_staffmodel` (`id`),
  ADD CONSTRAINT `sale_customerdebtrep_recorded_by_id_5a931187_fk_auth_user` FOREIGN KEY (`recorded_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `sale_customermodel`
--
ALTER TABLE `sale_customermodel`
  ADD CONSTRAINT `sale_customermodel_created_by_id_1014930c_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `sale_customerwalletmodel`
--
ALTER TABLE `sale_customerwalletmodel`
  ADD CONSTRAINT `sale_customerwalletm_customer_id_237f736a_fk_sale_cust` FOREIGN KEY (`customer_id`) REFERENCES `sale_customermodel` (`id`);

--
-- Constraints for table `sale_returnmodel`
--
ALTER TABLE `sale_returnmodel`
  ADD CONSTRAINT `sale_returnmodel_sale_item_id_b802aa3a_fk_sale_saleitemmodel_id` FOREIGN KEY (`sale_item_id`) REFERENCES `sale_saleitemmodel` (`id`);

--
-- Constraints for table `sale_salecategoryempty`
--
ALTER TABLE `sale_salecategoryempty`
  ADD CONSTRAINT `sale_salecategoryemp_category_id_1102382a_fk_inventory` FOREIGN KEY (`category_id`) REFERENCES `inventory_categorymodel` (`id`),
  ADD CONSTRAINT `sale_salecategoryempty_sale_id_eaaeb792_fk_sale_salemodel_id` FOREIGN KEY (`sale_id`) REFERENCES `sale_salemodel` (`id`);

--
-- Constraints for table `sale_saleitemmodel`
--
ALTER TABLE `sale_saleitemmodel`
  ADD CONSTRAINT `sale_saleitemmodel_product_id_43e32e35_fk_inventory` FOREIGN KEY (`product_id`) REFERENCES `inventory_productmodel` (`id`),
  ADD CONSTRAINT `sale_saleitemmodel_sale_id_5ab8cf9c_fk_sale_salemodel_id` FOREIGN KEY (`sale_id`) REFERENCES `sale_salemodel` (`id`),
  ADD CONSTRAINT `sale_saleitemmodel_stock_id_c8e7caab_fk_inventory` FOREIGN KEY (`stock_id`) REFERENCES `inventory_stockinmodel` (`id`);

--
-- Constraints for table `sale_salemodel`
--
ALTER TABLE `sale_salemodel`
  ADD CONSTRAINT `sale_salemodel_created_by_id_ea06a112_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `sale_salemodel_customer_id_80303570_fk_sale_customermodel_id` FOREIGN KEY (`customer_id`) REFERENCES `sale_customermodel` (`id`),
  ADD CONSTRAINT `sale_salemodel_driver_id_44681132_fk_human_res` FOREIGN KEY (`driver_id`) REFERENCES `human_resource_staffmodel` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
