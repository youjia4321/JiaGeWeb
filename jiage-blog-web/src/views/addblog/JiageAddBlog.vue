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
                  style="width: 300px"
                  clearable
                >
                  <Icon type="ios-person" slot="prepend" size="16"></Icon>
                </i-Input>
              </FormItem>
              <FormItem prop="blogContent">
                <div class="prompt">Content</div>
                <Input
                  v-model="formInline.blogContent"
                  type="textarea"
                  :rows="15"
                  placeholder="enter blog content..."
                />
              </FormItem>
              <FormItem>
                <Button
                  class="btn"
                  type="success"
                  size="large"
                  long
                  @click="handleSubmit('formInline')"
                >Published articles</Button>
              </FormItem>
            </Form>
          </div>
        </Card>
      </Content>
    </Layout>
    <Modal v-model="clickModal" title="Published articles" @on-ok="ok" @on-cancel="cancel">
      <Form :model="pubInline" :rules="pubRuleInline">
        <FormItem>
          <i-Input
            type="text"
            v-model="formInline.blogCategory"
            placeholder="enter blog category..."
            clearable
          ></i-Input>
        </FormItem>
        <FormItem>
          <i-Input
            type="text"
            v-model="formInline.blogTag"
            placeholder="enter blog tag..."
            clearable
          ></i-Input>
        </FormItem>
      </Form>
    </Modal>
  </div>
</template>

<script>
export default {
  data() {
    return {
      clickModal: false,
      blogInline: {
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
      },
      pubInline: {
        blogCategory: "",
        blogTag: ""
      },
      pubRuleInline: {
        blogCategory: [
          {
            required: true,
            message: "Please enter the blog categroy",
            trigger: "blur"
          }
        ],
        blogTag: [
          {
            required: true,
            message: "Please enter the blog tag",
            trigger: "blur"
          }
        ]
      }
    };
  },
  methods: {
    // 用户登录
    handleSubmit(name) {
      this.$refs[name].validate(valid => {
        if (valid) {
          this.clickModal = true;
        } else {
          this.$Message.error("Fail!");
        }
      });
    },
    ok(name) {
      this.$refs[name].validate(valid => {
        if (valid) {
          this.$Message.info("Clicked Ok");
        } else {
          this.$Message.error("Fail!");
        }
      });
    },
    cancel() {
      this.$Message.info("Clicked cancel");
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