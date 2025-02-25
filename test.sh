#!/bin/bash

# 检查python是否安装,是否是3以上版本

test_python_version() {
    python_version=$(python3 -V 2>&1 | awk '{print $2}')
    if [[ $python_version < 3 ]]; then
        echo "python version is less than 3"
        exit 1
    fi
}

test_python_version