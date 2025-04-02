##########################################################################################################
#   Description: 计算苍翼混沌效应策略树搭配
#   Authors:     BaiYuan <395642104@qq.com>
##########################################################################################################

import yaml
import time

from strategy import *

from typing import List, Optional, Literal, Dict
from itertools import combinations
from tqdm import tqdm
from datetime import datetime
from pathlib import Path

curPath = Path(__file__).parent.resolve()
resultPath = curPath / "results"
if not resultPath.exists():
    resultPath.mkdir(mode = 777)

class Character:
    '''角色, 一个角色可以搭配五种策略链, 以及最多五个双重策略'''
    def __init__(self, chainG0: StrategyChainGroup, chainG1: StrategyChainGroup, chainG2: StrategyChainGroup, chainG3: StrategyChainGroup, chainG4: StrategyChainGroup):
        '''输入五种chain开始初始化角色'''

        # chainGroup类型检查
        if chainG0.location != "普攻":
            raise KeyError(f"chainG0' location is {chainG0.location}, but 普攻 is needed")
        if chainG1.location != "技能":
            raise KeyError(f"chainG1' location is {chainG1.location}, but 技能 is needed")
        if chainG2.location != "冲刺":
            raise KeyError(f"chainG2' location is {chainG2.location}, but 冲刺 is needed")
        if chainG3.location != "传承技":
            raise KeyError(f"chainG3' location is {chainG3.location}, but 传承技 is needed")
        if chainG4.location != "召唤":
            raise KeyError(f"chainG4' location is {chainG4.location}, but 召唤 is needed")
        
        # 策略组冲突性检查
        for g1, g2 in combinations([chainG0, chainG1, chainG2, chainG3, chainG4], 2):
            if g1.subclass == g2.subclass:
                raise ValueError(f"{g1} 与 {g2} 类型冲突, 无法使用")

        # 初始化五个chainG
        self.chainG0 = chainG0
        self.chainG1 = chainG1
        self.chainG2 = chainG2
        self.chainG3 = chainG3
        self.chainG4 = chainG4

        self.chainGs = [chainG0, chainG1, chainG2, chainG3, chainG4]
        self.names = chainG0.names + chainG1.names + chainG2.names + chainG3.names + chainG4.names

    def searchLocation(self, name: str):
        '''通过名字搜索位置'''
        for chainG in self.chainGs:
            if name in chainG.names:
                return chainG.location
        return None

    def activatableDs(self, doubleStrategys: List[Strategy]):
        '''获取可激活的双重策略集合'''

        activatableDs = [ds for ds in doubleStrategys if set(ds.trigger) <= set(self.names)]
        return activatableDs

class FullCharacter:
    '''拥有五红策略的完整角色'''
    def __init__(self, character: Character, ds0: Strategy, ds1: Strategy, ds2: Strategy, ds3: Strategy, ds4: Strategy):
        '''加载五种双重策略, 确保所有的ds都是可激活的'''

        # 双重策略刻印位置
        self.doubleStrategyDict: Dict[str, Optional[Strategy]] = {
            "普攻" : None,
            "技能" : None,
            "冲刺" : None,
            "传承技" : None,
            "召唤" : None,
        }
        
        # 尝试加载
        self.character = character
        self.names = character.names + [ds0.name, ds1.name, ds2.name, ds3.name, ds4.name]
        
        usedTrigger = [] # 已使用触发位
        for ds in [ds0, ds1, ds2, ds3, ds4]:

            # 触发位判断
            #if bool(set(usedTrigger) & set(ds.trigger)):
            #    raise Exception("触发位已被使用")

            # 获取策略位置
            if ds.location != "auto":
                newLocation = ds.location
            elif ds.location == "auto" and isinstance(ds.trigger, list) and len(ds.trigger) == 1:
                newLocation = self.character.searchLocation(name = ds.trigger[0])
            else:
                raise ValueError(f"对于双重策略{ds.name}, 无法使用auto进行位置继承, 请修改源码")

            # 镶嵌策略
            if newLocation in self.doubleStrategyDict.keys() and self.doubleStrategyDict[newLocation] is None:
                self.doubleStrategyDict[newLocation] = ds
                usedTrigger += ds.trigger
            else:
                raise Exception(f"无法镶嵌策略{ds.name}")
            
        # 获取契合度
        self.fitScore = 0
        for ds in self.doubleStrategyDict.values():

            if ds is None or ds.entity is None:
                print(f"代码逻辑出错, 请修改entity定义或Fullcharacter逻辑")

            scoreList:List[int] = []
            for singleEntity in ds.entity:
                newScore = 0
                for chainG in character.chainGs:
                    if singleEntity in chainG.entity:
                        newScore += 3

                newScore = max(newScore, 1)
                scoreList.append(newScore)
            
            scoreList.sort(key = lambda a:a, reverse = True)
            self.fitScore += sum(scoreList[0:2]) # 仅计算分最高的最多两个词条

    def __str__(self):
        return f"普攻: {self.character.chainG0}->{self.doubleStrategyDict["普攻"]}\n" + \
        f"技能: {self.character.chainG1}->{self.doubleStrategyDict["技能"]}\n" +\
        f"冲刺: {self.character.chainG2}->{self.doubleStrategyDict["冲刺"]}\n" +\
        f"传承技: {self.character.chainG3}->{self.doubleStrategyDict["传承技"]}\n" +\
        f"召唤: {self.character.chainG4}->{self.doubleStrategyDict["召唤"]}\n"
                
