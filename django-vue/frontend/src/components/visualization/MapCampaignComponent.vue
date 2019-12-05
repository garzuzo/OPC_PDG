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
      }
    };
  },
  created(){
    for (var i = 0; i < 2; i++) {
        var msg=""
        if(this.filter.topicOne!=0){
            msg+= `topic_primary=${this.filter.topicOne}&`
        }
        if(this.filter.topicTwo !=0){
            msg+= `topic_secondary=${this.filter.topicTwo}&` 
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
        if(this.filter.idCampaign!=0){
            msg+= `id_campaign=${this.filter.idCampaign}&` 
        }
        //comuna
        if (i == 0) {
          msg += `type_filter=comuna`;
          api
            .getPercentage(msg)
            .then(response => {
              this.responseComuna = response;
            })
            .catch(err => console.log(err));
        } else {
          //corregimiento
          msg += `type_filter=corregimiento`;
          api
            .getPercentage(msg)
            .then(response => {
              this.responseCorregimiento = response;
            })
            .catch(err => console.log(err));
        }
      }
  },
  watch: {
    filter: {
      deep: true,
      // We have to move our method to a handler field
      handler(filter){
        for (var i = 0; i < 2; i++) {
        var msg=""
        if(filter.topicOne!=0){
            msg+= `topic_primary=${filter.topicOne}&`
        }
        if(filter.topicTwo !=0){
            msg+= `topic_secondary=${filter.topicTwo}&` 
        }
        if(filter.sex!=''){
            msg+= `gender=${filter.sex}&` 
        }
        if(filter.age!=''){
            msg+= `age=${filter.age}&` 
        }
        if(filter.education!=''){
            msg+= `education=${filter.education}&` 
        }
        if(filter.idCampaign!=0){
            msg+= `id_campaign=${filter.idCampaign}&` 
        }
        //comuna
        if (i == 0) {
          msg += `type_filter=comuna`;
          api
            .getPercentage(msg)
            .then(response => {
              this.responseComuna = response;
            })
            .catch(err => console.log(err));
        } else {
          //corregimiento
          msg += `type_filter=corregimiento`;
          api
            .getPercentage(msg)
            .then(response => {
              this.responseCorregimiento = response;
            })
            .catch(err => console.log(err));
        }
      }
      }
      
    }
  },
  computed:{
    options() {
      return {
        onEachFeature: this.onEachFeature(),
        style: this.styleFilterFunction
      };
    },
    styleFilterFunction() {
      const sex = this.filter.sex; // important! need touch fillColor in computed for re-calculate when change fillColor
      /*const respComuna = this.filterComuna
      const respCorregimiento = this.filterCorregimiento*/
      const respComuna = this.responseComuna;
      const respCorregimiento = this.responseCorregimiento;
      return (feature) => {

        var fillColor, 
        comuna_corregimiento = feature.properties.comuna_corregimiento;

        if(comuna_corregimiento < 23){
            if(respComuna[comuna_corregimiento] <= 0.10){ fillColor = "#cafff7";}
            else if(respComuna[comuna_corregimiento] > 0.10 && respComuna[comuna_corregimiento] <= 0.25){ fillColor = "#9bd7d5"}
            else if(respComuna[comuna_corregimiento] > 0.25 && respComuna[comuna_corregimiento] <= 0.5){ fillColor = "#129793"}
            else if(respComuna[comuna_corregimiento] > 0.5 && respComuna[comuna_corregimiento] <= 0.75){ fillColor = "#2f5887"}
            else if(respComuna[comuna_corregimiento] > 0.75 && respComuna[comuna_corregimiento] <= 1.0){ fillColor = "#2b374b"}

        }else{
            if(respCorregimiento[comuna_corregimiento] <= 0.10){ fillColor = "#cafff7";}
            if(respCorregimiento[comuna_corregimiento] > 0.10 && respCorregimiento[comuna_corregimiento] <= 0.25){ fillColor = "#9bd7d5"}
            else if(respCorregimiento[comuna_corregimiento] > 0.25 && respCorregimiento[comuna_corregimiento] <= 0.5){ fillColor = "#129793"}
            else if(respCorregimiento[comuna_corregimiento] > 0.5 && respCorregimiento[comuna_corregimiento] <= 0.75){ fillColor = "#2f5887"}
            else if(respCorregimiento[comuna_corregimiento] > 0.75 && respCorregimiento[comuna_corregimiento] <= 1.0){ fillColor = "#2b374b"}
        }
      
        return { color: "#999", weight: 2, fillColor: fillColor, fillOpacity: .8 };

      };
    }
  },
  methods: {    
    onEachFeature(){
        return (feature,layer) => {
            layer.bindTooltip(feature.properties.nombre);
        };
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