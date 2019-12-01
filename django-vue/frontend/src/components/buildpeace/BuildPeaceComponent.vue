<template>
  <div>
    <navbar-component></navbar-component>

    <div class="init">
      <v-container  class="fill-height" style="min-height: 100%">
        <!--INITIAL IMAGE -->
        <v-row style="padding-top: 20vh; padding-bottom:20vh;">
          <v-col sm="12" md="7">
            <h1 style="padding-bottom:10vh;">¡Construyamos Paz!</h1>
            <p>Para el Observatorio de Paz y Convivencia es de vital importancia comprender tu percepción de paz con el fin de aportar información valiosa para las campañas en curso de proyectos alineados a la construcción de paz y cultura ciudadana.
              ¡Ayudános a construir más paz!
            </p>
          </v-col>
        </v-row>
      </v-container>
    </div>

    <v-container>
      <!-- ACTIVE CAMPAIGN -->
      <v-speed-dial
        v-model="fab"
        bottom      
        left
        direction="top"
        transition="scale-transition"
        fixed
      >
      <template v-slot:activator>
          <v-btn
            v-model="fab"
            color="#0c186d"
            dark
            fab
          >
            <v-icon v-if="fab">mdi-close</v-icon>
            <v-icon v-else>mdi-share-variant</v-icon>
          </v-btn>
        </template>

        <twitter-button 
  class="share-button--circle share-button--outline"
  v-bind:url="url"
  btnText
  description="¡Ayudanos a construir más paz!"
/>

<facebook-button 
  class="share-button--circle share-button--outline"
  v-bind:url="url"
  btnText
  description="¡Ayudanos a construir más paz!"
/>
      </v-speed-dial>

      <v-container style="padding-top: 20vh;">
        <v-row justify="center">
          <v-col sm="8" md="5">
            <div class="form-group">
              <p for="campaign">Selecciona la campaña en la que deseas participar</p>
              <v-select
                :items="campaigns"
                :error-messages="campaignErrors"
                item-text="title"
                item-value="title"
                outlined
                v-model="campaign"
                return-object
                required
                class="input"
                color="#0C186D"
                name="campaign"
                @change="$v.campaign.$touch()"
              ></v-select>
            </div>
          </v-col>
        </v-row>
      </v-container>
      <!-- STEPPER -->
      <v-row align="center" justify="center">
        <v-col sm="8" md="8">
          <v-stepper v-model="e1">
            <!--TABS -->
            <v-stepper-header>
              <v-stepper-step color="#0C186D" class="input" :complete="e1 > 1" step="1">Narrativa</v-stepper-step>
              <v-divider v-if="!isLoggedIn"></v-divider>
              <v-stepper-step v-if="!isLoggedIn" color="#0C186D" class="input" :complete="e1 > 2" step="2">Personal</v-stepper-step>

              <v-divider v-if="!isLoggedIn"></v-divider>

              <v-stepper-step v-if="!isLoggedIn" color="#0C186D" class="input" :complete="e1 > 3" step="3">Territorio</v-stepper-step>

              <v-divider v-if="!isLoggedIn"></v-divider>

              <v-stepper-step v-if="!isLoggedIn" color="#0C186D" class="input" :complete="e1 > 4" step="4">Educación</v-stepper-step>
              <v-divider v-if="!isLoggedIn"></v-divider>

              <v-stepper-step v-if="!isLoggedIn" color="#0C186D" class="input" :complete="e1 > 5" step="5">Finalizar</v-stepper-step>
            </v-stepper-header>

            <!-- ITEMS INSIDE EACH TAB-->
            <v-stepper-items>

              <v-stepper-content step="1">
                <narrative-form-component :succes="succesUser" v-on:allToParent="allFromNarrativeChildClick"></narrative-form-component>
              </v-stepper-content>

              <v-stepper-content step="2">
                <personal-form-component v-on:allToParent="allFromPersonalChildClick"  v-on:before="beforePersonal"></personal-form-component>
              </v-stepper-content>

              <v-stepper-content step="3">
                <territory-form-component
                  v-on:allToParent="allFromTerritoryChildClick"
                  v-on:before="beforeTerritory"
                ></territory-form-component>
              </v-stepper-content>

              <v-stepper-content step="4">
                <education-form-component
                  v-on:allToParent="allFromEducationChildClick"
                  v-on:before="beforeEducation"
                ></education-form-component>
              </v-stepper-content>

              <v-stepper-content step="5">
                <save-info-component
                  v-on:allToParent="allFromFinishChildClick"
                  v-on:before="beforeFinish"
                ></save-info-component>
              </v-stepper-content>

            </v-stepper-items>
          </v-stepper>
        </v-col>
      </v-row>

      <v-row align="center" justify="center">
        <v-col cols="12" sm="12" md="8">
         <div v-if="submitStatus!=''" class="pa-5 alert alert-danger" role="alert">
          {{submitStatus}}
      </div>
      <div v-if="succes!=''" class="pa-5 alert alert-success" role="alert">
           {{succes}}
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import api from "../../axios.js";
import { required } from "vuelidate/lib/validators";
import { validationMixin } from "vuelidate";
import TwitterButton from "vue-share-buttons/src/components/TwitterButton";
import FacebookButton from "vue-share-buttons/src/components/FacebookButton";

