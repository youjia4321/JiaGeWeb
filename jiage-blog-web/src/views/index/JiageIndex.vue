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
          <div style="min-height: 450px;"></div>
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
