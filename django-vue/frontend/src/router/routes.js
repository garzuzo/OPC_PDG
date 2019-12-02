import BuildPeaceComponent from '@/components/buildpeace/BuildPeaceComponent'
import AboutUsComponent from '@/components/aboutus/AboutUsComponent'
import PieChartComponent from '@/components/chart/PieChartComponent'
import CampaignsComponent from '@/components/campaign/CampaignsComponent'
import ProfileComponent from '@/components/profile/ProfileComponent'
import FrontPageComponent from '@/components/frontpage/FrontPageComponent'
import VisualizationCampaignComponent from '@/components/visualization/VisualizationCampaignComponent'
import VisualizationGeneralComponent from '@/components/visualization/VisualizationGeneralComponent'
import LoginComponent from '@/components/auth/LoginComponent'
import OpenDataComponent from '@/components/opendata/OpenDataComponent'
const routes = [
  { path: '/datosabiertos', component: OpenDataComponent },
  { path: '/construirpaz', component: BuildPeaceComponent },
  { path: '/sobrenosotros', component: AboutUsComponent },
  {path: '/home', component: FrontPageComponent},
  {path: '/pie', component: PieChartComponent},
  {path: '/campanas', component: CampaignsComponent},
  {path: '/perfil', component: ProfileComponent, meta: { requiresAuth: true }},
  {path: '/visualizacampana', component: VisualizationCampaignComponent},
  {path: '/visualiza', component: VisualizationGeneralComponent},
  {path: '/login', component: LoginComponent},
  { path: '/', redirect: '/home' },
  { path: '*', redirect: '/' }   
];

export default routes;