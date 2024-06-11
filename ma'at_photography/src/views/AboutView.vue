<script setup lang="ts">
import HeaderComponent from '@/components/HeaderComponent.vue'
import FooterComponent from '@/components/FooterComponent.vue'
import { ref } from 'vue';
const isHidden = ref(true)
</script>

<template>
  <HeaderComponent />
  <div class="info-wrapper">
    <div class="autor-wrapper">
    <img src="@/assets/DSCF0093.jpg" class="autor-pic" @click = "isHidden = !isHidden"/>
    <img src="@/assets/DSCF0093.jpg" class="autor-pic" @click = "isHidden = !isHidden"/>
    <img src="@/assets/DSCF0093.jpg" class="autor-pic"/>
    <img src="@/assets/DSCF0093.jpg" class="autor-pic"/>
    <img src="@/assets/DSCF0093.jpg" class="autor-pic"/>
    <img src="@/assets/DSCF0093.jpg" class="autor-pic"/>
    <img src="@/assets/DSCF0093.jpg" class="autor-pic"/>
    <img src="@/assets/DSCF0093.jpg" class="autor-pic"/>
    <img src="@/assets/DSCF0093.jpg" class="autor-pic"/>
    <img src="@/assets/DSCF0093.jpg" class="autor-pic"/>
    </div>
  <div class="socials-wrapper" v-show="isHidden">
    <img src="@/assets/DSCF0093.jpg" class="autor-pic__larger"/>
    <button class="socials-button">hello</button>
    <button class="socials-button">hello</button>
    <button class="socials-button">hello</button>
  </div>
  <div class="socials-wrapper" v-show="!isHidden">
    click the userpic to see the author's socials
  </div>
</div>
  <FooterComponent class="footer" />
</template>

<style scoped lang="scss">
@media only screen and (max-width: 600px) {
  .info-wrapper {
  display: flex;
  flex-direction: row;
  height: 75vh;
  width: 90vw;
  justify-content: space-between;
  overflow-x: hidden;
  overflow-y: hidden;
}

.autor-wrapper {
  display: flex;
  flex-direction: row;
  max-height: 75vh;
  width: 30vw;
  justify-content: space-between;
  flex-wrap: wrap;
  align-items: center;
  margin-left: 7vw;
}

  .autor-pic {
  border-radius: 50%;
  width: 50px;
  height: 50px;
  margin-top: 1vh;
  position: relative;

  &:hover {
    box-shadow: 2px 2px 5px 0px rgb(95, 94, 94);
  }

  &__larger {
    width: 150px;
    height: 150px;
    border-radius: 50%;
  }
}

.socials-wrapper {
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 1vh;
  height: 75vh;
  width: 51vw;
  display: flex;
  margin-left: 7vw;
  font-family: 'Cinzel', serif;
  font-size: 15px;
}

.socials-button {
width: 40vw;
height: 4vh;
border-radius: 10px;
border: 1px solid black;
background-color: #f2efe5;
transition: 0.5s;
margin-top: 2vh;
margin-bottom: 2vh;
&:hover {
    box-shadow: 0 0 30px rgba(151, 151, 151);
    height: 5vh;
    transition: 0.5s;
}
}
}

@media only screen and (min-width: 600px) {
  .info-wrapper {
  display: flex;
  flex-direction: row;
  height: 75vh;
  width: 90vw;
  justify-content: space-between;
  overflow-x: hidden;
  overflow-y: hidden;
}

.autor-wrapper {
  display: flex;
  flex-direction: row;
  max-height: 75vh;
  width: 30vw;
  justify-content: space-between;
  flex-wrap: wrap;
  align-items: center;
  margin-left: 7vw;
}

  .autor-pic {
  border-radius: 50%;
  width: 50px;
  height: 50px;
  margin-top: 1vh;
  position: relative;

  &:hover {
    box-shadow: 2px 2px 5px 0px rgb(95, 94, 94);
  }

  &__larger {
    width: 150px;
    height: 150px;
    border-radius: 50%;
  }
}

.socials-wrapper {
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 1vh;
  height: 75vh;
  width: 55vw;
  display: flex;
  margin-left: 10vw;
  font-family: 'Cinzel', serif;
  font-size: 20px;
}

.socials-button {
width: 40vw;
height: 4vh;
border-radius: 10px;
border: 1px solid black;
background-color: #f2efe5;
transition: 0.5s;
margin-top: 2vh;
margin-bottom: 2vh;
&:hover {
    box-shadow: 0 0 30px rgba(151, 151, 151);
    height: 5vh;
    transition: 0.5s;
}
}
}

@media only screen and (min-width: 1200px) {
  .info-wrapper {
  display: flex;
  flex-direction: row;
  height: 75vh;
  width: 90vw;
  justify-content: space-between;
  overflow-x: hidden;
  overflow-y: hidden;
}

.autor-wrapper {
  display: flex;
  flex-direction: row;
  max-height: 75vh;
  width: 30vw;
  justify-content: space-between;
  flex-wrap: wrap;
  align-items: center;
  margin-left: 7vw;
}

  .autor-pic {
  border-radius: 50%;
  width: 150px;
  height: 150px;
  margin-top: 1vh;
  position: relative;

  &:hover {
    box-shadow: 2px 2px 5px 0px rgb(95, 94, 94);
  }

  &__larger {
    width: 500px;
    height: 500px;
    border-radius: 50%;
  }
}

.socials-wrapper {
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 1vh;
  margin-top: 1vh;
  height: 75vh;
  width: 51vw;
  display: flex;
  margin-left: 15vw;
  font-family: 'Cinzel', serif;
  font-size: 40px;
}

.socials-button {
width: 20vw;
height: 5vh;
border-radius: 10px;
border: 1px solid black;
background-color: #f2efe5;
transition: 0.5s;
margin-top: 2vh;
margin-bottom: 2vh;
&:hover {
    box-shadow: 0 0 30px rgba(151, 151, 151);
    height: 5vh;
    transition: 0.5s;
}
}
}


</style>
