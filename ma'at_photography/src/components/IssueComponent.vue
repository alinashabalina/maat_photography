<script setup lang="ts">
defineProps<{
  name: String,
  link: String
}>()
</script>

<template>
  <div class="issue">
    <div class="cover2"></div>
    <div class="page5"></div>
    <div class="page4"></div>
    <div class="page3"></div>
    <div class="page2"></div>
    <div class="page1"></div>
    <div class="cover1"> {{ name }}</div>
  </div>
</template>

<style scoped lang="scss">
@media only screen and (max-width: 600px) {

  body {
    display: flex;
    justify-content: center;
    align-items: center;
    perspective: 100vw;
    background: #ccc;
  }

  .issue {
    transform-style: preserve-3d;
    position: relative;
    height: 20vh;
    width: 30vw;
    cursor: pointer;
    backface-visibility: visible;
  }

  .cover1, .cover2, .page1, .page2, .page3, .page4, .page5 {
    transform-style: preserve-3d;
    position: absolute;
    width: 20vw;
    height: 100%;
    top: 0; left: 0;
    transform-origin: left center;
    transition: transform .5s ease-in-out, box-shadow .35s ease-in-out;
  }

  .cover1, .cover2 {
    background-color: #555555;
    color: white;
    font-family: 'Cinzel', serif;
    font-size: 14px;
    text-align: center;
    line-height: 20vh;
  }


  .cover1, .page1, .page3, .page5 {
    border-bottom-right-radius: .5em;
    border-top-right-radius: .5em;
  }

  .cover2, .page2, .page4 {
    border-bottom-right-radius: .5em;
    border-top-right-radius: .5em;
  }

  .page1 {
    background: #efefef;
  }

  .page2 {
    background: #efefef;
  }

  .page3 {
    background: #f5f5f5;
  }

  .page4 {
    background: #f5f5f5;
  }

  .page5 {
    background: #fafafa;
  }

  .issue:hover .cover1 {
    transform: rotateY(-160deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page1 {
    transform: rotateY(-150deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page2 {
    transform: rotateY(-30deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page3 {
    transform: rotateY(-140deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page4 {
    transform: rotateY(-40deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page5 {
    transform: rotateY(-130deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .cover2 {
    transform: rotateY(-20deg) scale(1.1);
  }
}

@media only screen and (min-width: 600px) {

  body {
    display: flex;
    justify-content: center;
    align-items: center;
    perspective: 100vw;
    background: #ccc;
    width: 100%;
  }

  .issue {
    transform-style: preserve-3d;
    position: relative;
    height: 20vh;
    width: 30vw;
    cursor: pointer;
    backface-visibility: visible;
  }

  .cover1, .cover2, .page1, .page2, .page3, .page4, .page5 {
    transform-style: preserve-3d;
    position: absolute;
    width: 30vw;
    top: 0; left: 0;
    transform-origin: left center;
    transition: transform .5s ease-in-out, box-shadow .35s ease-in-out;
  }

  .cover1, .cover2 {
    background-color: #555555;
  }

  .cover1, .page1, .page3, .page5 {
    border-bottom-right-radius: .5em;
    border-top-right-radius: .5em;
  }

  .cover2, .page2, .page4 {
    border-bottom-right-radius: .5em;
    border-top-right-radius: .5em;
  }

  .page1 {
    background: #efefef;
  }

  .page2 {
    background: #efefef;
  }

  .page3 {
    background: #f5f5f5;
  }

  .page4 {
    background: #f5f5f5;
  }

  .page5 {
    background: #fafafa;
  }

  .issue:hover .cover1 {
    transform: rotateY(-160deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page1 {
    transform: rotateY(-150deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page2 {
    transform: rotateY(-30deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page3 {
    transform: rotateY(-140deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page4 {
    transform: rotateY(-40deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page5 {
    transform: rotateY(-130deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .cover2 {
    transform: rotateY(-20deg) scale(1.1);
  }
}

@media only screen and (min-width: 1000px) {

  body {
    display: flex;
    justify-content: center;
    align-items: center;
    perspective: 100vw;
    background: #ccc;
  }

  .issue {
    transform-style: preserve-3d;
    position: relative;
    height: 20vh;
    width: 30vw;
    cursor: pointer;
    backface-visibility: visible;
  }

  .cover1, .cover2, .page1, .page2, .page3, .page4, .page5 {
    transform-style: preserve-3d;
    position: absolute;
    width: 15vw;
    height: 30vh;
    top: 0; left: 0;
    transform-origin: left center;
    transition: transform .5s ease-in-out, box-shadow .35s ease-in-out;
  }

  .cover1, .cover2 {
    background-color: #555555;
  }

  .cover1, .page1, .page3, .page5 {
    border-bottom-right-radius: .5em;
    border-top-right-radius: .5em;
  }

  .cover2, .page2, .page4 {
    border-bottom-right-radius: .5em;
    border-top-right-radius: .5em;
  }

  .page1 {
    background: #efefef;
  }

  .page2 {
    background: #efefef;
  }

  .page3 {
    background: #f5f5f5;
  }

  .page4 {
    background: #f5f5f5;
  }

  .page5 {
    background: #fafafa;
  }

  .issue:hover .cover1 {
    transform: rotateY(-160deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page1 {
    transform: rotateY(-150deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page2 {
    transform: rotateY(-30deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page3 {
    transform: rotateY(-140deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page4 {
    transform: rotateY(-40deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .page5 {
    transform: rotateY(-130deg) scale(1.1);
    box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  }

  .issue:hover .cover2 {
    transform: rotateY(-20deg) scale(1.1);
  }
}


</style>