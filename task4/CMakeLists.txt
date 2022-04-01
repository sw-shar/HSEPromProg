cmake_minimum_required(VERSION 3.5)

set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)

set(CMAKE_INSTALL_RPATH "$ORIGIN/../lib")



project(Task4)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${Task4_SOURCE_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${Task4_SOURCE_DIR}/lib)

find_package(GTest CONFIG REQUIRED)
enable_testing()

add_subdirectory(B)
add_subdirectory(C)

