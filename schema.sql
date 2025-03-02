DROP DATABASE IF EXISTS `customers`;
CREATE DATABASE IF NOT EXISTS `customers` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `customers`;

CREATE TABLE `customers` (
  `id` uuid NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) NOT NULL,
  `phone` varchar(16) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `phone` (`phone`,`email`);
COMMIT;
