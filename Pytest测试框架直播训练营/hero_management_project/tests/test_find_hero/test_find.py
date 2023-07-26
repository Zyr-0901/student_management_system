# import pytest
# from hero.hero_management import HeroManagement
#
#
# @pytest.mark.parametrize('name',[
#     "张三",
#     "李四"
# ], ids=["查询张三", "查询李四"])
# def test_find_hero(name: str):
#     # 先创建数据进入
#     manager = HeroManagement()
#     manager.create_hero("张三", 10, 20)
#
#     result = manager.find_hero(name)
#     assert result
