<template>
 <div id="app">
    <l-map :center="[-23.752961, -57.854357]" :zoom="6" style="height: 500px;" :options="mapOptions">
      <l-choropleth-layer :data="pyDepartmentsData" titleKey="department_name" idKey="department_id" :value="value" :extraValues="extraValues" geojsonIdKey="dpto" :geojson="paraguayGeojson" :colorScale="colorScale">
        <template slot-scope="props">
          <l-info-control :item="props.currentItem" :unit="props.unit" title="Department" placeholder="Hover over a department"/>
          <l-reference-chart title="Girls school enrolment" :colorScale="colorScale" :min="props.min" :max="props.max" position="topright"/>
        </template>
      </l-choropleth-layer>
    </l-map>
  </div>
</template>

<script>
//lat-lng="[3.359889, -76.638565]
import { InfoControl, ReferenceChart, ChoroplethLayer } from 'vue-choropleth'

import {LMap} from 'vue2-leaflet';

import { geojson } from '../../data/py-departments-geojson'
import paraguayGeojson from '../../data/paraguay.json'
import { pyDepartmentsData } from '../../data/py-departments-data'
export default {
name: 'ChoroplethMap',
 components:{
'l-map':LMap,
  'l-info-control': InfoControl, 
    'l-reference-chart': ReferenceChart, 
    'l-choropleth-layer': ChoroplethLayer 
 },
 data(){
   return {
       pyDepartmentsData,
      paraguayGeojson,
      colorScale: ["e7d090", "e9ae7b", "de7062"],
      value: {
        key: "amount_w",
        metric: "% girls"
      },
      extraValues: [{
        key: "amount_m",
        metric: "% boys"
      }],
      mapOptions: {
        attributionControl: true
      },
      currentStrokeColor: '3d3213'
    }
   
 },
  methods: {
    zoomUpdated (zoom) {
      this.zoom = zoom;
    },
    centerUpdated (center) {
      this.center = center;
    },
    boundsUpdated (bounds) {
      this.bounds = bounds;
    }

}
}
</script>

<style scoped>

body {
  background-color: #e7d090;
  margin-left: 100px;
  margin-right: 100px;
}
#map {
  background-color: #eee;
}
</style>