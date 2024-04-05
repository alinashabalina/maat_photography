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
  width: 150px;
  border: none;
  border-radius: 5px;
  font-family: 'Cinzel', serif;
  font-weight: 600;
  transition: 1s;
  &:hover {
    background-color: #b4b4b8;
    box-shadow: 0 0 30px rgba(151, 151, 151);
    height: 60px;
  }
}
</style>
