<template>
  <div>
    <navbar-component></navbar-component>

    <div class="init">
      <v-container>
        <!--INITIAL IMAGE -->
        <v-row>
          <v-col cols="7">
            <br />
            <h1>Campañas</h1>
            <br />
            <br />
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam egestas, metus ac dignissim mattis, metus risus pretium ligula, ut mattis purus eros at nisl.</p>
            <br />
          </v-col>
        </v-row>
      </v-container>
    </div>

    <v-container>
      <h3>Campañas Activas</h3>
      <v-row justify="center">
        <v-col v-for="n in 9" :key="n" cols="5">
          <campaign-item-component></campaign-item-component>
        </v-col>
      </v-row>

      <h3>Campañas Pasadas</h3>
      <v-col cols="5">
        <form class="form-inline">
        <div class="form-group div-filter">
          <label for="filter" class="filter mr-2 mb-5">Filtrar Campañas:</label>
          <v-select
            :items="years"
            outlined
            v-model="year"
            required
            class="input"
            color="#0C186D"
            name="filter"
          ></v-select>
        </div>
        </form>
      </v-col>

      <v-row justify="center">
        <v-col v-for="n in 9" :key="n" class="d-flex child-flex" cols="5">
          <campaign-item-component></campaign-item-component>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      years: ["2019", "2018", "2017"],
      year: ""
    };
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
.init {
  background-image: url("../../assets/handpeace.png");
  background-size: cover;
}

h1 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 64px;
  line-height: 96px;
  color: #0c186d;
}

h3 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 44px;
  line-height: 66px;

  color: #0c186d;
  margin-left: 13%;
}

.filter {
  font-family: "Poppins";
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 36px;
  color: #000000;
}

.div-filter{
  margin-left: 30%;
}

p {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 36px;
}

</style>