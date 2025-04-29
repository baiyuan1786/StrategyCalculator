##########################################################################################################
#   Description: 光系策略
#   Authors:     BaiYuan <395642104@qq.com>
##########################################################################################################

from .base import Strategy, StrategyTree

class 光枪(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "光", subclass = "光枪")

        self.add(newStra = Strategy(name = "传承技光枪", level = 0, location = "传承技", entity = ["光枪"]))
        self.add(newStra = Strategy(name = "技能光枪", level = 0, location = "技能", entity = ["光枪"]))

        self.add(newStra = Strategy(name = "圣光光枪", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "光枪禁锢", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "光枪强化", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "多重光枪", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "落雷光枪", level = 3, location = "auto", trigger = ["冲刺落雷"], entity = ["光枪", "落雷"]))
        self.add(newStra = Strategy(name = "闪光光枪", level = 3, location = "auto", trigger = ["传承技闪光"], entity = ["光枪", "闪光"]))

    
class 闪光(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "光", subclass = "闪光")

        self.add(newStra = Strategy(name = "传承技闪光", level = 0, location = "传承技", entity = ["闪光"]))

        self.add(newStra = Strategy(name = "闪光强化", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "大范围闪光", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "受击闪光", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "致盲延长", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "火弹闪光", level = 3, location = "auto", trigger = ["技能火弹"], entity = ["火弹", "闪光"]))
        self.add(newStra = Strategy(name = "火弹闪光", level = 3, location = "auto", trigger = ["传承技火弹"], entity = ["火弹", "闪光"]))
        self.add(newStra = Strategy(name = "标记闪光", level = 3, location = "auto", trigger = ["圣光标记"], entity = ["圣光标记", "闪光"]))
        self.add(newStra = Strategy(name = "光枪闪光", level = 3, location = "auto", trigger = ["技能光枪"], entity = ["光枪", "闪光"]))
        self.add(newStra = Strategy(name = "光枪闪光", level = 3, location = "auto", trigger = ["传承技光枪"], entity = ["光枪", "闪光"]))
        self.add(newStra = Strategy(name = "影链致盲", level = 3, location = "auto", trigger = ["普攻影链"], entity = ["暗影链条", "致盲"]))
        self.add(newStra = Strategy(name = "影链致盲", level = 3, location = "auto", trigger = ["技能影链"], entity = ["暗影链条", "致盲"]))


class 光波(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "光", subclass = "光波")

        self.add(newStra = Strategy(name = "普攻光波", level = 0, location = "普攻", entity = ["光波"]))

        self.add(newStra = Strategy(name = "光波强化", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "光波眩晕", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "灵活充能", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "增强光波", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "光波传递", level = 3, location = "auto", trigger = ["普攻光波"], entity = ["光波"]))
        self.add(newStra = Strategy(name = "光波快充", level = 3, location = "普攻", trigger = ["普攻光波"], entity = ["光波", "光阵"]))
        self.add(newStra = Strategy(name = "光枪光波", level = 3, location = "auto", trigger = ["传承技光枪"], entity = ["光波", "光枪"]))
        self.add(newStra = Strategy(name = "光枪光波", level = 3, location = "auto", trigger = ["技能光枪"], entity = ["光波", "光枪"]))

class 光阵(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "光", subclass = "光阵")

        self.add(newStra = Strategy(name = "召唤光阵", level = 0, location = "召唤", entity = ["光阵"]))

        self.add(newStra = Strategy(name = "光阵致盲", level = 1, location = "auto", trigger = "auto", entity = ["致盲"]))
        self.add(newStra = Strategy(name = "光阵庇护", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "光阵增幅", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "大型光阵", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "光阵吸引", level = 3, location = "auto", trigger = ["召唤光阵"], entity = ["光阵"]))
        self.add(newStra = Strategy(name = "持久光阵", level = 3, location = "auto", trigger = ["传承技闪光"], entity = ["光阵", "闪光"]))

class 圣光标记(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "光", subclass = "圣光标记")

        self.add(newStra = Strategy(name = "圣光标记", level = 0, location = "冲刺", entity = ["圣光标记"]))

        self.add(newStra = Strategy(name = "稳定标记", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "标记强化", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "随机标记", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "标记共鸣", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "至圣标记", level = 3, location = "普攻", trigger = ["普攻光波", "圣光标记"], entity = ["光波", "圣光标记"]))
        self.add(newStra = Strategy(name = "冰刺标记", level = 3, location = "召唤", trigger = ["召唤冰刺", "圣光标记"], entity = ["冰刺", "圣光标记"]))
        self.add(newStra = Strategy(name = "标记光阵", level = 3, location = "召唤", trigger = ["召唤光阵", "圣光标记"], entity = ["光阵", "圣光标记"]))
        
      