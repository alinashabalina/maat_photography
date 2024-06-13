<script setup lang="ts">
import { ref } from 'vue'
import MenuButtonComponent from '@/components/MenuButtonComponent.vue'
import ModalWindow from '@/components/ModalWindowComponent.vue'
const signup = ref('login')
const showModal = ref(false)
</script>

<template>
  <div class="outer-wrapper">
    <div class="inner-wrapper">
      <div class="menu-btn">
        <img src="@/assets/menu.png" class="menu-icon" alt="menu icon"/>
        menu
      </div>
      <router-link :to="'/'" class="menu-btn">home</router-link>
      <router-link :to="'about'" class="menu-btn">about</router-link>
      <router-link :to="'gallery'" class="menu-btn">gallery</router-link>
      <router-link :to="'join'" class="menu-btn">join</router-link>
      <MenuButtonComponent :data="signup" @click="showModal = true" class="menu-btn"/>
      <Teleport to="body" />
      <ModalWindow :isShown="showModal" @close="showModal = false" header="explore with us">
      </ModalWindow>
    </div>
  </div>
</template>

<style scoped lang="scss">
@media only screen and (max-width: 600px) {
  .outer-wrapper {
  width: 90vw;
  height: 15vh;
  border-top: 3px solid #000;
  border-bottom: 3px solid #000;
  margin-left: auto;
  margin-right: auto;
}
.inner-wrapper {
  width: 90vw;
  height: 13.5vh;
  margin-top: 4px;
  margin-bottom: 4px;
  border-top: 1px solid #000;
  border-bottom: 1px solid #000;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.menu-icon {
  width: 25px;
  height: 25px;
}

.menu-btn {
  height: 5vh;
  width: 20vw;
  border: none;
  border-radius: 5px;
  font-family: 'Cinzel', serif;
  font-weight: 600;
  display: flex;
  justify-content: space-around;
  align-items: center;
  text-transform: uppercase;
  text-decoration: none;
  font-size: 9px;
  color: black;
}

}

@media only screen and (min-width: 600px) {
 .outer-wrapper {
  width: 90vw;
  height: 15vh;
  border-top: 3px solid #000;
  border-bottom: 3px solid #000;
  margin-left: auto;
  margin-right: auto;
}
.inner-wrapper {
  width: 90vw;
  height: 13.5vh;
  margin-top: 4px;
  margin-bottom: 4px;
  border-top: 1px solid #000;
  border-bottom: 1px solid #000;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.menu-icon {
  width: 40px;
  height: 40px;
}

.menu-btn {
  height: 5vh;
  width: 25vw;
  border: none;
  border-radius: 5px;
  font-family: 'Cinzel', serif;
  font-weight: 600;
  display: flex;
  justify-content: space-around;
  align-items: center;
  text-transform: uppercase;
  text-decoration: none;
  font-size: 25px;
  color: black;
}


}

@media only screen and (min-width: 1200px) {

.outer-wrapper {
  width: 98vw;
  height: 100px;
  border-top: 3px solid #000;
  border-bottom: 3px solid #000;
  margin-left: auto;
  margin-right: auto;
}
.inner-wrapper {
  width: 98vw;
  height: 90px;
  margin-top: 4px;
  margin-bottom: 4px;
  border-top: 1px solid #000;
  border-bottom: 1px solid #000;
  display: flex;
  justify-content: space-between;
  align-items: center;
}


.menu-icon {
  width: 45px;
  height: 45px;
}

.menu-btn {
  height: 50px;
  width: 130px;
  border: none;
  border-radius: 5px;
  font-family: 'Cinzel', serif;
  font-weight: 600;
  display: flex;
  justify-content: space-around;
  align-items: center;
  text-transform: uppercase;
  text-decoration: none;
  font-size: 22px;
  color: black;
  transition: 1s;
  &:hover {
    background-color: #b4b4b8;
    box-shadow: 0 0 30px rgba(151, 151, 151);
    height: 60px;
  }
}
}


</style>
