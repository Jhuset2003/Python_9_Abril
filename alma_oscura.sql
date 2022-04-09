-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-04-2022 a las 00:13:45
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `alma oscura`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `armaduras`
--

CREATE TABLE `armaduras` (
  `id` int(11) NOT NULL,
  `pechera` varchar(100) DEFAULT NULL,
  `casco` varchar(100) DEFAULT NULL,
  `guantes` varchar(100) DEFAULT NULL,
  `botas` varchar(100) DEFAULT NULL,
  `pantalones` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `armaduras`
--

INSERT INTO `armaduras` (`id`, `pechera`, `casco`, `guantes`, `botas`, `pantalones`) VALUES
(1, 'Hierro', 'Hierro', 'Hierro', 'Hierro', 'Hierro'),
(2, 'Hierro', 'Hierro', 'Hierro', 'Hierro', 'Hierro'),
(3, 'Hierro', 'Hierro', 'Hierro', 'Hierro', 'Hierro'),
(4, 'Hierro', 'Hierro', 'Hierro', 'Hierro', 'Hierro'),
(5, 'Hierro', 'Hierro', 'Hierro', 'Hierro', 'Hierro');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `armas`
--

CREATE TABLE `armas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `tipo` varchar(100) DEFAULT NULL,
  `daño` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `armas`
--

INSERT INTO `armas` (`id`, `nombre`, `tipo`, `daño`) VALUES
(1, 'escalibur', 'espada', 100),
(2, 'escalibur', 'espada', 100),
(3, 'escalibur', 'espada', 100),
(4, 'escalibur', 'espada', 100),
(5, 'escalibur', 'espada', 100);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clases`
--

CREATE TABLE `clases` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `tipo` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `clases`
--

INSERT INTO `clases` (`id`, `nombre`, `tipo`) VALUES
(1, 'caballero', 'elfo'),
(2, 'caballero', 'elfo'),
(3, 'caballero', 'elfo'),
(4, 'caballero', 'elfo'),
(5, 'caballero', 'elfo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personajes_ds`
--

CREATE TABLE `personajes_ds` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `id_clase` int(11) DEFAULT NULL,
  `id_arma` int(11) DEFAULT NULL,
  `id_armaduras` int(11) DEFAULT NULL,
  `nivel` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `personajes_ds`
--

INSERT INTO `personajes_ds` (`id`, `nombre`, `id_clase`, `id_arma`, `id_armaduras`, `nivel`) VALUES
(5, 'ajqp', 1, 1, 1, 10),
(6, 'aj', 5, 5, 5, 20),
(7, 'JEG', 1, 1, 1, 80),
(8, 'JEG', 2, 2, 2, 100),
(9, 'JEG', 3, 3, 3, 100),
(10, 'JEG', 4, 4, 4, 20),
(11, 'JEG', 1, 1, 1, 50),
(12, 'JEG', 1, 1, 1, 50),
(13, 'JEG', 1, 1, 1, 50),
(14, 'kjqwnqnfksd', 1, 1, 1, 100);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `armaduras`
--
ALTER TABLE `armaduras`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `armas`
--
ALTER TABLE `armas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `clases`
--
ALTER TABLE `clases`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `personajes_ds`
--
ALTER TABLE `personajes_ds`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FkArma_idx` (`id_arma`),
  ADD KEY `FkClase_idx` (`id_clase`),
  ADD KEY `FkArmaduras_idx` (`id_armaduras`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `armaduras`
--
ALTER TABLE `armaduras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `armas`
--
ALTER TABLE `armas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `clases`
--
ALTER TABLE `clases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `personajes_ds`
--
ALTER TABLE `personajes_ds`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `personajes_ds`
--
ALTER TABLE `personajes_ds`
  ADD CONSTRAINT `FkArma` FOREIGN KEY (`id_arma`) REFERENCES `armas` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FkArmaduras` FOREIGN KEY (`id_armaduras`) REFERENCES `armaduras` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FkClase` FOREIGN KEY (`id_clase`) REFERENCES `clases` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
