# 针对英雄管理系统的增加功能，完成等价类与边界值的测试。要求测试数据使用单独的文件维护。
# 使用参数化减少代码量，提高代码的可维护性。
# 原有需求发生变化，边界值都增加1（变为最大值100，最小值2）。如何在不改变原始测试数据情况下，还能依然完成对修改需求后的测试（使用fixture）。
# 编写自动化测试用例，结合 Allure 与截图技术等自动生成带截图与操作步骤的测试报告。
# 将有效等价类和无效等价类的场景分别用标签进行分类。
import os
import sys
import allure
import pytest

sys.path.append(os.getcwd())

from src.hero.hero_management import HeroManagement
from utils.deal_yaml import DealYaml


# @pytest.mark.parametrize('name, volume, power', [
#     ["张三", 30, 20],
#     ["李四", 40, 50],
#     ["王五", 50, 100],
# ])
# def test_add_hero_basic(name, volume, power):
#     # 传入测试用例
#     # 调用创建方法,创建
#     # 根据生成条数判断是否创建成功
#     manger = HeroManagement()
#     pre_len = len(manger.hero_list)
#     manger.create_hero(name, volume, power)
#     assert len(manger.hero_list) == pre_len + 1
#

# @pytest.mark.parametrize('power', [
#     10, 20, 30
# ])
# @pytest.mark.parametrize('volume', [
#     20,
#     50,
#     70
# ])
# @pytest.mark.parametrize('name', [
#     "张三",
#     "李四",
#     "王五"
# ])
# def test_add_hero_cartesian(name, volume, power):
#     manger = HeroManagement()
#     pre_len = len(manger.hero_list)
#     manger.create_hero(name, volume, power)
#     assert len(manger.hero_list) == pre_len + 1
@pytest.fixture()
def volumes_update(request):
    data = request.param
    data[1] += 1
    return data


@pytest.mark.createHeroValid
@pytest.mark.parametrize('volumes_update',
                         DealYaml.load_yaml('datas/hero_management.yaml').get('validDatas'),
                         indirect=True)
def test_add_valid(volumes_update):
    name = volumes_update[0]
    volume = volumes_update[1]
    power = volumes_update[2]
    desc = volumes_update[3]
    # 传入测试用例
    # 调用创建方法,创建
    # 根据生成条数判断是否创建成功
    allure.dynamic.title(desc)
    manger = HeroManagement()
    pre_len = len(manger.hero_list)
    with allure.step(f"步骤一: 获取参数, 姓名:{name};血量:{volume};攻击力:{power}"):
        pass
    with allure.step(f"步骤二: 创建英雄"):
        manger.create_hero(name, volume, power)

    with allure.step(f"步骤三: 判断是否创建成功"):
        assert len(manger.hero_list) == pre_len + 1


@pytest.mark.createHeroInvalid
@pytest.mark.parametrize('name, volume, power, desc',
                         DealYaml.load_yaml('datas/hero_management.yaml').get('invalidDatas'))
def test_add_invalid(name, volume, power, desc):
    # 传入测试用例
    # 调用创建方法,创建
    # 根据生成条数判断是否创建成功
    allure.dynamic.title(desc)
    manger = HeroManagement()
    pre_len = len(manger.hero_list)
    with allure.step(f"步骤一: 获取参数, 姓名:{name};血量:{volume};攻击力:{power}"):
        pass
    with allure.step(f"步骤二: 创建英雄"):
        manger.create_hero(name, volume, power)

    with allure.step(f"步骤三: 判断是否创建成功"):
        assert len(manger.hero_list) == pre_len + 1
