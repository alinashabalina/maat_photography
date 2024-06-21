<script lang="ts" setup>
defineProps<{
  data: String
}>()
</script>

<template>
  <button class="header-btn">{{ data }}</button>
</template>

<style lang="scss" scoped>
@use '../views/views';
@use 'components';

.header-btn {
  height: 50px;
  width: 150px;
  border: none;
  border-radius: 5px;
  font-family: views.$primary-font;
  font-weight: 600;
  transition: 1s;

  &:hover {
    background-color: components.$dark-grey;
    box-shadow: 0 0 30px rgba(151, 151, 151);
    height: 60px;
  }
}
</style>
