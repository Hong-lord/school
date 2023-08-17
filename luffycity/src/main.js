import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from "axios";
import '@/assets/css/global.css';

import cookies from 'vue-cookies';


import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// import '@/assets/element-variables.scss'
Vue.use(ElementUI);

// import 'bootstrap'

// 配置全局自定义设置
import settings from '@/assets/js/settings';
Vue.prototype.$settings = settings;
// 在所有需要与后台交互的组件中：this.$settings.base_url + '再拼接具体后台路由'


Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');


// 配置
Vue.prototype.$axios = axios;
Vue.prototype.$cookies = cookies;
