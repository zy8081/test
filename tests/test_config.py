# Desc: 测试配置文件,全局配置,用于动态指定 minimake 的路径
import os
import pytest

@pytest.fixture(scope="session")
def minimake_executable():
    """获取 minimake 可执行文件路径，支持环境变量设置"""
    return os.getenv("MINIMAKE_PATH", "./minimake")  # 默认当前目录
