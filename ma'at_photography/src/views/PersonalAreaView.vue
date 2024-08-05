<script setup lang="ts">
import {ref} from "vue"
import HeaderComponent from "@/components/HeaderComponent.vue";
import PACardComponent from "@/components/PACardComponent.vue";
import { UserStore } from '@/stores/UserStore'
const favorites = ref("favorite pictures")
const reading = ref("reading list")
const orders = ref("orders")
const store = UserStore()
store.getData(27)
const details = store.getDetails[0]
</script>

<template>
  <HeaderComponent/>
  <div class="card-wrapper">
    <PACardComponent class="card" :header="favorites">
      <div v-for="item in details.user_favorites" :key="item"> {{ item }} </div>
    </PACardComponent>
    <PACardComponent class="card" :header="reading">
      <div v-for="item in details.user_reads" :key="item"> {{ item }} </div>
    </PACardComponent>
    <PACardComponent class="card"  :header="orders">
      <div v-for="item in details.user_orders" :key="item"> {{ item }} </div>
    </PACardComponent>
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
    align-items: center;
  }

  .card {
    margin-top: 5vh;
    margin-right: auto;
    margin-left: auto;
    width: 90vw;
  }
}

@media only screen and (min-width: 600px) {
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
    width: 85vw;
  }
}

@media only screen and (min-width: 1000px) {
  .card-wrapper {
    width: 100vw;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content: space-between;
  }

  .card {
    margin-top: 5vh;
    margin-right: auto;
    margin-left: auto;
    width: 85vw;
  }
}
</style>