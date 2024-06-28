<script lang="ts" setup>
import { useTextStore } from '@/stores/TextStore'
const store = useTextStore()
</script>

<template>
  <div class="header">lorem ipsum</div>
  <div class="text">{{ store.getTextMain}} </div>
</template>

<style lang="scss" scoped>
@use '../views/views';

@media only screen and (max-width: 600px) {
  .header {
    text-align: center;
    text-transform: uppercase;
    font-size: 20px;
  }
  .text {
    font-family: views.$primary-font;
    font-size: 12px;
  }
}

@media only screen and (min-width: 600px) {
  .header {
    text-align: center;
    text-transform: uppercase;
    font-size: 80px;
  }
  .text {
    font-family: views.$primary-font;
    font-size: 60px;
    text-align: center;
  }
}

@media only screen and (min-width: 1000px) {
  .header {
    text-align: center;
    text-transform: uppercase;
    font-size: 60px;
  }
  .text {
    font-family: views.$primary-font;
    font-size: 26px;
    text-align: center;
  }
}
</style>