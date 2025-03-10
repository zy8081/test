import subprocess

# 任务1: 预处理与文件读取

# 任务3：规则解析与存储

# 任务2: 静态语法检查
def test_valid_makefile(minimake_executable):
    """测试正确的 Makefile 解析"""
    result = subprocess.run([minimake_executable, "-f", "tests/assets/Makefile_basic"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Parsed successfully" in result.stdout

def test_invalid_makefile(minimake_executable):
    """测试无效 Makefile 解析错误"""
    result = subprocess.run([minimake_executable, "-f", "tests/assets/Makefile_invalid"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "Syntax error" in result.stderr

# 任务3：规则解析与存储