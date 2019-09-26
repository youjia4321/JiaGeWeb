<template>
  <div id="app">
    <router-view name="header"></router-view>
    <router-view name="default"></router-view>
    <router-view name="footer"></router-view>
    <BackTop></BackTop>
  </div>
</template>

<script>
export default {
  name: "app"
};
</script>

<style>
.ivu-breadcrumb a {
  color: #fff !important;
}
.ivu-avatar > img {
  vertical-align: initial;
}
::-webkit-scrollbar {
  width: 5px;
  height: 5px;
  background-color: rgba(245, 245, 245, 0.47);
}
/*定义滚动条的轨道，内阴影及圆角*/
::-webkit-scrollbar-track {
  border-radius: 10px;
  background-color: #f5f5f5;
}
/*定义滑块，内阴影及圆角*/
::-webkit-scrollbar-thumb {
  border-radius: 10px;
  background-color: rgba(85, 85, 85, 0.25);
}
</style>
