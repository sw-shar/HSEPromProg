cmake_minimum_required(VERSION 3.5)

set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)

set(CMAKE_INSTALL_RPATH "$ORIGIN/../lib")



project(Task4)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${Task4_SOURCE_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${Task4_SOURCE_DIR}/lib)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/e2239ee6043f73722e7aa812a459f54a28552929.zip
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

add_subdirectory(B)
add_subdirectory(C)

