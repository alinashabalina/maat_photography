<script setup lang="ts">
defineProps<{
  data: String
}>()
</script>

<template>
  <button class="header-btn">{{ data }}</button>
</template>

<style scoped lang="scss">
.header-btn {
  height: 50px;
  width: 130px;
  border: none;
  border-radius: 5px;
  font-family: 'Cinzel', serif;
  font-weight: 600;
  &:hover {
    background-color: #b4b4b8;
    transition: 1s;
    height: 60px;
  }
}
</style>
