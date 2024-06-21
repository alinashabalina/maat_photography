<script lang="ts" setup>
import ArticleComponent from "@/components/ArticleComponent.vue";

const text = "lala"
</script>

<template>
  <div class="wrapper">
    <div class="wrapper-light">
      <div class="header">Issue {{ $route.params.id }}</div>
      <div class="wrapper__light">
        <ArticleComponent :text="text"/>
      </div>
    </div>
    <div class="wrapper__dark">
      <router-link :to="`/issue/${$route.params.id}/article`"><img alt="article pic" class="small-pic"
                                                                   src="@/assets/DSC3218.jpg"/></router-link>
      <router-link :to="`/issue/${$route.params.id}/gallery`"><img alt="article pic" class="small-pic"
                                                                   src="@/assets/DSC3218.jpg"/></router-link>
      <router-link :to="`/issue/${$route.params.id}/gallery`"><img alt="article pic" class="small-pic"
                                                                   src="@/assets/DSC3218.jpg"/></router-link>
    </div>
  </div>

</template>

<style lang="scss" scoped>
@use "views";

@media only screen and (max-width: 600px) {

  .header {
    font-family: views.$issue-font;
    font-weight: 400;
    font-style: normal;
    font-size: 60px;
  }
  .wrapper {
    width: 99vw;
    height: 102vh;
    display: flex;
    margin-top: -2vh;

    &__light {
      width: 60vw;
      padding-top: 6vh;
    }

    &__dark {
      width: 40vw;
      background-color: views.$dark-wrapper;
      display: flex;
      flex-direction: column;
      justify-content: space-around;
    }
  }

  .wrapper-light {
    display: flex;
    flex-direction: column;
  }

  .small-pic {
    width: 34vw;
    height: 30vh;
    margin-left: 2vw;
    border-radius: 10px;
  }

}

@media only screen and (min-width: 600px) {
  .header {
    font-family: views.$issue-font;
    font-weight: 400;
    font-style: normal;
    font-size: 60px;
  }
  .wrapper {
    width: 99vw;
    height: 102vh;
    display: flex;
    margin-top: -2vh;

    &__light {
      width: 60vw;
      padding-top: 6vh;
    }

    &__dark {
      width: 40vw;
      background-color: views.$dark-wrapper;
      display: flex;
      flex-direction: column;
      justify-content: space-around;
    }
  }

  .wrapper-light {
    display: flex;
    flex-direction: column;
  }

  .small-pic {
    width: 34vw;
    height: 30vh;
    margin-left: 2vw;
    border-radius: 20px;
  }


}

@media only screen and (min-width: 1000px) {
  .header {
    font-family: views.$issue-font;
    font-weight: 400;
    font-style: normal;
    font-size: 100px;
  }
  .wrapper {
    width: 99vw;
    height: 102vh;
    display: flex;
    margin-top: -2vh;
    overflow: hidden;

    &__light {
      width: 62vw;
      padding-top: 6vh;
    }

    &__dark {
      width: 40vw;
      background-color: views.$dark-wrapper;
      display: flex;
      flex-direction: column;
      justify-content: space-around;
    }
  }

  .wrapper-light {
    display: flex;
    flex-direction: column;
  }

  .small-pic {
    width: 35vw;
    height: 30vh;
    margin-left: 1vw;
    border-radius: 20px;
  }

}


</style>