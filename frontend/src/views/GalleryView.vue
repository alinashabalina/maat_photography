<script lang="ts" setup>
import HeaderComponent from "../components/HeaderComponent.vue";
import IssueComponent from "@/components/IssueComponent.vue";
import {ref} from "vue";
const issue = ref(0)
const issues = 4
const click = ref("click to open")

const routing = (ev: Event) => {window.location.href = `/issue/${ev.currentTarget?.id}`}
</script>

<template>
  <HeaderComponent class="header"/>
  <div class="wrapper"  v-for="issue in issues" :key="issue">
    <IssueComponent :name="issue.name" :click = "click" class="issue odd"
                    :id="issue.id" @click = "routing"/>
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
    height: 70vh;
    margin-left: auto;
    margin-right: auto;
    margin-top: 5vh;
    border-radius: 10px;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    box-shadow: 2px 2px 2px 2px #d1d1d3;
    padding-top: 20px;
    padding-bottom: 30px;
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

@media only screen and (min-width: 1000px) {

  .wrapper {
    height: 70vh;
    margin-left: auto;
    margin-right: auto;
    margin-top: 5vh;
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
}

</style>