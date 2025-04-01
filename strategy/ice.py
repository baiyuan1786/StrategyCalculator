##########################################################################################################
#   Description: 冰系策略
#   Authors:     BaiYuan <395642104@qq.com>
##########################################################################################################

from .base import Strategy, StrategyTree

class 寒冷(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "冰", subclass = "寒冷")

        self.add(newStra = Strategy(name = "普攻寒冷", level = 0, location = "普攻", entity = ["寒冷"]))
        self.add(newStra = Strategy(name = "技能寒冷", level = 0, location = "技能", entity = ["寒冷"]))

        self.add(newStra = Strategy(name = "寒气爆发", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "聚寒成冰", level = 1, location = "auto", trigger = "auto", entity = ["寒冷", "冰冻"]))

        self.add(newStra = Strategy(name = "冰霜爆破", level = 2, location = "auto", trigger = ["寒气爆发"], entity = ["寒气爆发"]))
        self.add(newStra = Strategy(name = "强力破冰", level = 2, location = "auto", trigger = ["聚寒成冰"]))

        self.add(newStra = Strategy(name = "冰锥极寒", level = 3, location = "auto", trigger = ["传承技冰锥"], entity = ["寒冷", "冰锥"]))
        self.add(newStra = Strategy(name = "冰锥极寒", level = 3, location = "auto", trigger = ["冲刺冰锥"], entity = ["寒冷", "冰锥"]))
        self.add(newStra = Strategy(name = "冰霜脉冲", level = 3, location = "auto", trigger = ["寒气爆发"], entity = ["寒气爆发", "麻痹"]))
        self.add(newStra = Strategy(name = "寒冰毒雾", level = 3, location = "auto", trigger = ["普攻毒雾"], entity = ["毒雾", "冰冻"]))
    
class 冰锥(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "冰", subclass = "冰锥")

        self.add(newStra = Strategy(name = "冲刺冰锥", level = 0, location = "冲刺", entity = ["冰锥", "寒冷"]))
        self.add(newStra = Strategy(name = "传承技冰锥", level = 0, location = "传承技", entity = ["冰锥", "寒冷"]))

        self.add(newStra = Strategy(name = "冰锥强化", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "闪避冰锥", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "受击冰锥", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "随机冰锥", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "光枪冰锥", level = 3, location = "auto", trigger = ["传承技光枪"], entity = ["光枪", "冰锥"]))
        self.add(newStra = Strategy(name = "光枪冰锥", level = 3, location = "auto", trigger = ["技能光枪"], entity = ["光枪", "冰锥"]))
        self.add(newStra = Strategy(name = "冰冻冰锥", level = 3, location = "普攻", trigger = ["聚寒成冰", "普攻寒冷"], entity = ["冰冻", "冰锥"]))
        self.add(newStra = Strategy(name = "冰冻冰锥", level = 3, location = "技能", trigger = ["聚寒成冰", "技能寒冷"], entity = ["冰冻", "冰锥"]))

class 冰刺(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "冰", subclass = "冰刺")

        self.add(newStra = Strategy(name = "召唤冰刺", level = 0, location = "召唤", entity = ["冰刺", "寒冷"]))

        self.add(newStra = Strategy(name = "冰刺强化", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "精准冰刺", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "冰刺穿透", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "多重冰刺", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "无尽冰刺", level = 3, location = "auto", trigger = ["召唤冰刺"], entity = ["冰刺"]))
        self.add(newStra = Strategy(name = "冰刺再生", level = 3, location = "auto", trigger = ["召唤冰刺"], entity = ["冰刺"]))
        self.add(newStra = Strategy(name = "影子冰刺", level = 3, location = "冲刺", trigger = ["冲刺影子", "召唤冰刺"], entity = ["冰刺", "影子"]))