import allure
import pytest
from deal_yaml import DealYaml
from hero.hero_management import HeroManagement


@pytest.mark.heroValid
@pytest.mark.parametrize('name, desc',
                         DealYaml.load_yaml('datas/hero_management.yaml').
                         get("find").
                         get("datas").
                         get("validDatas"))
def test_find_valid(name, desc):
    """
    :param name:
    :param desc:
    :return:
    """
    allure.dynamic.title(desc)
    management = HeroManagement()
    with allure.step(f"步骤一: 设置参数 name: {name},调用find_hero"):
        result = management.find_hero(name)
    with allure.step("步骤二: 断言,判断是否有数据返回"):
        assert result


@pytest.mark.xfail
@pytest.mark.heroInvalid
@pytest.mark.parametrize('name, desc',
                         DealYaml.load_yaml('datas/hero_management.yaml').
                         get("find").get("datas").get("invalidDatas"))
def test_find_invalid(name, desc):
    """
    :param name:
    :param desc:
    :return:
    """
    allure.dynamic.title(desc)
    management = HeroManagement()
    with allure.step(f"步骤一: 设置参数 name: {name}, 调用find_hreo"):
        result = management.find_hero(name)
    with allure.step("步骤二: 断言,判断是否有数据返回"):
        assert result
