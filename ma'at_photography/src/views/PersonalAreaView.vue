<script setup lang="ts">
import {ref} from "vue"
import HeaderComponent from "@/components/HeaderComponent.vue";
import PACardComponent from "@/components/PACardComponent.vue";
import FavoritesComponent from "@/components/shared/FavoritesComponent.vue";
const favorites = ref("favorite pictures")
const reading = ref("reading list")
const orders = ref("orders")
</script>

<template>
  <HeaderComponent/>
  <div class="card-wrapper">
    <PACardComponent class="card" :header="favorites"/>
    <FavoritesComponent></FavoritesComponent>
    <PACardComponent class="card" :header="reading"/>
    <PACardComponent class="card"  :header="orders"/>
  </div>

</template>

<style scoped lang="scss">
@use '../views/views';
@use '../components/components';

@media only screen and (max-width: 600px) {
  .card-wrapper {
    width: 95vw;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content: space-between;
  }

  .card {
    margin-top: 5vh;
    margin-right: auto;
    margin-left: auto;
  }
}

@media only screen and (min-width: 600px) {
}

@media only screen and (min-width: 1000px) {
}
</style>