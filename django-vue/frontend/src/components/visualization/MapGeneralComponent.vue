<template>
  <div style="height: 100%; width: 100%">
        
    <l-map
      style="height: 80%; width: 100%"
      :zoom="zoom"
      :center="center"
      @update:zoom="zoomUpdated"
      @update:center="centerUpdated"
      @update:bounds="boundsUpdated"
    >
      <l-tile-layer :url="url"></l-tile-layer>
      <l-geo-json
        :geojson="geojson.geojson"
        :options="options"
      >
      </l-geo-json>
    </l-map>
  </div>
</template>

<script>
import {LMap, LTileLayer, LGeoJson} from 'vue2-leaflet';
import axios from 'axios'
import comunas from '../../data/comunas.js';
import api from "../../axios.js";
import Vue from 'vue'

export default {
  components:{
'l-map':LMap,
  'l-tile-layer': LTileLayer,
  'l-geo-json': LGeoJson
 },
 props: {
    campaign: Object,
    filter: Object
  },
  data () {
    //var self= this
    return {
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      zoom: 10,
      center: [3.4256,-76.5231],
      bounds: null,
      responseComuna:{},
      responseCorregimiento:{},
      geojson: {
        geojson: comunas,
        /*options: {
        style: this.style,
        onEachFeature: function(feature, layer) {
        var comuna_corregimiento = feature.properties.comuna_corregimiento;
          if(comuna_corregimiento <23 && self.filter.sex=="mujeres"){
              layer.setStyle({
                  fillColor : "#006887"
              });
            }
          else if(comuna_corregimiento <23 && self.filter.sex=="hombres"){
              layer.setStyle({
                  fillColor : "#006787"
              });             
              
            }
          
        }
      }*/
      }
    };
  },
  computed:{
    options() {
      return {
        onEachFeature: this.onEachFeature(),
        style: this.styleFilterFunction
      };
    },
    styleFunction() {
      const sex = this.filter.sex; // important! need touch fillColor in computed for re-calculate when change fillColor
      return (feature) => {
        
        var fillColor,
          comuna_corregimiento = feature.properties.comuna_corregimiento;
      if(comuna_corregimiento <23 && sex=="Femenino"){fillColor = "#006887"}
      else if(comuna_corregimiento <23 && sex=="Masculino"){fillColor = "#ffa500"}      
      else if ( comuna_corregimiento < 23 && sex=="") {fillColor = "#006837"}
      else {fillColor = "#31a354"}  // no data
      return { color: "#999", weight: 2, fillColor: fillColor, fillOpacity: .6 };

      };
    },
    styleFilterFunction() {
      const sex = this.filter.sex; // important! need touch fillColor in computed for re-calculate when change fillColor
      const respComuna = this.filterComuna
      const respCorregimiento = this.filterCorregimiento
      return (feature) => {

        var fillColor, 
        comuna_corregimiento = feature.properties.comuna_corregimiento;

        if(comuna_corregimiento < 23){
            if(respComuna[comuna_corregimiento] <= 0.25){ fillColor = "#9bd7d5"}
            else if(respComuna[comuna_corregimiento] > 0.25 && respComuna[comuna_corregimiento] <= 0.5){ fillColor = "#129793"}
            else if(respComuna[comuna_corregimiento] > 0.5 && respComuna[comuna_corregimiento] <= 0.75){ fillColor = "#2f5887"}
            else if(respComuna[comuna_corregimiento] > 0.75 && respComuna[comuna_corregimiento] <= 1.0){ fillColor = "#2b374b"}

        }else{
            if(respCorregimiento[comuna_corregimiento] <= 0.25){ fillColor = "#9bd7d5"}
            else if(respCorregimiento[comuna_corregimiento] > 0.25 && respCorregimiento[comuna_corregimiento] <= 0.5){ fillColor = "#129793"}
            else if(respCorregimiento[comuna_corregimiento] > 0.5 && respCorregimiento[comuna_corregimiento] <= 0.75){ fillColor = "#2f5887"}
            else if(respCorregimiento[comuna_corregimiento] > 0.75 && respCorregimiento[comuna_corregimiento] <= 1.0){ fillColor = "#2b374b"}
        }
      
        return { color: "#999", weight: 2, fillColor: fillColor, fillOpacity: .8 };

      };
    },
    onEachFeatureFunction() {
        const sex= this.filter.sex
        return (feature, layer) => {
        var comuna_corregimiento = feature.properties.comuna_corregimiento;
          if(comuna_corregimiento <23 && sex=="Femenino"){
              layer.setStyle({
                  fillColor : "#006887"
              });
            }
          else if(comuna_corregimiento <23 && sex=="Masculino"){
              layer.setStyle({
                  fillColor : "#006787"
              });             
              
          }
          else if ( comuna_corregimiento < 23 && sex=="") {
              layer.setStyle({
                  fillColor : "#006837"
              });              
              }
        else {
            layer.setStyle({
                  fillColor : "#31a354"
              });    }
      };
        // no data
    },
    filterComuna(){     
        var msg=""
        if(this.filter.topicGeneral!=0){
            msg+= `topic_general=${this.filter.topicGeneral}&`
        }
        if(this.filter.sex!=''){
            msg+= `gender=${this.filter.sex}&` 
        }
        if(this.filter.age!=''){
            msg+= `age=${this.filter.age}&` 
        }
        if(this.filter.education!=''){
            msg+= `education=${this.filter.education}&` 
        }
        msg+= `type_filter=comuna`
        /*if(territory=="comuna"){
            
        }
        if(territory=="corregimiento"){
            msg+= `type_filter=${territory}`
        }*/
        api.getPercentage(msg).then(response =>{
            this.responseComuna = response
            /*if(territory=="comuna"){
                this.responseComuna = response
            }else{
                self.responseCorregimiento = response
            }*/
        }).catch(err=>console.log(err))
        return this.responseComuna
    },
    filterCorregimiento(){       
        var msg=""
        if(this.filter.topicGeneral!=0){
            msg+= `topic_primary=${this.filter.topicGeneral}&`
        }
        if(this.filter.sex!=''){
            msg+= `gender=${this.filter.sex}&` 
        }
        if(this.filter.age!=''){
            msg+= `age=${this.filter.age}&` 
        }
        if(this.filter.education!=''){
            msg+= `education=${this.filter.education}&` 
        }
        msg+= `type_filter=corregimiento`
        /*if(territory=="comuna"){
            
        }
        if(territory=="corregimiento"){
            msg+= `type_filter=${territory}`
        }*/
        api.getPercentage(msg).then(response =>{
            this.responseCorregimiento = response
            /*if(territory=="comuna"){
                this.responseComuna = response
            }else{
                self.responseCorregimiento = response
            }*/
        }).catch(err=>console.log(err))
        return this.responseCorregimiento
    }  
  },
  methods: {    
    onEachFeature(){
        return (feature,layer) => {
            layer.bindTooltip(feature.properties.nombre);
        };
    },
    style(feature){
          var fillColor,
          comuna_corregimiento = feature.properties.comuna_corregimiento;
      if(comuna_corregimiento <23 && this.filter.sex=="mujeres"){fillColor = "#006887"}
      else if(comuna_corregimiento <23 && this.filter.sex=="hombres"){fillColor = "#006787"}      
      else if ( comuna_corregimiento < 23 && this.filter.sex=="") {fillColor = "#006837"}
      else {fillColor = "#31a354"}  // no data
      return { color: "#999", weight: 2, fillColor: fillColor, fillOpacity: .6 };

          /*if (feature.properties.comuna_corregimiento > 11) {
            return {
              weight: 4,
              color: '#00FF00'
            }
          } else {
            return {
              weight: 4,
              color: '#FF0000'
            }
          }*/
    },  
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