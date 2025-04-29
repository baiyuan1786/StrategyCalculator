##########################################################################################################
#   Description: 电系策略
#   Authors:     BaiYuan <395642104@qq.com>
##########################################################################################################

from .base import Strategy, StrategyTree

class 感电(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "电", subclass = "感电")

        self.add(newStra = Strategy(name = "技能感电", level = 0, location = "技能", entity = ["感电", "脉冲"]))
        self.add(newStra = Strategy(name = "传承技感电", level = 0, location = "传承技", entity = ["感电", "脉冲"]))

        self.add(newStra = Strategy(name = "脉冲强化", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "大型脉冲", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "脉冲麻痹", level = 1, location = "auto", trigger = "auto", entity = ["脉冲", "麻痹"]))

        self.add(newStra = Strategy(name = "脉冲感电", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "闪电感电", level = 3, location = "auto", trigger = ["普攻闪电"], entity = ["闪电链", "感电", "脉冲"]))
        self.add(newStra = Strategy(name = "闪电感电", level = 3, location = "auto", trigger = ["技能闪电"], entity = ["闪电链", "感电", "脉冲"]))
        self.add(newStra = Strategy(name = "闪电感电", level = 3, location = "auto", trigger = ["电闪雷鸣"], entity = ["闪电链", "感电", "脉冲"]))
        self.add(newStra = Strategy(name = "黑洞脉冲", level = 3, location = "auto", trigger = ["传承技黑洞"], entity = ["黑洞", "脉冲"]))
        self.add(newStra = Strategy(name = "脉冲电桩", level = 3, location = "auto", trigger = ["传承技电桩"], entity = ["电桩", "脉冲"]))
        self.add(newStra = Strategy(name = "飞刃脉冲", level = 3, location = "auto", trigger = ["普攻飞刃"], entity = ["飞刃", "脉冲"]))

class 闪电链(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "电", subclass = "闪电链")

        self.add(newStra = Strategy(name = "普攻闪电", level = 0, location = "普攻", entity = ["闪电链"]))
        self.add(newStra = Strategy(name = "电闪雷鸣", level = 0, location = "传承技", entity = ["雷云", "闪电链"]))
        self.add(newStra = Strategy(name = "技能闪电", level = 0, location = "技能", entity = ["闪电链"]))

        self.add(newStra = Strategy(name = "闪电过载", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "闪电强化", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "闪电弹射", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "闪电延伸", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "电球闪电", level = 3, location = "auto", trigger = ["环绕电球"], entity = ["闪电链", "电球"]))
        self.add(newStra = Strategy(name = "触手闪电", level = 3, location = "auto", trigger = ["召唤触手"], entity = ["闪电链", "暗影触手"]))

class 落雷(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "电", subclass = "落雷")

        self.add(newStra = Strategy(name = "冲刺落雷", level = 0, location = "冲刺", entity = ["落雷"]))

        self.add(newStra = Strategy(name = "受击落雷", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "闪避落雷", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "落雷强化", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "落雷麻痹", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "双重落雷", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "光枪落雷", level = 3, location = "auto", trigger = ["传承技光枪"], entity = ["落雷", "光枪"]))
        self.add(newStra = Strategy(name = "光枪落雷", level = 3, location = "auto", trigger = ["技能光枪"], entity = ["落雷", "光枪"]))
        self.add(newStra = Strategy(name = "电球落雷", level = 3, location = "auto", trigger = ["环绕电球"], entity = ["落雷", "电球"]))
        self.add(newStra = Strategy(name = "落雷惩戒", level = 3, location = "auto", trigger = ["普攻影刺"], entity = ["落雷", "影子"]))
        self.add(newStra = Strategy(name = "落雷惩戒", level = 3, location = "auto", trigger = ["技能影刺"], entity = ["落雷", "影子"]))
        self.add(newStra = Strategy(name = "追踪落雷", level = 3, location = "冲刺", trigger = ["冲刺落雷", "技能感电"], entity = ["落雷", "感电"]))
        self.add(newStra = Strategy(name = "追踪落雷", level = 3, location = "冲刺", trigger = ["冲刺落雷", "传承技感电"], entity = ["落雷", "感电"]))

class 电球(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "电", subclass = "电球")

        self.add(newStra = Strategy(name = "环绕电球", level = 0, location = "召唤", entity = ["电球"]))

        self.add(newStra = Strategy(name = "大型电球", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "持久电球", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "扩张电球", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "密集电球", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "电球发射", level = 3, location = "auto", trigger = ["环绕电球"], entity = ["电球"]))
        self.add(newStra = Strategy(name = "影子电球", level = 3, location = "auto", trigger = ["环绕电球"], entity = ["电球", "影子"]))
        self.add(newStra = Strategy(name = "影子电球", level = 3, location = "auto", trigger = ["环绕电球"], entity = ["电球", "影子"]))
        self.add(newStra = Strategy(name = "感电电球", level = 3, location = "auto", trigger = ["技能感电"], entity = ["电球", "感电"]))
        self.add(newStra = Strategy(name = "感电电球", level = 3, location = "auto", trigger = ["传承技感电"], entity = ["电球", "感电"]))
        self.add(newStra = Strategy(name = "传导电桩", level = 3, location = "auto", trigger = ["传承技电桩"], entity = ["电球", "电桩"]))

class 电桩(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "电", subclass = "电桩")

        self.add(newStra = Strategy(name = "传承技电桩", level = 0, location = "传承技", entity = ["电桩"]))

        self.add(newStra = Strategy(name = "持久电桩", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "超载电桩", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "电桩吸附", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "大型电桩", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "电桩链接", level = 3, location = "auto", trigger = ["传承技电桩"], entity = ["电桩", "电网"]))
        self.add(newStra = Strategy(name = "光阵电桩", level = 3, location = "auto", trigger = ["召唤光阵"], entity = ["电桩", "光阵"]))
