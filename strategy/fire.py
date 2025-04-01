##########################################################################################################
#   Description: 火系策略
#   Authors:     BaiYuan <395642104@qq.com>
##########################################################################################################

from .base import Strategy, StrategyTree

class 燃烧(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "火", subclass = "燃烧")

        self.add(newStra = Strategy(name = "技能燃烧", level = 0, location = "技能", entity = ["燃烧"]))
        self.add(newStra = Strategy(name = "普攻燃烧", level = 0, location = "普攻", entity = ["燃烧"]))
        self.add(newStra = Strategy(name = "冲刺燃烧", level = 0, location = "冲刺", entity = ["燃烧"]))

        self.add(newStra = Strategy(name = "持久燃烧", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "聚火成炎", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "燃烧引燃", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "火焰漫步", level = 1, location = "auto", trigger = ["冲刺燃烧"]))

        self.add(newStra = Strategy(name = "强效燃烧", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "火环燃烧", level = 3, location = "auto", trigger = ["传承技火环"], entity = ["燃烧", "火环"]))
        self.add(newStra = Strategy(name = "火焰飞剑", level = 3, location = "auto", trigger = ["冲刺飞剑"], entity = ["燃烧", "飞剑"]))

class 火弹(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "火", subclass = "火弹")

        self.add(newStra = Strategy(name = "技能火弹", level = 0, location = "技能", entity = ["火弹"]))
        self.add(newStra = Strategy(name = "传承技火弹", level = 0, location = "传承技", entity = ["火弹"]))

        self.add(newStra = Strategy(name = "集中火弹", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "火弹弹射", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "火弹强化", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "多重火弹", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "爆燃火弹", level = 3, location = "技能", trigger = ["技能火弹"], entity = ["火弹", "燃烧"]))
        self.add(newStra = Strategy(name = "爆燃火弹", level = 3, location = "传承技", trigger = ["传承技火弹"], entity = ["火弹", "燃烧"]))
        self.add(newStra = Strategy(name = "雷云火弹", level = 3, location = "auto", trigger = ["电闪雷鸣"], entity = ["火弹", "雷云"]))

class 火环(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "火", subclass = "火环")

        self.add(newStra = Strategy(name = "传承技火环", level = 0, location = "传承技", entity = ["火环"]))

        self.add(newStra = Strategy(name = "大型火环", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "变形火环", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "受击火环", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "双发火环", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "风暴火环", level = 3, location = "传承", trigger = ["刀刃风暴"], entity = ["火环", "刀刃风暴"]))
        self.add(newStra = Strategy(name = "风暴火环", level = 3, location = "技能", trigger = ["刀刃风暴"], entity = ["火环", "刀刃风暴"]))
        self.add(newStra = Strategy(name = "焚弹火环", level = 3, location = "auto", trigger = ["传承技火环"], entity = ["火环", "火种"]))

class 地雷(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "火", subclass = "地雷")

        self.add(newStra = Strategy(name = "放置地雷", level = 0, location = "召唤", entity = ["地雷"]))

        self.add(newStra = Strategy(name = "地雷强化", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "额外地雷", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "地雷溅射", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "高效布雷", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "地雷火焰", level = 3, location = "auto", trigger = ["放置地雷"], entity = ["地雷"]))
        self.add(newStra = Strategy(name = "地雷闪光", level = 3, location = "auto", trigger = ["放置地雷"], entity = ["地雷", "闪光"]))

class 火精灵(StrategyTree):
    def __init__(self):
        super().__init__(attribute = "火", subclass = "火精灵")

        self.add(newStra = Strategy(name = "火精灵助战", level = 0, location = "普攻", entity = ["火精灵"]))

        self.add(newStra = Strategy(name = "火精灵强化", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "火精灵连击", level = 1, location = "auto", trigger = "auto"))
        self.add(newStra = Strategy(name = "快速分裂", level = 1, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "持久分裂", level = 2, location = "auto", trigger = "auto"))

        self.add(newStra = Strategy(name = "火精灵引爆", level = 3, location = "普攻", trigger = ["火精灵助战"], entity = ["火精灵", "燃烧"]))
        self.add(newStra = Strategy(name = "火弹火精灵", level = 3, location = "技能", trigger = ["技能火弹"], entity = ["火精灵", "火弹"]))
        self.add(newStra = Strategy(name = "火弹火精灵", level = 3, location = "传承技", trigger = ["传承技火弹"], entity = ["火精灵", "火弹"]))
        self.add(newStra = Strategy(name = "火精灵弹跳", level = 3, location = "auto", trigger = ["火精灵助战"], entity = ["火精灵"]))
      