import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import HowItWorksComponent from '@/components/frontpage/HowItWorksComponent'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HowItWorksComponent',
      component: HowItWorksComponent
    }
  ]
})
