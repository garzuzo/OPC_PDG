import BuildPeaceComponent from '@/components/BuildPeaceComponent'

const routes = [
  { path: '/construirpaz', component: BuildPeaceComponent },
  { path: '*', redirect: '/' }   
];

export default routes;