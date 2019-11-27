<template>
  <div>
    <navbar-component></navbar-component>

    <div class="init" style="padding-top: 10vh; padding-bottom: 10vh;">
      <h3 align="center">Tu perfil</h3>
      <v-row justify="center">
        <v-dialog v-model="dialogEdit" fullscreen hide-overlay transition="dialog-bottom-transition">
          <template v-slot:activator="{ on }">
            <v-btn :ripple="false" v-on="on" rounded class="ma-2 ma-5 edit" color="#ffffff">Editar información</v-btn>
            <!--<v-btn color="primary" dark v-on="on">Open Dialog</v-btn>-->
          </template>
          <v-card>
            <v-toolbar dark color="#0C186D">
              <v-btn icon dark @click="dialogEdit = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Editar perfil</v-toolbar-title>
            </v-toolbar>
            <edit-profile-component :profile="profile"></edit-profile-component>
          </v-card>
        </v-dialog>
        
      </v-row>

    <v-container>
      <v-row style="padding-top: 5vh;" justify="center">
        <v-col cols="3">
          <p>Estoy en <span>{{city}}</span></p>
        </v-col>

        <v-col cols="3">
           <p>He realizado <span>{{narratives}} narrativas</span></p>
        </v-col>

        <v-col v-if="roleUser==2" cols="3">
           <p>He creado <span>{{campaigns}} campañas</span></p>           
        </v-col>
      </v-row>
    </v-container>
    </div>

    <v-container style="padding-top: 10vh;"> 
      <h2>Has participado en las siguientes campañas:</h2>

      <v-row justify="space-around"> 
        <v-col cols="4">
            <h2 class="ml-3"> Activas </h2>
            <v-col v-for="campaign in activeCampaigns" v-bind:key="campaign.id" class="d-flex child-flex">
                <campaign-item-component color="#FFFFFF" :edit="false" :campaign="campaign"></campaign-item-component>
            </v-col>
        </v-col>

        <v-col cols="4">
            <h2 class="ml-3">Finalizadas </h2>
            <v-col v-for="campaign in notActiveCampaigns" v-bind:key="campaign.id" class="d-flex child-flex">
                <campaign-item-component color="#E1E1E9" :edit="false" :campaign="campaign"></campaign-item-component>
            </v-col>
        </v-col>   

        <v-col v-if="roleUser==2" cols="4">
            <h2 class="ml-3"> Creadas </h2>
            <v-col v-for="campaign in createdCampaigns" v-bind:key="campaign.id" class="d-flex child-flex">
                <campaign-item-component color="#E6CEFF" :edit="true" :campaign="campaign"></campaign-item-component>
            </v-col>

            <v-dialog v-model="dialogCampaign" persistent width="400px">
          <template v-slot:activator="{ on }">
            <v-btn v-if="roleUser==2" :ripple="false" v-on="on" rounded class="edit" dark color="#673ab7">Crear campaña</v-btn>
            <!--<v-btn color="primary" dark v-on="on">Open Dialog</v-btn>-->
          </template>
          <v-card>
            <v-toolbar dark color="#0C186D">
              <v-btn icon dark @click="dialogCampaign = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
               <v-toolbar-title>Crear campaña</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
            <create-campaign-component> </create-campaign-component>
            </v-card-text>
          </v-card>
        </v-dialog>
        </v-col>   
    </v-row>    

    </v-container>
    
    

    <!--<v-row justify="center">
      <v-col cols="5">
      <v-btn :ripple="false" rounded class="edit" dark color="#673ab7" @click="logout">Logout</v-btn>
      </v-col>
    </v-row>-->
  </div>
</template>

