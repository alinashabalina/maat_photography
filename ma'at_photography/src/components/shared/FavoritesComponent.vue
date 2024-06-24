<script setup lang="ts">

</script>

<template>
<img src="@/assets/heart.svg" alt="favorites icon" class="favorites">
</template>

<style scoped lang="scss">
 .favorites {
     filter: invert(73%) sepia(8%) saturate(91%) hue-rotate(202deg) brightness(99%) contrast(87%);
   &:hover {
     filter: invert(0%) sepia(12%) saturate(139%) hue-rotate(358deg) brightness(95%) contrast(84%);
   }
   &:active {
     filter: invert(0%) sepia(12%) saturate(139%) hue-rotate(358deg) brightness(95%) contrast(84%);
   }
 }
</style>