// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuetify from 'vuetify'
import "vuetify/dist/vuetify.min.css";
//import VeeValidate from 'vee-validate'
import routes from './router/routes'
import App from './App.vue'


//Vue.config.productionTip = false
window.Vue = require('vue');
Vue.use(VueRouter);
Vue.use(Vuetify)
//Vue.use(VeeValidate);

/**
 * The following block of code may be used to automatically register your
 * Vue components. It will recursively scan this directory for the Vue
 * components and automatically register them with their "basename".
 *
 * Eg. ./components/ExampleComponent.vue -> <example-component></example-component>
 */

const files = require.context('./', true, /\.vue$/i);
files.keys().map(key => Vue.component(key.split('/').pop().split('.')[0], files(key).default));


const router = new VueRouter({
  mode: 'history',
  routes 
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
