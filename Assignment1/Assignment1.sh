#!/bin/bash
# Script to compile and execute a c program in one step.

# Get file name without the .c extension
file_name=$(echo $1|sed 's/\(.*\)\.c/\1/')

# Compile the program with -o option to specify the name of the binary
gcc -o $file_name.out $1

# If there were no compilation errors, run the program
if [[ $? -eq 0 ]]; then
        ./$file_name.out
fi