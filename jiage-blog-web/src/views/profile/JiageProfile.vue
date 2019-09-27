<template>
  <JiageContent :title="title">
    <Card slot="main-content">
      <div style="min-height: 450px;">
        <el-tabs tab-position="left" :style="{padding: '40px 0'}">
          <el-tab-pane label="个人资料">个人资料</el-tab-pane>
          <el-tab-pane label="我的收藏">我的收藏</el-tab-pane>
          <el-tab-pane label="我的关注">我的关注</el-tab-pane>
          <el-tab-pane label="我的粉丝">我的粉丝</el-tab-pane>
          <el-tab-pane label="我的博客">我的博客</el-tab-pane>
          <el-tab-pane label="我的下载">我的下载</el-tab-pane>
          <el-tab-pane label="我的论坛">我的论坛</el-tab-pane>
        </el-tabs>
      </div>
    </Card>
  </JiageContent>
</template>

<script>
import JiageContent from "@/components/JiageContent";

export default {
  name: "JiageProfile",
  data() {
    return {
      title: "个人中心"
    };
  },
  components: {
    JiageContent
  }
};
</script>

<style scoped>
.layout {
  min-width: 1420px;
}
.ivu-breadcrumb > span:last-child {
  font-weight: normal;
  color: #999;
}
</style>