"""
测试1
测试权限组类
"""
import _pbot
log = _pbot.plog.DEFAULT_LOG.info
_pbot.plog.DEFAULT_LOG.info("测试-创建权限组1")
p = _pbot.pbot_cl.PermissionGroup("权限组1")
_pbot.plog.DEFAULT_LOG.info("测试-获取其权限")
_pbot.plog.DEFAULT_LOG.info(p.get_p())
_pbot.plog.DEFAULT_LOG.info("测试-更改其权限为4")
_pbot.plog.DEFAULT_LOG.info(p.set_p(4))
_pbot.plog.DEFAULT_LOG.info("测试-更改其权限为0")
_pbot.plog.DEFAULT_LOG.info(p.set_p(0))
_pbot.plog.DEFAULT_LOG.info("测试-更改其权限为q")
_pbot.plog.DEFAULT_LOG.info(p.set_p("q"))
# _pbot.plog.DEFAULT_LOG.info()
_pbot.plog.DEFAULT_LOG.info(f"测试-pg_list 内容：{_pbot.values.pg_list}")
log(f"测试-添加用户 菌叔 {p.add_user('菌叔')}")
log(f"测试-查看用户 {p.get_users()}")
log(f"测试-添加非法用户 b\"miku\" {p.add_user(b'miku')}")
log(f"测试-查看用户 {p.get_users()}")
log(f"测试-导出数据 {p.save()}")
data = {
            "Type": "PermissionGroup",
            "Name": "咕咕",
            "Permission": 5,
            "Users": [
                "Miku",
                "Duck",
                "菌叔"
            ]
        }
log(f"测试-载入数据 {p.load(data)}")
log(f"测试-查看用户 {p.get_users()}")
_pbot.plog.DEFAULT_LOG.info("测试-获取其权限")
_pbot.plog.DEFAULT_LOG.info(p.get_p())
