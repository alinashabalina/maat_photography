<script lang="ts" setup></script>

<template>
  <div class="outer-wrapper">
    <div class="inner-wrapper">
      <div class="socials-wrapper">
        <div class="socials-icons">
          <a href="https://t.me/maatzine"
          ><img class="tlgrm-icon socials" src="@/assets/telegram.png"
          /></a>
          <a href="https://www.instagram.com/maat.zine"
          ><img class="insta-icon socials" src="@/assets/insta.png"
          /></a>
        </div>
        <div class="socials-wrapper__attribute">
          icons designed by
          <a href="https://www.freepik.com/">freepik</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use 'components';

.outer-wrapper {
  width: 90vw;
  height: 10vh;
  border-top: 3px solid #000;
  border-bottom: 3px solid #000;
  margin-left: auto;
  margin-right: auto;
}

.inner-wrapper {
  width: 90vw;
  height: 9vh;
  margin-top: 4px;
  margin-bottom: 4px;
  border-top: 1px solid #000;
  border-bottom: 1px solid #000;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.socials-wrapper {
  width: 200px;
  height: 56px;
  margin-left: auto;
  margin-right: auto;

  &__attribute {
    font-size: 10px;
    text-align: center;
  }
}

.socials-icons {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.tlgrm-icon {
  width: 48px;
  height: 48px;
}

.insta-icon {
  width: 52px;
  height: 52px;
}

a {
  color: components.$dark-grey;

  &:visited {
    color: #000;
  }
}

.socials {
  &:hover {
    filter: drop-shadow(0px 0px 10px);
    transition: 0.2s;
  }
}
</style>
