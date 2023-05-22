# coding: utf-8
from sqlalchemy import (
    BigInteger,
    Column,
    ForeignKey,
    Index,
    Integer,
    SmallInteger,
    String,
    TIMESTAMP,
    Table,
    Text,
    text,
)
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, LONGTEXT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

# 自动生成
# sqlacodegen mysql+mysqlconnector://root:123456@127.0.0.1:3306/test > models.py


class Article(Base):
    __tablename__ = "article"
    __table_args__ = {"comment": "文章"}

    id = Column(INTEGER, primary_key=True, comment="编码")
    title = Column(String(128), comment="标题")
    author = Column(String(128), comment="作者")
    content = Column(String(255), comment="内容")
    status = Column(Integer, comment="状态")
    publish_at = Column(TIMESTAMP, comment="发布时间")
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP, index=True)
    create_by = Column(INTEGER)
    update_by = Column(INTEGER)


class SchemaMigration(Base):
    __tablename__ = "schema_migrations"

    version = Column(BigInteger, primary_key=True)
    dirty = Column(TINYINT(1), nullable=False)


class SysApi(Base):
    __tablename__ = "sys_api"

    id = Column(BigInteger, primary_key=True, comment="主键编码")
    handle = Column(String(128), comment="handle")
    title = Column(String(128), comment="标题")
    path = Column(String(128), comment="地址")
    type = Column(String(16), comment="接口类型")
    action = Column(String(16), comment="请求类型")
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    deleted_at = Column(DATETIME(fsp=3), index=True, comment="删除时间")
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")

    sys_menu_menus = relationship("SysMenu", secondary="sys_menu_api_rule")


class SysCasbinRule(Base):
    __tablename__ = "sys_casbin_rule"
    __table_args__ = (
        Index(
            "idx_sys_casbin_rule",
            "ptype",
            "v0",
            "v1",
            "v2",
            "v3",
            "v4",
            "v5",
            "v6",
            "v7",
            unique=True,
        ),
    )

    id = Column(BIGINT, primary_key=True)
    ptype = Column(String(100, "utf8mb4_general_ci"))
    v0 = Column(String(100, "utf8mb4_general_ci"))
    v1 = Column(String(100, "utf8mb4_general_ci"))
    v2 = Column(String(100, "utf8mb4_general_ci"))
    v3 = Column(String(100, "utf8mb4_general_ci"))
    v4 = Column(String(100, "utf8mb4_general_ci"))
    v5 = Column(String(100, "utf8mb4_general_ci"))
    v6 = Column(String(25, "utf8mb4_general_ci"))
    v7 = Column(String(25, "utf8mb4_general_ci"))


class SysColumn(Base):
    __tablename__ = "sys_columns"

    column_id = Column(BigInteger, primary_key=True)
    table_id = Column(BigInteger)
    column_name = Column(String(128))
    column_comment = Column(String(128))
    column_type = Column(String(128))
    go_type = Column(String(128))
    go_field = Column(String(128))
    json_field = Column(String(128))
    is_pk = Column(String(4))
    is_increment = Column(String(4))
    is_required = Column(String(4))
    is_insert = Column(String(4))
    is_edit = Column(String(4))
    is_list = Column(String(4))
    is_query = Column(String(4))
    query_type = Column(String(128))
    html_type = Column(String(128))
    dict_type = Column(String(128))
    sort = Column(BigInteger)
    list = Column(String(1))
    pk = Column(TINYINT(1))
    required = Column(TINYINT(1))
    super_column = Column(TINYINT(1))
    usable_column = Column(TINYINT(1))
    increment = Column(TINYINT(1))
    insert = Column(TINYINT(1))
    edit = Column(TINYINT(1))
    query = Column(TINYINT(1))
    remark = Column(String(255))
    fk_table_name = Column(LONGTEXT)
    fk_table_name_class = Column(LONGTEXT)
    fk_table_name_package = Column(LONGTEXT)
    fk_label_id = Column(LONGTEXT)
    fk_label_name = Column(String(255))
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    deleted_at = Column(DATETIME(fsp=3), index=True, comment="删除时间")
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")


class SysConfig(Base):
    __tablename__ = "sys_config"

    id = Column(BigInteger, primary_key=True, comment="主键编码")
    config_name = Column(String(128), comment="ConfigName")
    config_key = Column(String(128), comment="ConfigKey")
    config_value = Column(String(255), comment="ConfigValue")
    config_type = Column(String(64), comment="ConfigType")
    is_frontend = Column(String(64), comment="是否前台")
    remark = Column(String(128), comment="Remark")
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    deleted_at = Column(DATETIME(fsp=3), index=True, comment="删除时间")


