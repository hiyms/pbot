"""

"""

from . import values
from . import plog

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

    @plog.DEFAULT_LOG.catch(level="WARNING")
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

    @plog.DEFAULT_LOG.catch(level="WARNING")
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
            plog.DEFAULT_LOG.info(f"未找到此用户 {user_id}")
            return False

    def get_users(self) -> list:
        return self.__user_list

class EventClass:
    def __int__(self,name: str):
        log.info(f"创建事件 {str}")

