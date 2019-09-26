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
          <div class="infinite-list-wrapper" style="min-height: 450px;">
            <h3 class="title">{{ dataArr.title}}</h3>
            <div class="info">
              <p>
                <i>
                  作者：{{ dataArr.author }}
                  &nbsp;&nbsp;
                  发表时间：{{ dataArr.join_time }}
                  &nbsp;&nbsp;
                  分类：{{ dataArr.category }}
                  &nbsp;&nbsp;
                  标签：
                  <span
                    class="tag"
                    v-for="(dataArr, index) in dataArr.tags"
                    :key="index"
                  >{{ dataArr }}&nbsp;&nbsp;</span>
                </i>
              </p>
              <div>
                <pre>{{ dataArr.content }}</pre>
              </div>
              <br />
              <div class="blog-base-info">
                <Poptip trigger="hover" placement="right">
                  <Avatar :src="'http://192.168.1.65:8000/media/'+ dataArr.portrait "></Avatar>
                  <div class="api" slot="content">
                    <Avatar :src="'http://192.168.1.65:8000/media/'+ dataArr.portrait " />&nbsp;&nbsp;
                    <a class="person-info">访问主页</a>
                  </div>
                </Poptip>
                <i>
                  &nbsp;
                  <a class="person-info">{{ dataArr.author }}</a>
                </i>
                &nbsp;&nbsp;|&nbsp;&nbsp;阅读数：{{ dataArr.visit }} &nbsp;&nbsp;|&nbsp;&nbsp; 评论数：{{ dataArr.comment_count }}
              </div>
            </div>
          </div>
        </Card>
      </Content>
    </Layout>
  </div>
</template>
<script>
export default {
  name: "JiageDetails",
  data() {
    return {
      blogId: "",
      dataArr: []
    };
  },
  created() {
    this.blogId = this.$route.query.blogId;
    this.getBlogInfo();
  },
  methods: {
    getBlogInfo() {
      this.$http.blogDetails(this.blogId).then(resp => {
        if (resp.result.code === "200") {
          this.dataArr = resp.result.data;
        }
      });
    }
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
.title {
  font-weight: 600;
  cursor: pointer;
}
.info {
  color: #888383;
}
.tag {
  color: #f97311;
}
.person-info {
  font-size: 12px;
  text-decoration: none;
}
.avatar-img {
  cursor: pointer;
}
</style>
