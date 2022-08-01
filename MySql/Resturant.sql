-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3333
-- Generation Time: Jul 20, 2022 at 05:17 AM
-- Server version: 8.0.29
-- PHP Version: 7.4.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `resturant`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int NOT NULL,
  `first_name` text NOT NULL,
  `last_name` text NOT NULL,
  `points` int NOT NULL DEFAULT 0
);

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `first_name`, `last_name`, `points`) VALUES
(1, 'Tahsin', 'Ayman', 1000),
(2, 'Touhida', 'Akter', 2000),
(3, 'Rasheed', 'karim', 3000),
(4, 'Tasmiah', 'Tabassum', 4000),
(5, 'Abdullah', 'Al Adib', 0),
(6, 'Roushon', 'Ara', 5000);

-- --------------------------------------------------------

--
-- Stand-in structure for  `invoice`
-- (See below for the actual view)
--
CREATE TABLE `invoice` (
`id` int
,`first_name` text
,`last_name` text
,`product` text
,`quantity` int
,`unit_price` int
,`total_price` bigint
,`date` date
);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int NOT NULL,
  `customer_id` int NOT NULL,
  `date` date NOT NULL
);

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `customer_id`, `date`) VALUES
(1, 1, '2022-07-20'),
(2, 1, '2022-07-20'),
(3, 2, '2024-07-11'),
(4, 3, '2022-07-20'),
(5, 4, '2022-07-15'),
(6, 5, '2022-07-07');

-- --------------------------------------------------------

--
-- Table structure for table `order_items`
--

CREATE TABLE `order_items` (
  `id` int NOT NULL,
  `product_id` int NOT NULL,
  `order_id` int NOT NULL,
  `quantity` int NOT NULL DEFAULT '1',
  `unit_price` int NOT NULL
);

--
-- Dumping data for table `order_items`
--

INSERT INTO `order_items` (`id`, `product_id`, `order_id`, `quantity`, `unit_price`) VALUES
(3, 1, 1, 5, 1000),
(4, 2, 1, 2, 200),
(5, 3, 4, 3, 5000),
(6, 5, 4, 6, 6000),
(7, 6, 4, 7, 200),
(8, 3, 2, 2, 100);

-- --------------------------------------------------------

--
-- Stand-in structure for view `payment_invoice`
-- (See below for the actual view)
--
CREATE TABLE `payment_invoice` (
`customer_id` int
,`first_name` text
,`last_name` text
,`total_price` decimal(42,0)
);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int NOT NULL,
  `name` text NOT NULL,
  `quantity_in_stock` int NOT NULL DEFAULT '0'
);

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `quantity_in_stock`) VALUES
(1, 'Burger', 20),
(2, 'Pizza', 30),
(3, 'Pasta', 50),
(4, 'Fries', 100),
(5, 'Cake', 5),
(6, 'Chicken Wings', 30);

-- --------------------------------------------------------

--
-- Structure for view `invoice`
--
DROP TABLE IF EXISTS `invoice`;

CREATE ALGORITHM=UNDEFINED DEFINER=`tahsin`@`%` SQL SECURITY DEFINER VIEW `invoice`  AS SELECT `oi`.`id` AS `id`, `c`.`first_name` AS `first_name`, `c`.`last_name` AS `last_name`, `p`.`name` AS `product`, `oi`.`quantity` AS `quantity`, `oi`.`unit_price` AS `unit_price`, (`oi`.`quantity` * `oi`.`unit_price`) AS `total_price`, `o`.`date` AS `date` FROM (((`order_items` `oi` join `orders` `o` on((`oi`.`order_id` = `o`.`id`))) join `products` `p` on((`oi`.`product_id` = `p`.`id`))) join `customers` `c` on((`o`.`customer_id` = `c`.`id`)))  ;

-- --------------------------------------------------------

--
-- Structure for view `payment_invoice`
--
DROP TABLE IF EXISTS `payment_invoice`;

CREATE ALGORITHM=UNDEFINED DEFINER=`tahsin`@`%` SQL SECURITY DEFINER VIEW `payment_invoice`  AS SELECT `o`.`customer_id` AS `customer_id`, `c`.`first_name` AS `first_name`, `c`.`last_name` AS `last_name`, sum((`oi`.`quantity` * `oi`.`unit_price`)) AS `total_price` FROM (((`order_items` `oi` join `orders` `o` on((`oi`.`order_id` = `o`.`id`))) join `products` `p` on((`oi`.`product_id` = `p`.`id`))) join `customers` `c` on((`o`.`customer_id` = `c`.`id`))) GROUP BY `c`.`id``id`  ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `order_items`
--
ALTER TABLE `order_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_id` (`product_id`),
  ADD KEY `order_id` (`order_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `order_items`
--
ALTER TABLE `order_items`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`);

--
-- Constraints for table `order_items`
--
ALTER TABLE `order_items`
  ADD CONSTRAINT `order_items_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  ADD CONSTRAINT `order_items_ibfk_2` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
