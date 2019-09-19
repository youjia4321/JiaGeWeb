<template>
  <div class="layout">
    <Layout>
      <Content :style="{padding: '0 200px'}">
        <Breadcrumb :style="{margin: '20px 0'}">
          <BreadcrumbItem>Progresses</BreadcrumbItem>
          <BreadcrumbItem>Efforts to</BreadcrumbItem>
          <BreadcrumbItem>Forward</BreadcrumbItem>
        </Breadcrumb>
        <Card>
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
      </Content>
    </Layout>
  </div>
</template>

<script>
export default {};
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