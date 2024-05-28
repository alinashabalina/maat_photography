<script setup lang="ts">
import HeaderComponent from '@/components/HeaderComponent.vue'
import FooterComponent from '@/components/FooterComponent.vue'
</script>

<template>
  <HeaderComponent />
  <div class="info-wrapper">
    <div class="autor-wrapper">
    <img src="@/assets/DSCF0093.jpg" class="autor-pic"/>
    <div class="buttons-wrapper">
      <img src="@/assets/telegram.png" class="tlgrm-icon socials"/>
      <img src="@/assets/telegram.png" class="tlgrm-icon socials"/>
    </div>
  </div>
</div>
  <FooterComponent class="footer" />
</template>

<style scoped lang="scss">
.info-wrapper {
  display: flex;
  flex-direction: row;
}

.autor-pic {
  border-radius: 50%;
  width: 500px;
  height: 500px;
}

.buttons-wrapper {
  display: flex;
  flex-direction: row;
}

.autor-wrapper {
  display: flex;
  flex-direction: column;
}

.tlgrm-icon {
  width: 48px;
  height: 48px;
}
</style>
