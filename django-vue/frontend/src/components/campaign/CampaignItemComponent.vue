<template>
  <!--  <div>
        <h2> {{title}}</h2>
        <p> {{description}}</p>
        <p><v-icon>far fa-calendar-alt</v-icon>{{startDate}} - {{endDate}} </p>  
        <v-btn icon>
          <v-icon>fas fa-search</v-icon>
        </v-btn>
  </div>-->
  <v-card class="mx-auto" v-bind:color="color" dark max-width="400">
    <v-card-title>
      <h2>{{campaign.title}}</h2>
    </v-card-title>

    <v-card-text class="headline font-weight-bold">
      <p class="description">{{campaign.description}}</p>
    </v-card-text>

    <v-card-actions>
      <p class="ml-2">
        <v-icon color="#000000">far fa-calendar-alt</v-icon>
        {{campaign.startDate}} - {{campaign.endDate}}
      </p>

      <v-row align="center" justify="end">
        <!--DIALOG -->
        <!--<v-btn icon class="mr-2">
          <v-icon color="#000000">fas fa-search</v-icon>
        </v-btn>-->
        <v-dialog v-model="dialogEdit" width="400px" >
          <template v-slot:activator="{ on }">
             <v-btn icon v-if="edit" class="mr-2" v-on="on">
              <v-icon color="#000000">mdi-pencil</v-icon>
            </v-btn>
            <!--<v-btn color="primary" dark v-on="on">Open Dialog</v-btn>-->
          </template>
          <v-card>
            <v-toolbar dark color="#0C186D">
              <v-btn icon dark @click="dialogEdit = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>Editar campaña</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
            <create-campaign-component :edit="edit" :campaign="campaign"> </create-campaign-component>
            </v-card-text>
          </v-card>
        </v-dialog>

       

        <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
          <template v-slot:activator="{ on }">
            <v-btn v-if="!edit" icon class="mr-2" v-on="on">
              <v-icon color="#000000">fas fa-search</v-icon>
            </v-btn>
            <!--<v-btn color="primary" dark v-on="on">Open Dialog</v-btn>-->
          </template>
          <v-card>
            <v-toolbar dark color="#0C186D">
              <v-btn icon dark @click="dialog = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>{{campaign.title}}</v-toolbar-title>
            </v-toolbar>
            <report-campaign-component v-if="!logged" :campaign="campaign"> </report-campaign-component>
            <visualization-campaign-component v-if="logged" :logged="true"> </visualization-campaign-component>
          </v-card>
        </v-dialog>
      </v-row>
    </v-card-actions>
  </v-card>
</template>


<script>
import api from '../../axios'
export default {
  props: {
    color: String,
    campaign: Object,
    edit: Boolean,
    logged: Boolean,
  },
  data() {
    return {
      dialog: false,
      dialogEdit: false
    };
  },
  created(){
    if(this.logged){
      api.getPersonCampaignLogged(this.campaign.id).then(response=>{
        let data= {campaign:this.campaign.id, user: response.id}
        this.$store.dispatch("saveNarrative",data)
      }).catch(err=>console.log(err))      
    }    
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