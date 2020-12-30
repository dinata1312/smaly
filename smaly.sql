-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 30, 2020 at 05:22 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smaly`
--

-- --------------------------------------------------------

--
-- Table structure for table `detailpakaian`
--

CREATE TABLE `detailpakaian` (
  `idDetail` int(5) NOT NULL,
  `idTransaksi` int(5) NOT NULL,
  `idPaket` int(5) NOT NULL,
  `berat` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `paket`
--

CREATE TABLE `paket` (
  `idPaket` int(5) NOT NULL,
  `namaPaket` varchar(20) NOT NULL,
  `harga` int(5) NOT NULL,
  `jenis` varchar(15) NOT NULL,
  `durasi` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `paket`
--

INSERT INTO `paket` (`idPaket`, `namaPaket`, `harga`, `jenis`, `durasi`) VALUES
(1, 'Murah Njir', 5000, 'Pakaian', 3),
(2, 'Boneka Aja', 8000, 'Boneka', 3);

-- --------------------------------------------------------

--
-- Table structure for table `potonganharga`
--

CREATE TABLE `potonganharga` (
  `idPotongan` int(5) NOT NULL,
  `namaPotongan` varchar(25) NOT NULL,
  `jenisPotongan` enum('diskon','potongan harga') NOT NULL,
  `banyakPotongan` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `potonganharga`
--

INSERT INTO `potonganharga` (`idPotongan`, `namaPotongan`, `jenisPotongan`, `banyakPotongan`) VALUES
(99862, 'GEBYAR TAHUN BARU', 'diskon', 2000);

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `idTransaksi` int(5) NOT NULL,
  `namaPelanggan` varchar(15) NOT NULL,
  `status` enum('belum selesai','selesai') NOT NULL DEFAULT 'belum selesai',
  `idPotongan` int(5) DEFAULT NULL,
  `Mulai` date DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`idTransaksi`, `namaPelanggan`, `status`, `idPotongan`, `Mulai`) VALUES
(8, 'Nina', 'belum selesai', NULL, '2020-12-30');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `username` varchar(15) NOT NULL,
  `password` varchar(255) NOT NULL,
  `namaLengkap` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`username`, `password`, `namaLengkap`) VALUES
('ninacutez', 'admin123', 'karenina cutes abis');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `detailpakaian`
--
ALTER TABLE `detailpakaian`
  ADD PRIMARY KEY (`idDetail`),
  ADD KEY `idTransaksi` (`idTransaksi`),
  ADD KEY `idPaket` (`idPaket`);

--
-- Indexes for table `paket`
--
ALTER TABLE `paket`
  ADD PRIMARY KEY (`idPaket`);

--
-- Indexes for table `potonganharga`
--
ALTER TABLE `potonganharga`
  ADD PRIMARY KEY (`idPotongan`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`idTransaksi`),
  ADD KEY `idPotongan` (`idPotongan`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `detailpakaian`
--
ALTER TABLE `detailpakaian`
  MODIFY `idDetail` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `paket`
--
ALTER TABLE `paket`
  MODIFY `idPaket` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `potonganharga`
--
ALTER TABLE `potonganharga`
  MODIFY `idPotongan` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=99863;

--
-- AUTO_INCREMENT for table `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `idTransaksi` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `detailpakaian`
--
ALTER TABLE `detailpakaian`
  ADD CONSTRAINT `detailpakaian_ibfk_1` FOREIGN KEY (`idTransaksi`) REFERENCES `transaksi` (`idTransaksi`),
  ADD CONSTRAINT `detailpakaian_ibfk_2` FOREIGN KEY (`idPaket`) REFERENCES `paket` (`idPaket`);

--
-- Constraints for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi_ibfk_2` FOREIGN KEY (`idPotongan`) REFERENCES `potonganharga` (`idPotongan`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
