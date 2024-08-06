<script lang="ts" setup>
import {ref} from 'vue'
import HeaderComponent from "@/components/HeaderComponent.vue";

const email = ref('')
const social = ref('')
const name = ref('')
const isDisabled = ref(false)
const modalData = ref('')
const isShown = ref(true)

function submitForm(event: Event): any {
  event.preventDefault();
  fetch("http://127.0.0.1:5000/join",
      {
        method: "POST", body: JSON.stringify({email: email.value, name: name.value, link: social.value})
      })
      .then((response) => response.json())
      .then((data) => {
        modalData.value = data["message"];
        return modalData
      })
      .catch((error) => {
        modalData.value = "Oops something went wrong. Try again later";
        return modalData
      })
  email.value = '';
  name.value = '';
  social.value = '';
  isShown.value = !isShown.value;
}
</script>

<template>
  <HeaderComponent class="head"/>
  <div v-show="isShown">
    <div class="header">Join us</div>
    <form class="form-wrapper">
      <div class="email-wrapper">
        <div class="input-label">Enter your email</div>
        <input v-model="email" class="input-field input-field__email" type="email"/>
      </div>
      <div class="email-wrapper">
        <div class="input-label">Enter your name</div>
        <input v-model="name" class="input-field input-field__email" type="text"/>
      </div>
      <div class="email-wrapper">
        <div class="input-label">Enter your project link</div>
        <input v-model="social" class="input-field input-field__email" type="text"/>
      </div>
      <input :disabled="isDisabled" class="input-submit form-btn button-item"
             type="submit" value="join us" @click="submitForm"/>
    </form>
  </div>
  <div v-show="!isShown" class="form-wrapper_info"> {{ modalData }}</div>
</template>

<style lang="scss" scoped>
@use 'views';

@media only screen and (max-width: 600px) {
  .header {
    font-family: views.$primary-font;
    font-size: 40px;
    width: 99vw;
    text-align: center;
    margin-top: 10vh;
  }
  .form-wrapper {
    width: 50vh;
    height: 50vh;
    margin-left: auto;
    margin-right: auto;
    border-radius: 10px;

    &_info {
      margin-top: 10vh;
      height: 30vh;
      text-align: center;
      line-height: 40vh;
      font-family: views.$primary-font;
      font-size: 12px;
    }
  }

  .email-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .password-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .input-submit {
    margin-top: 30px;
    margin-left: 30vw;
  }

  .input-label {
    margin-top: 20px;
    margin-bottom: 10px;
    text-align: center;
    font-size: 18px;
  }

  .input-field {
    width: 60vw;
    height: 6vh;
    border: none;
    border-radius: 10px;
  }

}

@media only screen and (min-width: 600px) {
  .header {
    font-family: views.$primary-font;
    font-size: 60px;
    width: 99vw;
    text-align: center;
    margin-top: 10vh;
  }

  .form-wrapper {
    width: 30vh;
    height: 20vh;
    margin-left: auto;
    margin-right: auto;

    &_info {
      margin-top: 10vh;
      height: 30vh;
      text-align: center;
      line-height: 40vh;
      font-family: views.$primary-font;
      font-size: 30px;
    }
  }

  .email-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .password-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .input-submit {
    margin-top: 30px;
    margin-left: 9vw;
  }

  .input-label {
    margin-top: 20px;
    margin-bottom: 10px;
    text-align: center;
    font-size: 40px;
  }

  .input-field {
    width: 50vw;
    height: 4vh;
    border: none;
    border-radius: 10px;
  }

}

@media only screen and (min-width: 1000px) {

  .header {
    font-family: views.$primary-font;
    font-size: 80px;
    width: 99vw;
    text-align: center;
    margin-top: 10vh;
  }

  .form-wrapper {
    width: 500px;
    height: 250px;
    margin-left: auto;
    margin-right: auto;

    &_info {
      text-align: center;
    }
  }

  .email-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .password-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .input-submit {
    margin-top: 30px;
    margin-left: 150px;
  }

  .input-label {
    margin-top: 20px;
    margin-bottom: 10px;
    text-align: center;
    font-size: 18px;
  }

  .input-field {
    width: 400px;
    height: 60px;
    border: none;
    border-radius: 10px;
  }
}
</style>
