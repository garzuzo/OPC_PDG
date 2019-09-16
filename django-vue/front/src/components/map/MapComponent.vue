<template>
    
    <div>

<v-row align="center" justify="center">

<v-col cols=8>
<div id="app" style="height: 100%">
  <v-map :zoom=13 :center="[3.359889, -76.638565]" style="height: 850px; width: 600px">
    <v-tilelayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"></v-tilelayer>
    <v-marker :lat-lng="[3.359889, -76.638565]"></v-marker>
  </v-map>
</div>
</v-col>

<v-col cols=4>


<v-chip>
    Ingresa la campaña
</v-chip>
<v-menu>
Campañas activas
</v-menu>

<v-button>
Filtrar
</v-button>
</v-col>

</v-row>


    </div>
</template>

<script>

import {LMap,LMarker,LTileLayer} from 'vue2-leaflet';


export default {

    components:{
        'v-map':LMap,
        'v-marker':LMarker,
        'v-tilelayer':LTileLayer
    }
};
</script>


<style scoped>


</style>