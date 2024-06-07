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
  <div class="socials-wrapper">
    <button class="socials-button">hello</button>
    <button class="socials-button">hello</button>
    <button class="socials-button">hello</button>
  </div>
</div>
  <FooterComponent class="footer" />
</template>

<style scoped lang="scss">
.info-wrapper {
  display: flex;
  flex-direction: row;
  height: 75vh;
  width: 100vw;
  justify-content: space-around;
}

.autor-pic {
  border-radius: 50%;
  width: 500px;
  height: 500px;
  margin-top: 5vh;
}

.buttons-wrapper {
  display: flex;
  width: 300px;
  flex-direction: row;
  justify-content: space-between;
  margin-top: 50px;
}

.autor-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-left: 150px;
}

.tlgrm-icon {
  width: 48px;
  height: 48px;
}

.socials-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  height: 200px;
  margin-top: 5vh;
}

.socials-button {
width: 500px;
height: 50px;
border-radius: 10px;
border: 1px solid black;
background-color: #f2efe5;
transition: 0.5s;
&:hover {
    box-shadow: 0 0 30px rgba(151, 151, 151);
    height: 60px;
    transition: 0.5s;
}
}
</style>
