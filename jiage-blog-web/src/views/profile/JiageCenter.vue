<template>
  <JiageContent :title="title">
    <Card slot="main-content">
      <div class="infinite-list-wrapper" style="min-height: 450px;">
        <Layout>
          <Sider hide-trigger class="sider">
            <div class="avatar-box">
              <img
                class="avatar"
                :src="'http://192.168.1.65:8000/media/'+perosnInfo.portrait"
                width="150"
              />
            </div>
            <div class="click-avatar">
              <span @click="upload = true">修改头像</span>
            </div>
          </Sider>
          <Content class="i-content">
            <div class="profile">
              <p>
                ID：{{ perosnInfo.username }}&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp; &nbsp;
                <span
                  class="vip"
                >开通会员</span>
              </p>
              <p>Email：{{ perosnInfo.email }}</p>
              <p>Gender：{{ perosnInfo.gender }}</p>
              <p>Mobile：{{ perosnInfo.mobile }}</p>
            </div>
          </Content>
        </Layout>
      </div>
      <Modal v-model="upload" title="上传头像">
        <Upload
          ref="upload"
          type="drag"
          :before-upload="handleUpload"
          :on-success="uploadSuccess"
          :on-error="uploadError"
          :on-exceeded-size="handleMaxSize"
          :max-size="2048"
          :data="data"
          :format="['jpg', 'png', 'jpeg']"
          :on-format-error="handleFormatError2"
          action="http://192.168.1.65:8000/api/uploadAvatar"
        >
          <div style="padding: 20px 0">
            <Icon type="ios-cloud-upload" size="52" style="color: #3399ff"></Icon>
            <p>Click or drag picture here to upload</p>
          </div>
        </Upload>
        <div slot="footer">
          <Button type="primary" @click="cancelBtn">取消</Button>
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
      title: "个人中心",
      upload: false,
      author: "",
      pwd: "",
      perosnInfo: [],
      file: "",
      data: ""
    };
  },
  components: {
    JiageContent
  },
  inject: ["reload"],
  created() {
    let user = JSON.parse(sessionStorage.getItem("user"));
    this.author = user["username"];
    this.pwd = user["password"];
    this.getSelfInfo();
    this.data = { author: this.author };
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
    getSelfInfo() {
      this.$http
        .centerManage(this.author, this.getCookie("csrftoken"))
        .then(resp => {
          if (resp.result.code === "200") {
            this.perosnInfo = resp.result.data;
          }
        });
    },
    handleUpload(file) {
      this.file = file;
      return true;
    },
    uploadSuccess(res) {
      //上传成功
      this.$Message.info(res.result.msg);
      if (res.result.code == 200) {
        this.$http
          .userLogin(this.author, this.pwd, this.getCookie("csrftoken"))
          .then(resp => {
            if (resp.result.code === "200") {
              var obj = {
                username: this.author,
                password: this.pwd,
                avatar: resp.result.avatar
              };
              sessionStorage.setItem("user", JSON.stringify(obj));
            }
          });
      }
      this.reload();
    },
    handleFormatError2() {
      this.$Message.error("文件格式不正确,请上传jpg、jpeg、png格式文件");
    },
    uploadError(error) {
      this.$Message.info(error);
    },
    handleMaxSize(file) {
      this.$Notice.warning({
        title: "超出文件大小限制",
        desc: "文件 " + file.name + " 太大，不能超过 2M。"
      });
    },
    cancelBtn() {
      this.upload = false;
    }
  }
};
</script>

<style scoped lang="scss">
.avatar-box {
  text-align: center;
}
.avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  margin: 16px auto 0;
}
.sider {
  min-height: 450px;
  background: #fff;
}
.i-content {
  background: #fff;
}
.click-avatar {
  padding-top: 20px;
  cursor: pointer;
  font-size: 15px;
  text-align: center;
  color: #3399ea;
}
.profile {
  border: solid 1px #ded4d4;
  border-radius: 5px;
  padding: 20px;
  min-height: 450px;
}
.profile p {
  padding-bottom: 15px;
}
.vip {
  font-size: 12px;
  color: #3399ea;
  cursor: pointer;
}
</style>