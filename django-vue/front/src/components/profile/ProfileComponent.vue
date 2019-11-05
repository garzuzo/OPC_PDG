<template>
  <div>
    <navbar-component></navbar-component>

    <div class="init" style="padding-top: 10vh; padding-bottom: 10vh;">
      <h3 align="center">Tu perfil</h3>
      <div class="profile">
         <img src="@/assets/profile.png" />
        <h3 align="center">Johnatan Garzón</h3>
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
        
      </div>

    <v-container>
      <v-row style="padding-top: 5vh;" justify="center">
        <v-col cols="3">
          <p>Estoy en <span>Cali</span></p>
        </v-col>

        <v-col cols="3">
           <p>He realizado <span>2 narrativas</span></p>
        </v-col>

        <v-col cols="3">
           <p>He creado <span>0 campañas</span></p>
           <v-dialog v-model="dialogCampaign" persistent max-width="400px" v-bind:scrollable="scroll">
          <template v-slot:activator="{ on }">
            <v-btn :ripple="false" v-on="on" rounded class="edit" color="#ffffff">Crear campaña</v-btn>
            <!--<v-btn color="primary" dark v-on="on">Open Dialog</v-btn>-->
          </template>
          <v-card>
            <v-toolbar dark color="#0C186D">
              <v-btn icon dark @click="dialogCampaign = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
               <v-toolbar-title>Crear campaña</v-toolbar-title>
            </v-toolbar>
            <create-campaign-component> </create-campaign-component>
          </v-card>
        </v-dialog>

           
        </v-col>
      </v-row>
    </v-container>
    </div>

    <v-row justify="space-around"> 
        <v-col cols="5">
            <h2 align="center">Campañas activas </h2>
            <v-col v-for="campaign in activeCampaigns" v-bind:key="campaign.id" class="d-flex child-flex">
                <campaign-item-component color="#FFFFFF" :campaign="campaign"></campaign-item-component>
            </v-col>
        </v-col>

        <v-col cols="5">
            <h2 align="center">Campañas pasadas </h2>
            <v-col v-for="campaign in notActiveCampaigns" v-bind:key="campaign.id" class="d-flex child-flex">
                <campaign-item-component color="#E1E1E9" :campaign="campaign"></campaign-item-component>
            </v-col>
        </v-col>   
    </v-row>    

    <v-row justify="center">
      <v-col cols="5">
      <v-btn :ripple="false" rounded class="edit" dark color="#673ab7" @click="logout">Logout</v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import api from "../../axios.js";
export default {
  data() {
    return {
      activeCampaigns: [],
      notActiveCampaigns: [],
      dialogEdit: false,
      dialogCampaign: false,
      profile: {
        age: "03-03-1997",
        gender: "Masculino",
        name: "Johnatan",
        lastname: "Garzón",
        level: "En curso",
        higherEducation: "Universitaria",
        currentZone: "Urbana",
        currentState: "Valle del Cauca",
        currentCity: "Cali",
        currentComuna: "Comuna 5",
        currentNeighborhood: "Barrio Lomitas",
        currentCorregimiento: "Corregimiento Pance",
        currentVereda: "Pance (Cabecera)",
        originZone: "Urbana",
        originState: "Valle del Cauca",
        originCity: "Cali",
        originComuna: "Comuna 5",
        originNeighborhood: "Barrio Lomitas",
        originCorregimiento: "Corregimiento Pance",
        originVereda: "Pance (Cabecera)"
      }
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
        this.notActiveCampaigns = response;})
      .catch(err => console.log(err));
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