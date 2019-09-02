<template>
  <div>
    
     <v-col cols="4">
     <h3>Territorio donde vives </h3>
     <div class="form-group">
          <label for="currentZone">Zona*</label>
          <v-select
            :items="zones"
            outlined
            v-model="currentZone"
            required
            class="input"
            color="#0C186D"
            name="currentZone"
          ></v-select>
        </div>
     </v-col>

    <v-row align="center" justify="space-around">
      <!--FIRST COLUMN-->
      <v-col cols="4">
        <div class="form-group">
          <label for="currentState">Departamento*</label>
          <v-select
            :items="zones"
            outlined
            v-model="currentState"
            required
            class="input"
            color="#0C186D"
            name="currentState"
          ></v-select>

          <div class="form-group" v-if="currentZone == zones[1]">
            <label for="currentComuna">Comuna*</label>
            <v-text-field
              v-model="currentComuna"
              outlined
              color="#0C186D"
              height="16"
              required
              name="currentComuna"
              class="input"
            ></v-text-field>
          </div>

          <div class="form-group" v-if="currentZone == zones[0]">
            <label for="currentCorregimiento">Corregimiento*</label>
            <v-text-field
              v-model="currentCorregimiento"
              outlined
              color="#0C186D"
              height="16"
              required
              name="currentCorregimiento"
              class="input"
            ></v-text-field>
          </div>
        </div>
      </v-col>

      <!--SECOND COLUMN -->
      <v-col cols="4">
        <div class="form-group">
          <label for="currentCity">Ciudad*</label>
          <v-select
            :items="zones"
            outlined
            v-model="currentCity"
            required
            class="input"
            color="#0C186D"
            name="currentState"
          ></v-select>
        </div>

        <div class="form-group" v-if="currentZone == zones[1]">
          <label for="currentNeighborhood">Barrio*</label>
           <v-text-field
              v-model="currentNeighborhood"
              outlined
              color="#0C186D"
              height="16"
              required
              name="currentNeighborhood"
              class="input"
            ></v-text-field>
        </div>

        <div class="form-group" v-if="currentZone == zones[0]">
          <label for="currentVereda">Vereda*</label>
           <v-text-field
              v-model="currentVereda"
              outlined
              color="#0C186D"
              height="16"
              required
              name="currentVereda"
              class="input"
            ></v-text-field>
        </div>
      </v-col>
    </v-row>

    <!--ORIGIN TERRITORY -->
    <v-col cols="4">
     <h3>Territorio de origen</h3>
     <div class="form-group">
          <label for="originZone">Zona*</label>
          <v-select
            :items="zones"
            outlined
            v-model="originZone"
            required
            class="input"
            color="#0C186D"
            name="originZone"
          ></v-select>
        </div>
     </v-col>

    <v-row align="center" justify="space-around">
      <!--FIRST COLUMN-->
      <v-col cols="4">
        <div class="form-group">
          <label for="originState">Departamento*</label>
          <v-select
            :items="zones"
            outlined
            v-model="originState"
            required
            class="input"
            color="#0C186D"
            name="originState"
          ></v-select>

          <div class="form-group" v-if="originZone == zones[1]">
            <label for="originComuna">Comuna*</label>
            <v-text-field
              v-model="originComuna"
              outlined
              color="#0C186D"
              height="16"
              required
              name="originComuna"
              class="input"
            ></v-text-field>
          </div>

          <div class="form-group" v-if="originZone == zones[0]">
            <label for="originCorregimiento">Corregimiento*</label>
            <v-text-field
              v-model="originCorregimiento"
              outlined
              color="#0C186D"
              height="16"
              required
              name="originCorregimiento"
              class="input"
            ></v-text-field>
          </div>
        </div>
      </v-col>

      <!--SECOND COLUMN -->
      <v-col cols="4">
        <div class="form-group">
          <label for="originCity">Ciudad*</label>
          <v-select
            :items="zones"
            outlined
            v-model="originCity"
            required
            class="input"
            color="#0C186D"
            name="originState"
          ></v-select>
        </div>

        <div class="form-group" v-if="originZone == zones[1]">
          <label for="originNeighborhood">Barrio*</label>
           <v-text-field
              v-model="originNeighborhood"
              outlined
              color="#0C186D"
              height="16"
              required
              name="originNeighborhood"
              class="input"
            ></v-text-field>
        </div>

        <div class="form-group" v-if="originZone == zones[0]">
          <label for="originVereda">Vereda*</label>
           <v-text-field
              v-model="originVereda"
              outlined
              color="#0C186D"
              height="16"
              required
              name="originVereda"
              class="input"
            ></v-text-field>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "PersonalForm",
  //inject: ["$validator"],
  data() {
    return {
      currentZone: "",
      currentState:"",
      currentCity:"",
      currentComuna:"",
      currentNeighborhood:"",
      currentCorregimiento:"",
      currentVereda:"",
      originZone: "",
      originState:"",
      originCity:"",
      originComuna:"",
      originNeighborhood:"",
      originCorregimiento:"",
      originVereda:"",
      zones: ["Zona rural", "Zona urbana"]
    };
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");

.input {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
  line-height: 36px;
}

label {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
}

h3{
    font-family: "Roboto";
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
  text-align: center;
}
</style>
