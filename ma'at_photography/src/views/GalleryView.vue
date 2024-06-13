<script lang="ts" setup>
import HeaderComponent from "../components/HeaderComponent.vue";
import IssueComponent from "@/components/IssueComponent.vue";
import {ref} from "vue";
const issue1 = ref("issue 1")
const issue2 = ref("issue 2")
const issue3 = ref("issue 3")
const issue4 = ref("issue 4")
</script>

<template>
  <HeaderComponent class="header"/>
  <div class="wrapper">
    <IssueComponent :name="issue1" class="issue odd"/>
    <IssueComponent :name="issue2" class="issue disabled" />
    <IssueComponent :name="issue3" class="issue odd disabled"/>
    <IssueComponent :name="issue4" class="issue disabled"/>
  </div>
</template>

<style lang="scss" scoped>
@media only screen and (max-width: 600px) {

  .wrapper {
    height: 60vh;
    margin-left: auto;
    margin-right: auto;
    margin-top: 10vh;
    border-radius: 10px;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    box-shadow: 2px 2px 2px 2px #d1d1d3;
    padding-top: 30px;
  }

  .issue {
    margin-left: 10vw;
  }

  .odd {
    margin-left: 18vw;
  }

  .disabled {
    opacity: 30%;
  }


}

@media only screen and (min-width: 600px) {
  .wrapper {
    height: 60vh;
    margin-left: auto;
    margin-right: auto;
    margin-top: 10vh;
    border-radius: 10px;
    box-shadow: 2px 2px 2px 2px #d1d1d3;
  }

  .issue {
    margin-left: 20vw;
  }
}

@media only screen and (min-width: 1000px) {

  .wrapper {
    height: 60vh;
    margin-left: auto;
    margin-right: auto;
    margin-top: 10vh;
    border-radius: 10px;
    box-shadow: 2px 2px 2px 2px #d1d1d3;
  }

  .issue {
    margin-left: 20vw;
  }
}

</style>