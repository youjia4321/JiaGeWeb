<template>
  <Header>
    <Menu mode="horizontal" theme="dark" active-name="1">
      <div class="layout-logo">JiaGE</div>
      <div class="layout-operation">
        <MenuItem name="1">
          <Icon type="md-create" />写博客
        </MenuItem>
        <MenuItem name="2">
          <Icon type="md-mail" />消息
        </MenuItem>
        <MenuItem name="3" to="/login">登录</MenuItem>
        <MenuItem name="4" to="/register">注册</MenuItem>
      </div>
      <div class="layout-search">
        <Input suffix="ios-search" placeholder="输入搜索内容..." style="width: auto" />
      </div>
      <div class="layout-nav">
        <Breadcrumb>
          <BreadcrumbItem to="/">首页</BreadcrumbItem>
          <BreadcrumbItem>博客</BreadcrumbItem>
          <BreadcrumbItem>下载</BreadcrumbItem>
          <BreadcrumbItem>论坛</BreadcrumbItem>
          <BreadcrumbItem>问答</BreadcrumbItem>
          <BreadcrumbItem>商城</BreadcrumbItem>
          <BreadcrumbItem>活动</BreadcrumbItem>
          <BreadcrumbItem>招聘</BreadcrumbItem>
          <BreadcrumbItem>专题</BreadcrumbItem>
          <BreadcrumbItem>VIP会员</BreadcrumbItem>
        </Breadcrumb>
      </div>
    </Menu>
  </Header>
</template>

<script>
export default {};
</script>

<style scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  overflow: hidden;
  min-width: 1410px;
}
.layout-logo {
  width: 100px;
  height: 30px;
  line-height: 30px;
  background: #5b6270;
  border-radius: 3px;
  float: left;
  position: relative;
  top: 15px;
  left: 20px;
  padding-left: 20px;
  color: #fff;
}
.layout-operation {
  float: right;
  width: 300px;
  margin: 0 auto;
  margin-right: 20px;
}
.layout-search {
  float: right;
  width: 200px;
  margin: 0 auto;
  margin-right: 20px;
}
.layout-nav {
  float: right;
  width: 600px;
  margin: 0 auto;
  margin-right: 20px;
}
.ivu-menu-horizontal .ivu-menu-item {
  padding: 0 10px !important;
}
.ivu-breadcrumb{
  color: #fff;
}
.ivu-breadcrumb>span:last-child{
  color: #fff;
  font-weight: 200;
}
</style>