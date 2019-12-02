<template>
  <div>
    <navbar-component></navbar-component>

    <div class="init">
      <v-container class="fill-height" style="min-height: 100%">
        <!--INITIAL IMAGE -->
        <v-row style="padding-top: 20vh; padding-bottom:20vh;">
          <v-col sm="12" md="7">
            <h1 style="padding-bottom:10vh;">Datos Abiertos</h1>
            <p>Estamos comprometidos con los datos abiertos</p>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <div>
      <v-container style="padding-top:20vh;">
        <v-row justify="center">
          <v-col>
            <v-data-table
              dense
              height="600"
              :headers="headers"
              :items="json_data"
              :items-per-page="5"
              v-bind:loading="loading"
              loading-text="Cargando... por favor espere."
              v-bind:calculate-widths="width"
              class="elevation-1"
            ></v-data-table>

            <download-excel
              class="btn btn-default"
              :data="json_data"
              :fields="json_fields"
              type="csv"
              name="datos_narrativas_de_paz.xls"
            >
              <p>
                {{text_download}}
                <img :src="require(`@/assets/download_opendata.png`)" class="img" />
              </p>
            </download-excel>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>
 <!--loading loading-text="Cargando... por favor espere."-->
<script>
import Vue from "vue";
import api from "../../axios.js";
import JsonExcel from "vue-json-excel";
Vue.component("downloadExcel", JsonExcel);
export default {
  mounted() {
    api
      .getOpenData()
      .then(response => {
        this.json_data = response;
        this.loading = false;
      })
      .catch(err => console.log(err));
  },
  data() {
    return {
      text_download: "Descargar datos abiertos",
      json_data: [],
      loading: true,
      width: true,
      headers: [
        { text: "Genero", value: "Genero" },
        { text: "Nivel_educativo", value: "Nivel_educativo" },
        { text: "Nivel_alcanzado", value: "Nivel_alcanzado" },
        { text: "Narrativa", value: "Narrativa" },
        { text: "Palabras_clave_1", value: "Palabras_clave_1" },
        { text: "Palabras_clave_2", value: "Palabras_clave_2" },
        { text: "Palabras_clave_3", value: "Palabras_clave_3" },
        { text: "Palabras_clave_4", value: "Palabras_clave_4" },
        { text: "Palabras_clave_5", value: "Palabras_clave_5" },
        { text: "Barrio_vereda_actual", value: "Barrio_vereda_actual" },
        {
          text: "Comuna_corregimiento_actual",
          value: "Comuna_corregimiento_actual"
        },
        { text: "Ciudad_actual", value: "Ciudad_actual" },
        { text: "Departamento_actual", value: "Departamento_actual" },
        { text: "Pais_actual", value: "Pais_actual" },
        { text: "Barrio_vereda_origen", value: "Barrio_vereda_origen" },
        {
          text: "Comuna_corregimiento_origen",
          value: "Comuna_corregimiento_origen"
        },
        { text: "Ciudad_origen", value: "Ciudad_origen" },
        { text: "Departamento_origen", value: "Departamento_origen" },
        { text: "Pais_origen", value: "Pais_origen" }
      ],

      json_fields: {
        Nivel_educativo: "Nivel_educativo",
        Nivel_alcanzado: "Nivel_alcanzado",
        Narrativa: "Narrativa",
        Palabras_clave_1: "Palabras_clave_1",
        Palabras_clave_2: "Palabras_clave_2",
        Palabras_clave_3: "Palabras_clave_3",
        Palabras_clave_4: "Palabras_clave_4",
        Palabras_clave_5: "Palabras_clave_5",
        Barrio_vereda_actual: "Barrio_vereda_actual",
        Comuna_corregimiento_actual: "Comuna_corregimiento_actual",
        Ciudad_actual: "Ciudad_actual",
        Departamento_actual: "Departamento_actual",
        Pais_actual: "Pais_actual",
        Barrio_vereda_origen: "Barrio_vereda_origen",
        Comuna_corregimiento_origen: "Comuna_corregimiento_origen",
        Ciudad_origen: "Ciudad_origen",
        Departamento_origen: "Departamento_origen",
        Pais_origen: "Pais_origen"
      },
      json_meta: [
        [
          {
            key: "charset",
            value: "utf-8"
          }
        ]
      ]
    };
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");

.init {
  /*margin: 0 auto;
  width: 30%;*/
  background-image: url("../../assets/data.jpg");
  background-size: cover;
  height: 100vh;
}
h1 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: calc(32px + (64 - 32) * ((100vw - 300px) / (1600 - 300)));
  color: #0c186d;
}

p {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: calc(18px + (24 - 18) * ((100vw - 300px) / (1600 - 300)));
}
</style>