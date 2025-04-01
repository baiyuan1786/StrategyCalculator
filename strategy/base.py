##########################################################################################################
#   Description: 策略类基础
#   Authors:     BaiYuan <395642104@qq.com>
##########################################################################################################

from typing import Literal, List, Optional, Dict

class Strategy:
    '''策略'''
    def __init__(self, name: str, level: Literal[0, 1, 2, 3], location: Literal["普攻", "技能", "冲刺", "传承", "召唤", "auto"] = "auto", 
                 parent: Optional[List[str]] = None, trigger: Optional[List[str]] = None, attribute: Optional[str] = None, subclass: Optional[str] = None,
                 entity: Optional[List[str]] = None):
        """基础策略初始化
        对于一个策略来讲, 其在策略树上的位置只可能有四种层级, 
        其中第一层的策略影响了策略链占据的位置
        其中第四层一定是双重策略, 一个双重策略可能具有不同的触发列表或位置, 此时视作不同的双重策略
        对于双重策略来说, 一个策略如果被用来激活一个双重策略, 就不可被用于激活其他策略

        :param name: 策略名字
        :param level: 策略层级
        :param location: 策略位置, 设置为自动时, 继承其上位节点的位置
        :param parent: 父节点, 通常认为一个节点的父节点都被获取后, 子节点才会出现
        :param trigger: 触发节点
        :param attribute: 属性
        :param subclass: 子系
        :param entity: 词条
        """

        self.name = name            # 名字
        self.level = level          # 层级
        self.location = location    # 位置
        self.parent = parent        # 父节点
        self.trigger = trigger      # 触发节点
        self.attribute = attribute  # 属性
        self.subclass = subclass    # 子系
        self.entity = entity        # 词条

        if (self.level == 0 or self.level == 3) and self.entity is None:
            raise Exception(f"{self.name} 必须设置entity, 否则无法计算评分")

        if self.level != 0 and self.trigger is None:
            raise Exception(f"{self.name}: 非基础策略必须设置触发位")

        if isinstance(self.trigger, list) and len(self.trigger) >= 2 and self.location == "auto":
            raise Exception(f"{self.name}: 无法将location指定为auto, 请检查定义")
        
    def __str__(self):
        return f"{self.name}[{self.attribute}_{self.subclass}]"
        
class StrategyChain:
    '''策略链'''
    def __init__(self, node0: Strategy, node1: Strategy, node2: Strategy):
        '''初始化策略链, 仅前三个策略'''

        # 检查策略合法性
        if isinstance(node1.trigger, list) and node0.name not in node1.trigger:
            raise Exception(f"对于{node0.name}, {node1.name}无法触发")

        if isinstance(node2.trigger, list) and node1.name not in node2.trigger:
            raise Exception(f"对于{node0.name}, {node2.name}无法触发")

        self.node0 = node0
        self.node1 = node1
        self.node2 = node2
        self.location = node0.location # 策略链位置设定为首策略的位置
        self.names = [node0.name, node1.name, node2.name]       # 名字集合, 用来索引
        self.chainType = f"{node0.subclass}({node0.location})"  # 链类型, 例如 光枪(技能)
        self.subclass = node0.subclass
        self.attribute = node0.attribute

        self.entity = []
        for entity in [node0.entity, node1.entity, node2.entity]:
            if isinstance(entity, list):
                self.entity += entity
        self.entity = list(set(self.entity))

    def __str__(self):
        return f"{self.node0.name}->{self.node1.name}->{self.node2.name}"
    
class StrategyChainGroup:
    '''策略链组, 拥有相同链类型的策略链构成一个策略链组'''
    def __init__(self, allChains: List[StrategyChain], chainType: str):

        self.chains: List[StrategyChain] = [chain for chain in allChains if chain.chainType == chainType]
        self.chainType = chainType

        if len(self.chains) == 0:
            raise Exception("没有获取到策略链")
        
        self.names = []                     # 所有节点名称构成的集合
        self.entity = []                    # 词条
        for chain in self.chains:
            self.names += chain.names
            self.entity += chain.entity
        self.names = list(set(self.names))
        self.entity = list(set(self.entity))
        
        self.location = self.chains[0].location
        self.subclass = self.chains[0].subclass
        self.attribute = self.chains[0].attribute

    def __str__(self):
        return f"{self.chains[0].node0.name}[{self.attribute}_{self.subclass}]"

class StrategyTree:
    '''策略树'''
    def __init__(self, attribute: str, subclass: str):
        self.attribute = attribute
        self.subclass = subclass
        self.nodes: Dict[int, List[Strategy]] = {
            0: [],
            1: [],
            2: [],
            3: []
        }                                   # 策略节点
        self.strategys: List[Strategy] = [] # 全部策略

    def add(self, newStra: Strategy):
        '''添加新的策略进策略树中'''

        if not isinstance(newStra, Strategy):
            raise TypeError("策略树的加法只能与策略相加")

        # 追加属性和子类
        newStra.attribute = self.attribute
        newStra.subclass = self.subclass

        self.strategys.append(newStra)
        self.nodes[newStra.level].append(newStra)

    def chains(self):
        '''策略链'''

        chains: List[StrategyChain] = []
        for node0 in self.nodes[0]:
            for node1 in self.nodes[1]:
                for node2 in self.nodes[2]:
                    try:
                        newChain = StrategyChain(node0 = node0, node1 = node1, node2 = node2)
                    except Exception:
                        continue
                    else:
                        chains.append(newChain)

        return chains
    
    def chainGroups(self):
        '''策略链组'''

        allChains = self.chains()
        chainTypes = [f"{node0.subclass}({node0.location})"for node0 in self.nodes[0]]
        allchainGroups = [StrategyChainGroup(allChains, chainType) for chainType in chainTypes]
        return allchainGroups
    
    def allStrategys(self):
        '''所有策略'''
        return self.strategys

    def doubleStrategys(self):
        '''所有双重策略'''
        return self.nodes[3]