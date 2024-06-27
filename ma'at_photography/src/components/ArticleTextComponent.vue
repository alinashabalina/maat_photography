<script lang="ts" setup>

</script>

<template>
  <div class="text">lorem ipsum</div>
</template>

<style lang="scss" scoped>
@use '../views/views';

@media only screen and (max-width: 600px) {
  .text {
    font-family: views.$primary-font;
    font-size: 12px;
  }
}

@media only screen and (min-width: 600px) {
  .text {
    font-family: views.$primary-font;
    font-size: 40px;
  }
}

@media only screen and (min-width: 1000px) {
  .text {
    font-family: views.$primary-font;
    font-size: 20px;
  }
}
</style>