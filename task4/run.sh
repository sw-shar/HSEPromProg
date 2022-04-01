#!/bin/bash

set -e
set -x

mkdir -p build
cd build
cmake ..
make RunGenerator all