class SysDept(Base):
    __tablename__ = "sys_dept"

    dept_id = Column(BigInteger, primary_key=True)
    parent_id = Column(BigInteger)
    dept_path = Column(String(255))
    dept_name = Column(String(128))
    sort = Column(TINYINT)
    leader = Column(String(128))
    phone = Column(String(11))
    email = Column(String(64))
    status = Column(TINYINT)
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    deleted_at = Column(DATETIME(fsp=3), index=True, comment="删除时间")


class SysDictDatum(Base):
    __tablename__ = "sys_dict_data"

    dict_code = Column(BigInteger, primary_key=True)
    dict_sort = Column(BigInteger)
    dict_label = Column(String(128))
    dict_value = Column(String(255))
    dict_type = Column(String(64))
    css_class = Column(String(128))
    list_class = Column(String(128))
    is_default = Column(String(8))
    status = Column(TINYINT)
    default = Column(String(8))
    remark = Column(String(255))
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    deleted_at = Column(DATETIME(fsp=3), index=True, comment="删除时间")


class SysDictType(Base):
    __tablename__ = "sys_dict_type"

    dict_id = Column(BigInteger, primary_key=True)
    dict_name = Column(String(128))
    dict_type = Column(String(128))
    status = Column(TINYINT)
    remark = Column(String(255))
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    deleted_at = Column(DATETIME(fsp=3), index=True, comment="删除时间")


class SysJob(Base):
    __tablename__ = "sys_job"

    job_id = Column(BigInteger, primary_key=True)
    job_name = Column(String(255))
    job_group = Column(String(255))
    job_type = Column(TINYINT)
    cron_expression = Column(String(255))
    invoke_target = Column(String(255))
    args = Column(String(255))
    misfire_policy = Column(BigInteger)
    concurrent = Column(TINYINT)
    status = Column(TINYINT)
    entry_id = Column(SmallInteger)
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    deleted_at = Column(DATETIME(fsp=3), index=True, comment="删除时间")
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")


class SysLoginLog(Base):
    __tablename__ = "sys_login_log"

    id = Column(BigInteger, primary_key=True, comment="主键编码")
    username = Column(String(128), comment="用户名")
    status = Column(String(4), comment="状态")
    ipaddr = Column(String(255), comment="ip地址")
    login_location = Column(String(255), comment="归属地")
    browser = Column(String(255), comment="浏览器")
    os = Column(String(255), comment="系统")
    platform = Column(String(255), comment="固件")
    login_time = Column(TIMESTAMP, comment="登录时间")
    remark = Column(String(255), comment="备注")
    msg = Column(String(255), comment="信息")
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")


class SysMenu(Base):
    __tablename__ = "sys_menu"

    menu_id = Column(BigInteger, primary_key=True)
    menu_name = Column(String(128))
    title = Column(String(128))
    icon = Column(String(128))
    path = Column(String(128))
    paths = Column(String(128))
    menu_type = Column(String(1))
    action = Column(String(16))
    permission = Column(String(255))
    parent_id = Column(SmallInteger)
    no_cache = Column(TINYINT(1))
    breadcrumb = Column(String(255))
    component = Column(String(255))
    sort = Column(TINYINT)
    visible = Column(String(1))
    is_frame = Column(String(1), server_default=text("'0'"))
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    deleted_at = Column(DATETIME(fsp=3), index=True, comment="删除时间")

    roles = relationship("SysRole", secondary="sys_role_menu")


class SysMigration(Base):
    __tablename__ = "sys_migration"

    version = Column(String(191, "utf8mb4_general_ci"), primary_key=True)
    apply_time = Column(DATETIME(fsp=3))


class SysOperaLog(Base):
    __tablename__ = "sys_opera_log"

    id = Column(BigInteger, primary_key=True, comment="主键编码")
    title = Column(String(255), comment="操作模块")
    business_type = Column(String(128), comment="操作类型")
    business_types = Column(String(128), comment="BusinessTypes")
    method = Column(String(128), comment="函数")
    request_method = Column(String(128), comment="请求方式: GET POST PUT DELETE")
    operator_type = Column(String(128), comment="操作类型")
    oper_name = Column(String(128), comment="操作者")
    dept_name = Column(String(128), comment="部门名称")
    oper_url = Column(String(255), comment="访问地址")
    oper_ip = Column(String(128), comment="客户端ip")
    oper_location = Column(String(128), comment="访问位置")
    oper_param = Column(Text, comment="请求参数")
    status = Column(String(4), comment="操作状态 1:正常 2:关闭")
    oper_time = Column(TIMESTAMP, comment="操作时间")
    json_result = Column(String(255), comment="返回数据")
    remark = Column(String(255), comment="备注")
    latency_time = Column(String(128), comment="耗时")
    user_agent = Column(String(255), comment="ua")
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")


