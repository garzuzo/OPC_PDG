import HelloWorld from '@/components/HelloWorld'

const routes = [
  { path: '/', name:'HelloWorld', component: HelloWorld },
  { path: '*', redirect: '/' }   
];

export default routes;