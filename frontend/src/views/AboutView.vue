<script lang="ts" setup>
import HeaderComponent from '@/components/HeaderComponent.vue'
import FooterComponent from '@/components/FooterComponent.vue'
import { AboutStore } from '@/stores/AboutStore'
import {ref, toRaw} from "vue";
const isHidden = ref(true)
const store = AboutStore()
store.getallAbouts()
const items = store.abouts
const item: any = ref(items[0])
</script>

<template>
  <HeaderComponent/>
  <div class="info-wrapper">
    <div class="autor-wrapper">
      <img class="autor-pic" v-for="item in items[0]" :key="item.id" :src="item.photo_link" alt="author">
    </div>
    <div v-show="isHidden" class="socials-wrapper">
      click the userpic to see the author's socials
    </div>
  </div>
  <FooterComponent class="footer"/>
</template>

<style lang="scss" scoped>
@use 'views';

@media only screen and (max-width: 600px) {
  .info-wrapper {
    display: flex;
    flex-direction: row;
    height: 75vh;
    width: 90vw;
    justify-content: space-between;
    overflow-x: hidden;
    overflow-y: hidden;
  }

  .autor-wrapper {
    display: flex;
    flex-direction: row;
    max-height: 75vh;
    width: 30vw;
    justify-content: space-between;
    flex-wrap: wrap;
    align-items: center;
    margin-left: 7vw;
  }

  .autor-pic {
    border-radius: 50%;
    width: 50px;
    height: 50px;
    margin-top: 1vh;
    position: relative;

    &:hover {
      box-shadow: 2px 2px 5px 0 rgb(95, 94, 94);
    }

    &__larger {
      width: 150px;
      height: 150px;
      border-radius: 50%;
    }
  }

  .socials-wrapper {
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-bottom: 1vh;
    height: 75vh;
    width: 51vw;
    display: flex;
    margin-left: 7vw;
    font-family: views.$primary-font;
    font-size: 15px;
  }

  .socials-button {
    width: 40vw;
    height: 4vh;
    line-height: 4vh;
    border-radius: 10px;
    border: 1px solid black;
    background-color: views.$primary-color;
    transition: 0.5s;
    margin-top: 2vh;
    margin-bottom: 2vh;
    color: black;
    text-decoration: none;
    text-align: center;

    &:hover {
      box-shadow: 0 0 30px rgba(151, 151, 151);
      height: 5vh;
      line-height: 5vh;
      transition: 0.5s;
      color: inherit;
    }
  }
}

@media only screen and (min-width: 600px) {
  .info-wrapper {
    display: flex;
    flex-direction: row;
    height: 75vh;
    width: 90vw;
    justify-content: space-between;
    overflow-x: hidden;
    overflow-y: hidden;
  }

  .autor-wrapper {
    display: flex;
    flex-direction: row;
    max-height: 75vh;
    width: 30vw;
    justify-content: space-between;
    flex-wrap: wrap;
    align-items: center;
    margin-left: 7vw;
  }

  .autor-pic {
    border-radius: 50%;
    width: 50px;
    height: 50px;
    margin-top: 1vh;
    position: relative;

    &:hover {
      box-shadow: 2px 2px 5px 0 rgb(95, 94, 94);
    }

    &__larger {
      width: 150px;
      height: 150px;
      border-radius: 50%;
    }
  }

  .socials-wrapper {
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-bottom: 1vh;
    height: 75vh;
    width: 55vw;
    display: flex;
    margin-left: 10vw;
    font-family: views.$primary-font;
    font-size: 20px;
  }

  .socials-button {
    width: 40vw;
    height: 4vh;
    line-height: 2vh;
    border-radius: 10px;
    border: 1px solid black;
    background-color: #f2efe5;
    transition: 0.5s;
    margin-top: 2vh;
    margin-bottom: 2vh;
    text-align: center;
    color: black;

    &:hover {
      box-shadow: 0 0 30px rgba(151, 151, 151);
      height: 5vh;
      line-height: 5vh;
      transition: 0.5s;
      color:black;
    }
  }
}

@media only screen and (min-width: 1000px) {
  .info-wrapper {
    display: flex;
    flex-direction: row;
    height: 75vh;
    width: 90vw;
    justify-content: space-between;
    overflow-x: hidden;
    overflow-y: hidden;
  }

  .autor-wrapper {
    display: flex;
    flex-direction: row;
    max-height: 75vh;
    width: 30vw;
    justify-content: space-between;
    flex-wrap: wrap;
    align-items: center;
    margin-left: 7vw;
  }

  .autor-pic {
    border-radius: 50%;
    width: 150px;
    height: 150px;
    margin-top: 1vh;
    position: relative;

    &:hover {
      box-shadow: 2px 2px 5px 0 rgb(95, 94, 94);
    }

    &__larger {
      width: 500px;
      height: 500px;
      border-radius: 50%;
    }
  }

  .socials-wrapper {
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-bottom: 1vh;
    margin-top: 1vh;
    height: 75vh;
    width: 51vw;
    display: flex;
    margin-left: 15vw;
    font-family: views.$primary-font;
    font-size: 20px;
  }

  .socials-button {
    width: 20vw;
    height: 2vh;
    line-height: 2vh;
    border-radius: 10px;
    border: 1px solid black;
    background-color: views.$primary-color;
    transition: 0.5s;
    margin-top: 2vh;
    margin-bottom: 2vh;
    text-decoration: none;

    &:hover {
      box-shadow: 0 0 30px rgba(151, 151, 151);
      height: 3vh;
      line-height: 3vh;
      transition: 0.5s;
    }
  }
}

</style>
