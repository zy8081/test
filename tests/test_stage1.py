import subprocess

# 任务1:命令行参数解析
def test_help_option(minimake_executable):
    """测试 --help 选项"""
    result = subprocess.run([minimake_executable, "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    # 确保有 Usage 或 用法 字样
    assert "Usage" in result.stdout or "用法" in result.stdout
    assert "--help" in result.stdout

def test_invalid_option(minimake_executable):
    """测试无效选项"""
    result = subprocess.run([minimake_executable, "--iudwehiuwehiudhiuw"], capture_output=True, text=True)
    assert result.returncode != 0  # 错误返回值
    assert "Unknown option" in result.stderr or "未识别" in result.stderr or "无效" in result.stderr or "unrecognized option" in result.stderr

# 任务2:预处理与文件读取
def test_valid_makefile(minimake_executable):
    """测试正确的 Makefile 解析"""
    # 通过切换cwd到tests/assets/sandbox/test_valid_makefile目录，确保Makefile中的相对路径正确
    print("minimake_executable:",minimake_executable)
    result = subprocess.run([minimake_executable, "-v"], capture_output=True, text=True , cwd="tests/assets/sandbox/test_valid_makefile")
    # 比较cwd下Minimake_claered.mk和Minimake_claered_expected.mk文件内容是否一致
    with open("tests/assets/sandbox/test_valid_makefile/Minimake_cleared.mk") as f:
        result_content = f.read()
    with open("tests/assets/sandbox/test_valid_makefile/Minimake_claered_expected.mk") as f:
        expected_content = f.read()
    assert result_content == expected_content
    assert result.returncode == 0
    
# 任务1: 预处理与文件读取