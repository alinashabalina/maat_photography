<script lang="ts" setup>
import HeaderComponent from "@/components/HeaderComponent.vue";
import MinorPhotoComponent from "@/components/MinorPhotoComponent.vue";
import {useRoute} from "vue-router";
import {ref} from "vue";
const issues = JSON.parse(localStorage.getItem("issues") || '{}')
const route = useRoute()
const article = ref(0)
interface Issue {
  id: number,
  name: String,
  articles: number[],
  editorial: String,
  pictures: number[]
}
const issue = issues.find((el: Issue) => el.id.toString() === route.params.id)
console.log(issue)
</script>

<template>
  <HeaderComponent/>
  <div class="wrapper">
    <div class="wrapper-light">
      <div class="header"><img src="@/assets/ISSUE 1.png"></div>
    </div>
    <div v-for="article in issue.articles" :key="article">
      <router-link :to="`/issue/${$route.params.id}/article/${article}`"> {{ article }}</router-link>
    </div>
 </div>

</template>

<style lang="scss" scoped>
@use "views";
@use "../components/components";

@media only screen and (max-width: 600px) {

  .header {
    font-family: views.$issue-font;
    font-weight: 400;
    font-style: normal;
    font-size: 60px;
  }
  .wrapper {
    width: 99vw;
    height: 95vh;
    display: flex;

    &__light {
      width: 60vw;
      padding-top: 6vh;
    }

    &__dark {
      width: 40vw;
      background-color: #e8e1d4;
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      border-radius: 10px;
    }
  }

  .wrapper-light {
    display: flex;
    flex-direction: column;
  }

  .small-pic {
    width: 20vw;
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

    &__light {
      width: 60vw;
      padding-top: 6vh;
    }

    &__dark {
      width: 40vw;
      background-color: components.$mid-grey;
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
    width: 20vw;
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
    overflow: hidden;

    &__light {
      width: 62vw;
      padding-top: 6vh;
    }

    &__dark {
      width: 40vw;
      background-color: components.$mid-grey;
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
    width: 20vw;
    height: 50vh;
    margin-left: 1vw;
    border-radius: 20px;
  }

}

</style>