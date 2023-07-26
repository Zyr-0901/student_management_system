import pytest


@pytest.fixture(scope="module")
def data_processor(request):
    data = request.param
    # 这里可以进行数据处理
    return data * 2


# 使用 @pytest mark.parametrize 和 Fixture 参数化
@pytest.mark.parametrize("input_data, expected_output", [(1, 2), (3, 6)], indirect=["data_processor"])
def test_example(input_data, expected_output):
    # 测试代码
    assert input_data == expected_output
