def test_phony_target(minimake_executable):
    """测试 .PHONY 目标"""
    result = subprocess.run([minimake_executable, "clean", "-f", "tests/assets/Makefile_advanced"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Cleaning" in result.stdout

def test_variable_replacement(minimake_executable):
    """测试变量解析"""
    result = subprocess.run([minimake_executable, "-f", "tests/assets/Makefile_advanced"], capture_output=True, text=True)
    assert "Using compiler: gcc" in result.stdout
