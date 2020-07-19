# -*- coding: UTF-8 -*-

from nameko.rpc import rpc

class GreetingService:
    name = "greeting_service" # 自定义服务名称

    @rpc #入口点标记
    def hello(self, name):
        return "hello. %s??".format(name)
