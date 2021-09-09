# coding:utf-8

# 快速启动数据项
class QuickOpenItem:
    path="未设置"
    __icon=None
    
    def GetIcon(self):
        pass

    def Open(self):
        pass

# 命令脚本数据项
class ScriptItem:
    args=[]
    path="未设置"
    desc="未设置"
    __icon=None

    def GetIcon(self):
        pass

    def Run(self):
        pass