#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import patterns, url
from designer.view import up_works,views


urlpatterns = patterns('',

	# 设计师个人中心
    url(r'^works_upload$',up_works.works_upload,name = 'works_upload'),

	url(r'^works_save$',up_works.works_save,name = 'works_save'),

	#未处理页面，点击处理并提交 的处理表单；同时也是 未通过，点击重生申请发布的 处理表单
	url(r'^edit_submit$',up_works.edit_submit,name = 'edit_submit'),

	#设计师作品管理，显示 未处理 页面
	url(r'^workd_unexecute$',up_works.workd_unexecute,name = 'workd_unexecute'),

	#未处理页面的删除cao zuo
	url(r'^unexecute_delete$',up_works.unexecute_delete,name = 'unexecute_delete'),

	#未通过 页面
	url(r'^not_passed$',up_works.not_passed,name = 'not_passed'),

	#审核中,显示未审核的页面
	url(r'^auditing$',up_works.auditing,name = 'auditing'),

	#显示已发布页面
	#designer_works
	url(r'^designer_works$',up_works.designer_works,name = 'designer_works'),

	url(r'^has_published$',up_works.has_published,name = 'has_published'),

	#在已发布页面点击编辑后，传的值
	url(r'^published_edit$',up_works.published_edit,name = 'published_edit'),

	#deletePic  删除图片
	url(r'^deletePic$',up_works.deletePic,name = 'deletePic'),

	#在已发布页面点击编辑后，修改后提交的值
	url(r'^published_submit$',up_works.published_submit,name = 'published_submit'),

	#screenshot
	url(r'^screenshot$',up_works.screenshot,name = 'screenshot'),
	#设计师个人中心，设计师本人看到的
	url(r'^designer_personal$',views.my_personal,name = 'my_personal'),

	##作品管理的 已发布7和设计师个人主页 都是用的这个部分方法实现 按照下载次数排序 downed_list
	url(r'^sort_list$',views.sort_list,name = 'sort_list'),

	#搜索方法
	url(r'^unpublished_good_search$',views.unpublished_good_search,name = 'unpublished_good_search'),

	#搜索已发布商品的方法  published_good_search
	url(r'^published_good_search$',views.published_good_search,name = 'published_good_search'),

	#显示我的动态的页面 my_state
	url(r'^my_state$',views.my_state,name = 'my_state'),
	
	url(r'^works_visit$',views.works_visit,name = 'works_visit'),

	url(r'^setup$',views.setup,name = 'setup'),
    #下载
    url(r'^file_download$', up_works.file_download, name = 'file_download'),
	#show_3d
	url(r'^show_3d$',views.show_3d,name = 'show_3d'),

	#添加关注和收藏
	url(r'^add_focus$',views.add_focus,name = 'add_focus'),

	url(r'^cancel_focus$',views.cancel_focus,name = 'cancel_focus'),

	url(r'^add_collect$',views.add_collect,name = 'add_collect'),

	url(r'^cancel_collect$',views.cancel_collect,name = 'cancel_collect'),
	
	url(r'^add_alipay$',views.add_alipay,name = 'add_alipay'),
	#u_img
	url(r'^u_img$',views.u_img,name = 'u_img'),
)
