# xadmin全局配置
import xadmin
from xadmin import views
# from . import models

class GlobalSettings(object):
    """
    xadmin的全局配置
    """
    site_title = '路飞学城'
    site_footer = '路飞学城有限公司'
    list_editable =['name','img','link','is_delete','is_show','display_order']
    menu_style = 'accordion'  # 设置菜单折叠


xadmin.site.register(views.CommAdminView,GlobalSettings)
# 注册 BaseModel表

# xadmin.site.register(models.Banner)
