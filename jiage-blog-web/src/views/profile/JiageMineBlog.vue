<template>
  <JiageContent :title="title">
    <Card slot="main-content">
      <div class="infinite-list-wrapper" style="min-height: 450px;">
        <div v-for="item in dataArr" :key="item.id">
          <h3 class="title" @click="goBlogDetailPage(item.id)">{{ item.title}}</h3>
          <div class="info">
            <p>
              <i>
                {{ item.join_time }}
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
              <span class="blog-info">
                &nbsp;&nbsp;|&nbsp;&nbsp;
                阅读数
                <span class="dight">{{ item.visit }}</span> &nbsp;&nbsp;|&nbsp;&nbsp; 评论数
                <span class="dight">{{ item.comment_count }}</span>
              </span>
              <span class="operation">
                <span class="top">
                  <a>置顶</a>
                </span>&nbsp;&nbsp;|&nbsp;&nbsp;
                <span class="edit">
                  <a>编辑</a>
                </span>&nbsp;&nbsp;|&nbsp;&nbsp;
                <span class="del">
                  <a @click="showModal(item.id)">删除</a>
                </span>
              </span>
            </div>
          </div>
          <hr />
        </div>
      </div>
      <Modal v-model="modalDel" width="300">
        <p slot="header" style="color: #f60;">
          <Icon type="ios-information-circle"></Icon>
          <span>&nbsp;&nbsp;系统提示</span>
        </p>
        <p>确定要删除当前文章？</p>
        <div slot="footer">
          <Button type="error" size="large" long @click="handleDelBlog()">确认</Button>
        </div>
      </Modal>
    </Card>
  </JiageContent>
</template>

<script>
import JiageContent from "@/components/JiageContent";

export default {
  data() {
    return {
      title: "我的博客",
      author: "",
      dataArr: [],
      modalDel: false,
      delId: ""
    };
  },
  created() {
    let user = JSON.parse(sessionStorage.getItem("user"));
    this.author = user["username"];
    this.getSelfBlog();
  },
  components: {
    JiageContent
  },
  inject: ["reload"],
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
    getSelfBlog() {
      this.$http
        .selfBlogList(this.author, this.getCookie("csrftoken"))
        .then(resp => {
          if (resp.result.code === "200") {
            this.dataArr = resp.result.data;
          }
        });
    },
    goBlogDetailPage(id) {
      this.$router.push({
        name: "Details",
        query: { blogId: id }
      });
    },
    showModal(id) {
      this.modalDel = true;
      this.delId = id;
    },
    handleDelBlog() {
      this.$http.delBlog(this.delId, this.getCookie("csrftoken")).then(resp => {
        if (resp.result.code === "200") {
          this.modalDel = false;
          this.$Message.success(resp.result.msg);
          this.delId = "";
          this.reload();
        }
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

<style scoped lang="scss">
.title {
  font-weight: 600;
  cursor: pointer;
}
.title:hover {
  color: #b50d0d;
}
.info {
  color: #888383;
  cursor: pointer;
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
.operation {
  display: none;
  float: right;
}
.operation a {
  text-decoration: none;
}
.operation a:hover {
  opacity: 0.6;
}
.del a {
  color: red;
}
.info:hover {
  .operation {
    display: inline-block;
  }
}
.dight {
  color: #4b82e4;
}
</style>