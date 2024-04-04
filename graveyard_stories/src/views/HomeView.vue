<script setup lang="ts">
import HeaderComponent from '@/components/HeaderComponent.vue'
import FooterComponent from '@/components/FooterComponent.vue'
</script>

<template>
  <HeaderComponent />
  <div class="main-info-container">
    <img src="@/assets/DSCF0093.jpg" class="main-pic" />
  </div>
  <div class="header-text">MAʽAT</div>
  <FooterComponent class="footer" />
</template>

<style scoped>
.main-info-container {
  margin-top: 1%;
  width: 1300px;
  margin-left: auto;
  margin-right: auto;
  position: relative;
}

.main-pic {
  filter: grayscale(100%);
  width: inherit;
  height: 700px;
}

.footer {
  margin-top: 1%;
}

.header-text {
  font-size: 200px;
  color: white;
  font-family: 'Cinzel', serif;
  position: absolute;
  top: 30%;
  left: 45%;
}
</style>
