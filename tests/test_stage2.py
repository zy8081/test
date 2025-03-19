import subprocess


# 任务1：规则解析、存储与检查


# 任务2: 进行你的第一次编译
def test_first_run_makefile(minimake_executable):
    """测试正确的 Makefile 解析"""
    result = subprocess.run(
        [minimake_executable, "app"],
        capture_output=True,
        text=True,
        cwd="tests/assets/sandbox/test_first_run_makefile",
    )
    assert result.returncode == 0
    assert "Parsed successfully" in result.stdout
