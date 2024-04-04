<script setup lang="ts">
import { ref } from 'vue'
import MenuButtonComponent from '@/components/MenuButtonComponent.vue'
import ModalWindow from '@/components/ModalWindowComponent.vue'
const menu = ref('about us')
const signup = ref('explore')
const showModal = ref(false)
</script>

<template>
  <div class="outer-wrapper">
    <div class="inner-wrapper">
      <MenuButtonComponent :data="menu" class="menu-button" />
      <MenuButtonComponent :data="signup" id="show-modal" @click="showModal = true" />
      <Teleport to="body" />
      <ModalWindow :isShown="showModal" @close="showModal = false" />
    </div>
  </div>
</template>

<style scoped>
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
</style>
