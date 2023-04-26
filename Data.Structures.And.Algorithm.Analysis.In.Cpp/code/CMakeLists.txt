# set minimum cmake version
cmake_minimum_required(VERSION 3.5 FATAL_ERROR)

# project name and language
project(project LANGUAGES CXX)

add_executable(TestList TestList.cpp)
add_executable(TestRandom TestRandom.cpp Random.cpp)
add_executable(Fig10_63 Fig10_63.cpp Random.cpp)
