#!/bin/bash
# 环境变量设置
export MINIMAKE_PATH=$(pwd)/minimake

# 检查python是否安装,是否是3以上版本
test_python_version() {
    python_version=$(python3 -V 2>&1 | awk '{print $2}')
    if [[ $python_version < 3 ]]; then
        echo "python version is less than 3"
        exit 1
    else
        echo "python version is $python_version"
    fi
}

# 检测pytest是否安装
test_pytest() {
    pytest_version=$(pytest --version)
    if [[ $? -ne 0 ]]; then
        echo "pytest is not installed"
        echo "please run 'pip install pytest' to install pytest"
        exit 1
    else
        echo "pytest version is $pytest_version"
    fi
}

test_python_version
test_pytest

# 检验 MINIMAKE_PATH 环境变量

echo "MINIMAKE_PATH is $MINIMAKE_PATH"

# 检测minimake是否存在
if [[ ! -d $MINIMAKE_PATH ]]; then
    echo "minimake is not exist"
    echo "please check ./test.sh:3 MINIMAKE_PATH is correct"
    exit 1
fi

# 运行测试用例
pytest