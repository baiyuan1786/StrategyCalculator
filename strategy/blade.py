##########################################################################################################
#   Description: 刃系策略
#   Authors:     BaiYuan <395642104@qq.com>
##########################################################################################################

from .base import Strategy, StrategyTree

class 飞剑(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "刃", subclass = "飞剑")

        self.add(newStra = Strategy(name = "冲刺飞剑", level = 0, location = "冲刺", entity = ["飞剑"]))

        self.add(newStra = Strategy(name = "长距飞剑", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "染血飞剑", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "闪避飞剑", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "多重飞剑", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "嗜血飞剑", level = 3, location = "冲刺", trigger = ["冲刺飞剑"], entity = ["飞剑", "撕裂"]))
        self.add(newStra = Strategy(name = "双向飞剑", level = 3, location = "冲刺", trigger = ["冲刺飞剑"], entity = ["飞剑"]))

class 撕裂(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "刃", subclass = "撕裂")

        self.add(newStra = Strategy(name = "普攻撕裂", level = 0, location = "普攻", entity = ["撕裂"]))
        self.add(newStra = Strategy(name = "技能撕裂", level = 0, location = "技能", entity = ["撕裂"]))

        self.add(newStra = Strategy(name = "短距撕裂", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "撕裂加深", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "撕裂冲击", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "致命撕裂", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "针对影刺", level = 3, location = "auto", trigger = ["普攻撕裂"], entity = ["撕裂", "影刺"]))
        self.add(newStra = Strategy(name = "针对影刺", level = 3, location = "auto", trigger = ["技能撕裂"], entity = ["撕裂", "影刺"]))
        self.add(newStra = Strategy(name = "撕裂光阵", level = 3, location = "普攻", trigger = ["普攻撕裂", "召唤光阵"], entity = ["撕裂", "光阵"]))
        self.add(newStra = Strategy(name = "撕裂光阵", level = 3, location = "技能", trigger = ["技能撕裂", "召唤光阵"], entity = ["撕裂", "光阵"]))

class 刃环(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "刃", subclass = "刃环")

        self.add(newStra = Strategy(name = "召唤刃环", level = 0, location = "召唤", entity = ["刃环"]))

        self.add(newStra = Strategy(name = "精密切割", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "大号刃环", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "刃环拉扯", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "受击刃环", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "双生刃环", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "召唤回旋刃", level = 3, location = "auto", trigger = ["召唤刃环"], entity = ["刃环"]))
        self.add(newStra = Strategy(name = "嗜血刃环", level = 3, location = "auto", trigger = ["召唤刃环"], entity = ["刃环", "撕裂"]))
        self.add(newStra = Strategy(name = "连续刃环", level = 3, location = "auto", trigger = ["技能毒环"], entity = ["刃环", "毒环"]))

class 刀刃风暴(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "刃", subclass = "刀刃风暴")

        self.add(newStra = Strategy(name = "传承技风暴", level = 0, location = "传承技", entity = ["刀刃风暴"]))
        self.add(newStra = Strategy(name = "技能风暴", level = 0, location = "技能", entity = ["刀刃风暴"]))

        self.add(newStra = Strategy(name = "风暴拉扯", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "风暴扩大", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "风暴追踪", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "受击风暴", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "风暴加速", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "嗜血风暴", level = 3, location = "auto", trigger = ["传承技风暴"], entity = ["刀刃风暴", "撕裂"]))
        self.add(newStra = Strategy(name = "嗜血风暴", level = 3, location = "auto", trigger = ["技能风暴"], entity = ["刀刃风暴", "撕裂"]))

        self.add(newStra = Strategy(name = "黑洞刀刃", level = 3, location = "auto", trigger = ["传承技黑洞"], entity = ["刀刃风暴", "黑洞"]))

class 飞刃(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "刃", subclass = "飞刃")

        self.add(newStra = Strategy(name = "普攻飞刃", level = 0, location = "普攻", entity = ["飞刃"]))

        self.add(newStra = Strategy(name = "潜伏飞刃", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "飞刃轮舞", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "飞刃冲击", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "飞刃切割", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "传送飞刃", level = 3, location = "auto", trigger = ["普攻飞刃"], entity = ["飞刃"]))
        self.add(newStra = Strategy(name = "落雷飞刃", level = 3, location = "auto", trigger = ["冲刺落雷"], entity = ["飞刃", "落雷"]))