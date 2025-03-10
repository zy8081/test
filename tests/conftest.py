# Desc: 测试配置文件,全局配置,用于动态指定 minimake 的路径
import os
import pytest

@pytest.fixture(scope="session")
def minimake_executable():
    """获取 minimake 可执行文件路径，支持环境变量设置"""
    
    # 检测minimake路径是否存在
    if not os.path.exists(os.getenv("MINIMAKE_PATH", "./minimake")):
        raise FileNotFoundError("minimake executable not found")
    minimake_path = os.getenv("MINIMAKE_PATH", "./minimake")
    minimake_path = os.path.abspath(minimake_path)
    return minimake_path
