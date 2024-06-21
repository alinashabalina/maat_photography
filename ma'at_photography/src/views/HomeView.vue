<script setup lang="ts">
import { ref } from 'vue'
import HeaderComponent from '@/components/HeaderComponent.vue'
import FooterComponent from '@/components/FooterComponent.vue'
import ModalWindowComponent from '@/components/ModalWindowComponent.vue'
const showModal = ref(false)
</script>

<template>
  <HeaderComponent class="header"/>
  <div class="main-info-container">
    <img src="@/assets/DSCF0093.jpg" class="main-pic" />
  </div>
  <div class="header-text">
    <div class="header-text__header">MAʽAT</div>
    <div class="header-text__info">
      exploring the (under)world & concepts of life and death through photography
    </div>
  </div>
  <button class="signup-button" @click="showModal = true">Explore with us</button>
  <Teleport to="body" />
  <ModalWindowComponent
    :isShown="showModal"
    @close="showModal = false"
    header="explore with us"
  />
  <FooterComponent class="footer" />
</template>

<style scoped lang="scss">
@use 'views';

@media only screen and (max-width: 600px) {

.main-info-container {
  margin-top: 1vh;
  width: 90vw;
  margin-left: auto;
  margin-right: auto;
  position: relative;
}

.main-pic {
  filter: grayscale(150%);
  width: inherit;
  height: 90vh;
}

.footer {
  margin-top: 1vh;
}

.header-text {
  font-size: 60px;
  color: views.$white-header;
  font-family: views.$primary-font;
  position: absolute;
  top: 20%;
  left: 35%;

  &__info {
    font-size: 20px;
    width: 60%;
    margin-top: 1vh;
    text-align: justify;
  }

  &__2ndline {
    text-align: end;
  }
}

.signup-button {
  border: solid 2px white;
  background-color: transparent;
  width: 60vw;
  height: 8vh;
  position: absolute;
  top: 80%;
  left: 30%;
  color: views.$white-header;
  font-size: 20px;
  text-transform: uppercase;
  font-family: views.$primary-font;
  border-radius: 10px;
}

}

@media only screen and (min-width: 600px) {
  .main-info-container {
  margin-top: 1vh;
  width: 90vw;
  margin-left: auto;
  margin-right: auto;
  position: relative;
}

.main-pic {
  filter: grayscale(150%);
  width: inherit;
  height: 90vh;
}

.footer {
  margin-top: 1vh;
}

.header-text {
  font-size: 100px;
  color: views.$white-header;
  font-family: views.$primary-font;
  position: absolute;
  top: 20%;
  left: 35%;

  &__info {
    font-size: 40px;
    width: 60%;
    margin-top: 1vh;
    text-align: justify;
  }

  &__2ndline {
    text-align: end;
  }
}

.signup-button {
  border: solid 2px white;
  background-color: transparent;
  width: 40vw;
  height: 8vh;
  position: absolute;
  top: 80%;
  left: 30%;
  color: views.$white-header;
  font-size: 20px;
  text-transform: uppercase;
  font-family: views.$primary-font;
  border-radius: 10px;
}


}

@media only screen and (min-width: 1000px) {

  .main-info-container {
  margin-top: 1vh;
  width: 98vw;
  margin-left: auto;
  margin-right: auto;
  position: relative;
}

.main-pic {
  filter: grayscale(150%);
  width: 98vw;
  height: 90vh;
}

.footer {
  margin-top: 1vh;
}

.header-text {
  font-size: 200px;
  color: views.$white-header;
  font-family: views.$primary-font;
  position: absolute;
  top: 20%;
  left: 35%;

  &__info {
    font-size: 30px;
    width: 60%;
    margin-top: 1vh;
    text-align: justify;
  }

  &__2ndline {
    text-align: end;
  }
}

.signup-button {
  border: solid 2px white;
  background-color: transparent;
  width: 30vw;
  height: 8vh;
  position: absolute;
  top: 90%;
  left: 30%;
  color: views.$white-header;
  font-size: 20px;
  text-transform: uppercase;
  font-family: views.$primary-font;
  border-radius: 10px;
}
}


</style>
