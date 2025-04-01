# 苍翼混沌效应_策略计算器

## 1 前言

由于游戏<苍翼混沌效应>中, 作者总是无法触发五红策略, 对策略树不了解导致策略伤害不高红温了, 开发此工具



## 2 简介

本工具为python编写的, 针对苍翼混沌效应游戏的策略搭配的计算器, 

本工具录入了苍翼混沌效应的所有策略树的所有策略, 使用本工具可以计算对于某属性要求, 技能要求的**所有五红**策略搭配, **并进行适配度评分**, 方便玩家找到最适合的策略搭配

根据作者自己使用体验, 还行能用



## 3 使用环境搭建

使用本工具需要搭建python环境, 虽然作者会python打包, 但是conda的打包存在bug, 打包出来的文件太大, 不如不打包. 相信配置python环境如此简单, 每一个用户都能学会的



注意: python具有pip环境和conda环境两种环境, 为避免库冲突, 统一推荐使用conda环境, 关于anaconda的安装方法请自行百度, 这里不做说明, 仅介绍使用方法

注意2: 在使用前, 默认你已经会终端命令行操作方法, 并且正确地安装了conda



### 3.1 添加镜像源

如果是第一次安装conda, 建议添加镜像源, 国内的镜像源安装更快

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
```

### 3.2 创建新的环境

```
conda create --name StrategyCalculator python=3.12.3
```

创建完之后, 你需要激活新的环境

```
conda activate StrategyCalculator
```

### 3.3 安装三方库

先cd到工具目录下， 运行下面命令, **这个步骤可能需要管理员权限**

```
conda install --file requirements.txt
```

如果以上步骤都没有报错,  此时工具已经可以正常运行



## 4 工具使用方法介绍

使用前必须激活对应的conda环境

```
conda activate StrategyCalculator
```

按下面方法操作

### 4.1 调整config文件

工具以config文件作为输入, 该文件是yaml格式文件

目前可以调整的config有三个

|               | 意义                                                         | 输入                                                         |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| outputLen     | 输出搭配最大数量, 如果你不想看到几十万种组合, 推荐设置为较小的值, 如100 | 一个整数, 或者null(表示不限制)                               |
| needAttribute | 需要计算的属性, 支持刃, 暗, 电, 火, 冰, 光, 毒, 按照需要增删, 注意这个参数不影响双重策略的选择 | 一般输入两个属性即可, 最佳搭配一般都是两种属性               |
| includeStra   | 必须包括的策略, 例如["召唤冰刺", "无尽冰刺"]                 | 比如你就想使用"召唤冰刺"和"无尽冰刺"这两个策略, 可以设置这个属性 |

### 4.2 运行工具

```
python main.py
```

如果配置不合理会报错

### 4.3 查看结果

所有结果均保存在./results/ 下



## 5 注意事项

1. 由于游戏里无法直接看到双重策略需要哪些触发策略才可以被激活, 目前代码里的双重策略trriger属性大部分是作者推测的(详见源码class Strategy的trriger属性), 这些推测应该大部分是正确的, 但不排除少部分与实际存在差异, 因此计算出的搭配仅供参考

   如果你动手能力强, 可以直接修改源码策略的trriger属性, 或者在发现之后可以反馈给我, 不定期进行更新

2. 工具的计算结果仅是 "可以激活的策略搭配", 游戏中策略的获取条件和激活条件是不一样的, 请酌情判断你选择的搭配是否可以真的获取到(举例, 双重策略"影子转化"只需要有"普攻影刺"或"冲刺影刺"就可以激活, 但是你在战斗中想刷到这个策略需要有"影刺强化"和"放置地雷"两个策略才可以, 通过策略传承可以绕过这个问题)

3. 该工具对于搭配的评分"fitScore"是对于双重策略词条联动性的评分, 不代表策略搭配的DPS高或者真的好用, 仅供参考



另外, 觉得好用的话就点个星吧, 不定期更新其他有用的程序





