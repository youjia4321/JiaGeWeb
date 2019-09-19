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
            博客标题：
            <Input v-model="blogTitle" placeholder="enter blog subject..." style="width: 300px" />
            <div>{{ blogTitle }}</div>
            <br />
            正文：<Input v-model="blogContent" type="textarea" :rows="15" placeholder="enter something..." />
          </div>
        </Card>
      </Content>
    </Layout>
  </div>
</template>

<script>
export default {
  data() {
    return {
      blogTitle: "",
      blogContent: ""
    };
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