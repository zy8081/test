import subprocess
import os
import time

def test_dependency_check(minimake_executable):
    """测试依赖检查"""
    target_file = "tests/assets/sample_code/app"
    dep_file = "tests/assets/sample_code/main.c"

    # 先清理旧文件
    if os.path.exists(target_file):
        os.remove(target_file)

    # 运行 minimake 进行编译
    result = subprocess.run([minimake_executable, "-f", "tests/assets/Makefile_basic"], capture_output=True, text=True)
    assert result.returncode == 0
    assert os.path.exists(target_file)  # 目标文件生成

    # 修改依赖文件时间戳
    time.sleep(1)  # 避免时间戳相同
    os.utime(dep_file, None)

    # 再次运行 minimake，应触发重新编译
    result = subprocess.run([minimake_executable, "-f", "tests/assets/Makefile_basic"], capture_output=True, text=True)
    assert "Rebuilding" in result.stdout

def test_circular_dependency(minimake_executable):
    """测试循环依赖检测"""
    result = subprocess.run([minimake_executable, "-f", "tests/assets/Makefile_circular"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "Circular dependency detected" in result.stderr
