<template>
      <v-row justify="center">
    <v-col cols="12">
      <v-form class="form pa-5">
        <div class="form-group">
          <label for="title">Título*</label>
          <v-text-field
            v-model="title"
            :error-messages="titleErrors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="title"
            class="input"
            @input="$v.title.$touch()"
          ></v-text-field>
        </div>

        <div class="form-group">
          <label for="description">Descripción*</label>
          <v-textarea
            v-model="description"
            :error-messages="descriptionErrors"
            outlined
            color="#0C186D"
            counter="250"
            required
            name="description"
            class="input"
            @input="$v.description.$touch()"
          ></v-textarea>
        </div>

        <div class="form-group">
          <label for="startDate">Fecha de inicio*</label>
          <v-menu
            v-model="menuStart"
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
            v-model="startDate"
            :error-messages="startDateErrors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="startDate"
            class="input"
            v-on="on"
            @input="$v.startDate.$touch()"
          ></v-text-field>
            </template>
            <v-date-picker v-model="startDate" color="#0C186D" @input="menuStart = false"></v-date-picker>
          </v-menu>          
        </div>
        
        <div class="form-group">
          <label for="endDate">Fecha de finalización*</label>
          <v-menu
            v-model="menuEnd"
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
            v-model="endDate"
            :error-messages="endDateErrors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="endDate"
            class="input"
            v-on="on"
            @input="$v.endDate.$touch()"
          ></v-text-field>
            </template>
            <v-date-picker v-model="endDate" color="#0C186D" @input="menuEnd = false"></v-date-picker>
          </v-menu>

          
        </div>

        <div class="form-group">
          <label for="narrativesGoal">Meta de narrativas*</label>
          <v-text-field
            v-model="narrativesGoal"
            :error-messages="narrativesGoalErrors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="narrativesGoal"
            class="input"
            @input="$v.narrativesGoal.$touch()"
          ></v-text-field>
        </div>

        <div>
          <v-checkbox v-if="!edit"
          v-model="checkbox"
          label="¿Crear como campaña activa?"
          @change="check($event)"
        ></v-checkbox>
        <v-checkbox v-if="edit"
          v-model="checkbox"
          label="Activa"
          @change="check($event)"
        ></v-checkbox>
        </div>

        <v-row align="center" justify="center">
        <v-col cols="10">
         <div v-if="submitStatus!=''" class="pa-5 alert alert-danger" role="alert">
          Revisa las advertencias. Tienes algún error en los campos
          </div>
          <div v-if="succes!=''" class="pa-5 alert alert-success" role="alert">
           {{succes}}
          </div>
        </v-col>
      </v-row>
        <v-btn v-if="!edit" :ripple="false" class="login" tile color="#673AB7" dark @click="createCampaign">Crear</v-btn>
        <v-btn v-if="edit" :ripple="false" class="login" tile color="#673AB7" dark @click="editCampaign">Editar</v-btn>
      </v-form>
    </v-col>
  </v-row>
</template>

<script>
import api from '../../axios'
import { required, numeric } from "vuelidate/lib/validators";
import { validationMixin } from "vuelidate";

function dateMaxValue (date) {
      //const validator = minValue(new Date())
      const dateSplit = date.split("-")
      const dateFinal = new Date(parseInt(dateSplit[0]), parseInt(dateSplit[1])-1, parseInt(dateSplit[2]))
      const today = new Date().setHours(0,0,0,0)//.toISOString().split("T")[0]
      //today.setHours(0,0,0,0)
      return dateFinal > today
}

function endGreaterThanStart (date) {
      //const validator = minValue(new Date())
      const dateSplit = date.split("-")
      date = new Date(parseInt(dateSplit[0]), parseInt(dateSplit[1])-1, parseInt(dateSplit[2]))
      console.log(date)
      const startDateSplit =  this.startDate.split("-")
      const startDate = new Date(parseInt(startDateSplit[0]), parseInt(startDateSplit[1])-1, parseInt(startDateSplit[2]))
      return startDate <= date
}

function greaterThanCero(number){
    return number > 0
}

