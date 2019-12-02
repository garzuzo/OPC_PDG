<template>
  <div style="height: 100%; width: 100%">
    <!--<div class="info" style="height: 15%">
      CAMPAIGN {{campaign.id}}
      <span>Center: {{ center }}</span>
      <span>Zoom: {{ zoom }}</span>
      <span>Bounds: {{ bounds }}</span>
    </div>-->
    <l-map
      style="height: 80%; width: 100%"
      :zoom="zoom"
      :center="center"
      @update:zoom="zoomUpdated"
      @update:center="centerUpdated"
      @update:bounds="boundsUpdated"
    >
      <l-tile-layer :url="url"></l-tile-layer>
      <l-geo-json :geojson="geojson.geojson" :options="geojson.options"></l-geo-json>
    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer, LGeoJson } from "vue2-leaflet";
import axios from "axios";
import comunas from "../../data/comunas.js";
import api from "../../axios.js";
import PopupContent from "./PopUpComponent.vue";
import Vue from "vue";

export default {
  components: {
    "l-map": LMap,
    "l-tile-layer": LTileLayer,
    "l-geo-json": LGeoJson
  },
  props: {
    campaign: Object
  },
  data() {
    var self = this;
    return {
      url: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",
      zoom: 10,
      center: [3.4256, -76.5231],
      bounds: null,
      geojson: {
        geojson: comunas,
        options: {
          style: function(feature) {
            var fillColor,
              comuna_corregimiento = feature.properties.comuna_corregimiento;
            if (comuna_corregimiento < 23) {
              fillColor = "#006837";
            } else {
              fillColor = "#31a354";
            } // no data
            return {
              color: "#999",
              weight: 2,
              fillColor: fillColor,
              fillOpacity: 0.6
            };
          },
          onEachFeature: function(feature, layer) {
          
            let PopupCont = Vue.extend(PopupContent);
            var campaignPopup = self.campaign;
            let popup = new PopupCont({
              propsData: {
                campaign: campaignPopup,
                name: feature.properties.nombre,
                id: feature.properties.comuna_corregimiento
              }
            });

            layer.bindPopup(popup.$mount().$el, {
                  minWidth: 300,
                  maxHeight: 350
                });
                
          }
        }
      }
    };
  },
  methods: {
    zoomUpdated(zoom) {
      this.zoom = zoom;
    },
    centerUpdated(center) {
      this.center = center;
    },
    boundsUpdated(bounds) {
      this.bounds = bounds;
    }
  }
};
</script>