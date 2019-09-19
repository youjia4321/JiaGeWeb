<template>
  <Header>
    <Menu mode="horizontal" theme="dark">
      <div class="layout-logo">JiaGE</div>
      <div class="layout-operation">
        <MenuItem name="1" to="/add/blog">
          <Icon type="md-create" />写博客
        </MenuItem>
        <MenuItem v-if="auth" name="2" to="/account/login">
          <Icon type="md-mail" />消息
        </MenuItem>
        <MenuItem v-else name="2">
          <Dropdown>
            <Icon type="md-mail" />&nbsp;&nbsp;消息
            <DropdownMenu slot="list">
              <DropdownItem>评论</DropdownItem>
              <DropdownItem>关注</DropdownItem>
              <DropdownItem>点赞</DropdownItem>
              <DropdownItem>回答</DropdownItem>
              <DropdownItem>系统通知</DropdownItem>
            </DropdownMenu>
          </Dropdown>
        </MenuItem>
        <MenuItem v-if="auth" name="3" to="/account/login">登录</MenuItem>
        <MenuItem v-if="auth" name="4" to="/account/register">注册</MenuItem>
        <Dropdown v-else>
          <div class="avatar" style="color: #fff; cursor: pointer">
            <Avatar :src="'http://192.168.1.65:8000/media/'+backAvatar" size="small" />
            <!-- <Avatar :src="defaultAvatar" size="small" /> -->
            <Icon type="md-arrow-dropdown" />
          </div>
          <DropdownMenu slot="list">
            <router-link to="/account/index">
              <DropdownItem name="attention">
                <Icon type="ios-pricetags-outline" />&nbsp;我的关注
              </DropdownItem>
            </router-link>
            <router-link to="/account/index">
              <DropdownItem name="collection">
                <Icon type="ios-bookmark-outline" />&nbsp;我的收藏
              </DropdownItem>
            </router-link>
            <router-link to="/account/index">
              <DropdownItem name="profile">
                <Icon type="ios-person-outline" />&nbsp;个人中心
              </DropdownItem>
            </router-link>
            <router-link to="/account/index">
              <DropdownItem name="setting">
                <Icon type="ios-settings-outline" />&nbsp;账号设置
              </DropdownItem>
            </router-link>
            <router-link to="/account/index">
              <DropdownItem divided name="blog">
                <Icon type="ios-paper-outline" />&nbsp;我的博客
              </DropdownItem>
            </router-link>
            <router-link to="/account/index">
              <DropdownItem name="manage">
                <Icon type="ios-options-outline" />&nbsp;管理博客
              </DropdownItem>
            </router-link>
            <router-link to="/account/index">
              <DropdownItem name="download">
                <Icon type="ios-download-outline" />&nbsp;我的下载
              </DropdownItem>
            </router-link>
            <router-link to="/account/index">
              <DropdownItem name="bbs">
                <Icon type="ios-mic-outline" />&nbsp;我的论坛
              </DropdownItem>
            </router-link>
            <router-link to="/account/index">
              <DropdownItem divided name="help">
                <Icon type="ios-help-circle-outline" />&nbsp;帮助
              </DropdownItem>
            </router-link>
            <router-link to="/account/login">
              <DropdownItem name="logout">
                <Icon type="ios-log-out" />&nbsp;退出
              </DropdownItem>
            </router-link>
          </DropdownMenu>
        </Dropdown>
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
import defaultAvatar from "../assets/avatar/avatar1.jpg";

export default {
  data() {
    return {
      auth: true,
      user: "",
      backAvatar: "",
      defaultAvatar: defaultAvatar
    };
  },
  created() {
    this.authentication();
  },
  methods: {
    authentication() {
      let user = JSON.parse(sessionStorage.getItem("user"));
      if (user) {
        this.user = user.username;
        this.backAvatar = user.avatar;
        this.auth = false;
      }
    }
  }
};
</script>

<style scoped>
.ivu-menu-item {
  text-decoration: none;
}
.ivu-layout-header {
  min-width: 1420px;
  background: #24292e;
}
.ivu-menu-dark {
  background: #24292e;
}
.layout {
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  overflow: hidden;
}
.layout-logo {
  width: 100px;
  height: 30px;
  line-height: 30px;
  background: #fff;
  border-radius: 3px;
  float: left;
  position: relative;
  top: 15px;
  left: 20px;
  padding-left: 20px;
  color: #000;
  font-weight: 600;
}
.layout-operation {
  float: right;
  width: 300px;
  margin: 0 auto;
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
  padding: 0 15px !important;
}
.ivu-breadcrumb {
  color: #fff;
}
.ivu-breadcrumb > span:last-child {
  color: #fff;
  font-weight: normal;
}
.ivu-avatar > img {
  vertical-align: initial;
}
.ivu-dropdown-menu {
  min-width: 80px;
  letter-spacing: 1px;
}
.ivu-dropdown-menu a {
  color: #515a6e;
  text-decoration: none;
}
</style>