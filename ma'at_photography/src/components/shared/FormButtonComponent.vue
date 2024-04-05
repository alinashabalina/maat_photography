<script setup lang="ts">
defineProps<{
  action: String
}>()
</script>

<template>
  <button class="form-btn">{{ action }}</button>
</template>

<style scoped lang="scss"></style>
