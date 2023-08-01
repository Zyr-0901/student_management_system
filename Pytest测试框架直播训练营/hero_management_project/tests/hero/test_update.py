import allure
import pytest
from deal_yaml import DealYaml
from hero.hero_management import HeroManagement


@pytest.mark.heroValid
@pytest.mark.parametrize('name, volume, desc',
                         DealYaml.load_yaml("datas/hero_management.yaml").
                         get("update").
                         get("datas").
                         get("validDates"))
def test_update_valid(name, volume, desc):
    """
    :param name:
    :param volume:
    :param desc:
    :return:
    """
    allure.dynamic.title(desc)
    management = HeroManagement()
    with allure.step(f"步骤一: 设置参数, name: {name}, volume: {volume}"):
        result = management.update_hero(name, volume)
    with allure.step("步骤二: 判断更新后的信息与实际信息是否一致"):
        assert result[volume] == volume


@pytest.mark.xfail
@pytest.mark.heroInvalid
@pytest.mark.parametrize('name, volume, desc',
                         DealYaml.load_yaml('datas/hero_management.yaml').
                         get("update").
                         get("datas").
                         get("invalidDates"))
def test_update_invalid(name, volume, desc):
    """
    :param name:
    :param volume:
    :param desc:
    :return:
    """
    allure.dynamic.title(desc)
    management = HeroManagement()
    with allure.step(f"步骤一: 设置参数, name: {name}, volume: {volume}"):
        result = management.update_hero(name, volume)
    with allure.step("步骤二: 判断更新后的信息与实际信息是否一致"):
        assert result[volume] == volume