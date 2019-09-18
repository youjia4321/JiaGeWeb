<template>
  <div id="app">
    <router-view name="header"></router-view>
    <router-view name="default"></router-view>
  </div>
</template>

<script>

export default {
  name: 'app',
}
</script>

<style>
.ivu-breadcrumb a{
  color: #fff !important;
}
</style>
