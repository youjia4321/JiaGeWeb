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
            <div v-for="item in dataArr" :key="item.id">
              <h3 class="title" @click="goBlogDetailPage(item.id)">{{ item.title}}</h3>
              <div class="info">
                <p>
                  <i>
                    作者：{{ item.author }}
                    &nbsp;&nbsp;
                    发表时间：{{ item.join_time }}
                    &nbsp;&nbsp;
                    分类：{{ item.category }}
                    &nbsp;&nbsp;
                    标签：
                    <span
                      class="tag"
                      v-for="(item, index) in item.tags"
                      :key="index"
                    >{{ item }}&nbsp;&nbsp;</span>
                  </i>
                </p>
                <div>{{ item.content | capitalize }}</div>
                <br />
                <div class="blog-base-info">
                  <Poptip trigger="hover" :title="item.author" placement="right">
                    <Avatar
                      class="avatar-img"
                      :src="'http://192.168.1.65:8000/media/'+ item.portrait"
                      size="small"
                    />
                    <div class="api" slot="content">
                      <Avatar :src="'http://192.168.1.65:8000/media/'+ item.portrait" />&nbsp;&nbsp;
                      <a class="person-info">访问主页</a>
                    </div>
                  </Poptip>
                  <i>
                    &nbsp;
                    <a class="person-info">{{ item.author }}</a>
                  </i>
                  &nbsp;&nbsp;|&nbsp;&nbsp;阅读数：{{ item.visit }} &nbsp;&nbsp;|&nbsp;&nbsp; 评论数：{{ item.comment_count }}
                </div>
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
  name: "JiageIndex",
  data() {
    return {
      dataArr: []
    };
  },
  created() {
    this.listOfBlog();
  },
  methods: {
    listOfBlog() {
      var _this = this;
      _this.$http.listOfBlog().then(resp => {
        if (resp.result.code === "200") {
          _this.dataArr = resp.result.data;
        }
      });
    },
    goBlogDetailPage(id) {
      this.$router.push({
        name: "Details",
        query: { blogId: id }
      });
    }
  },
  filters: {
    capitalize(value) {
      if (!value) return "";
      if (value.length > 200) {
        return value.slice(0, 200) + "...";
      }
      return value;
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
.title:hover {
  color: #5760b1;
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
