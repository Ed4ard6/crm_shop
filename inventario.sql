-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-04-2023 a las 00:46:32
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inventario`
--
CREATE DATABASE IF NOT EXISTS `inventario` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `inventario`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id` int(11) NOT NULL,
  `descripcion` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`id`, `descripcion`) VALUES
(1, 'Papeleria'),
(2, 'Pañaleria'),
(3, 'Cosmeticos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `det_factura`
--

CREATE TABLE `det_factura` (
  `id` int(11) NOT NULL,
  `id_factura` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio_venta` int(11) NOT NULL,
  `total` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `det_factura`
--

INSERT INTO `det_factura` (`id`, `id_factura`, `id_producto`, `cantidad`, `precio_venta`, `total`) VALUES
(1, 1, 1, 3, 240, 720),
(2, 1, 2, 1, 2400, 2400);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facturas`
--

CREATE TABLE `facturas` (
  `id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `estado` varchar(55) NOT NULL DEFAULT 'Activa',
  `total` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `facturas`
--

INSERT INTO `facturas` (`id`, `fecha`, `estado`, `total`) VALUES
(1, '2023-04-05', 'Activa', 0),
(2, '2023-04-07', 'Activa', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id` int(11) NOT NULL,
  `nombre_producto` varchar(55) NOT NULL,
  `cate_produc` int(11) NOT NULL,
  `precio_compra` decimal(10,0) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio_venta` int(11) NOT NULL,
  `estado` varchar(55) NOT NULL DEFAULT 'Disponible'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id`, `nombre_producto`, `cate_produc`, `precio_compra`, `cantidad`, `precio_venta`, `estado`) VALUES
(1, 'Hojas', 1, '200', 100, 0, 'Disponible'),
(2, 'Cuaderno', 1, '2000', 100, 0, 'Disponible'),
(3, 'Tetero', 2, '12000', 60, 0, 'Disponible'),
(4, 'Labial', 3, '8000', 20, 0, 'Disponible'),
(5, 'Marcador', 1, '2500', 30, 3000, 'Disponible'),
(6, 'Lapiz', 1, '1300', 50, 1560, 'Disponible'),
(7, 'Crema_pañail', 2, '3000', 20, 3600, 'Disponible'),
(8, 'foami', 1, '2000', 15, 2400, 'Disponible'),
(9, 'pinza de cejas', 3, '3000', 60, 3600, 'Disponible'),
(10, 'Hojas_blancas', 1, '300', 40, 360, 'Disponible'),
(11, 'Hojas_blancas', 1, '300', 40, 360, 'Disponible'),
(12, 'Hojas_blancas', 1, '300', 40, 360, 'Disponible'),
(13, 'Hojas_blancas', 1, '300', 40, 360, 'Disponible'),
(14, 'Hojas_blancas', 1, '300', 40, 360, 'Disponible');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `det_factura`
--
ALTER TABLE `det_factura`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_factura` (`id_factura`),
  ADD KEY `id_producto` (`id_producto`);

--
-- Indices de la tabla `facturas`
--
ALTER TABLE `facturas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cate_produc` (`cate_produc`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `det_factura`
--
ALTER TABLE `det_factura`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `facturas`
--
ALTER TABLE `facturas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `det_factura`
--
ALTER TABLE `det_factura`
  ADD CONSTRAINT `det_factura_ibfk_1` FOREIGN KEY (`id_factura`) REFERENCES `facturas` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `det_factura_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`cate_produc`) REFERENCES `categoria` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
