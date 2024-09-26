import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LandingPageComponent } from './landing-page/landing-page.component';

const routeConfig: Routes = [
  {
    path: '',
    component: LandingPageComponent,
    title: 'YourFutureGuide',
  },
  {
    path: 'home',
    component: HomeComponent,
    title: 'YourFutureGuide',
  }
];

export default routeConfig;