class SysPost(Base):
    __tablename__ = "sys_post"

    post_id = Column(BigInteger, primary_key=True)
    post_name = Column(String(128))
    post_code = Column(String(128))
    sort = Column(TINYINT)
    status = Column(TINYINT)
    remark = Column(String(255))
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    deleted_at = Column(DATETIME(fsp=3), index=True, comment="删除时间")


class SysRole(Base):
    __tablename__ = "sys_role"

    role_id = Column(BigInteger, primary_key=True)
    role_name = Column(String(128))
    status = Column(String(4))
    role_key = Column(String(128))
    role_sort = Column(BigInteger)
    flag = Column(String(128))
    remark = Column(String(255))
    admin = Column(TINYINT(1))
    data_scope = Column(String(128))
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    deleted_at = Column(DATETIME(fsp=3), index=True, comment="删除时间")


class SysRoleDept(Base):
    __tablename__ = "sys_role_dept"

    role_id = Column(SmallInteger, primary_key=True, nullable=False)
    dept_id = Column(SmallInteger, primary_key=True, nullable=False)


class SysTable(Base):
    __tablename__ = "sys_tables"

    table_id = Column(BigInteger, primary_key=True)
    table_name = Column(String(255))
    table_comment = Column(String(255))
    class_name = Column(String(255))
    tpl_category = Column(String(255))
    package_name = Column(String(255))
    module_name = Column(String(255))
    module_front_name = Column(String(255), comment="前端文件名")
    business_name = Column(String(255))
    function_name = Column(String(255))
    function_author = Column(String(255))
    pk_column = Column(String(255))
    pk_go_field = Column(String(255))
    pk_json_field = Column(String(255))
    options = Column(String(255))
    tree_code = Column(String(255))
    tree_parent_code = Column(String(255))
    tree_name = Column(String(255))
    tree = Column(TINYINT(1), server_default=text("'0'"))
    crud = Column(TINYINT(1), server_default=text("'1'"))
    remark = Column(String(255))
    is_data_scope = Column(TINYINT)
    is_actions = Column(TINYINT)
    is_auth = Column(TINYINT)
    is_logical_delete = Column(String(1))
    logical_delete = Column(TINYINT(1))
    logical_delete_column = Column(String(128))
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    deleted_at = Column(DATETIME(fsp=3), index=True, comment="删除时间")
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")


class SysUser(Base):
    __tablename__ = "sys_user"

    user_id = Column(BigInteger, primary_key=True, comment="编码")
    username = Column(String(64), comment="用户名")
    password = Column(String(128), comment="密码")
    nick_name = Column(String(128), comment="昵称")
    phone = Column(String(11), comment="手机号")
    role_id = Column(BigInteger, comment="角色ID")
    salt = Column(String(255), comment="加盐")
    avatar = Column(String(255), comment="头像")
    sex = Column(String(255), comment="性别")
    email = Column(String(128), comment="邮箱")
    dept_id = Column(BigInteger, comment="部门")
    post_id = Column(BigInteger, comment="岗位")
    remark = Column(String(255), comment="备注")
    status = Column(String(4), comment="状态")
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    deleted_at = Column(DATETIME(fsp=3), index=True, comment="删除时间")


class TbDemo(Base):
    __tablename__ = "tb_demo"

    id = Column(BigInteger, primary_key=True, comment="主键编码")
    name = Column(String(128), comment="名称")
    created_at = Column(DATETIME(fsp=3), comment="创建时间")
    updated_at = Column(DATETIME(fsp=3), comment="最后更新时间")
    deleted_at = Column(DATETIME(fsp=3), index=True, comment="删除时间")
    create_by = Column(BigInteger, index=True, comment="创建者")
    update_by = Column(BigInteger, index=True, comment="更新者")


class User(Base):
    __tablename__ = "user"

    id = Column(String(20, "utf8mb4_general_ci"), primary_key=True)
    name = Column(String(20, "utf8mb4_general_ci"))


t_sys_menu_api_rule = Table(
    "sys_menu_api_rule",
    metadata,
    Column(
        "sys_menu_menu_id",
        ForeignKey("sys_menu.menu_id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "sys_api_id",
        ForeignKey("sys_api.id"),
        primary_key=True,
        nullable=False,
        index=True,
        comment="主键编码",
    ),
)


t_sys_role_menu = Table(
    "sys_role_menu",
    metadata,
    Column("role_id", ForeignKey("sys_role.role_id"), primary_key=True, nullable=False),
    Column(
        "menu_id",
        ForeignKey("sys_menu.menu_id"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)
