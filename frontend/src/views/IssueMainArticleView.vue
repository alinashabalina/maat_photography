<script setup lang="ts">

import HeaderComponent from "@/components/HeaderComponent.vue";
import ArticleComponent from "@/components/ArticleComponent.vue";
</script>

<template>
  <HeaderComponent/>
  <ArticleComponent/>
</template>

<style scoped lang="scss">
@use '../views/views';

@media only screen and (max-width: 600px) {
  .wrapper {
    height: 80vh;
    width: 97vw;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    margin-left: auto;
    margin-right: auto;
  }
}

@media only screen and (min-width: 600px) {

  .wrapper {
    height: 92vh;
    width: 98vw;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    margin-left: auto;
    margin-right: auto;
  }


}

@media only screen and (min-width: 1000px) {
  .article-pic {
    height: 20vh;
    width: 98vw;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-left: auto;
    margin-right: auto;
    border-radius: 20px;
  }

}
</style>