// import '@babel/polyfill'
import Vue from 'vue'
import App from './App.vue'
import iView from 'iview';
import 'iview/dist/styles/iview.css';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import router from './router/index'
import './assets/bootstrap/css/bootstrap.min.css';

import * as $http from './requests/index';

Vue.use(ElementUI);
Vue.use(iView);

Vue.prototype.$http = $http
Vue.config.productionTip = false

// 全局导航守卫
router.beforeEach((to, from, next) => {
  document.title = to.name; // //让页面title显示路由对应的name值
  let user = JSON.parse(sessionStorage.getItem("user"));
  if (to.path === '/account/login') {
    sessionStorage.removeItem("user");
  }
  if (to.meta.requireAuth) { // 判断该路由是否需要登录权限
    if (user) { //判断本地是否存在access_token
      next();
    } else {
      if (to.path === '/account/register') {
        next();
      } else {
        next({
          path: '/account/login'
        })
      }
    }
  }
  else {
    next();
  }
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
