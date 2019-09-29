<template>
  <div class="layout">
    <Layout>
      <Content :style="{padding: '0 200px'}">
        <Breadcrumb :style="{margin: '20px 0'}">
          <BreadcrumbItem>{{ title }}</BreadcrumbItem>
        </Breadcrumb>
        <slot name="main-content"></slot>
        <slot name="comment"></slot>
      </Content>
    </Layout>
  </div>
</template>
<script>
export default {
  name: "JiageContent",
  props: ["title"],
  data() {
    return {};
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
