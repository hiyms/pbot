"""

"""

from . import values
from . import plog
from typing import Any, NoReturn

log = plog.DEFAULT_LOG


class PermissionGroup:
    __user_list: list[str]

    def __init__(self, name: str, p: int = values.DEFAULT_P):
        """
        pbot用来描述权限组的根类
        :param p: 权限值，最小为1，最大为_pbot.__values.MAX_P所定义的值。
        """
        plog.DEFAULT_LOG.info(f"PermissionGroup初始化 Start（Name:{type(self).__name__}）")
        values.pg_list.append(self)
        self.__user_list = []
        self.__p = p
        self.name = name

    def __del__(self):
        if self in values.pg_list:
            values.pg_list.remove(self)
            plog.DEFAULT_LOG.info(f"{self.name}已卸载")

    @log.catch(level="WARNING")
    def set_p(self, p: int) -> bool:
        """
        设置权限组权限
        :param p: 权限值
        :return: 布尔值，用来描述修改权限是否成功
        """
        plog.DEFAULT_LOG.info(f"{self.name}设置权限{p}")
        if type(p) != type(1):
            plog.DEFAULT_LOG.warning(f"{p}不为整值")
            return False
        if p < 1 or p > values.MAX_P:
            plog.DEFAULT_LOG.warning(f"{p}不是一个可用的值")
            return False
        self.__p = p
        plog.DEFAULT_LOG.success(f"成功将{self.name}设置权限为{self.__p}")
        return True

    def get_p(self) -> int:
        """
        获取权限组权限
        :return: 权限组权限
        """
        return self.__p

    @log.catch(level="WARNING")
    def add_user(self, user_id: str) -> bool:
        """
        为权限组添加用户
        :param user_id: 用户id
        :return: 布尔值，描述是否成功
        """
        plog.DEFAULT_LOG.info(f"添加用户 {user_id}")
        if user_id in self.__user_list:
            plog.DEFAULT_LOG.warning("已添加过的用户")
            return False
        self.__user_list.append(str(user_id))
        plog.DEFAULT_LOG.success("成功添加用户")
        return True

    def del_user(self, user_id: str) -> bool:
        """
        为权限组删除用户
        :param user_id: 用户id
        :return: 布尔值，描述是否成功
        """
        plog.DEFAULT_LOG.info(f"删除用户 {user_id}")
        if user_id in self.__user_list:
            self.__user_list.remove(user_id)
            plog.DEFAULT_LOG.success(f"成功删除用户 {user_id}")
            return True
        else:
            plog.DEFAULT_LOG.warning(f"未找到此用户 {user_id}")
            return False

    def find_user(self, user_id: str) -> bool:
        """
        从权限组搜索用户
        :param user_id: 用户id
        :return: 布尔值
        """
        plog.DEFAULT_LOG.info(f"搜索用户 {user_id}")
        if user_id in self.__user_list:
            plog.DEFAULT_LOG.success(f"找到用户 {user_id}")
            return True
        else:
            plog.DEFAULT_LOG.warning(f"未找到此用户 {user_id}")
            return False

    def get_users(self) -> list:
        return self.__user_list

    def save(self) -> dict[any]:
        """
        保存权限组内容
        :return: 字典，存储该权限组数据
        """
        data = {
            "Type": "PermissionGroup",
            "Name": self.name,
            "Permission": self.__p,
            "Users": self.__user_list,
        }
        return data

    @log.catch(level="WARNING")
    def load(self, data: dict[any]) -> bool:
        """
        加载权限组数据
        :param data: 使用save保存的字典数据
        :return: 布尔值
        """
        log.info(f"{self.name}加载配置\n{data}")
        if data["Type"] != "PermissionGroup":
            log.warning("不支持的数据")
            return False
        self.name = data["Name"]
        self.__p = data["Permission"]
        self.__user_list = data["Users"]
        log.success("加载成功")
        return True


class EventClass:
    __hooks: list[Any]

    def __init__(self, name: str):
        """
        事件基类，用于表述pbot所以事件
        :param name: 事件名称
        """
        log.info(f"创建事件 {name}")
        self.__hooks = []
        self.name = name

    @classmethod
    @log.catch(level="WARNING")
    def __remind(cls, hook, **kwargs):
        """
        调用钩子函数的内部实现
        :param hook: 钩子函数
        :param kwargs: 参数
        """
        hook(**kwargs)

    @log.catch(level="WARNING")
    def add_hook(self, hook: Any, name: str):
        """
        添加钩子函数
        :param name: 钩子名称，仅用于日志
        :param hook: 钩子函数
        """
        log.info(f"{self.name}事件添加钩子{name}")
        self.__hooks.append({name: hook})

    @log.catch(level="WARNING")
    def del_hook(self, name: str) -> any:
        """
        删除钩子函数
        :param name: 钩子名称
        :return: 删除的钩子函数
        """
        log.info(f"{self.name}事件删除钩子 {name}")
        if name in self.__hooks:
            _ = self.__hooks[name]
            del self.__hooks[name]
            log.success(f"{self.name}事件成功删除钩子 {name}")
            return _
        else:
            log.warning(f"{self.name}事件未找到 {name} 钩子")

    def remind_hooks(self, **kwargs) -> NoReturn:
        """
        调用钩子函数
        :param kwargs: 调用钩子函数的参数
        """
        log.info("调用钩子函数")
        for i, y in self.__hooks.items():
            log.info(f"{self.name}事件调用钩子{i}")
            self.__remind(y, **kwargs)
