import BuildPeaceComponent from '@/components/buildpeace/BuildPeaceComponent'
import AboutUsComponent from '@/components/aboutus/AboutUsComponent'
import MapComponent from '@/components/map/MapComponent'
import ChoroplethMapComponent from '@/components/map/ChoroplethMapComponent'
import AuthComponent from '@/auth/Auth'
import PieChartComponent from '@/components/chart/PieChartComponent'
const routes = [
  { path: '/construirpaz', component: BuildPeaceComponent },
  { path: '/sobrenosotros', component: AboutUsComponent },
  {path: '/', component: ChoroplethMapComponent},
  {path: '/map', component: MapComponent},
  {path: '/pie', component: PieChartComponent},
  { path: '*', redirect: '/' }   
];

export default routes;