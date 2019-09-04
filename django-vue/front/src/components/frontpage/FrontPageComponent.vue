<template>
<div>

<v-row>


<v-col>


<h1>
{{title}}

</h1>

<p>
{{text}}
</p>

<v-btn
:ripple="false"
 class="ma-2 next"
outlined
 color="#673ab7"
@click="e1 = 2"
>

{{buttonText}}

</v-btn>

</v-col>


<v-col>





</v-col>

</v-row>



</div>



</template>

<script>
export default {
  name: "FrontPage",
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

h1{
  text-color:#0C186D;
}
</style>
