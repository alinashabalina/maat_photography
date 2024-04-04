<script setup lang="ts"></script>

<template>
  <div class="outer-wrapper">
    <div class="inner-wrapper">
      <div class="socials-wrapper">
        <div class="socials-icons">
          <img src="@/assets/telegram.png" class="tlgrm-icon" />
          <img src="@/assets/insta.png" class="insta-icon" />
        </div>
        <div class="socials-wrapper__attribute">
          icons designed by
          <a href="https://www.freepik.com">freepik</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.outer-wrapper {
  width: 100%;
  height: 100px;
  border-top: 3px solid #000;
  border-bottom: 3px solid #000;
}
.inner-wrapper {
  width: 100%;
  height: 90px;
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
  color: #b4b4b8;

  &:visited {
    color: #000;
  }
}
</style>
