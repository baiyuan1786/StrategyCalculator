##########################################################################################################
#   Description: 暗系策略
#   Authors:     BaiYuan <395642104@qq.com>
##########################################################################################################

from .base import Strategy, StrategyTree

class 触手(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "暗", subclass = "触手")

        self.add(newStra = Strategy(name = "召唤触手", level = 0, location = "召唤", entity = ["暗影触手"]))

        self.add(newStra = Strategy(name = "大型触手", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "速攻触手", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "触手集群", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "连击触手", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "暴躁触手", level = 3, location = "auto", trigger = ["召唤触手"], entity = ["暗影触手"]))
        self.add(newStra = Strategy(name = "触手吞噬", level = 3, location = "auto", trigger = ["召唤触手"], entity = ["暗影触手"]))
        self.add(newStra = Strategy(name = "影链牵引", level = 3, location = "auto", trigger = ["普攻影标"], entity = ["暗影链条"]))
        self.add(newStra = Strategy(name = "影链牵引", level = 3, location = "auto", trigger = ["技能影标"], entity = ["暗影链条"]))

    
class 影子(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "暗", subclass = "影子")

        self.add(newStra = Strategy(name = "冲刺影子", level = 0, location = "冲刺", entity = ["影子"]))

        self.add(newStra = Strategy(name = "影子反冲", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "影子强化", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "闪避影子", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "多重影子", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "影刃冲刺", level = 3, location = "auto", trigger = ["冲刺影子"], entity = ["影子", "影刃"]))
        self.add(newStra = Strategy(name = "概率影爆", level = 3, location = "auto", trigger = ["冲刺影子"], entity = ["影子", "影爆"]))
        self.add(newStra = Strategy(name = "冰影双剑", level = 3, location = "auto", trigger = ["玄冰剑刃"], entity = ["玄冰剑"]))
        self.add(newStra = Strategy(name = "影刃回收", level = 3, location = "auto", trigger = ["普攻飞刃"], entity = ["飞刃"]))

class 影刺(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "暗", subclass = "影刺")

        self.add(newStra = Strategy(name = "普攻影刺", level = 0, location = "普攻", entity = ["影子", "影刺"]))
        self.add(newStra = Strategy(name = "技能影刺", level = 0, location = "技能", entity = ["影子", "影刺"]))

        self.add(newStra = Strategy(name = "远程影刺", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "死亡影刺", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "受击影刺", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "影刺强化", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "影子穿刺", level = 3, location = "auto", trigger = ["冲刺影子"], entity = ["影子", "影刺"]))
        self.add(newStra = Strategy(name = "影子转化", level = 3, location = "auto", trigger = ["普攻影刺"], entity = ["影子", "影刺"]))
        self.add(newStra = Strategy(name = "影子转化", level = 3, location = "auto", trigger = ["技能影刺"], entity = ["影子", "影刺"]))

class 黑洞(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "暗", subclass = "黑洞")

        self.add(newStra = Strategy(name = "传承技黑洞", level = 0, location = "传承技", entity = ["黑洞"]))

        self.add(newStra = Strategy(name = "大型黑洞", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "黑洞爆炸", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "持久黑洞", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "黑洞盛宴", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "触手坍缩", level = 3, location = "auto", trigger = ["召唤触手"], entity = ["黑洞", "暗影触手"]))
        self.add(newStra = Strategy(name = "黑洞减速", level = 3, location = "auto", trigger = ["传承技黑洞"], entity = ["黑洞"]))
        self.add(newStra = Strategy(name = "影刺吸附", level = 3, location = "auto", trigger = ["普攻影刺"], entity = ["影刺"]))
        self.add(newStra = Strategy(name = "影刺吸附", level = 3, location = "auto", trigger = ["技能影刺"], entity = ["影刺"]))
        self.add(newStra = Strategy(name = "活性黑洞", level = 3, location = "auto", trigger = ["传承技黑洞"], entity = ["黑洞"]))

class 暗影标记(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "暗", subclass = "暗影标记")

        self.add(newStra = Strategy(name = "普攻影标", level = 0, location = "普攻", entity = ["暗影标记", "暗影链条"]))
        self.add(newStra = Strategy(name = "技能影标", level = 0, location = "技能", entity = ["暗影标记", "暗影链条"]))

        self.add(newStra = Strategy(name = "影标解限", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "影标增殖", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "影标连爆", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "强链影标", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "黑洞链接", level = 3, location = "auto", trigger = ["传承技黑洞"], entity = ["黑洞", "暗影链条"]))
        self.add(newStra = Strategy(name = "影链电桩", level = 3, location = "auto", trigger = ["传承技电桩"], entity = ["电桩", "暗影链条", "暗影标记"]))