<script>
import api from "../../axios.js";
export default {
  data() {
    return {
      activeCampaigns: [],
      notActiveCampaigns: [],
      userCampaigns: [],
      dialogEdit: false,
      dialogCampaign: false,
      city: '',
      narratives: 0, 
      campaigns: 0,
      roleUser: 0,
      profile: {
        gender: {id:0, typeGender: ""},
        level: {id:0, name: ""},
        higherEducation: {id:0, name: ""},
        currentZone: {id:0, zoneType: ""},
        currentState: {id:0, name: ""},
        currentCity: {id:0, name: ""},
        currentComuna: {id:0, name: ""},
        currentNeighborhood: {id:0, name: ""},
        currentCorregimiento: {id:0, name: ""},
        currentVereda: {id:0, name: ""}
      }
    };
  },
  created() {
    var activeCampaigns = []
    var notActiveCampaigns = []
    api.getProfileCampaigns().then(response => {

        this.narratives = response.length
        for(var i=0; i<response.length; i++){
            var act= response[i]
            if(act.isActive){
              activeCampaigns.push(act)
            }else{
              notActiveCampaigns.push(act)
            }
        }
        this.activeCampaigns = activeCampaigns
        this.notActiveCampaigns = notActiveCampaigns
    }).catch(err => console.log(err));

    api.getCityPerson().then(response => {
        this.city = response.city_name
    }).catch(err => console.log(err));
    
    api.getRoleUser().then(response => {
        this.roleUser = response.role_user
    }).catch(err => console.log(err));

    api.getProfile().then(response =>{
      this.profile.level.id = parseInt(response.achievedLevel.split("/")[0])
      this.profile.level.name = response.achievedLevel.split("/")[1]
       
      this.profile.higherEducation.id = parseInt(response.higherEd.split("/")[0])
      this.profile.higherEducation.name = response.higherEd.split("/")[1]

      this.profile.currentZone.id = parseInt(response.zoneActual.split("/")[0])
      this.profile.currentZone.zoneType = response.zoneActual.split("/")[1]
      
      this.profile.currentState.id = parseInt(response.state.split("/")[0])
      this.profile.currentState.name = response.state.split("/")[1]

      this.profile.currentCity.id = parseInt(response.city.split("/")[0])
      this.profile.currentCity.name = response.city.split("/")[1]

      if(this.profile.currentZone.zoneType== "Urbana"){
        this.profile.currentComuna.id= parseInt(response.comunaCorregimiento.split("/")[0])
        this.profile.currentComuna.name = response.comunaCorregimiento.split("/")[1]

        this.profile.currentNeighborhood.id= parseInt(response.neighborhoodVeredaActual.split("/")[0])
        this.profile.currentNeighborhood.name= response.neighborhoodVeredaActual.split("/")[1]
      }
      if(this.profile.currentZone.zoneType == "Rural"){
        this.profile.currentCorregimiento.id = parseInt(response.comunaCorregimiento.split("/")[0])
        this.profile.currentCorregimiento.name = response.comunaCorregimiento.split("/")[1]

        this.profile.currentVereda.id = parseInt(response.neighborhoodVeredaActual.split("/")[0])
        this.profile.currentVereda.name = response.neighborhoodVeredaActual.split("/")[0]
      }
    }).catch(err => console.log(err));
    /*api
      .getNotActiveCampaigns()
      .then(response => {
        this.notActiveCampaigns = response;})
      .catch(err => console.log(err));*/
  },
  computed:{
    createdCampaigns(){
      api.getCreatedCampaigns().then(response => {
        this.campaigns = response.length
        this.userCampaigns = response
      }).catch(err => console.log(err));
      return this.userCampaigns;
    }
  },
  methods:{
    logout(){
      this.$store
        .dispatch("logout")
        .then((resp) => {
          this.$router.push("/login")
        })
        .catch(err => {
          console.log(err);
        });
    },
  }
};
</script>

<style scoped>
.init {
  background-color: #673ab7;
}

.profile {
  margin: 0 auto;
  width: 20%;
}

h3 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 36px;
  line-height: 66px;

  color: #ffffff;
}

h2{
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 36px;
  line-height: 96px;
  color: #0c186d;

}
p {
  font-family: "Poppins";
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 20px;

  color: #ffffff;
}
span {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 18px;
  line-height: 20px;

  color: #ffffff;
}
.edit {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  text-transform: none !important;
}
</style>