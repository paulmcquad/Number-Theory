cmake_minimum_required(VERSION 3.11)

find_package(TBB REQUIRED COMPONENTS tbb)

add_executable(remainder2 remainder2.cpp)
target_link_libraries(remainder2 tbb)
