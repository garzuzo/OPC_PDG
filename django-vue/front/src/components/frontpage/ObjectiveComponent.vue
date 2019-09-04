<template>
<div>

<v-row>


<v-col>
<h4>
{{subtitle}}
</h4>

<h1>
{{title}}
</h1>

<p>
{{text}}
</p>
</v-col>


<v-col>

<v-img>



</v-img>



</v-col>

</v-row>



</div>


</template>



<script>
export default {
  name: "Objective",
  data() {
    return {
        subtitle:"Objetivo",
        title:"Construir paz entre todos",
        text:"Las Narrativas de Paz son relatos construidos colectivamente para definir lo que sí es la paz para los caleños. Estos relatos surgen de talleres que funcionan como espacios de encuentro para la construcción de una definición de paz desde un enfoque territorial. "
        };
  }
};
</script>
