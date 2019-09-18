<template>
  <div class="layout">
    <Layout>
      <router-view name="header"></router-view>
      <Content :style="{padding: '0 50px'}">
        <Breadcrumb :style="{margin: '20px 0'}">
          <BreadcrumbItem>Home</BreadcrumbItem>
          <BreadcrumbItem>Components</BreadcrumbItem>
          <BreadcrumbItem>Layout</BreadcrumbItem>
        </Breadcrumb>
        <Card>
          <div style="min-height: 450px;">Content</div>
        </Card>
      </Content>
      <Footer class="layout-footer-center">2018-2019 &copy; JiaGE Blog</Footer>
    </Layout>
  </div>
</template>
<script>
export default {};
</script>

<style scoped>
.layout-footer-center {
  text-align: center;
}
.ivu-breadcrumb>span:last-child{
  font-weight: 1;
  color: #999;
}
</style>
