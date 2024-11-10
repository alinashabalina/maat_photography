<script lang="ts" setup>
</script>

<template>
  <div class="slide-container" v-for="slide in slides" :key="slide.id">
    <span id="slider1"></span>
    <span id="slider2"></span>
    <span id="slider3"></span>
    <span id="slider4"></span>
    <span id="slider5"></span>
    <div class="image-container">
      <img :src="slide.photo_link" :class="slide.slider_class" alt="slider image" >
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use '../views/views';

@media only screen and (max-width: 600px) {

}

@media only screen and (min-width: 600px) {


}

@media only screen and (min-width: 1000px) {
  .slide-container {
    margin: 50vh auto 0 auto;
    transform: translateY(-50%);
    width: 600px;
    height: 450px;
    overflow: hidden;
  }
  img {
    width: 20%;
  }

  .image-container {
    display: inline-block;
    width: 3000px;
    height: 400px;
    position: relative;
    transition: left 1s;


    animation: slide 15s infinite;
  }
  .slider-image {
    float: left;
  }

  .button-container {
    position: relative;
    top: 10px;
  }

  .slider-button {
    height: 10px;
    width: 10px;
    margin: 4px;
    display: inline-block;
    border-radius: 5px;
    background-color: rgba(white, 0.5);
  }
  .slider-button:hover {
    background-color: rgba(white, 0.7);
  }

  #slider1:target ~ .image-container {
    left: 0px;
  }
  #slider2:target ~ .image-container {
    left: -600px;
  }
  #slider3:target ~ .image-container {
    left: -1200px;
  }
  #slider4:target ~ .image-container {
    left: -1800px;
  }
  #slider5:target ~ .image-container {
    left: -2400px;
  }

  .image-container:hover {
  }

  @keyframes slide {
    0% {
      left: 0;
    }
    20% {
      left: -600px;
    }
    40% {
      left: -1200px;
    }
    60% {
      left: -1800px;
    }
    80% {
      left: -2400px;
    }
    100% {
      left: 0;
    }
  }
}

</style>