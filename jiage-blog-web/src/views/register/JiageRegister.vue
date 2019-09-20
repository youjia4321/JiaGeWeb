<template>
  <div class="main-body">
    <div class="form">
      <Icon type="logo-octocat" size="60" />
      <h1>Create your account</h1>
    </div>
    <div class="login">
      <Form ref="formInline" :model="formInline" :rules="ruleInline">
        <FormItem prop="user">
          <div class="prompt">Username</div>
          <i-Input type="text" v-model="formInline.user" placeholder="Username" clearable>
            <Icon type="ios-person" slot="prepend" size="16"></Icon>
          </i-Input>
        </FormItem>
        <FormItem prop="email">
          <div class="prompt">Email address</div>
          <i-Input type="text" v-model="formInline.email" placeholder="Email address" clearable>
            <Icon type="ios-mail" slot="prepend" size="16"></Icon>
          </i-Input>
        </FormItem>
        <FormItem prop="password">
          <div class="prompt">Password</div>
          <i-Input type="password" v-model="formInline.password" placeholder="Password" clearable>
            <Icon type="ios-lock" slot="prepend" size="16"></Icon>
          </i-Input>
        </FormItem>
        <FormItem>
          <Button
            class="btn"
            type="primary"
            size="large"
            long
            :loading="modal_loading"
            @click="handleSubmit('formInline')"
          >Create new</Button>
        </FormItem>
      </Form>
    </div>
    <p class="register-link">
      Have a JiaGE account?
      <router-link to="/account/login">Sign in.</router-link>
    </p>
  </div>
</template>
<script>
export default {
  data() {
    return {
      modal_loading: false,
      formInline: {
        user: "",
        email: "",
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
        email: [
          {
            required: true,
            message: "Please enter the email",
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
          var email = this.formInline.email;
          this.$http
            .userRegister(
              email,
              username,
              password,
              this.getCookie("csrftoken")
            )
            .then(resp => {
              if (resp.result.code === "200") {
                this.$router.push({
                  path: "/account/login"
                });
                this.$Message.success(resp.result.msg);
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
  height: 337px;
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