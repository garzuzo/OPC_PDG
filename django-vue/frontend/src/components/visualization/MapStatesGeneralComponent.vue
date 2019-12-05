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
      <l-geo-json :geojson="geojson.geojson" :options="options"></l-geo-json>
    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer, LGeoJson } from "vue2-leaflet";
import axios from "axios";
import states from "../../data/states.js";
import api from "../../axios.js";
import Vue from "vue";

export default {
  components: {
    "l-map": LMap,
    "l-tile-layer": LTileLayer,
    "l-geo-json": LGeoJson
  },
  props: {
    campaign: Object,
    filter: Object
  },
  data() {
    //var self= this
    return {
      url: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",
      zoom: 6,
      center: [3.5573, -73.0811],
      bounds: null,
      responseState: {},
      geojson: {
        geojson: states
      }
    };
  },
  created(){
      var msg = "";
        if (this.filter.topicGeneral != 0) {
          msg += `topic_general=${this.filter.topicGeneral}&`;
        }
        if (this.filter.sex != "") {
          msg += `gender=${this.filter.sex}&`;
        }
        if (this.filter.age != "") {
          msg += `age=${this.filter.age}&`;
        }
        if (this.filter.education != "") {
          msg += `education=${this.filter.education}&`;
        }
        //comuna
        
          msg += `type_filter=state`;
          api
            .getPercentage(msg)
            .then(response => {
              this.responseState = response;
            })
            .catch(err => console.log(err));
  },
  watch: {
    filter: {
      deep: true,
      // We have to move our method to a handler field
      handler(filter){
        var msg = "";
        if (this.filter.topicGeneral != 0) {
          msg += `topic_general=${this.filter.topicGeneral}&`;
        }
        if (this.filter.sex != "") {
          msg += `gender=${this.filter.sex}&`;
        }
        if (this.filter.age != "") {
          msg += `age=${this.filter.age}&`;
        }
        if (this.filter.education != "") {
          msg += `education=${this.filter.education}&`;
        }
        //comuna
        
          msg += `type_filter=state`;
          api
            .getPercentage(msg)
            .then(response => {
              this.responseState = response;
            })
            .catch(err => console.log(err));
      }
      
    }
  },
  computed: {
    options() {
      return {
        onEachFeature: this.onEachFeature(),
        style: this.styleFilterFunction
      };
    },
    styleFilterFunction() {
      const respState= this.responseState;
      return feature => {
        var fillColor,
          state = feature.properties.DPTO;
        
        if (respState[state] <= 0.10) {
            fillColor = "#cafff7";
        }
        else if (respState[state] > 0.10 &&
            respState[state] <= 0.25) {
            fillColor = "#9bd7d5";
          } else if (
            respState[state] > 0.25 &&
            respState[state] <= 0.5
          ) {
            fillColor = "#129793";
          } else if (
            respState[state] > 0.5 &&
            respState[state] <= 0.75
          ) {
            fillColor = "#2f5887";
          } else if (
            respState[state] > 0.75 &&
            respState[state] <= 1.0
          ) {
            fillColor = "#2b374b";
          }

        return {
          color: "#999",
          weight: 2,
          fillColor: fillColor,
          fillOpacity: 0.8
        };
      };
    }
  },
  methods: {
    onEachFeature() {
      return (feature, layer) => {
        layer.bindTooltip(feature.properties.NOMBRE_DPT);
      };
    },
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