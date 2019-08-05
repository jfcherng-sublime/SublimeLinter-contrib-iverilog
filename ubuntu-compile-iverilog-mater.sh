#!/usr/bin/env bash

# This script compiles and installs the master branch iverilog.
# Tested on Ubuntu 18.04

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
THREAD_CNT=$(getconf _NPROCESSORS_ONLN)

INSTALL_DIR="/usr/local/iverilog"

sudo apt install -y autoconf gperf

pushd "/tmp" || exit

wget "https://github.com/steveicarus/iverilog/archive/master.zip" -O "iverilog.zip"
unzip "iverilog.zip"; rm -f "iverilog.zip"

pushd "iverilog-master" || exit

autoconf || exit
./configure --prefix="${INSTALL_DIR}" || exit
make -j"${THREAD_CNT}" || exit
sudo make install || exit

popd || exit

rm -rf "iverilog-master"

popd || exit