class StrategyTrees:
    '''策略树集合'''
    def __init__(self):
        # 初始化全部策略树
        self.allTrees: Dict[str, List[StrategyTree]] = {
            "刃" : [飞剑(), 撕裂(), 刃环(), 刀刃风暴()],
            "暗" : [触手(), 影子(), 影刺(), 黑洞()],
            "电" : [感电(), 闪电链(), 落雷(), 电球()],
            "火" : [燃烧(), 火弹(), 火环(), 地雷(), 火精灵()],
            "冰" : [寒冷(), 冰锥(), 冰刺()],
            "光" : [光枪(), 闪光(), 光波(), 光阵(), 圣光标记()],
            "毒" : [中毒(), 史莱姆(), 毒弹(), 毒液()]
        }

        self.attributes = list(self.allTrees.keys())
        self.allTreesList = [tree for trees in self.allTrees.values() for tree in trees] # 所有策略树列表

        # 初始化所有策略链组
        self.allChainGroups: Dict[str, List[StrategyChainGroup]] = {
            "普攻" : [],
            "技能" : [],
            "冲刺" : [],
            "传承技" : [],
            "召唤" : [],
        }

        for tree in self.allTreesList:
            for chainGroup in tree.chainGroups():
                if chainGroup.location in self.allChainGroups.keys():
                    self.allChainGroups[chainGroup.location].append(chainGroup)
                else:
                    raise KeyError(f"unRecognized location \"{chainGroup.location}\" for {chainGroup}")       

        # 初始化所有双重策略
        self.allDoubleStrategys: List[Strategy] = []
        for tree in self.allTreesList:
            self.allDoubleStrategys += tree.doubleStrategys()
        self.allDoubleStrategyNames = [ds.name for ds in self.allDoubleStrategys]

    def statPrint(self):
        '''状态输出'''

        # 策略链输出
        for location, chainGroups in self.allChainGroups.items():
            print(f"==={location}: 获取到 \"{len(chainGroups)}\" 个策略链组===")
            for index, chainGroup in enumerate(chainGroups):
                print(f"{index}. {chainGroup}")
            print("")

        print(f"获取到{len(self.allDoubleStrategys)}个双重策略")
        
    def caculate(self, needAttribute: List[str] = ["刃", "暗", "电", "火", "冰", "光", "毒"], includeStra: List[str] = [],
                 outputLen: Optional[int] = None):
        '''计算策略搭配
        首先需要明确一下, 对于一个角色, 其只有普攻, 技能, 冲刺, 传承, 召唤五个location, 每个location都有四个level的位置
        所以我们通过遍历计算, 就是计算5*4, 一共二十个策略的所有搭配, 找到所有拥有五红的搭配
        因为双重策略可能需要两个subclass的策略才能触发, 所以应该先计算左侧15个策略的搭配(五个策略链), 然后再计算双重策略搭配
        '''

        characters: List[Character] = []
        filleredChainGroups: Dict[str, List[StrategyChainGroup]] = {}
        fullCharacters: List[FullCharacter] = []

        now = datetime.now()
        fileName = f"results_{now.strftime("%Y%m%d_%H%M%S")}.txt"
        filePath = resultPath /fileName

        includeStra_double = [strategy for strategy in includeStra if strategy in self.allDoubleStrategyNames]
        includeStra_nonDouble = [strategy for strategy in includeStra if strategy not in self.allDoubleStrategyNames]

        print(f"策略链属性条件被设置为: {needAttribute}")
        print(f"必须包含的策略被设置为: {includeStra}")

        # 策略链过滤
        for key, chainGroups in self.allChainGroups.items():
            filleredChainGroups[key] = [chainGroup for chainGroup in chainGroups 
                                        if chainGroup.attribute in needAttribute]
            if len(filleredChainGroups[key]) == 0:
                raise Exception("没有足够多的策略链满足筛选条件, 请检查设置")
    
        # 获取所有character
        for chain0 in tqdm(filleredChainGroups["普攻"], unit = "chain", desc = "计算character搭配"):
            for chain1 in filleredChainGroups["技能"]:
                for chain2 in filleredChainGroups["冲刺"]:
                    for chain3 in filleredChainGroups["传承技"]:
                        for chain4 in filleredChainGroups["召唤"]:
                            try:
                                newCharacter = Character(chain0, chain1, chain2, chain3, chain4)
                            except KeyError as e:
                                raise e
                            except ValueError:
                                continue
                            else:
                                characters.append(newCharacter)

        # character过滤
        characters = [character for character in characters if set(includeStra_nonDouble) <= set(character.names)]
        if len(characters) == 0:
            raise Exception(f"没有character满足筛选条件, 请修改条件")
        else:
            print(f"获取到{len(characters)}个character")

        # 计算双重策略搭配
        for character in tqdm(characters, unit = "character", desc = "计算双重策略搭配"):

            # 裁剪能激活的双重策略
            activatableDs = character.activatableDs(doubleStrategys = self.allDoubleStrategys)

            if len(activatableDs) < 5:
                continue

            for ds0, ds1, ds2, ds3, ds4 in combinations(activatableDs, 5):
                try:
                    newFullCharacter = FullCharacter(character, ds0, ds1, ds2, ds3, ds4)
                except ValueError as e:
                    raise e
                except Exception:
                    continue
                else:
                    fullCharacters.append(newFullCharacter)

        # FullCharacter过滤
        fullCharacters = [character for character in fullCharacters if set(includeStra_double) <= set(character.names)]
        if len(fullCharacters) == 0:
            raise Exception(f"没有fullCharacter满足筛选条件, 请修改条件")
        else:
            print(f"获取到{len(fullCharacters)}个fullCharacter")

        # 排序
        print("进行排序输出...")
        fullCharacters.sort(key = lambda a : a.fitScore, reverse = True)

        # 输出
        with open(filePath, "a", encoding = "utf-8") as f:
            f.write(f"苍翼混沌效应_策略计算\n")
            f.write(f"NeedAttribute: {needAttribute}\n")
            f.write(f"IncludeStra: {includeStra}\n\n")

            for index, fullC in enumerate(fullCharacters):
                f.write(f"{index}, fitScore = {fullC.fitScore}:\n")
                f.write(fullC.__str__())
                f.write("\n")
                if isinstance(outputLen, int) and index >= outputLen:
                    break

            print(f"获取到{len(fullCharacters)}个可用搭配, 结果已写入{filePath}")

    def caculateAll(self):
        '''计算全部的两两组合'''
        for attribute1, attribute2 in combinations(self.attributes, 2):
            try:
                trees.caculate(needAttribute = [attribute1, attribute2], outputLen = 100)
            except Exception as e:
                print(str(e))
                continue
            finally:
                time.sleep(1)

if __name__ == "__main__":
    configPath = curPath / "config.yaml"
    with configPath.open("r", encoding = "utf-8") as f:
        file = yaml.safe_load(f)

    outputLen = file["outputLen"]
    includeStra = file["includeStra"]
    needAttribute = file["needAttribute"]

    trees = StrategyTrees()
    trees.caculate(needAttribute = needAttribute, includeStra = includeStra, outputLen = outputLen)
    #trees.caculateAll()