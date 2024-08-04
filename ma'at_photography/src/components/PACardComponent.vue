<script setup lang="ts">
defineProps<{
  header: String
}>()
</script>

<template>
<div class="wrapper">
<div class="header">{{ header }}</div>
  <slot></slot>
</div>
</template>

<style scoped lang="scss">
@use '../views/views';
@use 'components';

@media only screen and (max-width: 600px) {
  .wrapper {
    border-radius: 10px;
    border: solid 1px components.$mid-grey;
    width: 100vw;
    height: 40vh;
    text-align: center;
  }

  .header {
    font-family: views.$primary-font;
    text-transform: uppercase;
    font-size: larger;
    margin-top: 1vh;
    color: black;
  }
}

@media only screen and (min-width: 600px) {
  .wrapper {
    border-radius: 10px;
    border: solid 1px components.$mid-grey;
    width: 90vw;
    height: 40vh;
    text-align: center;
  }

  .header {
    font-family: views.$primary-font;
    text-transform: uppercase;
    font-size: larger;
    margin-top: 1vh;
    color: black;
  }
}

@media only screen and (min-width: 1000px) {
  .wrapper {
    border-radius: 10px;
    border: solid 1px components.$mid-grey;
    width: 90vw;
    height: 40vh;
    text-align: center;
  }

  .header {
    font-family: views.$primary-font;
    font-size: 28px;
    text-transform: uppercase;
    margin-top: 1vh;
    color: black;
  }
}
</style>