export default {
  name: "BuildPeace",
  mixins: [validationMixin],

  validations: {
    campaign : { title: {required} }
  },
  components: {
    TwitterButton,
    FacebookButton
  },
  data() {
    return {
      fab: false,
      url: 'http://pi2sis.icesi.edu.co/opc/#/construirpaz',
      e1: 0,
      narrative: "",
      word1: "",
      word2: "",
      word3: "",
      word4: "",
      word5: "",
      isLoggedIn: this.$store.getters.isLoggedIn,
      campaign: {id: 0, title:''},
      campaigns: [],
      submitStatus: "",
      succes:"",
      succesUser:"",
      dialog: false,
      scroll: false, 
      checkbox: false,
      //PERSONAL COMPONENT
      age: 0,
      gender: {id: 0, name:''},
      //EDUCATION COMPONENT
      level: {id: 0, name:''},
      higherEducation: {id: 0, name:''},
      //TERRITORY COMPONENT
      currentZone: {id: 0, zoneType:''},
      currentState: {id: 0, name:''},
      currentCity: {id: 0, name:''},
      currentComuna: {id: 0, name:''},
      currentNeighborhood: {id: 0, name:''},
      currentCorregimiento: {id: 0, name:''},
      currentVereda: {id: 0, name:''},
      originZone: {id: 0, zoneType:''},
      originState: {id: 0, name:''},
      originCity: {id: 0, name:''},
      originComuna: {id: 0, name:''},
      originNeighborhood: {id: 0, name:''},
      originCorregimiento: {id: 0, name:''},
      originVereda: {id: 0, name:''},
      //USER
      email:"",
      password:""
    };
  },
  created() {

    if(this.isLoggedIn){
      api.getUserActiveCampaigns().then(response => {
        this.campaigns = response;
      })
      .catch(err => console.log(err));
    }else{
      api
      .getActiveCampaigns()
      .then(response => {
        this.campaigns = response;
      })
      .catch(err => console.log(err));
    }
  },
  methods: {
    //PROPS FROM CHILDREN
    //Narrative
    allFromNarrativeChildClick(value) {
      this.narrative = value[0],
      this.word1 = value[1],
      this.word2 = value[2],
      this.word3 = value[3],
      this.word4 = value[4],
      this.word5 = value[5]
      this.e1 = parseInt(value[6]);

      if(this.isLoggedIn){
        this.$v.$touch()
      if(this.$v.$anyError){
        this.submitStatus = "Revisa las advertencias. Tienes algún error en los campos. Intenta de nuevo. "
        this.succesUser=""
      }else{
        this.submitStatus = ""
        this.succesUser=""
        let data = {
        campaign : this.campaign.id,
        narrative: this.narrative,
        word1: this.word1,
        word2: this.word2,
        word3: this.word3,
        word4: this.word4,
        word5: this.word5
      };
       api.saveNarrativeLoggedUser(data).then(response=> {
         this.succesUser="Tu narrativa ha sido guardada exitosamente. ¡Gracias por ayudarnos a construir paz!."
         let data= {campaign:response.campaign, user: response.id}
         this.$store.dispatch("saveNarrative",data)
         setTimeout(() => this.$router.push("/visualizacampaña"), 5000);
         }).catch(err=> console.log(err))
      }
      }

    },
    //Personal
    allFromPersonalChildClick(value) {
      this.age = value[0];
      this.gender = value[1];
      this.e1 = parseInt(value[2]);
    },
    beforePersonal(value) {
      this.e1 = value;
    },
    //Education
    allFromEducationChildClick(value) {
      this.higherEducation = value[0];
      this.level = value[1];
      this.e1 = parseInt(value[2]);
      //this.saveData();
    },
    /*allFromEducationRegister(){
      this.higherEducation = value[0];
      this.level = value[1];
      this.username = value[2];
      this.password = value[3];
      this.saveDataRegister();
    },*/
    beforeEducation(value) {
      this.e1 = value;
    },
    //Territory
    allFromTerritoryChildClick(value) {
      this.currentZone = value[0];
      this.currentState = value[1];
      this.currentCity = value[2];
      this.currentComuna = value[3];
      this.currentNeighborhood = value[4];
      this.currentCorregimiento = value[5];
      this.currentVereda = value[6];
      this.originZone = value[7];
      this.originState = value[8];
      this.originCity = value[9];
      this.originComuna = value[10];
      this.originNeighborhood = value[11];
      this.originCorregimiento = value[12];
      this.originVereda = value[13];
      this.e1 = parseInt(value[14]);
    },
    beforeTerritory(value) {
      this.e1 = value;
    },
    beforeFinish(value){
      this.e1 = value;
    },
    logout(){
      this.$store
        .dispatch("logout")
        .then((resp) => {
          this.$router.push("/profile")
        })
        .catch(err => {
          console.log(err);
        });
    },
    //Finish
    allFromFinishChildClick(value){
      if(value[0]=="register"){
        this.email = value[1];
        this.password = value[2];
        this.saveDataRegister();
      }else{
        this.saveData()
      }
    },
    //REAL HANDLE OF METHODS
    saveData() {
      this.$v.$touch()
      if(this.$v.$anyError){
        this.submitStatus = "Revisa las advertencias. Tienes algún error en los campos. Intenta de nuevo. "
      }else{
        this.submitStatus = ""
        console.log("HERE I AMMMMMM")
        let data = {
        campaign : this.campaign.id,
        age: this.age,
        gender: this.gender.id,
        level: this.level.id,
        higherEducation: this.higherEducation.id,
        currentZone: this.currentZone.id,
        currentState: this.currentState.id,
        currentCity: this.currentCity.id,
        currentComuna: this.currentComuna.id,
        currentNeighborhood: this.currentNeighborhood.id,
        currentCorregimiento: this.currentCorregimiento.id,
        currentVereda: this.currentVereda.id,
        originZone: this.originZone.id,
        originState: this.originState.id,
        originCity: this.originCity.id,
        originComuna: this.originComuna.id,
        originNeighborhood: this.originNeighborhood.id,
        originCorregimiento: this.originCorregimiento.id,
        originVereda: this.originVereda.id,
        narrative: this.narrative,
        word1: this.word1,
        word2: this.word2,
        word3: this.word3,
        word4: this.word4,
        word5: this.word5
      };
      //console.log(data)
      api.saveData(data).then((resp)=>{
        this.succes="Tu narrativa ha sido guardada exitosamente. ¡Gracias por ayudarnos a construir paz!."
        console.log(resp)
        let data= {campaign:resp.campaign, user: resp.id}
        console.log("DATOS ANTES DE STORE")
        console.log(data)
        this.$store.dispatch("saveNarrative",data)
        setTimeout(() => this.$router.push("/visualizacampaña"), 5000);
        }).catch(err=> {console.log(err)});
      }
      
    },
    saveDataRegister(){
      this.$v.$touch()
      if(this.$v.$anyError){
        this.submitStatus = "Revisa las advertencias. Tienes algún error en los campos. Intenta de nuevo."
      }else{
        this.submitStatus = ""
        console.log("HERE I AMMMMMM REGISTER")
        let data = {
        email : this.email,
        password : this.password,
        campaign : this.campaign.id,
        age: this.age,
        gender: this.gender.id,
        level: this.level.id,
        higherEducation: this.higherEducation.id,
        currentZone: this.currentZone.id,
        currentState: this.currentState.id,
        currentCity: this.currentCity.id,
        currentComuna: this.currentComuna.id,
        currentNeighborhood: this.currentNeighborhood.id,
        currentCorregimiento: this.currentCorregimiento.id,
        currentVereda: this.currentVereda.id,
        originZone: this.originZone.id,
        originState: this.originState.id,
        originCity: this.originCity.id,
        originComuna: this.originComuna.id,
        originNeighborhood: this.originNeighborhood.id,
        originCorregimiento: this.originCorregimiento.id,
        originVereda: this.originVereda.id,
        narrative: this.narrative,
        word1: this.word1,
        word2: this.word2,
        word3: this.word3,
        word4: this.word4,
        word5: this.word5
      };
      console.log(data)
      api.saveData(data).then((resp)=>{
        this.succes="Tu narrativa ha sido guardada exitosamente. ¡Gracias por ayudarnos a construir paz!."
        let data= {campaign:resp.campaign, user: resp.id}
        this.$store.dispatch("saveNarrative",data)
        setTimeout(() => this.$router.push("/visualizacampaña"), 5000);
        //this.$router.push("/login")
        }).catch(err=> {
          this.submitStatus= err.data.detail
      console.log(err)});
      }
    }
  },
  computed: {
    campaignErrors() {
      const errors = [];
      if (!this.$v.campaign.$dirty) return errors;
      !this.$v.campaign.title.required && errors.push("La campaña es requerida.");
      return errors;
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
body {
  background-color: #ffffff;
}
.init {
  background-image: url("../../assets/handpeace.png");
  background-size: cover;
  height: 100vh;
}

h1 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  /*calc([minimum size] + ([maximum size] - [minimum size]) * ((100vw - [minimum viewport width]) / ([maximum viewport width] - [minimum viewport width])));*/
  font-size: calc(32px + (64 - 32) * ((100vw - 300px) / (1600 - 300)));
  color: #0c186d;
}

p {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: calc(18px + (24 - 18) * ((100vw - 300px) / (1600 - 300)));
}

label {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
}

h3 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  text-align: center;
}

.next {
  text-transform: none;
  font-family: "Roboto";
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
  line-height: 33px;
  display: flex;
  align-items: center;
  text-align: center;
  letter-spacing: normal !important;
}

.save {
  text-transform: none;
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
  line-height: 33px;
  display: flex;
  align-items: center;
  text-align: center;
}
.input {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
  line-height: 36px;
}
</style>
