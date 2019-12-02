<template>
    <v-card class="mx-auto" max-width="400">
            <v-container>
              <v-col align="center">
                <img :src="require(`@/assets/${member.img}`)" class="img" />
                <h4>{{member.name}}</h4>
                <h5>{{member.profession}}</h5>
                <h5>{{member.place}}</h5>
              </v-col>
            </v-container>
          </v-card>

</template>
<script>
export default {
    props:{
      member: Object
    },
    data(){
      return {
        imgSandra:"@/assets/sandra.jpg"
      }
    }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
h4 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  line-height: 36px;

  color: #0c186d;
}

h5{
    font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 36px;

  color: #000000;
}

.img {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  margin-bottom:10px;
}
</style>