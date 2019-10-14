import BuildPeaceComponent from '@/components/buildpeace/BuildPeaceComponent'
import AboutUsComponent from '@/components/aboutus/AboutUsComponent'
import MapComponent from '@/components/map/MapComponent'
import ChoroplethMapComponent from '@/components/map/ChoroplethMapComponent'
import AuthComponent from '@/auth/Auth'
import PieChartComponent from '@/components/chart/PieChartComponent'
import CampaignsComponent from '@/components/campaign/CampaignsComponent'
import ProfileComponent from '@/components/profile/ProfileComponent'
import FrontPageComponent from '@/components/frontpage/FrontPageComponent'
const routes = [
  { path: '/construirpaz', component: BuildPeaceComponent },
  { path: '/sobrenosotros', component: AboutUsComponent },
  {path: '/home', component: FrontPageComponent},
  {path: '/choropleth', component: ChoroplethMapComponent},
  {path: '/map', component: MapComponent},
  {path: '/pie', component: PieChartComponent},
  {path: '/campañas', component: CampaignsComponent},
  {path: '/perfil', component: ProfileComponent},
  { path: '*', redirect: '/' }   
];

export default routes;