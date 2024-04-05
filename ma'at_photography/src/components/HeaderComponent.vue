<script setup lang="ts">
import { ref } from 'vue'
import MenuButtonComponent from '@/components/MenuButtonComponent.vue'
import ModalWindow from '@/components/ModalWindowComponent.vue'
const about = ref('about us')
const signup = ref('about you')
const showModal = ref(false)
const header = ref('header')
</script>

<template>
  <div class="outer-wrapper">
    <div class="inner-wrapper">
      <div class="menu-btn">
        <img src="@/assets/menu.png" class="menu-icon" />
        menu
      </div>
      <MenuButtonComponent :data="about" class="menu-button" />
      <MenuButtonComponent :data="signup" @click="showModal = true" />
      <Teleport to="body" />
      <ModalWindow :isShown="showModal" @close="showModal = false" header="header" />
    </div>
  </div>
</template>

<style scoped lang="scss">
.outer-wrapper {
  width: 100%;
  height: 100px;
  border-top: 3px solid #000;
  border-bottom: 3px solid #000;
}
.inner-wrapper {
  width: 100%;
  height: 90px;
  margin-top: 4px;
  margin-bottom: 4px;
  border-top: 1px solid #000;
  border-bottom: 1px solid #000;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button-wrapper {
  display: flex;
  width: 150px;
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
  font-size: 22px;
  color: black;
  transition: 1s;
  &:hover {
    background-color: #b4b4b8;
    box-shadow: 0 0 30px rgba(151, 151, 151);
    height: 60px;
  }
}
</style>
