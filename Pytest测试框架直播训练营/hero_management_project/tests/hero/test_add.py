# 修改建议
# 1. 只对create_hero做了测试，其他方法的也可以写一下
# 2. 测试数据太少，根据等价类方法，各种组合的情况可以多设计一些
# 3. @pytest.mark.parametrize('volumes_update',
#                          DealYaml.load_yaml('datas/hero_add.yaml').get('validDatas'),
#                          indirect=True)
# def test_add_valid(volumes_update):
#     name = volumes_update[0]
#     volume = volumes_update[1]
#     power = volumes_update[2]
#     desc = volumes_update[3]
#
# 这段代码也可以改造成下面的格式：
# @pytest.mark.createHeroInvalid
# @pytest.mark.parametrize('name, volume, power, desc',
#                          DealYaml.load_yaml('datas/hero_add.yaml').get('validDatas'))
# def test_add_valid(name, volume, power, desc):

# TODO
# 修改建议中的 test_add_valid(name, volume, power, desc): 改造,这边我用了fixture,还可以这样传参吗?

import allure
import pytest
from deal_yaml import DealYaml
from hero.hero_management import HeroManagement


@pytest.fixture(params=DealYaml.load_yaml('datas/hero_management.yaml').get("add").get("datas").get("validDates"))
def create_hero_params(request):
    """
    获取传入参数
    处理参数
    返回参数
    执行测试用例
    """
    params = request.param
    params[1] += 1
    return params


@pytest.mark.heroValid
# @pytest.mark.parametrize('name, volume, power, desc',
#                          DealYaml.load_yaml('datas/hero_management.yaml').
#                          get("add").
#                          get("datas").
#                          get("validDates"))
def test_add_valid(create_hero_params):
    """
    :param name:
    :param volume:
    :param power:
    :param desc:
    :return:

    获取当前英雄数量
    创建英雄
    在次获取英雄数量
    判断数量是否加1
    """
    name, volume, power, desc = create_hero_params
    allure.dynamic.title(desc)
    management = HeroManagement()
    with allure.step("步骤一: 获取当前英雄个数"):
        pre_count = len(management.hero_list)
    with allure.step("步骤二: 根据参数创建英雄"):
        management.create_hero(name, volume, power)
    with allure.step("步骤三: 获取创建后的英雄个数"):
        back_count = len(management.hero_list)
    with allure.step("步骤四: 断言,判断英雄总数是否加1"):
        assert pre_count + 1 == back_count


@pytest.mark.xfail
@pytest.mark.heroInvalid
# @pytest.mark.parametrize('name, volume, power, desc',
#                          DealYaml.load_yaml('datas/hero_management.yaml').
#                          get("add").
#                          get("datas").
#                          get("invalidDates"))
def test_add_invalid(create_hero_params):
    """
    :param name:
    :param volume:
    :param power:
    :param desc:
    :return:

    获取当前英雄数量
    创建英雄
    在次获取英雄数量
    判断数量是否加1
    """
    name, volume, power, desc = create_hero_params
    allure.dynamic.title(desc)
    management = HeroManagement()
    with allure.step("步骤一: 获取当前英雄个数"):
        pre_count = len(management.hero_list)
    with allure.step("步骤二: 根据参数创建英雄"):
        management.create_hero(name, volume, power)
    with allure.step("步骤三: 获取创建后的英雄个数"):
        back_count = len(management.hero_list)
    with allure.step("步骤四: 断言,判断英雄总数是否加1"):
        assert pre_count + 1 == back_count
