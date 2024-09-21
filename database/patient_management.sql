-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 20, 2024 at 06:14 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `patient_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment_list`
--

CREATE TABLE `appointment_list` (
  `id` bigint(20) NOT NULL,
  `appiontment_date` date DEFAULT NULL,
  `hospital_name` varchar(100) DEFAULT NULL,
  `appiontment_time` varchar(100) DEFAULT NULL,
  `serial_number` varchar(100) DEFAULT NULL,
  `appointment_status` varchar(30) NOT NULL,
  `patient_remarks` longtext DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `doctor_name_id` bigint(20) DEFAULT NULL,
  `patient_name_id` bigint(20) DEFAULT NULL,
  `schedule_name_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
(25, 'Can add Appointment List', 7, 'add_appointmentlist'),
(26, 'Can change Appointment List', 7, 'change_appointmentlist'),
(27, 'Can delete Appointment List', 7, 'delete_appointmentlist'),
(28, 'Can view Appointment List', 7, 'view_appointmentlist'),
(29, 'Can add Doctors Department', 8, 'add_doctordepartment'),
(30, 'Can change Doctors Department', 8, 'change_doctordepartment'),
(31, 'Can delete Doctors Department', 8, 'delete_doctordepartment'),
(32, 'Can view Doctors Department', 8, 'view_doctordepartment'),
(33, 'Can add Doctor List', 9, 'add_doctorlist'),
(34, 'Can change Doctor List', 9, 'change_doctorlist'),
(35, 'Can delete Doctor List', 9, 'delete_doctorlist'),
(36, 'Can view Doctor List', 9, 'view_doctorlist'),
(37, 'Can add Hospital List', 10, 'add_hospitallist'),
(38, 'Can change Hospital List', 10, 'change_hospitallist'),
(39, 'Can delete Hospital List', 10, 'delete_hospitallist'),
(40, 'Can view Hospital List', 10, 'view_hospitallist'),
(41, 'Can add Medical Test', 11, 'add_medicaltests'),
(42, 'Can change Medical Test', 11, 'change_medicaltests'),
(43, 'Can delete Medical Test', 11, 'delete_medicaltests'),
(44, 'Can view Medical Test', 11, 'view_medicaltests'),
(45, 'Can add pathologist Info', 12, 'add_pathologistlist'),
(46, 'Can change pathologist Info', 12, 'change_pathologistlist'),
(47, 'Can delete pathologist Info', 12, 'delete_pathologistlist'),
(48, 'Can view pathologist Info', 12, 'view_pathologistlist'),
(49, 'Can add Patient List', 13, 'add_patientlist'),
(50, 'Can change Patient List', 13, 'change_patientlist'),
(51, 'Can delete Patient List', 13, 'delete_patientlist'),
(52, 'Can view Patient List', 13, 'view_patientlist'),
(53, 'Can add Pharmacy Info', 14, 'add_pharmacyinfo'),
(54, 'Can change Pharmacy Info', 14, 'change_pharmacyinfo'),
(55, 'Can delete Pharmacy Info', 14, 'delete_pharmacyinfo'),
(56, 'Can view Pharmacy Info', 14, 'view_pharmacyinfo'),
(57, 'Can add Prescription', 15, 'add_prescription'),
(58, 'Can change Prescription', 15, 'change_prescription'),
(59, 'Can delete Prescription', 15, 'delete_prescription'),
(60, 'Can view Prescription', 15, 'view_prescription'),
(61, 'Can add Patient Test Report', 16, 'add_patienttestreport'),
(62, 'Can change Patient Test Report', 16, 'change_patienttestreport'),
(63, 'Can delete Patient Test Report', 16, 'delete_patienttestreport'),
(64, 'Can view Patient Test Report', 16, 'view_patienttestreport'),
(65, 'Can add Patient Test', 17, 'add_patienttest'),
(66, 'Can change Patient Test', 17, 'change_patienttest'),
(67, 'Can delete Patient Test', 17, 'delete_patienttest'),
(68, 'Can view Patient Test', 17, 'view_patienttest'),
(69, 'Can add Patient Medicine', 18, 'add_patientmedicine'),
(70, 'Can change Patient Medicine', 18, 'change_patientmedicine'),
(71, 'Can delete Patient Medicine', 18, 'delete_patientmedicine'),
(72, 'Can view Patient Medicine', 18, 'view_patientmedicine'),
(73, 'Can add Doctor Schedule', 19, 'add_doctorschedule'),
(74, 'Can change Doctor Schedule', 19, 'change_doctorschedule'),
(75, 'Can delete Doctor Schedule', 19, 'delete_doctorschedule'),
(76, 'Can view Doctor Schedule', 19, 'view_doctorschedule');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'doctor_app', 'appointmentlist'),
(8, 'doctor_app', 'doctordepartment'),
(9, 'doctor_app', 'doctorlist'),
(19, 'doctor_app', 'doctorschedule'),
(10, 'doctor_app', 'hospitallist'),
(11, 'doctor_app', 'medicaltests'),
(12, 'doctor_app', 'pathologistlist'),
(13, 'doctor_app', 'patientlist'),
(18, 'doctor_app', 'patientmedicine'),
(17, 'doctor_app', 'patienttest'),
(16, 'doctor_app', 'patienttestreport'),
(14, 'doctor_app', 'pharmacyinfo'),
(15, 'doctor_app', 'prescription'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-09-18 10:50:47.049420'),
(2, 'auth', '0001_initial', '2024-09-18 10:50:47.990121'),
(3, 'admin', '0001_initial', '2024-09-18 10:50:48.179751'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-09-18 10:50:48.193712'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-09-18 10:50:48.207716'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-09-18 10:50:48.284959'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-09-18 10:50:48.346422'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-09-18 10:50:48.411650'),
(9, 'auth', '0004_alter_user_username_opts', '2024-09-18 10:50:48.428638'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-09-18 10:50:48.482519'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-09-18 10:50:48.491532'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-09-18 10:50:48.505520'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-09-18 10:50:48.530186'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-09-18 10:50:48.573291'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-09-18 10:50:48.698260'),
(16, 'auth', '0011_update_proxy_permissions', '2024-09-18 10:50:48.734240'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-09-18 10:50:48.763222'),
(18, 'doctor_app', '0001_initial', '2024-09-18 10:50:51.263813'),
(19, 'sessions', '0001_initial', '2024-09-18 10:50:51.357556'),
(20, 'doctor_app', '0002_auto_20240920_0021', '2024-09-19 18:21:09.905321');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('cwqwncciw9djo08bm26tyk7nobiqiadr', '.eJxljDEKgDAUQ69S_iyCq5NuLj2DRFu06G_F1kHEu2uFiuCWkJd3kHJ9cGtrFJVFlpoFaypJqlxIjN3WiQYell5AM8x8Ezw6z7DVEHveO76RzevX9-SPrZ4meCENEpdEiMNfE_YlXhcEo22g8wKbmjvo:1srMAU:TlTWXI82u5JmqqxLZCPBegVJ_--e6TL6s_M2X3U4YbE', '2024-10-03 18:46:18.320225');

-- --------------------------------------------------------

--
-- Table structure for table `doctor_department`
--

CREATE TABLE `doctor_department` (
  `id` bigint(20) NOT NULL,
  `department_name` varchar(100) NOT NULL,
  `details` longtext NOT NULL,
  `create_date` date NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `doctor_department`
--

INSERT INTO `doctor_department` (`id`, `department_name`, `details`, `create_date`, `status`) VALUES
(1, 'ENT', 'This is ENT Department', '0000-00-00', 1),
(2, 'Cardiology', 'This is Cardiology department', '0000-00-00', 1);

-- --------------------------------------------------------

--
-- Table structure for table `doctor_list`
--

CREATE TABLE `doctor_list` (
  `id` bigint(20) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `user_email` varchar(100) NOT NULL,
  `user_password` varchar(100) DEFAULT NULL,
  `user_phone` varchar(100) DEFAULT NULL,
  `user_nid` varchar(100) DEFAULT NULL,
  `running_age` varchar(100) DEFAULT NULL,
  `gender` varchar(10) NOT NULL,
  `fathers_name` varchar(100) NOT NULL,
  `mothers_name` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `qualification` varchar(255) NOT NULL,
  `spectialist` varchar(255) NOT NULL,
  `working_hour` varchar(100) NOT NULL,
  `weekly_off_day` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `zipcode` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `user_images` varchar(100) NOT NULL,
  `upload_date` date NOT NULL,
  `status` tinyint(1) NOT NULL,
  `department_id` bigint(20) DEFAULT NULL,
  `hospital_name_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `doctor_list`
--

INSERT INTO `doctor_list` (`id`, `first_name`, `last_name`, `user_email`, `user_password`, `user_phone`, `user_nid`, `running_age`, `gender`, `fathers_name`, `mothers_name`, `designation`, `qualification`, `spectialist`, `working_hour`, `weekly_off_day`, `city`, `state`, `zipcode`, `address`, `user_images`, `upload_date`, `status`, `department_id`, `hospital_name_id`) VALUES
(1, 'Md. Mahbub', 'Hasan', 'mhosman@gmail.com', '123456', '01902353784', '34434343434', '45', 'Male', 'Rashid Mia', 'Somola Akter', 'Associate Professor, ENT & Head Neck Surgery', 'MBBS, FCPS (ENT), MS (ENT)', 'Specialist & Head Neck Surgeon', '04:00 - 10:00', 'Friday', 'Kendua', 'Netrokona', '2480', 'Test', '', '0000-00-00', 0, 1, 1),
(2, 'Lt. Col. Dr. Md. Momin Uddin ', 'Kallol', 'kallol@gmail.com', '12345678', '01902353784', '34434343434', '45', 'Male', 'Rashid Mia', 'Somola Akter', 'Classified ENT Specialist & Head Neck Surgeon, ENT', 'MBBS (SSMC), FCPS (ENT), DLO, MCPS', 'ENT (Ear, Nose, Throat) Specialist & Head Neck Cancer Surgeon', '04:00 - 10:00', 'Friday', 'Kendua', 'Netrokona', '2480', 'Test', '', '0000-00-00', 0, 1, 1),
(5, 'M.H', 'Osman', 'mhosman2@gmail.com', '123456', '01902353784', '34434343434', '45', 'Male', 'Rashid Mia', 'Somola Akter', 'Associate Professor, ENT & Head Neck Surgery', 'MBBS, FCPS (ENT), MS (ENT)', 'Specialist & Head Neck Surgeon', '04:00 - 10:00', 'Friday', 'Kendua', 'Netrokona', '2480', 'Test', '', '0000-00-00', 0, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `doctor_schedule`
--

CREATE TABLE `doctor_schedule` (
  `id` bigint(20) NOT NULL,
  `schedule_time_in` time(6) DEFAULT NULL,
  `schedule_time_out` time(6) DEFAULT NULL,
  `schedule_date` date NOT NULL,
  `create_date` date NOT NULL,
  `status` tinyint(1) NOT NULL,
  `doctor_name_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `doctor_schedule`
--

INSERT INTO `doctor_schedule` (`id`, `schedule_time_in`, `schedule_time_out`, `schedule_date`, `create_date`, `status`, `doctor_name_id`) VALUES
(1, '04:00:00.000000', '05:00:00.000000', '2024-09-21', '0000-00-00', 1, 1),
(2, '06:00:00.000000', '07:00:00.000000', '2024-09-21', '0000-00-00', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `hospital_info`
--

CREATE TABLE `hospital_info` (
  `id` bigint(20) NOT NULL,
  `hospital_name` varchar(100) DEFAULT NULL,
  `hotline` varchar(100) DEFAULT NULL,
  `address` longtext DEFAULT NULL,
  `web_link` varchar(100) DEFAULT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `hospital_info`
--

INSERT INTO `hospital_info` (`id`, `hospital_name`, `hotline`, `address`, `web_link`, `status`) VALUES
(1, 'Alchemi Hospital Pvt. Ltd.', '1234567', 'Charpara moor, Mymensingh.', NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `medical_tests`
--

CREATE TABLE `medical_tests` (
  `id` bigint(20) NOT NULL,
  `test_name` varchar(100) NOT NULL,
  `short_name` varchar(40) NOT NULL,
  `test_price` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `pathologist_list`
--

CREATE TABLE `pathologist_list` (
  `id` bigint(20) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `user_password` varchar(100) NOT NULL,
  `user_phone` varchar(100) NOT NULL,
  `working_hour` varchar(100) NOT NULL,
  `weekly_off_day` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `spectialist` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `zipcode` varchar(100) NOT NULL,
  `address1` longtext NOT NULL,
  `address2` longtext NOT NULL,
  `created` date NOT NULL,
  `status` tinyint(1) NOT NULL,
  `department_id` bigint(20) DEFAULT NULL,
  `hospital_name_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `patient_list`
--

CREATE TABLE `patient_list` (
  `id` bigint(20) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `user_email` varchar(100) DEFAULT NULL,
  `user_password` varchar(100) DEFAULT NULL,
  `user_phone` varchar(100) DEFAULT NULL,
  `user_nid` varchar(100) DEFAULT NULL,
  `running_age` varchar(100) DEFAULT NULL,
  `gender` varchar(3) NOT NULL,
  `fathers_name` varchar(100) NOT NULL,
  `mothers_name` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `zipcode` varchar(100) NOT NULL,
  `address1` longtext DEFAULT NULL,
  `address2` longtext DEFAULT NULL,
  `patient_images` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `patient_list`
--

INSERT INTO `patient_list` (`id`, `first_name`, `last_name`, `user_email`, `user_password`, `user_phone`, `user_nid`, `running_age`, `gender`, `fathers_name`, `mothers_name`, `city`, `state`, `zipcode`, `address1`, `address2`, `patient_images`, `status`, `created`) VALUES
(1, 'Md. Akkas', 'Mia', 'akkas@gmail.com', '12345678', '01902353773', '1234567', '23', 'Mal', 'Rashid Mia', 'Somola Akter', 'Kendua', 'Netrokona', '2480', 'Horipur, Amtola, Kendua.', NULL, '', 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `patient_medicine`
--

CREATE TABLE `patient_medicine` (
  `id` bigint(20) NOT NULL,
  `medicine_name` longtext NOT NULL,
  `created` date NOT NULL,
  `status` tinyint(1) NOT NULL,
  `appointment_id` bigint(20) DEFAULT NULL,
  `doctor_name_id` bigint(20) NOT NULL,
  `patient_name_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `patient_tests`
--

CREATE TABLE `patient_tests` (
  `id` bigint(20) NOT NULL,
  `created` date NOT NULL,
  `status` tinyint(1) NOT NULL,
  `appointment_id` bigint(20) DEFAULT NULL,
  `doctor_name_id` bigint(20) DEFAULT NULL,
  `patient_name_id` bigint(20) DEFAULT NULL,
  `test_name_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `patient_test_report`
--

CREATE TABLE `patient_test_report` (
  `id` bigint(20) NOT NULL,
  `test_report` longtext NOT NULL,
  `create_date` date NOT NULL,
  `status` tinyint(1) NOT NULL,
  `appointment_id` bigint(20) DEFAULT NULL,
  `doctor_name_id` bigint(20) DEFAULT NULL,
  `pathologist_name_id` bigint(20) DEFAULT NULL,
  `patient_name_id` bigint(20) DEFAULT NULL,
  `test_name_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `pharmacy_info`
--

CREATE TABLE `pharmacy_info` (
  `id` bigint(20) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `user_password` varchar(100) NOT NULL,
  `user_phone` varchar(100) NOT NULL,
  `pharmacy_name` varchar(100) NOT NULL,
  `pharmacy_address` longtext NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `zipcode` varchar(100) NOT NULL,
  `address1` longtext NOT NULL,
  `address2` longtext NOT NULL,
  `created` date NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `prescription`
--

CREATE TABLE `prescription` (
  `id` bigint(20) NOT NULL,
  `test_name` longtext NOT NULL,
  `Medicine_name` longtext NOT NULL,
  `serial_number` int(11) NOT NULL,
  `created` date NOT NULL,
  `status` tinyint(1) NOT NULL,
  `doctor_name_id` bigint(20) NOT NULL,
  `patient_name_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment_list`
--
ALTER TABLE `appointment_list`
  ADD PRIMARY KEY (`id`),
  ADD KEY `appointment_list_doctor_name_id_f2e77b07_fk_doctor_list_id` (`doctor_name_id`),
  ADD KEY `appointment_list_patient_name_id_82e7096d_fk_patient_list_id` (`patient_name_id`),
  ADD KEY `appointment_list_schedule_name_id_c68f7fd6_fk_doctor_schedule_id` (`schedule_name_id`);

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
-- Indexes for table `doctor_department`
--
ALTER TABLE `doctor_department`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `doctor_list`
--
ALTER TABLE `doctor_list`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_email` (`user_email`),
  ADD KEY `doctor_list_hospital_name_id_5b8e6856_fk_hospital_info_id` (`hospital_name_id`),
  ADD KEY `doctor_list_department_id_0dabd646_fk_doctor_department_id` (`department_id`);

--
-- Indexes for table `doctor_schedule`
--
ALTER TABLE `doctor_schedule`
  ADD PRIMARY KEY (`id`),
  ADD KEY `doctor_schedule_doctor_name_id_f645936c_fk_doctor_list_id` (`doctor_name_id`);

--
-- Indexes for table `hospital_info`
--
ALTER TABLE `hospital_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `medical_tests`
--
ALTER TABLE `medical_tests`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pathologist_list`
--
ALTER TABLE `pathologist_list`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_email` (`user_email`),
  ADD KEY `pathologist_list_department_id_e7024f74_fk_doctor_department_id` (`department_id`),
  ADD KEY `pathologist_list_hospital_name_id_d42f64df_fk_hospital_info_id` (`hospital_name_id`);

--
-- Indexes for table `patient_list`
--
ALTER TABLE `patient_list`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_email` (`user_email`);

--
-- Indexes for table `patient_medicine`
--
ALTER TABLE `patient_medicine`
  ADD PRIMARY KEY (`id`),
  ADD KEY `patient_medicine_appointment_id_f37b830a_fk_appointment_list_id` (`appointment_id`),
  ADD KEY `patient_medicine_doctor_name_id_3cbe6634_fk_doctor_list_id` (`doctor_name_id`),
  ADD KEY `patient_medicine_patient_name_id_430db101_fk_patient_list_id` (`patient_name_id`);

--
-- Indexes for table `patient_tests`
--
ALTER TABLE `patient_tests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `patient_tests_appointment_id_28db77c5_fk_appointment_list_id` (`appointment_id`),
  ADD KEY `patient_tests_doctor_name_id_a7380b1c_fk_doctor_list_id` (`doctor_name_id`),
  ADD KEY `patient_tests_patient_name_id_67f5ef68_fk_patient_list_id` (`patient_name_id`),
  ADD KEY `patient_tests_test_name_id_8848ff6b_fk_medical_tests_id` (`test_name_id`);

--
-- Indexes for table `patient_test_report`
--
ALTER TABLE `patient_test_report`
  ADD PRIMARY KEY (`id`),
  ADD KEY `patient_test_report_appointment_id_03b25d4c_fk_appointme` (`appointment_id`),
  ADD KEY `patient_test_report_doctor_name_id_41d58486_fk_doctor_list_id` (`doctor_name_id`),
  ADD KEY `patient_test_report_pathologist_name_id_9eab69b3_fk_pathologi` (`pathologist_name_id`),
  ADD KEY `patient_test_report_patient_name_id_3b572cd4_fk_patient_list_id` (`patient_name_id`),
  ADD KEY `patient_test_report_test_name_id_4013b1e8_fk_medical_tests_id` (`test_name_id`);

--
-- Indexes for table `pharmacy_info`
--
ALTER TABLE `pharmacy_info`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_email` (`user_email`);

--
-- Indexes for table `prescription`
--
ALTER TABLE `prescription`
  ADD PRIMARY KEY (`id`),
  ADD KEY `prescription_doctor_name_id_2427a02d_fk_doctor_list_id` (`doctor_name_id`),
  ADD KEY `prescription_patient_name_id_ddf01765_fk_patient_list_id` (`patient_name_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment_list`
--
ALTER TABLE `appointment_list`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `doctor_department`
--
ALTER TABLE `doctor_department`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `doctor_list`
--
ALTER TABLE `doctor_list`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `doctor_schedule`
--
ALTER TABLE `doctor_schedule`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hospital_info`
--
ALTER TABLE `hospital_info`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `medical_tests`
--
ALTER TABLE `medical_tests`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pathologist_list`
--
ALTER TABLE `pathologist_list`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `patient_list`
--
ALTER TABLE `patient_list`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `patient_medicine`
--
ALTER TABLE `patient_medicine`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `patient_tests`
--
ALTER TABLE `patient_tests`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `patient_test_report`
--
ALTER TABLE `patient_test_report`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pharmacy_info`
--
ALTER TABLE `pharmacy_info`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `prescription`
--
ALTER TABLE `prescription`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appointment_list`
--
ALTER TABLE `appointment_list`
  ADD CONSTRAINT `appointment_list_doctor_name_id_f2e77b07_fk_doctor_list_id` FOREIGN KEY (`doctor_name_id`) REFERENCES `doctor_list` (`id`),
  ADD CONSTRAINT `appointment_list_patient_name_id_82e7096d_fk_patient_list_id` FOREIGN KEY (`patient_name_id`) REFERENCES `patient_list` (`id`),
  ADD CONSTRAINT `appointment_list_schedule_name_id_c68f7fd6_fk_doctor_schedule_id` FOREIGN KEY (`schedule_name_id`) REFERENCES `doctor_schedule` (`id`);

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
-- Constraints for table `doctor_list`
--
ALTER TABLE `doctor_list`
  ADD CONSTRAINT `doctor_list_department_id_0dabd646_fk_doctor_department_id` FOREIGN KEY (`department_id`) REFERENCES `doctor_department` (`id`),
  ADD CONSTRAINT `doctor_list_hospital_name_id_5b8e6856_fk_hospital_info_id` FOREIGN KEY (`hospital_name_id`) REFERENCES `hospital_info` (`id`);

--
-- Constraints for table `doctor_schedule`
--
ALTER TABLE `doctor_schedule`
  ADD CONSTRAINT `doctor_schedule_doctor_name_id_f645936c_fk_doctor_list_id` FOREIGN KEY (`doctor_name_id`) REFERENCES `doctor_list` (`id`);

--
-- Constraints for table `pathologist_list`
--
ALTER TABLE `pathologist_list`
  ADD CONSTRAINT `pathologist_list_department_id_e7024f74_fk_doctor_department_id` FOREIGN KEY (`department_id`) REFERENCES `doctor_department` (`id`),
  ADD CONSTRAINT `pathologist_list_hospital_name_id_d42f64df_fk_hospital_info_id` FOREIGN KEY (`hospital_name_id`) REFERENCES `hospital_info` (`id`);

--
-- Constraints for table `patient_medicine`
--
ALTER TABLE `patient_medicine`
  ADD CONSTRAINT `patient_medicine_appointment_id_f37b830a_fk_appointment_list_id` FOREIGN KEY (`appointment_id`) REFERENCES `appointment_list` (`id`),
  ADD CONSTRAINT `patient_medicine_doctor_name_id_3cbe6634_fk_doctor_list_id` FOREIGN KEY (`doctor_name_id`) REFERENCES `doctor_list` (`id`),
  ADD CONSTRAINT `patient_medicine_patient_name_id_430db101_fk_patient_list_id` FOREIGN KEY (`patient_name_id`) REFERENCES `patient_list` (`id`);

--
-- Constraints for table `patient_tests`
--
ALTER TABLE `patient_tests`
  ADD CONSTRAINT `patient_tests_appointment_id_28db77c5_fk_appointment_list_id` FOREIGN KEY (`appointment_id`) REFERENCES `appointment_list` (`id`),
  ADD CONSTRAINT `patient_tests_doctor_name_id_a7380b1c_fk_doctor_list_id` FOREIGN KEY (`doctor_name_id`) REFERENCES `doctor_list` (`id`),
  ADD CONSTRAINT `patient_tests_patient_name_id_67f5ef68_fk_patient_list_id` FOREIGN KEY (`patient_name_id`) REFERENCES `patient_list` (`id`),
  ADD CONSTRAINT `patient_tests_test_name_id_8848ff6b_fk_medical_tests_id` FOREIGN KEY (`test_name_id`) REFERENCES `medical_tests` (`id`);

--
-- Constraints for table `patient_test_report`
--
ALTER TABLE `patient_test_report`
  ADD CONSTRAINT `patient_test_report_appointment_id_03b25d4c_fk_appointme` FOREIGN KEY (`appointment_id`) REFERENCES `appointment_list` (`id`),
  ADD CONSTRAINT `patient_test_report_doctor_name_id_41d58486_fk_doctor_list_id` FOREIGN KEY (`doctor_name_id`) REFERENCES `doctor_list` (`id`),
  ADD CONSTRAINT `patient_test_report_pathologist_name_id_9eab69b3_fk_pathologi` FOREIGN KEY (`pathologist_name_id`) REFERENCES `pathologist_list` (`id`),
  ADD CONSTRAINT `patient_test_report_patient_name_id_3b572cd4_fk_patient_list_id` FOREIGN KEY (`patient_name_id`) REFERENCES `patient_list` (`id`),
  ADD CONSTRAINT `patient_test_report_test_name_id_4013b1e8_fk_medical_tests_id` FOREIGN KEY (`test_name_id`) REFERENCES `medical_tests` (`id`);

--
-- Constraints for table `prescription`
--
ALTER TABLE `prescription`
  ADD CONSTRAINT `prescription_doctor_name_id_2427a02d_fk_doctor_list_id` FOREIGN KEY (`doctor_name_id`) REFERENCES `doctor_list` (`id`),
  ADD CONSTRAINT `prescription_patient_name_id_ddf01765_fk_patient_list_id` FOREIGN KEY (`patient_name_id`) REFERENCES `patient_list` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;