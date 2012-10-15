# Install script for directory: /home/john/src/clean_install/gr-dt/python

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "dt_python")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/dt" TYPE FILE FILES
    "/home/john/src/clean_install/gr-dt/python/__init__.py"
    "/home/john/src/clean_install/gr-dt/python/get_usrp_time.py"
    "/home/john/src/clean_install/gr-dt/python/my_first_python_block.py"
    "/home/john/src/clean_install/gr-dt/python/my_first_msg_block.py"
    "/home/john/src/clean_install/gr-dt/python/my_second_msg_block.py"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "dt_python")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "dt_python")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/dt" TYPE FILE FILES
    "/home/john/src/clean_install/gr-dt/build/python/__init__.pyc"
    "/home/john/src/clean_install/gr-dt/build/python/get_usrp_time.pyc"
    "/home/john/src/clean_install/gr-dt/build/python/my_first_python_block.pyc"
    "/home/john/src/clean_install/gr-dt/build/python/my_first_msg_block.pyc"
    "/home/john/src/clean_install/gr-dt/build/python/my_second_msg_block.pyc"
    "/home/john/src/clean_install/gr-dt/build/python/__init__.pyo"
    "/home/john/src/clean_install/gr-dt/build/python/get_usrp_time.pyo"
    "/home/john/src/clean_install/gr-dt/build/python/my_first_python_block.pyo"
    "/home/john/src/clean_install/gr-dt/build/python/my_first_msg_block.pyo"
    "/home/john/src/clean_install/gr-dt/build/python/my_second_msg_block.pyo"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "dt_python")

