project(C)


add_executable(CTest main_test.cpp tests.cpp)

target_link_libraries(CTest gtest_main ClassLib)
target_include_directories(CTest PRIVATE ${Task4_SOURCE_DIR})


add_executable(C main.cpp)

target_link_libraries(C ClassLib)
target_include_directories(C PRIVATE ${Task4_SOURCE_DIR})

target_link_libraries(C gtest_main)
add_test(NAME example_test COMMAND C)

INSTALL(
    TARGETS C
    RUNTIME DESTINATION exe/bin
    LIBRARY DESTINATION exe/lib
)
