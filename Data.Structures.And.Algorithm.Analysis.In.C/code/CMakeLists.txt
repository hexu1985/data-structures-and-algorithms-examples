# set minimum cmake version
cmake_minimum_required(VERSION 3.5 FATAL_ERROR)

# project name and language
project(project LANGUAGES C)

add_executable(testlist testlist.c list.c)
add_executable(teststkl teststkl.c stackli.c)
