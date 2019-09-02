import BuildPeaceComponent from '@/components/buildpeace/BuildPeaceComponent'

const routes = [
  { path: '/construirpaz', component: BuildPeaceComponent },
  { path: '*', redirect: '/' }   
];

export default routes;