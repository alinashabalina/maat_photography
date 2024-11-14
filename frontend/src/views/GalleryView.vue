<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { VueSpinnerOval } from 'vue3-spinners';
import { mande } from 'mande'
import HeaderComponent from "../components/HeaderComponent.vue";
import IssueComponent from "@/components/IssueComponent.vue";
const allissues = ref([])
const api = mande("http://127.0.0.1:5000/issues")
const loading = ref(true)
const message: any = ref('')
const click = ref("click to open")
const issue: any = ref({"id": 4, "name": "hruhru"})
const routing = (ev: any) => {window.location.href = `/issue/${ev.currentTarget.id}`; }

onMounted(async () => {
  loading.value = true
  try {
    const res: any = await api.get()
    allissues.value = res["issues"]
    localStorage.setItem("issues", JSON.stringify(res["issues"]))
  } catch (error) {
    message.value = error
  } finally {
    loading.value = false
  }
})

</script>

<template>
  <HeaderComponent class="header"/>
  <div class="wrapper">
    <IssueComponent v-for="issue in allissues" :key="issue.id" :name="issue.name" :click = "click" class="issue odd"
                    :id="issue.id" @click = "routing"/>
   <VueSpinnerOval v-if="loading" size="200" color="black" class="spinner" />
    <div v-if="message"> {{ message }}</div>
  </div>y

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

  .spinner {
    margin-left: auto;
    margin-right: auto;
    width: 20vw;
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

  .spinner {
    margin-left: auto;
    margin-right: auto;
    margin-top: 20vh;
    width: 40vw;
  }

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

  .spinner {
    margin-left: auto;
    margin-right: auto;
    margin-top: 20vh;
    width: 40vw;
  }
}


</style>