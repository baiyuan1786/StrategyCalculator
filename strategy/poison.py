##########################################################################################################
#   Description: 毒系策略
#   Authors:     BaiYuan <395642104@qq.com>
##########################################################################################################

from .base import Strategy, StrategyTree

class 中毒(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "毒", subclass = "中毒")

        self.add(newStra = Strategy(name = "普攻毒雾", level = 0, location = "普攻", entity = ["中毒", "毒雾"]))
        self.add(newStra = Strategy(name = "技能毒环", level = 0, location = "技能", entity = ["中毒", "毒环"]))

        self.add(newStra = Strategy(name = "受击毒雾", level = 1, location = "auto", trigger = ["普攻毒雾"]))
        self.add(newStra = Strategy(name = "毒雾污染", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "强效中毒", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "毒雾扩散", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "受击毒环", level = 1, location = "auto", trigger = ["技能毒环"]))

        self.add(newStra = Strategy(name = "急性中毒", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "电解化毒", level = 3, location = "auto", trigger = ["普攻闪电"], entity = ["闪电链", "中毒"]))
        self.add(newStra = Strategy(name = "电解化毒", level = 3, location = "auto", trigger = ["技能闪电"], entity = ["闪电链", "中毒"]))
        self.add(newStra = Strategy(name = "电解化毒", level = 3, location = "auto", trigger = ["电闪雷鸣"], entity = ["闪电链", "中毒"]))
        self.add(newStra = Strategy(name = "剧毒史莱姆", level = 3, location = "auto", trigger = ["召唤史莱姆"], entity = ["史莱姆", "中毒"]))
        self.add(newStra = Strategy(name = "毒液催化", level = 3, location = "auto", trigger = ["传承技毒液"], entity = ["毒液", "中毒"]))
        self.add(newStra = Strategy(name = "毒液催化", level = 3, location = "auto", trigger = ["技能毒液"], entity = ["毒液", "中毒"]))

class 史莱姆(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "毒", subclass = "史莱姆")

        self.add(newStra = Strategy(name = "召唤史莱姆", level = 0, location = "召唤", entity = ["史莱姆"]))

        self.add(newStra = Strategy(name = "自爆史莱姆", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "长效史莱姆", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "大型史莱姆", level = 2, location = "auto", trigger = ["自爆史莱姆"]))
        self.add(newStra = Strategy(name = "极速史莱姆", level = 2, location = "auto", trigger = ["长效史莱姆"]))

        self.add(newStra = Strategy(name = "分裂史莱姆", level = 3, location = "auto", trigger = ["召唤史莱姆"], entity = ["史莱姆"]))
        self.add(newStra = Strategy(name = "附身史莱姆", level = 3, location = "auto", trigger = ["召唤史莱姆"], entity = ["史莱姆"]))
        self.add(newStra = Strategy(name = "毒液史莱姆", level = 3, location = "auto", trigger = ["传承技毒液"], entity = ["史莱姆", "毒液"]))
        self.add(newStra = Strategy(name = "毒液史莱姆", level = 3, location = "auto", trigger = ["技能毒液"], entity = ["史莱姆", "毒液"]))

class 毒弹(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "毒", subclass = "毒弹")

        self.add(newStra = Strategy(name = "冲刺毒弹", level = 0, location = "冲刺", entity = ["毒弹"]))

        self.add(newStra = Strategy(name = "烈性毒弹", level = 1, location = "auto", trigger = "auto", entity = ["中毒"]))
        self.add(newStra = Strategy(name = "闪避毒弹", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "浓缩毒弹", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "扩散毒弹", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "中毒毒弹", level = 3, location = "auto", trigger = ["普攻毒雾"], entity = ["毒弹", "中毒"]))
        self.add(newStra = Strategy(name = "中毒毒弹", level = 3, location = "auto", trigger = ["技能毒环"], entity = ["毒弹", "中毒"]))
        self.add(newStra = Strategy(name = "分裂毒弹", level = 3, location = "auto", trigger = ["冲刺毒弹"], entity = ["毒弹"]))
        self.add(newStra = Strategy(name = "河豚毒弹", level = 3, location = "auto", trigger = ["传承技河豚"], entity = ["毒弹", "河豚", "毒泡"]))


class 毒液(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "毒", subclass = "毒液")

        self.add(newStra = Strategy(name = "传承技毒液", level = 0, location = "传承技", entity = ["毒液"]))
        self.add(newStra = Strategy(name = "技能毒液", level = 0, location = "技能", entity = ["毒液"]))

        self.add(newStra = Strategy(name = "长效毒液", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "毒液扩大", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "烈性毒液", level = 1, location = "auto", trigger = "auto", entity = ["中毒"]))

        self.add(newStra = Strategy(name = "毒素累积", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "毒液残留", level = 3, location = "auto", trigger = ["冲刺毒弹"], entity = ["毒液", "毒弹"]))
        self.add(newStra = Strategy(name = "地雷毒液", level = 3, location = "auto", trigger = ["放置地雷"], entity = ["毒液", "地雷"]))

class 毒泡河豚(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "毒", subclass = "毒泡河豚")

        self.add(newStra = Strategy(name = "传承技河豚", level = 0, location = "传承技", entity = ["河豚", "毒泡"]))

        self.add(newStra = Strategy(name = "毒泡久喷", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "毒泡延距", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "大型毒泡", level = 1, location = "auto", trigger = "auto", entity = ["中毒"]))

        self.add(newStra = Strategy(name = "河豚延续", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "燃气毒泡", level = 3, location = "auto", trigger = ["普攻燃烧"], entity = ["燃烧", "毒泡"]))
        self.add(newStra = Strategy(name = "燃气毒泡", level = 3, location = "auto", trigger = ["冲刺燃烧"], entity = ["燃烧", "毒泡"]))
        self.add(newStra = Strategy(name = "燃气毒泡", level = 3, location = "auto", trigger = ["技能燃烧"], entity = ["燃烧", "毒泡"]))
        
        self.add(newStra = Strategy(name = "泡状毒液", level = 3, location = "auto", trigger = ["技能毒液"], entity = ["毒液", "毒泡"]))
        self.add(newStra = Strategy(name = "泡状毒液", level = 3, location = "auto", trigger = ["传承技毒液"], entity = ["毒液", "毒泡"]))
