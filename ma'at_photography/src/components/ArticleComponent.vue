<script setup lang="ts">
defineProps<{
  text: String
}>()
</script>

<template>
  <img class="article-pic" src="@/assets/DSC3218.jpg" alt="main article picture"/>
  <div class="article-text"> {{ text }} </div>
</template>

<style scoped lang="scss">
@use '../views/views';

@media only screen and (max-width: 600px) {
  .article-pic {
    width: 97%;
    border-radius: 20px;
  }

  .article-text {
    font-family: views.$primary-font;
    font-size: 18px;
  }
}

@media only screen and (min-width: 600px) {
  .article-pic {
    width: 99%;
    border-radius: 20px;
  }

  .article-text {
    font-family: views.$primary-font;
    font-size: 40px;
  }

}

@media only screen and (min-width: 1000px) {
  .article-pic {
    width: 98%;
    height: 40%;
    border-radius: 20px;
  }

  .article-text {
    font-family: views.$primary-font;
    font-size: 32px;
  }
}
</style>