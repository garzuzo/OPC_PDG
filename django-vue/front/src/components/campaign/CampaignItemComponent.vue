<template>
  <!--  <div>
        <h2> {{title}}</h2>
        <p> {{description}}</p>
        <p><v-icon>far fa-calendar-alt</v-icon>{{startDate}} - {{endDate}} </p>  
        <v-btn icon>
          <v-icon>fas fa-search</v-icon>
        </v-btn>
  </div>-->
  <v-card class="mx-auto" color="#E1E1E9" dark max-width="400">
    <v-card-title>
      <h2>{{title}}</h2>
    </v-card-title>

    <v-card-text class="headline font-weight-bold">
      <p class="description">{{description}}</p>
    </v-card-text>

    <v-card-actions>
      <p class="ml-2">
        <v-icon>far fa-calendar-alt</v-icon>
        {{startDate}} - {{endDate}}
      </p>

      <v-row align="center" justify="end">
        <v-btn icon class="mr-2">
          <v-icon>fas fa-search</v-icon>
        </v-btn>
      </v-row>
    </v-card-actions>
  </v-card>
</template>


</template>

<script>
export default {
  data() {
    return {
      title: "Campaña Río Cali",
      description: "Esta campaña es para el cuidado del río Cali",
      startDate: "24/06/2019",
      endDate: "05/09/2019",
      color: "#FFFFFF"
    };
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
h2 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 20px;
  line-height: 20px;
  color: #000000;
}

.description {
  font-family: Poppins;
  font-style: normal;
  font-weight: 300;
  font-size: 18px;
  line-height: 27px;

  color: #000000;
}

p {
  font-family: Poppins;
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
  line-height: 20px;
  /* or 100% */

  color: #000000;
}
</style>