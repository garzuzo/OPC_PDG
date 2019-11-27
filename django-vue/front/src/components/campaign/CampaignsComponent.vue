<template>
  <div>
    <navbar-component></navbar-component>

    <div class="init">
      <v-container class="fill-height" style="min-height: 100%">
        <!--INITIAL IMAGE -->
        <v-row style="padding-top: 20vh; padding-bottom:20vh;">
          <v-col cols="7">
            <h1 style="padding-bottom:10vh;">Campañas</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam egestas, metus ac dignissim mattis, metus risus pretium ligula, ut mattis purus eros at nisl.</p>
          </v-col>
        </v-row>
      </v-container>
    </div>

    <v-container>
      <h3>Campañas Activas</h3>
      <v-row justify="center">
        <v-col v-for="campaign in activeCampaigns" v-bind:key="campaign.id" cols="5">
          <campaign-item-component color="#FFFFFF" :campaign="campaign"></campaign-item-component>
        </v-col>
      </v-row>

      <h3>Campañas Finalizadas</h3>
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

      <v-row v-if="year == ''" justify="center">
        <v-col v-for="campaign in notActiveCampaigns" v-bind:key="campaign.id" cols="5">
          <campaign-item-component color="#E1E1E9" :campaign="campaign"></campaign-item-component>
        </v-col>
      </v-row>

      <v-row v-if="year != ''" justify="center">
        <v-col v-for="campaign in filterCampaigns" v-bind:key="campaign.id" cols="5">
          <campaign-item-component color="#E1E1E9" :campaign="campaign"></campaign-item-component>
        </v-col>
      </v-row>  
    </v-container>
  </div>
</template>

<script>
import api from "../../axios.js";

export default {
  data() {
    return {
      years: [],
      year: "",
      activeCampaigns: [],
      notActiveCampaigns: []
    };
  },
  created() {
    api
      .getActiveCampaigns()
      .then(response => {
        this.activeCampaigns = response;
      })
      .catch(err => console.log(err));
    
    api
      .getNotActiveCampaigns()
      .then(response => {
        this.notActiveCampaigns = response;
        const dateYears = new Set()
        for(var i=0; i < this.notActiveCampaigns.length; i++){
          var date= this.notActiveCampaigns[i].endDate.split("-");
          dateYears.add(new Date(parseInt(date[0]), parseInt(date[1])-1, parseInt(date[2])).getFullYear());
        }
        this.years = Array.from(dateYears)
      })
      .catch(err => console.log(err));
  },
  computed: {
    filterCampaigns(){
      var campaigns = []
      if(this.year != ""){
        for(var i=0; i < this.notActiveCampaigns.length; i++){
          var campaign = this.notActiveCampaigns[i];
          if(campaign.endDate.split("-")[0] == this.year){
            campaigns.push(campaign)
          }
        }
      }
      return campaigns
    }
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