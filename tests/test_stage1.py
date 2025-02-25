import subprocess

# 任务1:命令行参数解析
def test_help_option(minimake_executable):
    """测试 --help 选项"""
    result = subprocess.run([minimake_executable, "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Usage" in result.stdout  # 确保有 Usage 提示

def test_invalid_option(minimake_executable):
    """测试无效选项"""
    result = subprocess.run([minimake_executable, "--iudwehiuwehiudhiuw"], capture_output=True, text=True)
    assert result.returncode != 0  # 错误返回值
    assert "Unknown option" in result.stderr

# 任务2:简单命令执行