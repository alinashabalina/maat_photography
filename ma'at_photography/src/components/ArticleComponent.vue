<script setup lang="ts">
import MainPhotoComponent from "@/components/MainPhotoComponent.vue";
</script>

<template>
  <MainPhotoComponent class="article-pic" />
</template>

<style scoped lang="scss">
@use '../views/views';

@media only screen and (max-width: 600px) {
  .article-pic {
    width: 90vw;
    height: 20vh;
    border-radius: 20px;
    margin-top: 3vh;
  }
}

@media only screen and (min-width: 600px) {
  .article-pic {
    height: 10vh;
    border-radius: 20px;
    margin-top: 3vh;
  }

}

@media only screen and (min-width: 1000px) {
  .article-pic {
    width: 95vw;
    height: 20vh;
    border-radius: 20px;
    margin-top: 1vh;
  }
}
</style>