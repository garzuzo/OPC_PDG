<template>
    <div>
    <h4>
  {{subtitle}}
    </h4>
<h1>
    {{title}}
</h1>

<v-btn>


</v-btn>
<p>
{{description}}
</p>
    </div>
</template>


<script>
export default {
  name: "HowItWorks",
  data() {
    return {
      subtitle:"Cómo funciona",
      title:"Construir paz entre todos",
      description:"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam egestas, metus ac dignissim mattis, metus risus pretium ligula, ut mattis purus eros at nisl."
    };
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap');

h4{
  color:#0C186D;
}

</style>