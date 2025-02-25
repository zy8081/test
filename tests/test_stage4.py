import subprocess
import os

def test_build_execution(minimake_executable):
    """测试构建执行"""
    result = subprocess.run([minimake_executable, "-f", "tests/assets/Makefile_basic"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "gcc -o app main.c utils.c" in result.stdout  # 确保 gcc 被调用

def test_command_error_handling(minimake_executable):
    """测试构建错误时中断"""
    result = subprocess.run([minimake_executable, "-f", "tests/assets/Makefile_error"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "Build failed" in result.stderr
