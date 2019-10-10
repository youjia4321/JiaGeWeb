<template>
  <JiageContent :title="title">
    <Card slot="main-content">
      <div class="infinite-list-wrapper" style="min-height: 450px;">
        <div v-if="show">
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
              <div v-html="$options.filters.capitalize(item.content)"></div>
              <br />
              <div class="blog-base-info">
                <Poptip trigger="hover" :title="item.author" placement="right">
                  <Avatar
                    class="avatar-img"
                    :src="api+'/media/'+ item.portrait"
                    size="small"
                  />
                  <div class="api" slot="content">
                    <Avatar :src="api+'/media/'+ item.portrait" />&nbsp;&nbsp;
                    <a class="person-info">访问主页</a>
                  </div>
                </Poptip>
                <i>
                  &nbsp;
                  <a class="person-info">{{ item.author }}</a>
                </i>
                <span class="blog-info">
                  阅读数
                  <span class="dight">{{ item.visit }}</span> &nbsp;&nbsp;|&nbsp;&nbsp; 评论数
                  <span class="dight">{{ item.comment_count }}</span>
                </span>
              </div>
            </div>
          </div>
        </div>
        <div v-else>
          <h3>暂无文章...</h3>
        </div>
      </div>
    </Card>
  </JiageContent>
</template>
<script>
import JiageContent from "@/components/JiageContent";

export default {
  name: "JiageIndex",
  data() {
    return {
      title: "博客首页",
      dataArr: [],
      cateName: "",
      show: true,
      api: this.api
    };
  },
  created() {
    this.cateName = this.$route.query.cateName;
    this.listOfBlog();
  },
  components: {
    JiageContent
  },
  methods: {
    getCookie(name) {
      var value = "; " + document.cookie;
      var parts = value.split("; " + name + "=");
      if (parts.length === 2)
        return parts
          .pop()
          .split(";")
          .shift();
    },
    listOfBlog() {
      var _this = this;
      _this.$http
        .getChooseCategory(this.cateName, this.getCookie("csrftoken"))
        .then(resp => {
          if (resp.result.code === "200") {
            _this.dataArr = resp.result.data;
            if (_this.dataArr.length === 0) {
              this.show = false;
            }
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
  color: #b50d0d;
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
h3 {
  font-size: 22px;
}
.blog-info {
  float: right;
}
.dight {
  color: #4b82e4;
}
.sider {
  background: #fff;
}
.tag-list {
  width: 135px;
}
.cate-list {
  position: fixed;
  display: grid;
}
</style>
