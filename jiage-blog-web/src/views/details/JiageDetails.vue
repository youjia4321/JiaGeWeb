<template>
  <JiageContent :title="title">
    <Card slot="main-content">
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
          <div class="blog-content" v-html="dataArr.content"></div>
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
            &nbsp;&nbsp;|&nbsp;&nbsp;
            <a
              v-if="auth"
              @click="modalComment = true"
            >去评论</a>
            <router-link v-else to="/account/login">去评论</router-link>
          </div>
          <Modal title="发表评论" v-model="modalComment" @on-ok="handleSubmit">
            <Form>
              <FormItem>
                <i-Input type="textarea" v-model="content" placeholder="想对作者说点什么..."></i-Input>
              </FormItem>
            </Form>
          </Modal>
        </div>
      </div>
    </Card>
    <div slot="comment" class="comments">
      <h4 class="comment-title">热评</h4>
      <div v-if="isComment">
        <div v-for="(item, index) in dataComments" :key="index" class="info-box">
          <span class="info-avatar">
            <Avatar :src="'http://192.168.1.65:8000/media/'+ item.portrait " size="small"></Avatar>&nbsp;&nbsp;
          </span>
          <span class="info-author">{{item.author}}：</span>
          <span class="info-content">{{item.content}}</span>
          <span class="info-time">&nbsp;&nbsp;&nbsp;&nbsp;{{item.pub}}</span>
          &nbsp;&nbsp;
          <a class="report">举报</a>
          &nbsp;&nbsp;
          <a class="response">回复</a>
        </div>
      </div>
      <div v-else>暂无评论</div>
    </div>
  </JiageContent>
</template>
<script>
import JiageContent from "@/components/JiageContent";

export default {
  name: "JiageDetails",
  data() {
    return {
      modalComment: false,
      username: "",
      content: "",
      title: "博客详情",
      blogId: "",
      dataArr: [],
      dataComments: [],
      auth: true,
      isComment: true
    };
  },
  created() {
    this.blogId = this.$route.query.blogId;
    this.getBlogInfo();
    let user = JSON.parse(sessionStorage.getItem("user"));
    if (user) {
      this.username = user["username"];
    } else {
      this.auth = false;
    }
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
    getBlogInfo() {
      this.$http.getBlogDetails(this.blogId).then(resp => {
        if (resp.result.code === "200") {
          this.dataArr = resp.result.data;
          this.dataComments = resp.result.comments;
          if (this.dataComments.length === 0) {
            this.isComment = false;
          }
        }
      });
    },
    handleSubmit() {
      if (
        this.content.indexOf(" ") >= 0 ||
        (this.content === null) | (this.content === "")
      ) {
        this.$Message.error("评论不能为空格或者null值");
      } else {
        this.$http
          .postBlogDetails(
            this.blogId,
            this.username,
            this.content,
            this.getCookie("csrftoken")
          )
          .then(resp => {
            if (resp.result.code === "200") {
              this.$Message.success("发表评论成功");
              this.reload();
            } else {
              this.$Message.error("发表评论失败");
            }
          });
      }
    }
  }
};
</script>

<style scoped lang="scss">
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
.comments {
  border: solid 1px #e0d8d6;
  padding: 20px;
  border-radius: 4px;
}
.comment-title {
  margin-bottom: 15px;
  font-weight: 600;
}
.info-box {
  font-size: 13px;
  margin-bottom: 15px;
}
.info-box:hover {
  .report,
  .response {
    display: inline-block;
  }
}
.info-avatar {
  cursor: pointer;
}
.info-time {
  font-size: 12px;
  color: gray;
}
.report,
.response {
  font-size: 11px;
  display: none;
  text-decoration: none;
}
.report:hover,
.response:hover {
  opacity: 0.6;
}
h3 {
  font-size: 22px;
}
.blog-content {
  border: 1px solid #ece9e9;
  padding: 20px;
  border-radius: 5px;
}
</style>