export default {
  mixins: [validationMixin],

  validations: {
    title : { required},
    description: {required}, 
    startDate : {required},
    endDate: {required, dateMaxValue, endGreaterThanStart},
    narrativesGoal: {required, numeric, greaterThanCero}
  },
  props:{
    edit: Boolean,
    campaign: Object
  },
    data(){
        return{
            title: "", 
            description: "", 
            startDate: new Date().toISOString().substr(0, 10), 
            endDate: new Date().toISOString().substr(0, 10), 
            narrativesGoal: 0,
            menuStart: false, 
            menuEnd: false,
            submitStatus: "",
            succes : "",
            checkbox:false
        }
    },
    created(){
      if(this.edit){
        this.title= this.campaign.title
        this.description = this.campaign.description
        this.startDate = this.campaign.startDate
        this.endDate = this.campaign.endDate
        this.narrativesGoal = this.campaign.narrativesGoal
        this.checkbox = this.campaign.isActive
      }
    },
    methods:{
      createCampaign(){
        this.$v.$touch()
      if(this.$v.$anyError){
        this.submitStatus = "Error"
        this.succes = ""
      }else{
        this.submitStatus = ""
        this.succes = ""
        let data = {
        title: this.title,
        description: this.description,
        start_date : this.startDate,
        end_date: this.endDate,
        accumulated_narratives: 0,
        narratives_goal: this.narrativesGoal,
        is_active: this.checkbox
      };
      console.log(data)
      console.log(this.$store.state.token)
        api.saveCampaign(data).then(response => {this.succes = "Tu campaña ha sido creada con éxito"}).catch(err=> {console.log(err)})
      }
      },
      editCampaign(){
        this.$v.$touch()
      if(this.$v.$anyError){
        this.submitStatus = "Error"
        this.succes = ""
      }else{
        this.submitStatus = ""
        this.succes = ""
        let data = {
        id: this.campaign.id,
        title: this.title,
        description: this.description,
        start_date : this.startDate,
        end_date: this.endDate,
        narratives_goal: this.narrativesGoal,
        is_active: this.checkbox
      };
      console.log(data)
      console.log(this.$store.state.token)
        api.editCampaign(data).then(response => {this.succes = "Tu campaña ha sido actualizada con éxito"}).catch(err=> {console.log(err)})
      }
      }
    },
    computed:{

      titleErrors() {
      const errors = [];
      if (!this.$v.title.$dirty) return errors;
      !this.$v.title.required && errors.push("Título es requerido.");
      return errors;
    },
    descriptionErrors() {
      const errors = [];
      if (!this.$v.description.$dirty) return errors;
      !this.$v.description.required && errors.push("Descripción es requerida.");
      return errors;
    },
    startDateErrors() {
      const errors = [];
      if (!this.$v.startDate.$dirty) return errors;
      !this.$v.startDate.required && errors.push("Fecha de inicio es requerida.");
      return errors;
    },
    endDateErrors() {
      const errors = [];
      if (!this.$v.endDate.$dirty) return errors;
      !this.$v.endDate.required && errors.push("Fecha de finalización es requerida.");
      !this.$v.endDate.dateMaxValue && errors.push("Fecha de inicio debe ser mayor a la fecha actual.");
      !this.$v.endDate.endGreaterThanStart && errors.push("Fecha de finalización debe ser mayor a la fecha de inicio.");
      return errors;
    },
    narrativesGoalErrors() {
      const errors = [];
      if (!this.$v.narrativesGoal.$dirty) return errors;
      !this.$v.narrativesGoal.required && errors.push("Meta de narrativas es requerida.");
      !this.$v.narrativesGoal.numeric && errors.push("Meta de narrativas debe ser un valor numérico.");
      !this.$v.narrativesGoal.greaterThanCero && errors.push("Meta de narrativas debe ser mayor a 0.");
      return errors;
    },
    }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
.col-form {
  background: #e1e1e9;
  height: 100vh;
}

.form {
  background: #ffffff;
}

.login {
  border-radius: 5px;
  text-transform: none !important;
  text-decoration: none !important;
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
}

h3 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  color: #0c186d;
}
</style>