<template>
  <div class="layout">
    <Layout>
      <router-view name="header"></router-view>
      <Content :style="{padding: '0 200px'}">
        <Breadcrumb :style="{margin: '20px 0'}">
          <BreadcrumbItem>Home</BreadcrumbItem>
          <BreadcrumbItem>Components</BreadcrumbItem>
          <BreadcrumbItem>Layout</BreadcrumbItem>
        </Breadcrumb>
        <Card>
          <div style="min-height: 450px;">
          </div>
        </Card>
      </Content>
      <Footer class="layout-footer-center">copyright &copy; 2018-2019 JiaGE Blog. Inc</Footer>
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
.layout-footer-center {
  text-align: center;
  /* position: fixed;
  bottom: 0;
  left: 0;
  right: 0; */
}
.ivu-breadcrumb > span:last-child {
  font-weight: normal;
  color: #999;
}
</style>
