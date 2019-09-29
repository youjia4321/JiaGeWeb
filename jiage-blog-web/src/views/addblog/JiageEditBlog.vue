<template>
  <JiageContent :title="title">
    <Card slot="main-content">
      <div class="infinite-list-wrapper" style="min-height: 450px;">
        <Form ref="formInline" :model="formInline" :rules="ruleInline">
          <FormItem prop="blogTitle">
            <div class="prompt">Subject</div>
            <i-Input
              type="text"
              v-model="formInline.blogTitle"
              placeholder="enter blog subject..."
              style="width: 300px"
              clearable
            >
              <Icon type="ios-school" slot="prepend" size="16"></Icon>
            </i-Input>
          </FormItem>
          <FormItem prop="blogAuthor">
            <div class="prompt">Author</div>
            <i-Input
              type="text"
              v-model="formInline.blogAuthor"
              placeholder="enter blog author..."
              style="width: 300px; color: #000"
              disabled
            >
              <Icon type="ios-person" slot="prepend" size="16"></Icon>
            </i-Input>
          </FormItem>

          <FormItem prop="blogContent">
            <div class="prompt">Content</div>
            <vue-editor v-model="formInline.blogContent"></vue-editor>
          </FormItem>
          <FormItem>
            <Button
              class="btn"
              type="success"
              size="large"
              long
              @click="handleBlogSub('formInline')"
            >Published articles</Button>
          </FormItem>
        </Form>
      </div>
    </Card>
  </JiageContent>
</template>

<script>
import JiageContent from "@/components/JiageContent";
import { VueEditor } from "vue2-editor";

export default {
  data() {
    return {
      title: "编辑文章",
      formInline: {
        blogTitle: "",
        blogContent: "",
        blogAuthor: ""
      },
      ruleInline: {
        blogTitle: [
          {
            required: true,
            message: "Please enter the blog subject",
            trigger: "blur"
          }
        ],
        blogAuthor: [
          {
            required: true,
            message: "Please enter the blog author",
            trigger: "blur"
          }
        ],
        blogContent: [
          {
            required: true,
            message: "Please enter the blog content",
            trigger: "blur"
          }
        ]
      }
    };
  },
  components: {
    JiageContent,
    VueEditor
  },
  inject: ["reload"],
  created() {
    this.blogId = this.$route.query.blogId;
    this.getBlogInfo();
    let user = JSON.parse(sessionStorage.getItem("user"));
    this.formInline.blogAuthor = user["username"];
  },
  methods: {
    getBlogInfo() {
      this.$http.getBlogEdit(this.blogId).then(resp => {
        if (resp.result.code === "200") {
          this.formInline.blogTitle = resp.result.title;
          this.formInline.blogContent = resp.result.content;
        }
      });
    },
    // 获取csrftoken
    getCookie(name) {
      var value = "; " + document.cookie;
      var parts = value.split("; " + name + "=");
      if (parts.length === 2)
        return parts
          .pop()
          .split(";")
          .shift();
    },
    // 编辑保存
    handleBlogSub(name) {
      var _this = this;
      this.$refs[name].validate(valid => {
        if (valid) {
          var title = _this.formInline.blogTitle;
          var content = _this.formInline.blogContent;
          _this.$http
            .postSaveBlog(
              this.blogId,
              title,
              content,
              _this.getCookie("csrftoken")
            )
            .then(resp => {
              if (resp.result.code === "200") {
                _this.$Message.success(resp.result.msg);
                this.$router.push({
                  name: "Mineblog"
                });
                this.reload();
              } else {
                _this.$Message.error(resp.result.msg);
              }
            });
        } else {
          _this.$Message.error("Fail!");
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
.prompt {
  font-size: 13px;
  font-weight: 600;
}
.btn {
  font-weight: 600;
}
</style>