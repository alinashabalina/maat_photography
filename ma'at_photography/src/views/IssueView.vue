<script lang="ts" setup>

</script>

<template>
  <div class="wrapper">
    <div class="wrapper-light">
    <div class="header">Issue {{ $route.params.id }}</div>
    <div class="wrapper__light"></div>
    </div>
    <div class="wrapper__dark"></div>
  </div>

</template>

<style lang="scss" scoped>
@use "views";
@media only screen and (max-width: 600px) {


  .header {
    font-family: views.$issue-font;
    font-weight: 400;
    font-style: normal;
    font-size: 40px;
  }
  .wrapper {
    width: 99vw;
    height: 102vh;
    display: flex;
    margin-top: -2vh;

    &__light {
      width: 60vw;
    }

    &__dark {
      width: 40vw;
      background-color: views.$dark-wrapper;
    }
  }

  .wrapper-light {
    display: flex;
    flex-direction: column;
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
    }

    &__dark {
      width: 40vw;
      background-color: views.$dark-wrapper;
      margin-right: -2vw;
    }
  }

  .wrapper-light {
    display: flex;
    flex-direction: column;
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

    &__light {
      width: 62vw;
    }

    &__dark {
      width: 40vw;
      background-color: views.$dark-wrapper;
      margin-left: -2vw;
    }
  }

  .wrapper-light {
    display: flex;
    flex-direction: column;
  }
}


</style>