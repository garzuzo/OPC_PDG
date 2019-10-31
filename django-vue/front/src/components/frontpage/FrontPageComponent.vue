<template>
<div>

<navbar-component></navbar-component>

    <div class="init">
      <v-container>
        <!--INITIAL IMAGE -->
        <v-row>
          <v-col cols="7">
            <br />
            <h1>Narrativas de Paz</h1>
            <br />
            <br />
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam egestas, metus ac dignissim mattis, metus risus pretium ligula, ut mattis purus eros at nisl. </p>
            <br />
            <br />
            <v-btn :ripple="false" depressed rounded class="ma-2 ml-5 btn" color="#673AB7" dark to="/construirpaz">Quiero construir paz</v-btn>
          </v-col>
        </v-row>
      </v-container>
    </div>

    <how-it-works-component></how-it-works-component>

    <objective-component> </objective-component>
     <testimonial-component> </testimonial-component>
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
  font-size: 64px;
  line-height: 96px;
  color: #0c186d;
}

p {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 36px;
}

</style>
