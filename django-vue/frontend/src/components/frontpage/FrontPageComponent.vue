<template>
<div>

<navbar-component></navbar-component>

    <div class="init">
      <v-container class="fill-height" style="min-height: 100%">
        <!--INITIAL IMAGE -->
        <v-row style="padding-top: 20vh; padding-bottom:20vh;">
          <v-col sm="12" md="7">
            <h1 style="padding-bottom:10vh;">Narrativas de Paz</h1>
            <p style="padding-bottom:5vh;">El Observatorio de Paz y Convivencia (OPC) de la Secretaría de Paz y Cultura Ciudadana de la Alcaldía de Santiago de Cali tiene como objetivo realizar mediciones de la percepción de la paz bajo el mandato ciudad-región. </p>
            <v-btn :ripple="false" depressed rounded class="mx-2 pa-5 btn peace" color="#673AB7" dark to="/construirpaz">Quiero construir paz</v-btn>
          </v-col>
        </v-row>
      </v-container>
    </div>

    <how-it-works-component style="padding-top: 20vh; padding-bottom: 20vh;"></how-it-works-component>

    <objective-component > </objective-component>
     <testimonial-component style="padding-top: 20vh; padding-bottom: 20vh;"> </testimonial-component>
     <campaign-component> </campaign-component>


</div>



</template>

<script>
export default {
  data() {
    return {

      title:"Narrativas de Paz",
      text:"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam egestas, metus ac dignissim mattis, metus risus pretium ligula, ut mattis purus eros at nisl. ",
      buttonText:"Quiero construir Paz"
        };
  }
};
</script>


<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
body {
  background-color: white;
}

.init {
  background-image: url("../../assets/handpeace.png");
  background-size: cover;
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

.peace{
  text-transform: none !important;
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1600 - 300)));
  line-height: 24px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
</style>
