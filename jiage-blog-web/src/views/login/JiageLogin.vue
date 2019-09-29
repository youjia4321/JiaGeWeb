<template>
  <div class="main-body">
    <div class="form">
      <Icon type="logo-octocat" size="60" />
      <h1>Sign in to JiaGE</h1>
    </div>
    <div class="login">
      <Form ref="formInline" :model="formInline" :rules="ruleInline">
        <FormItem prop="user">
          <div class="prompt">Username or email address</div>
          <i-Input type="text" v-model="formInline.user" placeholder="Username or Email" clearable>
            <Icon type="ios-person" slot="prepend" size="16"></Icon>
          </i-Input>
        </FormItem>
        <FormItem prop="password">
          <div class="prompt">Password</div>
          <i-Input
            type="password"
            v-model="formInline.password"
            placeholder="Password"
            clearable
            @keyup.enter.native="handleSubmit('formInline')"
          >
            <Icon type="ios-lock" slot="prepend" size="16"></Icon>
          </i-Input>
        </FormItem>
        <FormItem>
          <div class="prompt" style="float: left">
            <Checkbox v-model="checked">记住密码</Checkbox>
          </div>
          <div class="prompt" style="float: right">
            <a>Forgot password?</a>
          </div>
        </FormItem>
        <FormItem>
          <Button
            class="btn"
            type="success"
            size="large"
            long
            :loading="modal_loading"
            @click="handleSubmit('formInline')"
          >Sign in</Button>
        </FormItem>
      </Form>
    </div>
    <p class="register-link">
      New to JiaGE?
      <router-link to="/account/register">Create an account.</router-link>
    </p>
  </div>
</template>
<script>
export default {
  data() {
    return {
      checked: false,
      modal_loading: false,
      formInline: {
        user: "",
        password: ""
      },
      ruleInline: {
        user: [
          {
            required: true,
            message: "Please enter the user name",
            trigger: "blur"
          }
        ],
        password: [
          {
            required: true,
            message: "Please enter the password",
            trigger: "blur"
          }
        ]
      }
    };
  },
  mounted() {
    let userinfo = localStorage.getItem("jiageWebInfo");
    if (userinfo) {
      // 如果存在就自动填写用户信息
      userinfo = JSON.parse(localStorage.getItem("jiageWebInfo"));
      this.formInline.user = userinfo.username;
      this.formInline.password = userinfo.password;
      this.checked = userinfo.checked;
    }
  },
  methods: {
    // post请求需要获取csrftoken
    getCookie(name) {
      var value = "; " + document.cookie;
      var parts = value.split("; " + name + "=");
      if (parts.length === 2)
        return parts
          .pop()
          .split(";")
          .shift();
    },
    // 用户登录
    handleSubmit(name) {
      this.$refs[name].validate(valid => {
        if (valid) {
          this.modal_loading = true;
          var username = this.formInline.user;
          var password = this.formInline.password;
          this.$http
            .userLogin(username, password, this.getCookie("csrftoken"))
            .then(resp => {
              if (resp.result.code === "200") {
                if (this.checked == true) {
                  let userinfo = {
                    username: resp.result.username,
                    password: password,
                    checked: true
                  };
                  localStorage.setItem(
                    "jiageWebInfo",
                    JSON.stringify(userinfo)
                  );
                } else {
                  localStorage.removeItem("jiageWebInfo");
                }
                var obj = {
                  username: resp.result.username,
                  password: this.formInline.password,
                  avatar: resp.result.avatar
                };
                sessionStorage.setItem("user", JSON.stringify(obj));

                this.$router.push({
                  path: "/index"
                });
              } else {
                this.$Message.error(resp.result.msg);
              }
              this.modal_loading = false;
            });
        }
      });
    }
  }
};
</script>

<style scoped>
.form {
  text-align: center;
  width: 400px;
  margin: 0 auto;
  margin-top: 30px;
  margin-bottom: 25px;
}
.form h1 {
  font-size: 24px;
  font-weight: 100;
  letter-spacing: -0.5px;
}
.login {
  width: 308px;
  margin: 0 auto;
  border: 1px solid #d8dee2;
  height: 320px;
  border-radius: 5px;
  padding: 20px;
  font-size: 14px;
  margin-bottom: 15px;
}
.prompt {
  font-size: 13px;
  font-weight: 600;
}
.btn {
  font-weight: 600;
}
.register-link {
  margin: 0 auto;
  width: 308px;
  padding: 15px 20px;
  text-align: center;
  border: 1px solid #d8dee2;
  border-radius: 5px;
}
</style>