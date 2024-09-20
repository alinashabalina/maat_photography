<script setup lang="ts">
defineProps<{
  name: String
}>()
</script>

<template>
  <button class="tooltip">{{ name }}</button>
</template>

<style scoped lang="scss">
.tooltip {
  width: 1vw;
  height: 1vh;
  background-color: rgb(95, 94, 94);
}

</style>
